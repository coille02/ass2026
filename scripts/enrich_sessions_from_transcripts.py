import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRANSCRIPTS = ROOT.parent / "aws_summit_seoul_2026" / "transcripts"


TERM_GROUPS = {
    "agent": ["에이전트", "agent", "agentic", "AgentCore", "Strands", "MCP", "워크플로", "자동화"],
    "developer": ["Kiro", "Claude Code", "Cursor", "Amazon Q", "코드", "개발", "테스트", "배포", "리팩토링", "IaC"],
    "data": ["데이터", "RAG", "Knowledge", "카탈로그", "Lake Formation", "Redshift", "S3", "Glue", "Athena", "OpenSearch", "ClickHouse"],
    "security": ["보안", "권한", "인증", "인가", "감사", "로그", "필터링", "KMS", "IAM", "CloudTrail", "Zero Trust", "프라이빗"],
    "ops": ["운영", "장애", "모니터링", "AIOps", "DevOps", "관측", "CloudWatch", "알람", "리스크", "온콜"],
    "business": ["고객", "추천", "상담", "상품", "마케팅", "리뷰", "전환", "매출", "전략", "비즈니스"],
    "infra": ["EKS", "Lambda", "서버리스", "GPU", "Trainium", "HyperPod", "Slurm", "ParallelCluster", "아키텍처", "인프라"],
    "governance": ["거버넌스", "비용", "평가", "품질", "정확도", "추적", "승인", "정책", "표준"],
}

