# sel-sec302 - Amazon Bedrock AgentCore 로 AI 시대의 Zero Trust 구현하기

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

- 시간/트랙/레벨/발표자: 2026-05-21 14:30-15:10 KST / Track 7 / 300 - Advanced / 이민우(AWS), 황재훈(AWS)
- 요약: AI 에이전트가 도구와 API를 직접 호출하는 시대에 Zero Trust를 어떻게 적용할지 다룬 보안 세션이다. Amazon Bedrock AgentCore Identity와 Gateway를 사용해 에이전트의 신원, 사용자 위임 권한, 도구 접속, 자격 증명 보관을 중앙에서 관리하는 패턴이 소개됐다. 발표는 에이전트의 자율성을 유지하되 API 키나 OAuth 토큰을 안전하게 다루고, MCP 도구 연결을 통제 가능한 경로로 만드는 것이 핵심이라고 설명했다.
- 주요 포인트:
  - AI 에이전트도 사용자, 서비스, 도구와 마찬가지로 명시적 신원과 최소 권한 원칙을 가져야 한다.
  - AgentCore Identity는 에이전트와 사용자 위임 권한을 관리하고, 안전한 credential 저장소와 연계된다.
  - AgentCore Gateway는 MCP, API 등 도구 호출 경로를 중앙화해 보안 정책과 관측성을 적용하기 쉽게 만든다.
  - Zero Trust의 초점은 "에이전트를 막는 것"이 아니라, 어떤 권한으로 어떤 도구를 언제 호출했는지 통제하는 것이다.
- AWS/기술 키워드: Amazon Bedrock AgentCore, AgentCore Identity, AgentCore Gateway, Zero Trust, MCP, OAuth, API Key, Credential Store, Security
- AX TF 관점/회사 AX 도입 시사점: 사내 에이전트가 Jira, GitHub, DB, 사내 API를 호출하게 되면 토큰 관리와 권한 위임이 즉시 핵심 리스크가 된다. AX TF는 에이전트별 계정, 사용자 위임 범위, 도구 게이트웨이, 감사 로그를 표준 아키텍처로 정하고 개발팀이 임의 토큰을 프롬프트나 설정 파일에 넣지 않도록 해야 한다.
- 공유용 한줄: AI 에이전트 보안의 출발점은 모델 필터가 아니라, 신원·권한·도구 호출을 Zero Trust로 묶는 것이다.
