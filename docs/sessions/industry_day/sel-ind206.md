# sel-ind206 - [미래에셋증권] Convert To AI-Ready Data 미래에셋증권의 GraphRAG 기반 상품지식DB 구축기

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

**Title/Time/Track/Speakers**  
- 제목: [미래에셋증권] Convert To AI-Ready Data 미래에셋증권의 GraphRAG 기반 상품지식DB 구축기
- 시간: 2026-05-20 12:50-13:30 KST
- 트랙: Industry Day / Financial Services / Analytics, Artificial Intelligence, Databases
- 발표자: 강인호 솔루션즈 아키텍트, AWS; 이우람 수석 매니저, 미래에셋증권; 최창균 선임 매니저, 미래에셋증권

**핵심 요약**  
미래에셋증권은 ETF, 펀드, 채권 같은 금융 상품의 정형·비정형 데이터를 GraphRAG 기반 상품지식DB로 전환한 사례를 공유했다. 세션은 일반 RAG가 문서 유사도 검색에 머무를 때 발생하는 의미·관계·수치 정확성 한계를 짚고, 온톨로지와 지식 그래프가 금융 질의의 신뢰성을 높이는 이유를 설명했다. 발표에서는 Amazon Neptune 계열 그래프 데이터베이스와 Amazon Bedrock Knowledge Bases의 그래프 기능이 언급됐고, 내부망에서 Bedrock LLM을 쓰는 구조도 향후 과제로 제시됐다. 실제 구축 과정에서는 문서 파싱, 엔티티/관계 추출, 표준화, 임계값 조정, 관리자 검증 패널이 핵심 작업으로 소개됐다.

**주요 포인트**
- 금융 상품 검색은 빠른 답보다 보수적이고 정확하며 설명 가능한 답이 중요하다는 전제에서 시작.
- 온톨로지는 금융 상품 지식을 기계가 이해할 수 있는 지도처럼 정의하는 역할로 설명.
- ETF, 펀드, 국내 채권을 1차 대상 상품으로 선정해 GraphRAG 효과가 큰 영역부터 접근.
- 추출된 엔티티와 관계를 그대로 쓰지 않고 표준화·정제·임계값 조정으로 그래프 품질을 관리.
- 답변 생성 시 실제 데이터 기반 답변, 금지 규칙, 관리자 검증을 둬 금융권 요구사항에 맞춤.

**AWS/기술 키워드**  
GraphRAG, Knowledge Graph, Ontology, Amazon Neptune, Amazon Bedrock Knowledge Bases, Bedrock LLM, RAG, Semantic Router, 금융 상품 DB, AI-ready data

**현장 메모로 남길 점**  
금융권 RAG는 "그럴듯한 답"이 아니라 출처와 관계가 검증되는 답이 핵심이다. GraphRAG는 LLM 프로젝트가 아니라 데이터 모델링과 도메인 온톨로지 프로젝트라는 점을 강조하면 좋다.

**블로그용 한줄**  
미래에셋증권은 상품 데이터를 그래프로 재구성해 금융 AI 검색의 정확도와 설명 가능성을 높이는 GraphRAG 접근을 보여줬다.
