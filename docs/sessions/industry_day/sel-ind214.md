# sel-ind214 - [요기요] 요기요의 AIOps: SRE 운영의 콘솔 탈출기

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

**제목/시간/트랙/발표자**  
- 제목: [요기요] 요기요의 AIOps: SRE 운영의 콘솔 탈출기
- 시간: 2026-05-20 15:30-15:50 KST
- 트랙: Industry Day / Retail & Consumer Goods, Software & Internet / Artificial Intelligence, Cloud Operations
- 발표자: 최낙권 Account Manager, AWS; 김예준 선임연구원, 위대한상상

**핵심 요약**  
AWS는 AIOps를 관찰, 이해, 행동으로 이어지는 운영 자동화 흐름으로 설명하며 Amazon Bedrock AgentCore를 소개했다. 요기요는 30개 이상 AWS 계정과 60개 이상 마이크로서비스를 운영하면서 Datadog, Argo CD, Grafana, Elasticsearch, CDN 로그 등 여러 도구를 오가야 하는 SRE 업무 부담을 겪고 있었다. 위대한상상은 AgentCore 기반 운영 포털을 만들고, 자연어 질문으로 서비스 영향도 분석, 리소스 최적화, 이벤트 리포트를 생성하는 구조를 구현했다. 핵심 성과는 모든 판단을 자동화한 것이 아니라 탐색 시간을 줄이고 근거를 정량화해 운영자가 더 중요한 의사결정에 집중하도록 만든 점이었다.

**주요 포인트**
- Bedrock AgentCore의 Runtime, Identity, Memory, Gateway를 활용해 에이전트 배포, 권한, 대화 맥락, 운영 도구 연결을 통합했다.
- 운영 포털은 CloudFront, ALB, Cognito, Lambda Authorizer를 거쳐 AgentCore로 요청을 보내고, MCP 형태의 Lambda 도구가 AWS·외부 관측 데이터를 조회한다.
- 연결 데이터에는 AWS 컴퓨트·네트워크·DB·스토리지·보안·모니터링·비용 지표와 Prometheus, Loki, Datadog, CDN 로그 등이 포함됐다.
- AI Assistant는 Elasticache 대역폭 병목과 read replica 증설 필요성 같은 판단을 콘솔 5개를 오가던 작업보다 빠르게 정리했다.
- 리소스 최적화는 피크 구간 기준 병목 시뮬레이션으로 Graviton 전환, 다운사이징, 세대 교체를 비교했고 Elasticache 비용 55% 절감, 작업 효율 10배 이상 향상을 확인했다.

**AWS/기술 키워드**  
Amazon Bedrock AgentCore, AgentCore Runtime, AgentCore Identity, AgentCore Memory, AgentCore Gateway, AWS Lambda, MCP, Amazon CloudFront, ALB, Amazon Cognito, Amazon Aurora, Amazon DynamoDB, ElastiCache, Prometheus, Loki, Datadog, Grafana, Argo CD

**현장 메모로 남길 점**  
요기요가 얻은 교훈은 "전문 에이전트를 많이 나누는 것"보다 단일 에이전트가 하나의 판단 맥락 안에서 원본 데이터를 해석하는 방식이 더 자연스럽고 정확했다는 점이다.

**블로그용 한줄**  
요기요는 Bedrock AgentCore 기반 AIOps로 흩어진 운영 지표를 자연어 분석과 표준 리포트로 묶어 SRE의 콘솔 탐색 시간을 크게 줄였다.

### 전사 기반 상세 보강

- 세션 맥락: [요기요] 요기요의 AIOps: SRE 운영의 콘솔 탈출기
- 공식 설명 보강: 요기요 서비스가 고도화되면서 모니터링 운영과 장애 분석을 위해 다수의 콘솔과 로그를 교차 분석해야 했습니다. 본 세션에서는 요기요에서 Agent Core 기반 AI로 지표 관측→상관관계 분석→변경 이력 대조→RCA 근거화를 통해 요기요 인프라 운영 효율을 획기적으로 개선한 AIOps 여정을 공유합니다.
- 전사에서 반복적으로 확인된 키워드: 에이전트, 운영, 데이터, 모니터링, 로그, 자동화, 고객, 전환, MCP, 인증
- 발표에서 두드러진 주제 축: ops, agent, data, security

#### 발표 흐름
- 초반: 에이전트, 운영, 고객, 배포, 데이터 중심으로 ops, agent, data를 다룬다.
- 중반: 데이터, 운영, 에이전트, 모니터링, 로그 중심으로 ops, agent, data를 다룬다.
- 후반: 에이전트, 운영, 데이터, 추천, 전환 중심으로 ops, agent, data를 다룬다.

#### 전사에서 확인할 만한 구간
- 00:13 부근: 운영 관련 설명이 나온다. 핵심 문맥은 `이번 세션에서는 운영 환경에서 해야 할 많은 업무들이 AYOPS를 통해서`
- 00:37 부근: 데이터, 운영 관련 설명이 나온다. 핵심 문맥은 `물론 데이터 센터나 서버실에서 직접 서버를 설치해서 운영하시다는`
- 08:42 부근: 데이터, 에이전트, 운영 관련 설명이 나온다. 핵심 문맥은 `이 사이크를 운영한 구성되어 있는 운영 포털 에이전트코어 데이터소스`
- 10:05 부근: 데이터, 로그 관련 설명이 나온다. 핵심 문맥은 `코스트 관련된 지표들과 프럼의 테우스, 로키, 데이터독, CDN 로그 같은`
- 18:29 부근: 에이전트, 운영 관련 설명이 나온다. 핵심 문맥은 `운영을 하면서 겪게 되는 문제들은 대부분 여러 가지 도매인에 있는 영역이라 에이전트 호출이 늘어날수록`
