from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "ai_day_summary.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def main() -> None:
    intro = "\n".join(
        [
            "# AWS Summit Seoul 2026 AI Day 영상 요약",
            "",
            "작성 기준: AWS Summit Seoul 2026 Day 2 | AI Day 세션 VOD를 기준으로 정리했습니다. 각 세션은 가능한 경우 VOD 음성 전사를 기반으로 요약하고, 전사나 VOD 접근이 실패한 경우 공식 세션 메타데이터 기반 보조 요약으로 표시합니다.",
            "",
            "## 읽는 방법",
            "",
            "각 세션은 동일한 형식으로 정리했습니다.",
            "",
            "- 세션 정보: 시간, 트랙, 레벨, 발표자, 태그",
            "- 핵심 요약: 발표의 문제의식과 결론",
            "- 주요 포인트: 발표에서 실제로 기억할 만한 내용",
            "- AWS/기술 키워드: 언급된 서비스, 아키텍처, 방법론",
            "- AX TF 관점: 회사 AX 도입 논의와 연결할 수 있는 시사점",
            "- 공유용 한줄: 내부 공유 시 바로 가져다 쓸 수 있는 문장",
            "",
            "## 전체 흐름 메모",
            "",
            "AI Day의 큰 흐름은 생성형 AI를 실제 프로덕션으로 가져가기 위한 데이터, 개발 방법론, 보안, 인프라, 평가, 운영 체계에 집중되어 있습니다. Industry Day가 산업별 적용 사례를 보여줬다면, AI Day는 그 사례를 가능하게 하는 플랫폼과 운영 원칙을 더 깊게 다룹니다. 특히 AgentCore, Strands Agents, Kiro, SageMaker, Bedrock, AI-ready data, AI 보안, MLOps/AIOps, 추론 인프라 최적화가 반복적으로 등장합니다.",
            "",
        ]
    )

    parts = [intro]
    index = read(ROOT / "ai_day_session_index.md")
    if index:
        parts.append("## 세션 인덱스\n\n" + "\n".join(index.splitlines()[2:]) + "\n")

    parts.append("## 세션별 요약\n")
    for idx in range(1, 5):
        batch = ROOT / "summaries" / f"ai_day_batch{idx}.md"
        if batch.exists():
            parts.append(read(batch).strip() + "\n")
        else:
            parts.append(f"<!-- ai_day_batch{idx}.md pending -->\n")

    OUT.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
