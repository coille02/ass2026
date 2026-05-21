import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_sessions(path: Path) -> list[dict]:
    sessions = json.loads(path.read_text(encoding="utf-8"))
    return sorted(
        sessions,
        key=lambda item: (
            item.get("eventStart") or "",
            item.get("customCategory") or "",
            item.get("sessionEventId") or item.get("crvmEventId") or "",
        ),
    )


def session_id(item: dict) -> str:
    return item.get("sessionEventId") or item.get("crvmEventId") or ""


def title(item: dict) -> str:
    return item.get("eventtitle") or item.get("crvmEventName") or session_id(item)


def split_sections(summary_path: Path) -> dict[str, str]:
    text = summary_path.read_text(encoding="utf-8")
    marker = "## 세션별 요약"
    body = text.split(marker, 1)[1] if marker in text else text

    sections: dict[str, list[str]] = {}
    current_id: str | None = None
    current: list[str] = []

    def flush() -> None:
        nonlocal current_id, current
        if current_id:
            sections[current_id] = current
        current_id = None
        current = []

    for line in body.splitlines():
        matched = re.match(r"^##\s+(sel-[\w-]+)(?:\s+-\s+.*)?$", line)
        if matched:
            flush()
            current_id = matched.group(1)
            current = []
            continue

        if line.startswith("# "):
            continue

        if current_id:
            current.append(line)

    flush()
    return {key: "\n".join(value).strip() for key, value in sections.items()}


def normalize_body(body: str) -> str:
    lines = [
        line
        for line in body.splitlines()
        if not line.startswith("[개별 세션 문서](")
    ]
    while lines and not lines[0].strip():
        lines.pop(0)
    return "\n".join(lines).strip()


def build_day(day: str, title_text: str, summary_file: str, data_file: str) -> None:
    sessions = load_sessions(ROOT / "data" / data_file)
    sections = split_sections(ROOT / "docs" / summary_file)
    session_dir = ROOT / "docs" / "sessions" / day
    session_dir.mkdir(parents=True, exist_ok=True)

    index_lines = [
        f"# AWS Summit Seoul 2026 {title_text} 세션별 정리",
        "",
        "세션 단위로 다시 정리한 문서입니다. 각 세션 제목을 클릭하면 개별 요약 문서로 이동합니다.",
        "",
        "## 세션 목록",
        "",
        "| 시간 | 트랙 | ID | 세션 |",
        "|---|---|---|---|",
    ]

    summary_lines = [
        f"# AWS Summit Seoul 2026 {title_text} 영상 요약",
        "",
        "이 문서는 AWS Summit Seoul 2026 라이브스트림 VOD와 세션 메타데이터를 바탕으로 세션별로 정리한 것이다. 실제 공유와 탐색이 쉽도록 세션 단위로 재구성했다.",
        "",
        "## 세션 인덱스",
        "",
        "| 시간 | 트랙 | ID | 세션 |",
        "|---|---|---|---|",
    ]

    ordered_sections: list[tuple[dict, str]] = []
    for item in sessions:
        sid = session_id(item)
        body = normalize_body(sections.get(sid, ""))
        if not body:
            body = "- 요약: 기존 배치 요약에서 세션 내용을 찾지 못해 세션 메타데이터 확인이 필요하다."
        ordered_sections.append((item, body))

        time = (item.get("eventStart") or "")[11:16]
        track = (item.get("customCategory") or "").replace("AWS Summit Seoul - ", "")
        session_link = f"sessions/{day}/{sid}.md"
        row = f"| {time} | {track} | {sid} | [{title(item)}]({session_link}) |"
        index_lines.append(row)
        summary_lines.append(row)

    summary_lines.extend(["", "## 세션별 요약", ""])

    for item, body in ordered_sections:
        sid = session_id(item)
        heading = f"{sid} - {title(item)}"
        session_text = "\n".join(
            [
                f"# {heading}",
                "",
                f"[{title_text} 전체 요약으로 돌아가기](../../{summary_file})",
                "",
                body,
                "",
            ]
        )
        (session_dir / f"{sid}.md").write_text(session_text, encoding="utf-8")

        summary_lines.extend(
            [
                f"## {heading}",
                "",
                f"[개별 세션 문서](sessions/{day}/{sid}.md)",
                "",
                body,
                "",
            ]
        )

    (ROOT / "docs" / f"{day}_sessions.md").write_text(
        "\n".join(index_lines).rstrip() + "\n", encoding="utf-8"
    )
    (ROOT / "docs" / summary_file).write_text(
        "\n".join(summary_lines).rstrip() + "\n", encoding="utf-8"
    )


def main() -> None:
    build_day("industry_day", "Industry Day", "industry_day_summary.md", "industry_day_sessions.json")
    build_day("ai_day", "AI Day", "ai_day_summary.md", "ai_day_sessions.json")


if __name__ == "__main__":
    main()
