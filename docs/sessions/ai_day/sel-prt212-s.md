# sel-prt212-s - Snowflake + AWS 통합 AI 전략: Cortex Code가 연결하는 데이터와 인텔리전스 (sponsored by Snowflake)

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

- 시간/트랙/레벨/발표자: 15:30-15:50 KST / Track 6 / 200 - Intermediate / 김현정, Senior Partner Solution Engineer, Snowflake
- 요약: Snowflake와 AWS를 함께 써서 엔터프라이즈 AI용 통합 데이터 파운데이션을 만드는 접근을 소개했다. 발표자는 Snowflake 고객의 상당수가 AWS 리전에서 운영 중이며, S3, Glue Catalog, Iceberg, Bedrock, MCP, Cortex AI/Agent, Amazon Quick, AgentCore 같은 연동으로 데이터 이동 없이 AI 워크플로를 구성할 수 있다고 설명했다.
- 주요 포인트:
  - AI 도입의 과제를 복잡한 파이프라인, 분산된 도구, LLM 통제/보안 요구로 정리하고, Snowflake의 편의성, 연결성, 신뢰성을 해결 축으로 제시했다.
  - AWS Marketplace 원클릭 시작, S3 External Stage, Glue Catalog/Iceberg 통합으로 기존 데이터 레이크와 연결하는 패턴을 강조했다.
  - Bedrock 기반 모델, Cortex AI, Cortex Agent/Code를 통해 자연어 기반 데이터 탐색, 코드 생성, 커스텀 앱/에이전트 개발을 가속하는 흐름을 소개했다.
  - 고객 사례에서는 단일 데이터 소스와 거버넌스 체계를 통해 접근 속도와 전사 데이터 통제를 개선하고 AI 인사이트 탐색까지 확장했다고 설명했다.
- AWS/기술 키워드: Snowflake, AWS Marketplace, Amazon S3, AWS Glue Data Catalog, Apache Iceberg, Amazon Bedrock, MCP, Cortex AI, Cortex Agent, Cortex Code, Amazon Quick, Bedrock AgentCore
- AX TF 관점/회사 AX 도입 시사점: AX 도입은 모델보다 데이터 연결과 거버넌스가 먼저 병목이 된다. 사내 데이터 레이크/웨어하우스에서 데이터를 복사하지 않고 AI 도구가 안전하게 접근하는 표준 경로를 만들고, 개발자는 자연어/코드 생성 도구를 붙여 데이터 분석 앱과 에이전트를 빠르게 실험할 수 있게 해야 한다.
- 공유용 한줄: Snowflake+AWS 조합은 "데이터 이동 없는 AI"와 중앙 거버넌스를 동시에 노리는 엔터프라이즈 AX 데이터 기반 전략이다.

### 전사 기반 상세 보강

- 세션 맥락: Snowflake + AWS 통합 AI 전략: Cortex Code가 연결하는 데이터와 인텔리전스 (sponsored by Snowflake)
- 공식 설명 보강: Snowflake와 AWS로 엔터프라이즈 AI를 위한 통합 데이터 파운데이션을 구현하는 방법을 소개합니다. Cortex AI, Bedrock, S3, Glue 통합을 기반으로 데이터 엔지니어링부터 에이전트 개발까지 자연어로 가속화하는 Cortex Code를 소개합니다.
- 전사에서 반복적으로 확인된 키워드: 데이터, 에이전트, 코드, 고객, 카탈로그, 로그, S3, 개발, 운영, 정책
- 발표에서 두드러진 주제 축: data, developer, agent, business

#### 발표 흐름
- 초반: 데이터, 코드, 고객, 전략, 정책 중심으로 data, developer, agent를 다룬다.
- 중반: 데이터, 에이전트, 개발, 카탈로그, S3 중심으로 data, developer, agent를 다룬다.
- 후반: 데이터, 에이전트, 테스트, 고객, 코드 중심으로 data, developer, agent를 다룬다.

#### 전사에서 확인할 만한 구간
- 00:15 부근: 데이터, 코드 관련 설명이 나온다. 핵심 문맥은 `코택스 코드가 연결하는 데이터와 인텔리전스라는 주제로`
- 05:24 부근: 워크플로 관련 설명이 나온다. 핵심 문맥은 `스노플랩 내에선은 이 네이티브 통합된 AI 워크플로우를 구현하실 수가 있는데요.`
- 05:39 부근: MCP 관련 설명이 나온다. 핵심 문맥은 `또한 스노플랩에 지원되는 관령 MCP 서버관에 연동도 구성이 가능하시고요.`
- 10:02 부근: S3, 데이터 관련 설명이 나온다. 핵심 문맥은 `S3 버케세있는 이 데이터 연결에서`
- 21:19 부근: 데이터, 카탈로그 관련 설명이 나온다. 핵심 문맥은 `조직내 사용자들이 데이터 카탈로그 형태로 쉽게 탐색하고`
