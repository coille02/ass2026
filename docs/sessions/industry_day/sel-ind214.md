# [요기요] 요기요의 AIOps: SRE 운영의 콘솔 탈출기

[Industry Day 세션 목록으로 돌아가기](../../industry_day_sessions.md)

## 세션 정보

- 시간: 2026-05-20 15:30-15:50 KST
- 트랙: Track 4
- 분류: 레벨: 200 - Intermediate, 산업: Retail & Consumer Goods, 산업: Software & Internet, 주제: Artificial Intelligence, 주제: Cloud Operations
- 발표자: 최낙권 Account Manager, AWS; 김예준 선임연구원, 위대한상상

## 발표 주제

AWS는 AIOps를 관찰, 이해, 행동으로 이어지는 운영 자동화 흐름으로 설명하며 Amazon Bedrock AgentCore를 소개했다.

요기요는 30개 이상 AWS 계정과 60개 이상 마이크로서비스를 운영하면서 Datadog, Argo CD, Grafana, Elasticsearch, CDN 로그 등 여러 도구를 오가야 하는 SRE 업무 부담을 겪고 있었다. 위대한상상은 AgentCore 기반 운영 포털을 만들고, 자연어 질문으로 서비스 영향도 분석, 리소스 최적화, 이벤트 리포트를 생성하는 구조를 구현했다.

## 주요 내용

- Bedrock AgentCore의 Runtime, Identity, Memory, Gateway를 활용해 에이전트 배포, 권한, 대화 맥락, 운영 도구 연결을 통합했다.
- 운영 포털은 CloudFront, ALB, Cognito, Lambda Authorizer를 거쳐 AgentCore로 요청을 보내고, MCP 형태의 Lambda 도구가 AWS·외부 관측 데이터를 조회한다.
- 연결 데이터에는 AWS 컴퓨트·네트워크·DB·스토리지·보안·모니터링·비용 지표와 Prometheus, Loki, Datadog, CDN 로그 등이 포함됐다.
- AI Assistant는 Elasticache 대역폭 병목과 read replica 증설 필요성 같은 판단을 콘솔 5개를 오가던 작업보다 빠르게 정리했다.
- 리소스 최적화는 피크 구간 기준 병목 시뮬레이션으로 Graviton 전환, 다운사이징, 세대 교체를 비교했고 Elasticache 비용 55% 절감, 작업 효율 10배 이상 향상을 확인했다.

## 세부 내용

### 배경과 문제 인식

요기요 서비스가 고도화되면서 모니터링 운영과 장애 분석을 위해 다수의 콘솔과 로그를 교차 분석해야 했습니다. 본 세션에서는 요기요에서 Agent Core 기반 AI로 지표 관측→상관관계 분석→변경 이력 대조→RCA 근거화를 통해 요기요 인프라 운영 효율을 획기적으로 개선한 AIOps 여정을 공유합니다.

발표는 이 배경에서 출발해 실제 서비스나 운영 환경에서 어떤 제약이 있었고, 이를 해결하기 위해 어떤 기술 선택과 구현 방식을 택했는지를 설명했다. 단순한 기능 소개보다 현장에서 마주한 병목, 데이터 흐름, 운영 책임을 어떻게 정리했는지가 핵심 맥락이다.

### 구현 접근

- Bedrock AgentCore의 Runtime, Identity, Memory, Gateway를 활용해 에이전트 배포, 권한, 대화 맥락, 운영 도구 연결을 통합했다.
- 운영 포털은 CloudFront, ALB, Cognito, Lambda Authorizer를 거쳐 AgentCore로 요청을 보내고, MCP 형태의 Lambda 도구가 AWS·외부 관측 데이터를 조회한다.
- 연결 데이터에는 AWS 컴퓨트·네트워크·DB·스토리지·보안·모니터링·비용 지표와 Prometheus, Loki, Datadog, CDN 로그 등이 포함됐다.
- AI Assistant는 Elasticache 대역폭 병목과 read replica 증설 필요성 같은 판단을 콘솔 5개를 오가던 작업보다 빠르게 정리했다.

### 운영과 확장 관점

- 리소스 최적화는 피크 구간 기준 병목 시뮬레이션으로 Graviton 전환, 다운사이징, 세대 교체를 비교했고 Elasticache 비용 55% 절감, 작업 효율 10배 이상 향상을 확인했다.

## 정리

이 세션은 [요기요] 요기요의 AIOps: SRE 운영의 콘솔 탈출기 이라는 주제를 통해, 실제 산업 현장에서 AWS와 AI/클라우드 기술을 어떻게 서비스 개선과 운영 효율로 연결했는지를 보여줬다. 핵심은 새로운 도구의 나열이 아니라 문제를 정의하고, 데이터와 아키텍처를 정리하며, 운영자가 신뢰할 수 있는 방식으로 결과를 만드는 과정에 있었다.
