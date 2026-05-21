# sel-sec201 - Agent-Driven 개발 환경, 보안 강화 전략은?

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

- 시간/트랙/레벨/발표자: 12:50-13:30 KST / Track 7, Security & Identity / 200 Intermediate / 이지영(AWS), 한태경(AWS)
- 요약: Claude Code, Kiro IDE, GitHub Copilot 같은 Agent-Driven 개발 환경에서는 코드 작성 속도가 보안 검토 속도를 압도하므로, 설계검토, 코드리뷰, 침투테스트를 자동화하는 AWS Security Agent 접근이 필요하다고 설명했다. 보안 요구사항을 조직별로 정의하고, PR 리뷰와 전체 코드 리뷰에서 취약점 탐지와 remediation 제안을 수행하는 흐름을 시연했다.
- 주요 포인트:
  - AI 개발은 취약한 코드가 빠르게 생산·배포될 위험을 키운다.
  - 보안은 배포 전 마지막 관문이 아니라 설계와 코드 작성 시점으로 당겨져야 한다.
  - Security Agent는 설계검토, 코드리뷰, 침투테스트를 각각 수행하고, 취약점 체인과 권한 상승 가능성까지 검증한다.
  - 단순히 “취약점 있음”을 알려주는 수준을 넘어 수정안과 리포트를 생성하는 것이 개발자 경험 측면에서 중요하다.
- AWS/기술 키워드: AWS Security Agent, secure SDLC, PR review, code remediation, penetration testing, OWASP Top 10, vulnerability chaining
- AX TF 관점/회사 AX 도입 시사점: AI 코딩 도구 도입 기준에 “보안 에이전트 리뷰 통과”를 포함해야 한다. 특히 사내 표준 보안 요구사항, 금지 API, 시크릿 처리, 개인정보 처리 기준을 에이전트가 검사할 수 있는 룰셋으로 만들어야 한다.
- 공유용 한줄: AI 개발 속도를 허용하려면 보안 리뷰도 에이전트 속도로 따라붙어야 한다.
