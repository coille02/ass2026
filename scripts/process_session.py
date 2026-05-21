import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path


BASE = "https://site-assets.corrivium.live/cms/events/aws-summitsel26"
WORKDIR = Path(__file__).resolve().parent
META_DIR = WORKDIR / "metadata"
AUDIO_DIR = WORKDIR / "audio"
TRANSCRIPT_DIR = WORKDIR / "transcripts"
SUMMARY_DIR = WORKDIR / "summaries"


def ensure_dirs():
    for path in (META_DIR, AUDIO_DIR, TRANSCRIPT_DIR, SUMMARY_DIR):
        path.mkdir(parents=True, exist_ok=True)


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path, data):
    Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def urlopen_text(url):
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Referer": "https://summitseoul.awslivestream.com/",
            "Origin": "https://summitseoul.awslivestream.com",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8")


def fetch_frontend(event_id):
    ensure_dirs()
    out = META_DIR / f"{event_id}.frontend.json"
    if out.exists():
        return read_json(out)
    data = json.loads(urlopen_text(f"{BASE}/{event_id}/prod/frontend.json"))
    write_json(out, data)
    return data


def find_vod_url(frontend):
    for video in frontend.get("videos", []):
        if video.get("id") == "VOD" and video.get("videoUrl"):
            return video["videoUrl"]
    for video in frontend.get("videos", []):
        if video.get("videoUrl"):
            return video["videoUrl"]
    raise RuntimeError("No videoUrl found")


def ffmpeg_path():
    env_path = os.environ.get("FFMPEG")
    if env_path:
        return env_path
    try:
        import imageio_ffmpeg

        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception as exc:
        raise RuntimeError("ffmpeg not found; install imageio-ffmpeg or set FFMPEG") from exc


def extract_audio(event_id):
    ensure_dirs()
    frontend = fetch_frontend(event_id)
    vod_url = find_vod_url(frontend)
    out = AUDIO_DIR / f"{event_id}.wav"
    if out.exists() and out.stat().st_size > 100_000:
        return out
    ffmpeg = ffmpeg_path()
    headers = "Referer: https://summitseoul.awslivestream.com/\r\nOrigin: https://summitseoul.awslivestream.com/\r\n"
    cmd = [
        ffmpeg,
        "-y",
        "-headers",
        headers,
        "-i",
        vod_url,
        "-vn",
        "-ac",
        "1",
        "-ar",
        "16000",
        "-c:a",
        "pcm_s16le",
        str(out),
    ]
    subprocess.run(cmd, check=True)
    return out


def transcribe(event_id, model_name="small"):
    ensure_dirs()
    out = TRANSCRIPT_DIR / f"{event_id}.txt"
    if out.exists() and out.stat().st_size > 1000:
        return out
    audio = extract_audio(event_id)
    from faster_whisper import WhisperModel

    model = WhisperModel(model_name, device="cpu", compute_type="int8")
    segments, info = model.transcribe(
        str(audio),
        language="ko",
        vad_filter=True,
        beam_size=1,
        condition_on_previous_text=False,
    )
    with out.open("w", encoding="utf-8") as f:
        f.write(f"# event_id={event_id} language={info.language} duration={info.duration}\n")
        for segment in segments:
            text = re.sub(r"\s+", " ", segment.text.strip())
            if text:
                f.write(f"[{segment.start:07.2f}-{segment.end:07.2f}] {text}\n")
    return out


def metadata_markdown(event_id):
    frontend = fetch_frontend(event_id)
    hp = frontend.get("homePage", {})
    meta = frontend.get("metaTags", {})
    speakers = frontend.get("eventPanel", {}).get("speakersSection", {}).get("speakers", [])
    speaker_text = ", ".join(
        f"{s.get('name', '').strip()} ({s.get('title', '').strip()})".strip()
        for s in speakers
        if s.get("name")
    )
    return "\n".join(
        [
            f"- ID: `{event_id}`",
            f"- 제목: {hp.get('eventtitle') or meta.get('title') or event_id}",
            f"- 시간: {hp.get('eventStart', '')} - {hp.get('eventEnd', '')} {hp.get('timezoneLabel', '')}",
            f"- 태그: {meta.get('filterTags', '')}",
            f"- 발표자: {speaker_text or 'N/A'}",
            f"- 공식 설명: {re.sub('<[^>]+>', '', hp.get('description') or meta.get('description') or '').strip()}",
        ]
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("event_id")
    parser.add_argument("--model", default="small")
    parser.add_argument("--metadata-only", action="store_true")
    args = parser.parse_args()
    ensure_dirs()
    if args.metadata_only:
        print(metadata_markdown(args.event_id))
        return
    transcript = transcribe(args.event_id, args.model)
    print(transcript)


if __name__ == "__main__":
    main()
