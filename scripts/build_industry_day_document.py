from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "industry_day_summary.md"


def read(path):
    return path.read_text(encoding="utf-8") if path.exists() else ""


def main():
    intro = "\n".join(
        [
            "# AWS Summit Seoul 2026 Industry Day 영상 요약",
            "",
            "작성 기준: AWS Summit Seoul 2026 Day 1 | Industry Day 세션 VOD를 기준으로 정리했다. 각 세션은 가능한 경우 VOD 음성 전사를 기반으로 요약하고, 전사나 VOD 접근에 실패한 경우 공식 세션 메타데이터 기반 보조 요약으로 표시한다.",
            "",
            "## 읽는 방법",
            "",
            "각 세션은 동일한 형식으로 정리한다.",
            "",
            "- 세션 정보: 시간, 트랙, 발표자, 태그",
            "- 핵심 요약: 발표의 문제의식과 결론",
            "- 주요 포인트: 발표에서 실제로 기억할 만한 내용",
            "- AWS/기술 키워드: 언급된 서비스, 아키텍처, 방법론",
            "- 현장 메모로 남길 점: 참석 후기나 블로그에 붙이기 좋은 관찰",
            "- 블로그용 한줄: 후기에 바로 가져다 쓸 수 있는 문장",
            "",
            "## 전체 흐름 메모",
            "",
            "Industry Day의 큰 흐름은 산업별 AI 적용 사례가 단순한 PoC를 넘어 실제 운영, 개발 방식, 고객 경험, 물리 세계 자동화로 확장되고 있다는 점이다. 특히 에이전틱 AI, AI-DLC, 피지컬 AI, 영상/멀티모달 AI, 데이터 거버넌스, 마이그레이션 자동화가 반복적으로 등장한다. 발표들은 공통적으로 \"모델을 붙였다\"보다 \"기존 업무와 데이터 구조를 AI가 이해하고 실행할 수 있는 형태로 바꿨다\"는 쪽에 초점이 있다.",
            "",
        ]
    )

    parts = [intro]
    index = read(ROOT / "session_index.md")
    if index:
        parts.append("## 세션 인덱스\n\n" + "\n".join(index.splitlines()[2:]) + "\n")

    parts.append("## 세션별 요약\n")
    for idx in range(1, 7):
        batch = ROOT / "summaries" / f"batch{idx}.md"
        if batch.exists():
            parts.append(read(batch).strip() + "\n")
        elif idx == 1 and (ROOT / "summaries" / "sel-ind234-gs-retail.md").exists():
            parts.append("<!-- batch1 pending; GS리테일 세션 선반영 -->\n")
            parts.append(read(ROOT / "summaries" / "sel-ind234-gs-retail.md").strip() + "\n")
        else:
            parts.append(f"<!-- batch{idx}.md pending -->\n")

    OUT.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
