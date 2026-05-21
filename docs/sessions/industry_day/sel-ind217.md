# sel-ind217 - LG전자, 에이전틱 AI 기반 멀티에이전트 플랫폼 구축을 통한 업무혁신

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

**제목/시간/트랙/발표자**  
- 제목: LG전자, 에이전틱 AI 기반 멀티에이전트 플랫폼 구축을 통한 업무혁신
- 시간: 2026-05-20 14:30-15:10 KST
- 트랙: Manufacturing & Industrial / Industry Solutions
- 발표자: 문필재 팀장, LG전자 한국영업본부 AX플랫폼

**핵심 요약**  
LG전자 한국영업본부는 고객 데이터 플랫폼과 대시보드 AI에서 출발해, 정형/비정형/멀티모달 데이터를 다루는 멀티 에이전트 플랫폼 “Agent One”으로 AX를 확장했다. 영업본부는 오프라인 매장, 온라인 판매, B2B 영업, 마케팅, 물류, 신제품 지원 등 다양한 업무를 수행하기 때문에 AI 에이전트도 데이터 분석을 넘어 교육, CRM, GEO 모니터링, 상담 기록, 유튜브/뉴스 분석, 실적 분석, CAD 도면 자동화로 넓어졌다. 플랫폼은 개별 에이전트를 포털처럼 호출하거나 planner가 적합한 에이전트를 선택하고, collector/coder/reporter 등 역할을 나눠 리포트를 생성하는 구조로 설명됐다. 향후에는 에이전트 워크플로 빌더와 영업본부 온톨로지를 통해 현업 담당자가 직접 에이전트들을 연결하는 방향을 준비하고 있다.

**주요 포인트**
- 기존 DX 조직은 CDP와 경영 지표 대시보드를 운영했고, 2024년에는 자연어로 고객 조건을 입력해 세그먼트를 추출하는 챗인사이트/챗봇 형태를 만들었다.
- 2025년에는 내부/외부 데이터, API, 검색을 결합해 분석 리포트를 만드는 멀티 에이전트 “Deep Analyst” 형태로 확장했다.
- Agent One은 AWS 인프라, Redshift, Aurora, RAG, vector search, Amazon Bedrock, Amazon Transcribe, Amazon IVS, Amazon Q/QuickSight 계열 기능을 조합해 멀티모달 업무를 처리한다.
- Role Playing Agent는 판매 매니저 교육 영상을 Amazon IVS로 녹화해 S3에 저장하고, 영상/표정/제스처와 음성을 분리 분석한 뒤 Bedrock으로 평가 기준표 기반 피드백을 생성한다.
- 구독 대시보드/챗봇 사례는 QuickSight 필터 맥락을 에이전트가 이해해 현재 보고 있는 지역의 판매 트렌드나 지도 분석을 이어서 답변하는 방식이었다.
- AutoGen CRM은 캠페인 기획, CDP 기반 타게팅, 세그먼트 생성, 카피라이팅, 이미지 생성, 발송, 성과 분석까지 CRM 흐름을 여러 에이전트가 나눠 처리한다.
- GEO 모니터링은 AI 검색/추천 시대에 LG전자 제품이 어떤 질문에서 어떻게 인용되고 추천되는지를 직접 수집/분석하는 사례였다.
- CAD 도면 자동화는 공간 면적 산출, 제품 스펙 선정, 배치, 검토 자동화를 목표로 하며 전문점 설계 검토의 80% 이상 자동화를 추진 중이라고 소개됐다.

**AWS/기술 키워드**
- Amazon Bedrock, Amazon Transcribe, Amazon IVS, Amazon S3, Amazon Aurora, Amazon Redshift, Amazon QuickSight, RAG, vector search, 멀티모달 AI, agent orchestration, ontology, CAD automation

**현장 메모로 남길 점**
- LG전자의 사례는 “에이전트 하나”가 아니라 영업본부 업무 전체에 작은 에이전트들을 깔고, 이후 워크플로로 연결해 실제 생산성으로 묶어내려는 플랫폼 접근이었다.

**블로그용 한줄**
- “LG전자는 Agent One을 통해 데이터 분석을 넘어 매장 교육, CRM, B2B 도면 업무까지 현업형 멀티 에이전트로 확장하고 있었다.”
