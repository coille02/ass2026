# sel-ind233 - [AMOREPACIFIC] AMOREPACIFIC의 AWS 기반 AI뷰티테크 플랫폼 서비스

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

**Title/Time/Track/Speakers**  
- 제목: [AMOREPACIFIC] AMOREPACIFIC의 AWS 기반 AI뷰티테크 플랫폼 서비스
- 시간: 2026-05-20 12:50-13:30 KST
- 트랙: Industry Day / Retail & Consumer Goods / Artificial Intelligence, Industry Solutions
- 발표자: 김종혁 솔루션즈 아키텍트, AWS; 노치국 상무, AMOREPACIFIC

**핵심 요약**  
아모레퍼시픽은 뷰티 카운슬러의 경험과 피부·두피·컬러 데이터를 AI 플랫폼으로 표준화한 여정을 소개했다. 발표 전반부는 Amazon EKS 기반 마이크로서비스와 Amazon SageMaker 기반 진단 모델로 사진 한 장에서 피부 상태를 분석하고, 원본 이미지는 즉시 삭제하는 보안·개인정보 보호 흐름을 설명했다. 후반부는 오프라인 상담 노하우, 연구 데이터, 고객 경험을 "AI-ready data"로 바꾸는 것이 단순 데이터 축적보다 중요하다는 메시지에 집중했다. 향후에는 Amazon Bedrock AgentCore 기반 AI 뷰티 카운슬링과 Beauty Tech as a Service 형태의 확장을 목표로 제시했다.

**주요 포인트**
- 피부 사진을 여러 AI 모델이 동시에 진단해 모공, 주름, 멜라닌, 홍반 등 세부 상태를 분석.
- 앱, 매장 키오스크, 웹 어디서든 동일 품질의 진단 경험을 제공하는 플랫폼화를 지향.
- EKS 기반 마이크로서비스, SageMaker 기반 모델 운영, 보안 모니터링, 데이터 수집·진단·결과 사이클을 결합.
- 2년에 걸친 IDC의 AWS 마이그레이션 이후 AI 뷰티테크 플랫폼을 확장했다고 언급.
- 생성형 AI 시대에는 고객을 "가족처럼 잘 아는" 도메인 데이터와 성분·주의사항 지식이 차별화 포인트가 된다고 설명.

**AWS/기술 키워드**  
Amazon EKS, Amazon SageMaker, Amazon Bedrock AgentCore, AI Beauty Tech, Beauty Concierge, 마이크로서비스, AI-ready data, 개인정보 보호, SaaS

**현장 메모로 남길 점**  
뷰티 AI의 경쟁력은 모델 자체보다 측정 데이터, 상담 노하우, 제품 지식, 고객 맥락을 하나의 서비스 흐름으로 묶는 데 있다. "데이터가 많다"와 "AI가 쓸 수 있는 데이터다"의 차이를 블로그에서 짚으면 좋다.

**블로그용 한줄**  
아모레퍼시픽은 AWS 기반 진단 플랫폼으로 뷰티 카운슬러의 경험을 표준화하고, AI 뷰티테크를 서비스형 플랫폼으로 확장하고 있다.

### 전사 기반 상세 보강

- 세션 맥락: [AMOREPACIFIC] AMOREPACIFIC의 AWS 기반 AI뷰티테크 플랫폼 서비스
- 공식 설명 보강: AMOREPACIFIC Beauty Concierge(Beauty Tech as a Service)는 AWS와 함께 K-뷰티 산업의 소프트웨어 경계를 확장한 플랫폼입니다. Amazon SageMaker와 EKS를 기반으로 개별 진단 도구를 뷰티 카운셀링 서비스로 진화시킨 여정과, 다양한 AI 진단 서비스를 통한 비즈니스 가치 창출 사례 및 SaaS 전환 전략을 소개합니다.
- 전사에서 반복적으로 확인된 키워드: 고객, 데이터, 에이전트, 개발, 상담, 추천, 인프라, 표준, 감사, 리뷰
- 발표에서 두드러진 주제 축: business, data, developer, agent

#### 발표 흐름
- 초반: 데이터, 고객, 개발, 인프라, EKS 중심으로 business, data, developer를 다룬다.
- 중반: 고객, 데이터, 추천, 개발, 표준 중심으로 business, data, developer를 다룬다.
- 후반: 에이전트, 고객, 상담, 데이터, 인가 중심으로 business, data, developer를 다룬다.

#### 전사에서 확인할 만한 구간
- 04:26 부근: 고객, 상담 관련 설명이 나온다. 핵심 문맥은 `고객의 구매 이력이라든지 상담내역`
- 07:04 부근: S3, 데이터 관련 설명이 나온다. 핵심 문맥은 `분성형 데이터는 아마존 S3 기반의 데이터레이크에 싸워서 다시 AI가 학습할 수 있도록 했습니다.`
- 14:01 부근: 고객, 추천 관련 설명이 나온다. 핵심 문맥은 `그리고 넷플릭스는 추천으로 고객의 선택을 만들어냈고`
- 22:44 부근: 고객, 데이터 관련 설명이 나온다. 핵심 문맥은 `바로 고객 여정의 데이터 기반에`
- 28:52 부근: 상담, 추천 관련 설명이 나온다. 핵심 문맥은 `진단 상담, 추천, 검색, 기존을 갖고 있던 모든 요소 AI 기술을`
