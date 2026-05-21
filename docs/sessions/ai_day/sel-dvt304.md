# sel-dvt304 - [삼성전자] 200개국 삼성 스마트 TV 앱 데이터를 자연어로 묻다: 에이전틱 AI on AWS

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

- 시간/트랙/레벨/발표자: 2026-05-21 14:30-15:10 KST / Track 3 / 300 - Advanced / 이혜원(AWS), 이아름(AWS), 임경택(삼성전자)
- 요약: 삼성 스마트 TV 앱 운영 데이터를 자연어로 질의하기 위해 LangGraph 멀티 에이전트를 Amazon Bedrock AgentCore 기반으로 프로덕션에 올린 사례다. 세션은 AgentCore Runtime, Gateway, Identity, Observability, Evaluation을 각각 운영 가능한 에이전트 플랫폼의 구성 요소로 풀어 설명했다. MCP를 통해 내부 API와 외부 도구 연결을 표준화하고, Okta IdP 연동과 자연어 기반 접근 제어, OpenTelemetry 트레이싱, CI 평가 자동화를 적용한 점이 실무적으로 중요했다.
- 주요 포인트:
  - 200개국 TV 앱 데이터 운영 문제를 자연어 질의와 멀티 에이전트로 풀되, 프로덕션 요구사항을 먼저 정의했다.
  - AgentCore Runtime은 Supervisor 패턴의 멀티 에이전트를 실행하는 기반으로, Gateway는 MCP 서버와 도구 연결을 중앙 관리한다.
  - Identity/Policy 연동으로 사용자의 권한과 에이전트의 도구 호출 권한을 함께 통제했다.
  - OpenTelemetry 기반 계층형 트레이싱으로 Sub-Agent별 실행 흐름을 추적하고, Evaluation을 CI에 넣어 품질을 자동 검증했다.
- AWS/기술 키워드: Amazon Bedrock AgentCore, LangGraph, MCP, AgentCore Runtime, Gateway, Identity, Okta, OpenTelemetry, Evaluation, CI
- AX TF 관점/회사 AX 도입 시사점: 사내 데이터 질의형 에이전트를 만들 때도 "데모 챗봇"이 아니라 권한, 도구 게이트웨이, 관측성, 평가 자동화를 처음부터 플랫폼 요구사항으로 잡아야 한다. 내부 API를 MCP로 감싸면 Claude Code류 개발 에이전트와 현업 분석 에이전트가 같은 도구 표준을 공유할 수 있다.
- 공유용 한줄: 삼성 사례의 핵심은 자연어 질의가 아니라, 에이전트를 프로덕션 서비스처럼 배포·통제·관측·평가한 점이다.
