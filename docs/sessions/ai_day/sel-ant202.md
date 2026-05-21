# sel-ant202 - 나야, 차세대 OpenSearch: 에이전틱 AI를 곁들인

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

- 시간/트랙/레벨/발표자: 16:10-16:50 KST / Track 2 / 200 - Intermediate / 김새름, 테크니컬 어카운트 매니저, AWS; 이승철, 테크니컬 어카운트 매니저, AWS
- 요약: OpenSearch가 키워드 검색을 넘어 시맨틱 검색, 벡터 검색, 에이전틱 검색의 기반 인프라로 진화하고 있다는 내용이었다. 발표자는 클러스터 운영 관측성, 비용 절감 기능, 대규모 벡터 성능, MCP 서버와 에이전틱 메모리를 함께 소개했다.
- 주요 포인트:
  - 검색은 어휘 매칭에서 의미 검색, 하이브리드 검색, 에이전트가 직접 여러 단계로 탐색하는 에이전틱 검색으로 진화하고 있다.
  - Amazon OpenSearch Service는 관리형/서버리스 운영, 한 자리 ms 수준 응답, 데이터 연결성, 클러스터 인사이트를 통한 운영 관측성을 제공한다.
  - 파생 소스 기능으로 스토리지를 최대 40% 줄이고, 계층형 벡터 스토리지로 메모리를 최대 32배 절감하는 비용 최적화 기능을 소개했다.
  - 자동 시맨틱 보강, GPU 가속 벡터 인덱싱, MCP 서버, 에이전틱 메모리, 전문화된 에이전트로 OpenSearch 위에 AI 앱을 만드는 데모를 보여줬다.
- AWS/기술 키워드: Amazon OpenSearch Service, OpenSearch Serverless, Vector Search, Semantic Search, Hybrid Search, Cluster Insights, Derived Source, GPU Acceleration, MCP Server, Agentic Memory
- AX TF 관점/회사 AX 도입 시사점: 사내 에이전트의 품질은 검색/메모리 인프라 품질에 크게 좌우된다. 문서 검색, 로그 분석, 업무 지식 조회를 각각 만들기보다 OpenSearch 기반 벡터/시맨틱/에이전틱 검색 계층을 공통 플랫폼으로 검토할 만하다.
- 공유용 한줄: 에이전트 시대의 검색은 단순 RAG 저장소가 아니라 메모리, 관측성, 도구 호출의 핵심 인프라다.
