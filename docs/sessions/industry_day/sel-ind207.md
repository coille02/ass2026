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

### 전사 기반 상세 보강

- 세션 맥락: [현대카드] 현대카드 데이터 사이언스 플랫폼 진화 여정: Hybrid to Coding 에이전트
- 공식 설명 보강: 현대카드가 온프레미스-클라우드 하이브리드 아키텍처(HDSP)를 구축하고, 이를 기반으로 SageMaker 환경에서 코딩 에이전트를 구현한 여정을 공유합니다. 금융권 특유의 보안·규제 환경에서 오픈소스 LLM을 활용해 실시간 코드 제안, 코드 리뷰 등 개발 생산성을 향상시킨 실용적 사례를 다룹니다.
- 전사에서 반복적으로 확인된 키워드: 코드, 에이전트, 데이터, GPU, 개발, 인프라, 비용, 리뷰, 감사, 운영
- 발표에서 두드러진 주제 축: developer, infra, agent, data

#### 발표 흐름
- 초반: GPU, 데이터, 개발, 비용, 인프라 중심으로 developer, infra, agent를 다룬다.
- 중반: 코드, 에이전트, 개발, 비용, 데이터 중심으로 developer, infra, agent를 다룬다.
- 후반: 코드, 에이전트, 개발, 리뷰, 데이터 중심으로 developer, infra, agent를 다룬다.

#### 전사에서 확인할 만한 구간
- 01:01 부근: 개발, 에이전트, 코드 관련 설명이 나온다. 핵심 문맥은 `세이지메이커 기반의 코딩 에이전트 코드버프를 개발하던 개발 여정기를 함께 들어보고자합니다.`
- 07:35 부근: EKS, GPU 관련 설명이 나온다. 핵심 문맥은 `전체 EKS를 관리하는 부담, GPU를 관리하는 부담을`
- 15:39 부근: 인프라, 코드 관련 설명이 나온다. 핵심 문맥은 `뺑지는 호출하면 한 번장 코드가 양쪽 인프라를 인식해서 동작`
- 20:34 부근: 배포, 코드 관련 설명이 나온다. 핵심 문맥은 `배포 나가는 시점에 다시 코드를 튜닝하고`
- 20:55 부근: 에이전트, 코드 관련 설명이 나온다. 핵심 문맥은 `클로드 코드나 AWS 키로와 같은 훌륭한 코딩 에이전트가 이미 시중에`
