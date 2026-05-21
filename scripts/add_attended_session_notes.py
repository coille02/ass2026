from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


NOTES = {
    "industry_day": {
        "summary": "industry_day_summary.md",
        "sessions": {
            "sel-ind234": """### 직접 들은 뒤 메모

GS SHOP 세션은 AX를 추상적인 생산성 향상 구호가 아니라 실제 추천 품질을 올리는 데이터 파이프라인으로 풀어낸 점이 좋았다. 숏폼 영상에서 상품, 장면, 스타일, 분위기, 구매 신호를 뽑아내고 이를 추천에 다시 연결하는 방식은 카카오페이에서도 금융 상품, 혜택, 이벤트, 콘텐츠 추천을 고도화할 때 참고할 만하다. 특히 핀테크에서는 추천이 곧 신뢰 문제와 연결되기 때문에, AI가 만든 태그와 설명을 그대로 쓰기보다 검증 가능한 메타데이터로 축적하고 추천 근거를 남기는 구조가 중요하다고 느꼈다.
""",
            "sel-ind302": """### 직접 들은 뒤 메모

K-POP 글로벌 라이브 세션은 대규모 실시간 트래픽과 AI 자막을 함께 운영한 사례라 인상적이었다. 금융 서비스에서도 이벤트성 트래픽, 대규모 알림, 실시간 상담, 장애 상황 공지처럼 순간적으로 부하가 몰리는 흐름이 있다. 카카오페이 관점에서는 AI 기능 자체보다 멀티 리전, 장애 전환, 비용 통제, 품질 폴백까지 포함한 운영 설계가 더 크게 다가왔다. AI 자막도 단순 번역이 아니라 도메인 맥락과 출력 규칙을 넣어 품질을 잡았는데, 금융 약관이나 고객 안내 문구에도 같은 접근이 필요하다.
""",
            "sel-ind211": """### 직접 들은 뒤 메모

바비톡의 AX 여정은 작게 만들고 빠르게 검증하는 방식이 가장 기억에 남았다. 처음부터 거대한 플랫폼을 만들기보다 리뷰 검수, 검색, 상담, 여행 가이드처럼 실제 고객 문제와 내부 업무 문제를 하나씩 풀어가며 에이전트를 키웠다. 카카오페이에서도 AX TF가 처음부터 완성형 플랫폼을 목표로 잡기보다, 고객센터 상담 보조, 가맹점 문의 분류, 내부 정책 검색, 개발자 업무 보조처럼 효과가 보이는 작은 단위부터 시작하는 것이 현실적이라고 느꼈다.
""",
            "sel-ind209": """### 직접 들은 뒤 메모

빗썸 세션은 핀테크 회사 입장에서 가장 직접적으로 참고할 만했다. Claude Code를 막는 것이 아니라 Bedrock, SSO, 프라이빗 네트워크, 감사 로그, 비용 관리, 프롬프트 필터링을 붙여 안전하게 쓰게 만드는 방향이 핵심이었다. 카카오페이도 개발자들이 이미 AI 도구를 쓰고 있다면, 사용을 금지하거나 개인 역량에 맡기는 것보다 금융권 수준의 통제와 개발자 경험을 함께 만족시키는 내부 AI 개발 플랫폼을 고민해야 한다. 특히 팀별 스킬 공유, 감사 가능한 로그, 모델 라우팅, 비용 가시화는 AX TF에서 우선순위 높게 볼 만하다.
""",
        },
    },
    "ai_day": {
        "summary": "ai_day_summary.md",
        "sessions": {
            "sel-aim305": """### 직접 들은 뒤 메모

삼성 어카운트 세션은 대규모 사용자 기반 서비스에서 AIOps를 에이전틱하게 풀어가는 방향을 보여줬다. 21억 사용자 규모라는 숫자 자체보다, 복잡한 운영 이벤트를 사람이 다 보는 구조에서 AI가 이상 징후를 찾고 원인을 좁히고 조치 후보를 제시하는 구조로 바꾸는 흐름이 중요했다. 카카오페이도 결제, 송금, 인증, 증권, 보험처럼 서비스 경계가 넓기 때문에 장애 탐지와 영향도 분석, 고객 영향 추정, 사후 리포트 작성에 AIOps를 적용할 여지가 크다.
""",
            "sel-prt302-s": """### 직접 들은 뒤 메모

완성차 지능형 상품 전략 플랫폼 세션은 AI와 서버리스가 업무 의사결정 플랫폼으로 연결되는 모습을 보여줬다. 자동차 상품 전략이라는 도메인은 다르지만, 여러 데이터 소스를 묶어 시장 변화와 상품 전략을 빠르게 분석한다는 구조는 핀테크에도 맞다. 카카오페이에서는 금융 상품, 혜택, 가맹점, 사용자 행동, 리스크 지표를 연결해 상품/마케팅/제휴 담당자가 직접 탐색할 수 있는 내부 전략 에이전트로 확장해볼 수 있다.
""",
            "sel-biz204": """### 직접 들은 뒤 메모

20만 Amazonian의 AI 내재화 경험은 AX 확산을 도구 배포가 아니라 조직 변화로 봐야 한다는 점을 보여줬다. Quick Desktop 같은 업무 환경은 개인이 여러 AI 도구를 흩어져 쓰는 상태를 줄이고, 회사가 승인한 데이터와 도구 안에서 AI를 쓰게 만드는 방향으로 이해됐다. 카카오페이에서도 Claude Code, Cursor, Amazon Q, Bedrock, 사내 LLM 도구 사용 경험을 하나의 업무 포털이나 스킬 허브로 연결하면, 개인 생산성을 팀과 전사 역량으로 바꾸는 출발점이 될 수 있다.
""",
        },
    },
}


def append_once(text: str, note: str) -> str:
    title = note.splitlines()[0].strip()
    if title in text:
        return text
    return text.rstrip() + "\n\n" + note.strip() + "\n"


def update_session_file(day: str, sid: str, note: str) -> None:
    path = ROOT / "docs" / "sessions" / day / f"{sid}.md"
    text = path.read_text(encoding="utf-8")
    path.write_text(append_once(text, note), encoding="utf-8")


def update_summary(day: str, summary_file: str, sid: str, note: str) -> None:
    path = ROOT / "docs" / summary_file
    text = path.read_text(encoding="utf-8")
    marker = f"## {sid} - "
    start = text.find(marker)
    if start == -1:
        marker = f"## {sid}"
        start = text.find(marker)
    if start == -1:
        return

    next_start = text.find("\n## sel-", start + 1)
    if next_start == -1:
        section = text[start:]
        rest = ""
    else:
        section = text[start:next_start]
        rest = text[next_start:]

    updated = append_once(section, note)
    path.write_text(text[:start] + updated + rest, encoding="utf-8")


def main() -> None:
    for day, config in NOTES.items():
        for sid, note in config["sessions"].items():
            update_session_file(day, sid, note)
            update_summary(day, config["summary"], sid, note)


if __name__ == "__main__":
    main()
