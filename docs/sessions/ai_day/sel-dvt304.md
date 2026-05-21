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

### 전사 기반 상세 보강

- 세션 맥락: [삼성전자] 200개국 삼성 스마트 TV 앱 데이터를 자연어로 묻다: 에이전틱 AI on AWS
- 공식 설명 보강: 본 세션에서는 Amazon Bedrock AgentCore를 활용하여 LangGraph 멀티 에이전트를 프로덕션 환경에 배포한 실전 사례를 공유합니다. AgentCore Runtime에서 Supervisor 패턴의 멀티 에이전트를 실행하고, MCP(Model Context Protocol)를 통해 내부 API 등 외부 도구를 표준화된 방식으로 연결합니다. Gateway로 MCP 서버를 중앙 관리하고 에이전트 트래픽을 제어하며, Policy & Identity로...
- 전사에서 반복적으로 확인된 키워드: 에이전트, 운영, 데이터, 개발, 품질, 코드, 테스트, 배포, MCP, 전환
- 발표에서 두드러진 주제 축: agent, ops, developer, data

#### 발표 흐름
- 초반: 에이전트, 운영, 개발, 데이터, 코드 중심으로 agent, ops, developer를 다룬다.
- 중반: 에이전트, 운영, 개발, 품질, 데이터 중심으로 agent, ops, developer를 다룬다.
- 후반: 에이전트, 데이터, 운영, 품질, 코드 중심으로 agent, ops, developer를 다룬다.

#### 전사에서 확인할 만한 구간
- 02:53 부근: 개발, 에이전트, 운영 관련 설명이 나온다. 핵심 문맥은 `에이전트코어는 에이전트를 개발하고 운영하는 걸 도와주는 서비스입니다.`
- 08:56 부근: 배포, 에이전트, 운영 관련 설명이 나온다. 핵심 문맥은 `에이전트를 만들고 배포하고 또 운영하는 이러한 흐름을 하나로 묶어놓은 플랫폼이자 서비스라고 봐주시면 됩니다`
- 13:10 부근: 에이전트, 운영, 테스트 관련 설명이 나온다. 핵심 문맥은 `에이전트코어 런타임은 이 테스트 기반의 에이전트를 운영 가능한 구조로 변환하는 그런 계층입니다.`
- 24:58 부근: 배포, 에이전트, 코드 관련 설명이 나온다. 핵심 문맥은 `에이전트와 툴 코드를 수정하여 각각 재배포해야 했습니다.`
- 25:53 부근: MCP, 배포, 에이전트 관련 설명이 나온다. 핵심 문맥은 `에이전트와 여러 mcp 서버를 배포하였고`
