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
