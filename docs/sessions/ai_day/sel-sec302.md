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

### 전사 기반 상세 보강

- 세션 맥락: Amazon Bedrock AgentCore 로 AI 시대의 Zero Trust 구현하기
- 공식 설명 보강: 이 세션에서는 Amazon Bedrock AgentCore Identity와 Gateway를 활용하여 AI 시대의 Zero Trust 보안 모델을 구현하는 방법을 다룹니다. AgentCore Identity와 Gateway를 사용하여 중앙화된 에이전트 신원 관리, 안전한 자격 증명 저장소를 통한 AI 에이전트의 인증 및 권한 부여, 안전한 도구(MCP, API 등) 연결을 지원하는 방법을 배웁니다. 이를 통해 참석자는 AI 에이전트의 자율성을 유지하면서도...
- 전사에서 반복적으로 확인된 키워드: 에이전트, MCP, 인증, 권한, 고객, 개발, 보안, 코드, agent, 데이터
- 발표에서 두드러진 주제 축: agent, security, developer, business

#### 발표 흐름
- 초반: 에이전트, 권한, 보안, 인증, agent 중심으로 agent, security, developer를 다룬다.
- 중반: 에이전트, MCP, 코드, 인증, 개발 중심으로 agent, security, developer를 다룬다.
- 후반: MCP, 에이전트, 인증, 고객, agent 중심으로 agent, security, developer를 다룬다.

#### 전사에서 확인할 만한 구간
- 12:59 부근: 로그, 인가, 인증 관련 설명이 나온다. 핵심 문맥은 `인가운드 인증 흐름을 살펴보면 먼저 사용자가 어플리케이션의 로그인합니다`
- 17:04 부근: IAM, 인가, 인증 관련 설명이 나온다. 핵심 문맥은 `AWS 리소스의 액세스의 경우에 AWS IAM 인증인가 방식이 사용됩니다.`
- 22:29 부근: MCP, 보안, 에이전트 관련 설명이 나온다. 핵심 문맥은 `저희는 그러한 에이전트 코어, 에이전트와 MCP 도구 간에 스케일러블 문제로 어떻게 안전하고 강력하고 또 손쉽게 보안이 확보된 상태로 회결할 수 있는지를 살펴보겠습니다.`
- 30:56 부근: 에이전트, 인가, 인증 관련 설명이 나온다. 핵심 문맥은 `에이전트가 에이전트코와 통신할 때 인증 인가를 받을 때`
- 39:34 부근: 감사, 인가, 인증 관련 설명이 나온다. 핵심 문맥은 `중심지점을 통해서 인증, 인가, 라오팅, 자격증명, 감사, 로딩, 네트워크 격리까지 한 번에 다 해결이 됩니다.`
