from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


NOTES = {
    "industry_day": {
        "summary": "industry_day_summary.md",
        "sessions": {
            "sel-ind234": """### 직접 들은 뒤 메모

GS SHOP 세션은 AX를 추상적인 생산성 향상 구호가 아니라 실제 추천 품질을 올리는 데이터 파이프라인으로 풀어낸 점이 좋았다. 숏폼 영상에서 상품, 장면, 스타일, 분위기, 구매 신호를 뽑아내고 이를 추천에 다시 연결하는 방식이 핵심이었다. 단순히 영상을 요약하는 것이 아니라 추천에 쓸 수 있는 신호를 만들어내는 구조였다.

우리 회사에서도 금융 상품, 혜택, 이벤트, 가맹점, 콘텐츠 추천을 고도화하려면 비슷한 접근이 필요하다. AI가 만든 태그나 설명을 그대로 노출하기보다, 추천 근거로 쓸 수 있는 검증 가능한 메타데이터를 축적해야 한다. 핀테크에서는 추천이 곧 신뢰 문제와 연결되므로 “왜 이 혜택이나 상품을 추천했는지” 설명 가능한 데이터 구조가 중요하다.
""",
            "sel-ind302": """### 직접 들은 뒤 메모

K-POP 글로벌 라이브 세션은 대규모 실시간 트래픽과 AI 자막을 함께 운영한 사례라 인상적이었다. AI 자막 자체도 흥미로웠지만, 더 크게 보인 것은 멀티 리전, 장애 전환, 비용 통제, 품질 폴백까지 포함한 운영 설계였다. 라이브 서비스에서 AI 기능은 별도 부가 기능이 아니라 서비스 안정성과 함께 설계되어야 한다는 점이 남았다.

우리 회사에서도 이벤트성 트래픽, 대규모 알림, 실시간 상담, 장애 상황 공지처럼 순간적으로 부하가 몰리는 흐름이 많다. AI가 고객 안내 문구를 만들거나 상담 답변을 보조하더라도 장애 시 안전하게 멈추고, 잘못된 답변을 막고, 사람에게 넘기는 폴백이 필요하다. AI 자막에서 도메인 맥락과 출력 규칙을 넣어 품질을 잡은 것처럼, 금융 약관이나 고객 안내 문구에도 도메인별 규칙과 검증 기준이 필요하다.
""",
            "sel-ind211": """### 직접 들은 뒤 메모

바비톡의 AX 여정은 작게 만들고 빠르게 검증하는 방식이 가장 기억에 남았다. 처음부터 거대한 플랫폼을 만들기보다 리뷰 검수, 검색, 상담, 여행 가이드처럼 실제 고객 문제와 내부 업무 문제를 하나씩 풀어가며 에이전트를 키웠다. AI를 유행처럼 붙인 것이 아니라, 비즈니스 문제를 정하고 그 문제를 해결하는 pocket service를 빠르게 실험하는 방식이었다.

우리 회사에서도 AX TF가 처음부터 완성형 플랫폼을 목표로 잡으면 속도가 느려질 수 있다. 고객센터 상담 보조, 가맹점 문의 분류, 내부 정책 검색, 장애 회고 초안, 개발자 업무 보조처럼 효과가 보이는 작은 단위부터 시작하는 것이 현실적이다. 작은 성공이 쌓여야 스킬허브와 Agent Builder의 요구사항도 구체화된다.
""",
            "sel-ind209": """### 직접 들은 뒤 메모

빗썸 세션은 핀테크 회사 입장에서 가장 직접적으로 참고할 만했다. Claude Code를 막는 것이 아니라 Bedrock, SSO, 프라이빗 네트워크, 감사 로그, 비용 관리, 프롬프트 필터링을 붙여 안전하게 쓰게 만드는 방향이 핵심이었다. 개발자 경험을 살리면서도 금융권 내부통제 요구를 맞추려는 접근이었다.

우리 회사도 개발자들이 이미 AI 도구를 쓰고 있다면, 사용을 금지하거나 개인 역량에 맡기는 것보다 안전한 내부 AI 개발 플랫폼을 고민해야 한다. 팀별 스킬 공유, 감사 가능한 로그, 모델 라우팅, 비용 가시화, 코드/데이터 반출 정책은 AX TF에서 우선순위 높게 볼 만하다. 이 세션은 AX가 생산성 도구 도입이면서 동시에 보안 아키텍처 과제라는 점을 분명하게 보여줬다.
""",
        },
    },
    "ai_day": {
        "summary": "ai_day_summary.md",
        "sessions": {
            "sel-aim305": """### 직접 들은 뒤 메모

삼성 어카운트 세션은 대규모 사용자 기반 서비스에서 AIOps를 에이전틱하게 풀어가는 방향을 보여줬다. 21억 사용자 규모라는 숫자 자체보다, 복잡한 운영 이벤트를 사람이 다 보는 구조에서 AI가 이상 징후를 찾고 원인을 좁히고 조치 후보를 제시하는 구조로 바꾸는 흐름이 중요했다. 운영자가 보는 로그와 알람을 AI가 업무 맥락으로 묶어주는 방식이었다.

우리 회사도 결제, 송금, 인증, 증권, 보험처럼 서비스 경계가 넓기 때문에 장애 탐지와 영향도 분석이 쉽지 않다. AIOps는 자동 조치보다 고객 영향 추정, 원인 후보 정리, 공지 초안, 사후 리포트 작성부터 시작하는 것이 현실적이다. 특히 장애 대응 과정에서 사람의 판단은 유지하되, AI가 상황 정리와 문서화를 줄여주는 방향이 효과적일 것 같다.
""",
            "sel-prt302-s": """### 직접 들은 뒤 메모

완성차 지능형 상품 전략 플랫폼 세션은 AI와 서버리스가 업무 의사결정 플랫폼으로 연결되는 모습을 보여줬다. 자동차 상품 전략이라는 도메인은 다르지만, 여러 데이터 소스를 묶어 시장 변화와 상품 전략을 빠르게 분석한다는 구조는 핀테크에도 맞다. 중요한 점은 AI가 답변만 하는 것이 아니라 담당자가 의사결정에 필요한 데이터를 한 흐름에서 탐색하게 만든다는 점이었다.

우리 회사에서는 금융 상품, 혜택, 가맹점, 사용자 행동, 리스크 지표, 캠페인 성과를 연결한 내부 전략 에이전트로 확장해볼 수 있다. 상품/마케팅/제휴 담당자가 직접 질문하고 초안을 얻되, 민감 데이터 접근과 결과 검증은 플랫폼이 통제해야 한다. 이 사례는 사내 Agent Builder가 단순 질의응답이 아니라 의사결정 워크벤치가 될 수 있음을 보여줬다.
""",
            "sel-biz204": """### 직접 들은 뒤 메모

이 세션에서 가장 인상적이었던 부분은 knowledge worker의 하루를 AI가 어떻게 줄여주는지였다. 기존에 쓰던 메일, 메시지, 캘린더, 문서, 스프레드시트, 대시보드가 끊어진 도구로 남아 있으면 AI는 답변만 잘하는 도구에 머문다. Quick Desktop은 각자의 업무 맥락을 지식 그래프처럼 만들고, 그 맥락을 기반으로 미팅 준비, 자료 생성, 이메일 작성, 비즈니스 리뷰, 아침 요약, 퇴근 후 자동 작업까지 이어주는 방향이었다.

우리 회사에도 이 접근은 꽤 잘 맞는다. 개발자에게는 Claude Code류 도구가 필요하지만, 사무직과 현업 담당자에게는 정책 문서, 회의록, 지라, 대시보드, 메신저, 캘린더를 연결한 업무형 AI 데스크톱이 더 직접적인 AX가 될 수 있다. 예를 들어 아침에 출근했을 때 전날 이후의 주요 이슈, 미처리 결재, 고객/가맹점 이슈, 장애 관련 업데이트, 오늘 회의 준비 항목을 요약해주고, 퇴근 후에는 정해둔 리포트 초안이나 데이터 확인 작업을 수행하게 할 수 있다. 다만 우리 회사는 핀테크 회사이기 때문에 개인화된 업무 그래프를 만들 때 고객 정보, 금융 거래 정보, 내부 정책 문서의 권한 경계를 분명히 해야 한다.
""",
        },
    },
}


def append_once(text: str, note: str) -> str:
    title = note.splitlines()[0].strip()
    if title in text:
        return text
    return text.rstrip() + "\n\n" + note.strip() + "\n"


def replace_note(text: str, note: str) -> str:
    marker = "### 직접 들은 뒤 메모"
    if marker not in text:
        return append_once(text, note)
    head, rest = text.split(marker, 1)
    next_heading = rest.find("\n## ")
    if next_heading == -1:
        return head.rstrip() + "\n\n" + note.strip() + "\n"
    return head.rstrip() + "\n\n" + note.strip() + rest[next_heading:]


def update_session_file(day: str, sid: str, note: str) -> None:
    path = ROOT / "docs" / "sessions" / day / f"{sid}.md"
    text = path.read_text(encoding="utf-8")
    path.write_text(replace_note(text, note), encoding="utf-8")


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

    updated = replace_note(section, note)
    path.write_text(text[:start] + updated + rest, encoding="utf-8")


def main() -> None:
    for day, config in NOTES.items():
        for sid, note in config["sessions"].items():
            update_session_file(day, sid, note)
            update_summary(day, config["summary"], sid, note)


if __name__ == "__main__":
    main()
