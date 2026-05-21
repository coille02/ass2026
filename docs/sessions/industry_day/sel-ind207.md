# sel-ind207 - [현대카드] 현대카드 데이터 사이언스 플랫폼 진화 여정: Hybrid to Coding 에이전트

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

**제목/시간/트랙/발표자**  
- 제목: [현대카드] 현대카드 데이터 사이언스 플랫폼 진화 여정: Hybrid to Coding 에이전트
- 시간: 2026-05-20 14:30-15:10 KST
- 트랙: Financial Services / Artificial Intelligence, Developer Tools
- 발표자: 김훈 솔루션즈 아키텍트(AWS), 이광식 팀장(현대카드)

**핵심 요약**  
현대카드는 금융권 규제 환경에서 데이터 사이언스 플랫폼을 하이브리드 구조로 진화시키고, SageMaker 환경에 특화된 코딩 에이전트 “코드버프”를 구축했다. AWS 발표 파트에서는 금융망 분리 완화 흐름 속에서 민감 데이터는 내부망/GPU 기반 오픈소스 모델로, 비식별 데이터와 고성능 모델 요구는 Bedrock PrivateLink 기반 접근으로 나누는 전략이 제시됐다. 현대카드는 온프레미스 유휴 GPU와 SageMaker를 결합한 HDSP를 통해 학습 비용과 GPU 부족 문제를 줄이고, 동일한 Docker 이미지와 HDSP 엔진으로 원소스 개발 경험을 제공했다. 이후 코드버프는 사내 private LLM, RAG, 미들웨어/툴, 멀티 에이전트 구조를 결합해 SageMaker Notebook 안에서 코드 생성, 리뷰, 보안 검사, 인프라 인지 최적화를 지원했다.

**주요 포인트**
- AWS는 금융권 생성형 AI 인프라 옵션으로 자체 GPU 서빙과 Bedrock 기반 관리형 모델 접근을 함께 제시했고, 데이터 성격에 따라 병행할 수 있다고 설명했다.
- 현대카드 HDSP는 온프레미스는 학습, AWS는 SageMaker Pipeline과 endpoint 기반 serving/workflow로 역할을 나눈 투트랙 구조다.
- 통합 Docker 이미지와 HDSP 엔진을 통해 같은 코드가 SageMaker와 온프레미스 Jupyter/Kubernetes 양쪽에서 동작하도록 했다.
- 학습 워크로드의 대부분을 온프레미스로 처리해 비용을 크게 줄이고, GPU/CPU 사용 비중도 도입 전 3:7에서 7:3으로 반전됐다고 소개했다.
- 코드버프는 오픈소스/공식 도구를 적극 활용하고, 금융권 특화 보안 스캔, SageMaker 인스턴스 측정, 내부 RAG 등 필요한 부분만 자체 개발했다.
- 메인 planner와 6개 도메인별 sub-agent가 Python, Athena query, Airflow DAG, Spark script, SageMaker tuning 등 영역을 나눠 담당한다.
- 노트북 요약, 보안 검출, 코드 리뷰, notebook 자동 생성, 인프라 스펙에 맞는 pandas/Polars/Dask/cuDF 권고 등이 데모로 제시됐다.

**AWS/기술 키워드**
- Amazon SageMaker, Amazon Bedrock, AWS PrivateLink, EKS Hybrid Nodes, GPU instances, Capacity Blocks, EMR, Athena, Airflow, Spark, RAG, MCP, private LLM

**현장 메모로 남길 점**
- 금융권 AI 도입은 “외부 도구를 쓸 수 있나”보다 “규제와 내부 데이터를 전제로 어떤 개발 경험을 재구성할 것인가”가 더 중요했다.
- 코드버프는 일반 코딩 에이전트를 그대로 가져온 것이 아니라 SageMaker Notebook과 금융 보안 맥락에 맞춘 플랫폼화 사례였다.

**블로그용 한줄**
- “현대카드는 하이브리드 데이터 사이언스 플랫폼 위에 금융권 맞춤 코딩 에이전트를 얹어, 규제 환경에서도 ML 개발 생산성을 끌어올리는 길을 보여줬다.”