def load_sessions(path: Path) -> dict[str, dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return {
        item.get("sessionEventId") or item.get("crvmEventId"): item
        for item in data
    }


def parse_segments(text: str) -> list[tuple[float, float, str]]:
    segments = []
    for match in re.finditer(r"\[(\d+(?:\.\d+)?)-(\d+(?:\.\d+)?)\]\s*([^\[]+)", text):
        body = re.sub(r"\s+", " ", match.group(3)).strip()
        if body:
            segments.append((float(match.group(1)), float(match.group(2)), body))
    return segments


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = text.replace("니다 니다", "니다")
    return text


def contains_term(text: str, term: str) -> bool:
    return term.lower() in text.lower()


def group_scores(text: str) -> Counter:
    scores = Counter()
    for group, terms in TERM_GROUPS.items():
        for term in terms:
            scores[group] += len(re.findall(re.escape(term), text, flags=re.IGNORECASE))
    return scores


def top_terms(text: str, limit: int = 10) -> list[str]:
    counts = Counter()
    for terms in TERM_GROUPS.values():
        for term in terms:
            count = len(re.findall(re.escape(term), text, flags=re.IGNORECASE))
            if count:
                counts[term] += count
    return [term for term, _ in counts.most_common(limit)]


def pick_segments(segments: list[tuple[float, float, str]], groups: list[str], limit: int = 5) -> list[tuple[float, str, list[str]]]:
    candidates = []
    for start, _end, body in segments:
        matched = []
        for group in groups:
            for term in TERM_GROUPS[group]:
                if contains_term(body, term):
                    matched.append(term)
        if matched:
            candidates.append((len(set(matched)), start, clean_text(body), sorted(set(matched), key=str.lower)))

    selected = []
    used_buckets = set()
    for _score, start, body, terms in sorted(candidates, key=lambda item: (-item[0], item[1])):
        bucket = int(start // 300)
        if bucket in used_buckets and len(selected) < limit - 1:
            continue
        used_buckets.add(bucket)
        selected.append((start, body, terms[:4]))
        if len(selected) >= limit:
            break
    return sorted(selected, key=lambda item: item[0])


def flow_by_thirds(segments: list[tuple[float, float, str]], groups: list[str]) -> list[str]:
    if not segments:
        return []
    max_time = max(end for _start, end, _body in segments)
    labels = [("초반", 0, max_time / 3), ("중반", max_time / 3, max_time * 2 / 3), ("후반", max_time * 2 / 3, max_time + 1)]
    lines = []
    for label, lo, hi in labels:
        chunk = " ".join(body for start, _end, body in segments if lo <= start < hi)
        terms = top_terms(chunk, 5)
        group_names = [g for g in groups if group_scores(chunk)[g] > 0][:3]
        if terms:
            lines.append(f"- {label}: {', '.join(terms)} 중심으로 {', '.join(group_names) if group_names else '발표 주제'}를 다룬다.")
    return lines


def build_enrichment(sid: str, session: dict, transcript_text: str) -> str:
    segments = parse_segments(transcript_text)
    if len(transcript_text) < 1000 or len(segments) < 10:
        return "\n".join(
            [
                "### 전사 기반 상세 보강",
                "",
                "- 전사 상태: 이 세션은 VOD 전사에 발화가 거의 없어 공식 세션 메타데이터 중심으로만 확인할 수 있다.",
                "- 보강 방향: 발표 영상 또는 발표자료를 별도로 확보하면 세부 구현 방식, 수치, 운영 경험을 추가 확인해야 한다.",
                "",
            ]
        )

    full = " ".join(body for _start, _end, body in segments)
    scores = group_scores(full)
    groups = [group for group, score in scores.most_common() if score > 0][:4]
    terms = top_terms(full, 10)
    selected = pick_segments(segments, groups, 5)
    flow = flow_by_thirds(segments, groups)

    title = session.get("eventtitle") or session.get("crvmEventName") or sid
    description = clean_text(session.get("description") or "")
    if len(description) > 260:
        description = description[:260].rsplit(" ", 1)[0] + "..."

    lines = ["### 전사 기반 상세 보강", ""]
    lines.append(f"- 세션 맥락: {title}")
    if description:
        lines.append(f"- 공식 설명 보강: {description}")
    if terms:
        lines.append(f"- 전사에서 반복적으로 확인된 키워드: {', '.join(terms)}")
    if groups:
        lines.append(f"- 발표에서 두드러진 주제 축: {', '.join(groups)}")
    lines.append("")
    lines.append("#### 발표 흐름")
    lines.extend(flow or ["- 전사 구간별 흐름을 자동 추출하기 어려워 기존 요약과 메타데이터를 함께 확인해야 한다."])
    lines.append("")
    lines.append("#### 전사에서 확인할 만한 구간")
    for start, body, matched_terms in selected:
        minute = int(start // 60)
        second = int(start % 60)
        topic = ", ".join(matched_terms)
        if len(body) > 140:
            body = body[:140].rsplit(" ", 1)[0] + "..."
        lines.append(f"- {minute:02d}:{second:02d} 부근: {topic} 관련 설명이 나온다. 핵심 문맥은 `{body}`")
    lines.append("")
    return "\n".join(lines)


def replace_section(text: str, section: str) -> str:
    marker = "### 전사 기반 상세 보강"
    next_markers = ["\n### 직접 들은 뒤 메모", "\n## sel-", "\n# "]
    if marker not in text:
        insert_before = text.find("\n### 직접 들은 뒤 메모")
        if insert_before == -1:
            return text.rstrip() + "\n\n" + section.strip() + "\n"
        return text[:insert_before].rstrip() + "\n\n" + section.strip() + "\n" + text[insert_before:]

    start = text.find(marker)
    end_candidates = [
        text.find(next_marker, start + len(marker))
        for next_marker in next_markers
        if text.find(next_marker, start + len(marker)) != -1
    ]
    end = min(end_candidates) if end_candidates else len(text)
    return text[:start].rstrip() + "\n\n" + section.strip() + "\n" + text[end:]


def update_day(day: str, summary_name: str, sessions: dict[str, dict]) -> None:
    session_dir = ROOT / "docs" / "sessions" / day
    summary_path = ROOT / "docs" / summary_name
    summary_text = summary_path.read_text(encoding="utf-8")

    for session_file in sorted(session_dir.glob("sel-*.md")):
        sid = session_file.stem
        transcript_path = TRANSCRIPTS / f"{sid}.txt"
        transcript_text = transcript_path.read_text(encoding="utf-8", errors="replace") if transcript_path.exists() else ""
        enrichment = build_enrichment(sid, sessions.get(sid, {}), transcript_text)

        session_text = session_file.read_text(encoding="utf-8")
        session_file.write_text(replace_section(session_text, enrichment), encoding="utf-8")

        marker = f"## {sid}"
        start = summary_text.find(marker)
        if start == -1:
            continue
        next_start = summary_text.find("\n## sel-", start + 1)
        if next_start == -1:
            chunk = summary_text[start:]
            rest = ""
        else:
            chunk = summary_text[start:next_start]
            rest = summary_text[next_start:]
        summary_text = summary_text[:start] + replace_section(chunk, enrichment).rstrip() + rest

    summary_path.write_text(summary_text.rstrip() + "\n", encoding="utf-8")


def main() -> None:
    industry = load_sessions(ROOT / "data" / "industry_day_sessions.json")
    ai = load_sessions(ROOT / "data" / "ai_day_sessions.json")
    update_day("industry_day", "industry_day_summary.md", industry)
    update_day("ai_day", "ai_day_summary.md", ai)


if __name__ == "__main__":
    main()
