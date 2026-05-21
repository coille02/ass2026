# Snowflake + AWS 통합 AI 전략: Cortex Code가 연결하는 데이터와 인텔리전스 (sponsored by Snowflake)

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

## 세션 정보

- 시간: 2026-05-21 15:30-15:50 KST
- 트랙: Track 6
- 레벨: 200 - Intermediate
- 발표자: 김현정, Senior Partner Solution Engineer, Snowflake
- 주제: Artificial Intelligence, Developer Tools, Industry Solutions

## 발표 주제

Snowflake와 AWS로 엔터프라이즈 AI를 위한 통합 데이터 파운데이션을 구현하는 방법을 소개합니다. Cortex AI, Bedrock, S3, Glue 통합을 기반으로 데이터 엔지니어링부터 에이전트 개발까지 자연어로 가속화하는 Cortex Code를 소개합니다.

Snowflake와 AWS를 함께 써서 엔터프라이즈 AI용 통합 데이터 파운데이션을 만드는 접근을 소개했다. 발표자는 Snowflake 고객의 상당수가 AWS 리전에서 운영 중이며, S3, Glue Catalog, Iceberg, Bedrock, MCP, Cortex AI/Agent, Amazon Quick, AgentCore 같은 연동으로 데이터 이동 없이 AI 워크플로를 구성할 수 있다고 설명했다.

## 주요 내용

- AI 도입의 과제를 복잡한 파이프라인, 분산된 도구, LLM 통제/보안 요구로 정리하고, Snowflake의 편의성, 연결성, 신뢰성을 해결 축으로 제시했다.
- AWS Marketplace 원클릭 시작, S3 External Stage, Glue Catalog/Iceberg 통합으로 기존 데이터 레이크와 연결하는 패턴을 강조했다.
- Bedrock 기반 모델, Cortex AI, Cortex Agent/Code를 통해 자연어 기반 데이터 탐색, 코드 생성, 커스텀 앱/에이전트 개발을 가속하는 흐름을 소개했다.
- 고객 사례에서는 단일 데이터 소스와 거버넌스 체계를 통해 접근 속도와 전사 데이터 통제를 개선하고 AI 인사이트 탐색까지 확장했다고 설명했다.

## 세부 내용

### 문제의식과 배경

AI 도입의 과제를 복잡한 파이프라인, 분산된 도구, LLM 통제/보안 요구로 정리하고, Snowflake의 편의성, 연결성, 신뢰성을 해결 축으로 제시했다. AWS Marketplace 원클릭 시작, S3 External Stage, Glue Catalog/Iceberg 통합으로 기존 데이터 레이크와 연결하는 패턴을 강조했다.

### 접근 방식과 아키텍처

Bedrock 기반 모델, Cortex AI, Cortex Agent/Code를 통해 자연어 기반 데이터 탐색, 코드 생성, 커스텀 앱/에이전트 개발을 가속하는 흐름을 소개했다. 고객 사례에서는 단일 데이터 소스와 거버넌스 체계를 통해 접근 속도와 전사 데이터 통제를 개선하고 AI 인사이트 탐색까지 확장했다고 설명했다.

### 운영 포인트와 확장 방향

관련 기술 키워드는 Snowflake, AWS Marketplace, Amazon S3, AWS Glue Data Catalog, Apache Iceberg, Amazon Bedrock, MCP, Cortex AI, Cortex Agent, Cortex Code, Amazon Quick, Bedrock AgentCore이다.

## 정리

이 세션의 핵심은 Snowflake + AWS 통합 AI 전략: Cortex Code가 연결하는 데이터와 인텔리전스 (sponsored by Snowflake)를 단순한 기능 소개가 아니라 실제 업무와 운영 환경에 적용하기 위한 조건으로 풀어냈다는 점이다. AI 도입의 과제를 복잡한 파이프라인, 분산된 도구, LLM 통제/보안 요구로 정리하고, Snowflake의 편의성, 연결성, 신뢰성을 해결 축으로 제시했다.

발표는 AI 활용이 성과로 이어지려면 모델이나 도구 선택뿐 아니라 데이터, 권한, 운영 절차, 관측 가능성을 함께 설계해야 한다는 메시지로 정리된다.
