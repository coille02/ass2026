# AWS Summit Seoul 2026 Industry Day - Batch 2 Summaries

> Worker 2 assigned sessions: sel-wps105, sel-ind225, sel-ind233, sel-ind206, sel-ind212, sel-ind210, sel-ind224, sel-ind302, sel-ind204. All summaries below are based on generated VOD transcripts plus official session metadata.

## sel-wps105

**Title/Time/Track/Speakers**  
- 제목: [정보통신산업진흥원] AI G3 코리아: NIPA와 AWS가 만드는 공공 혁신
- 시간: 2026-05-20 11:10-11:50 KST
- 트랙: Industry Day / Government, Healthcare & Life Sciences, State and Local Government / Analytics, Industry Solutions
- 발표자: 김득중 부원장, 정보통신산업진흥원 NIPA

**핵심 요약**  
NIPA가 대한민국의 AI G3 도약을 위해 추진하는 공공 AX 전략과 2026년 주요 사업 방향을 소개한 세션이다. 발표에서는 정부 AI 예산 확대, AI 컴퓨팅 인프라, 국산 AI 반도체, 한국형 파운데이션 모델, 피지컬 AI, 산업·공공 AI 대전환 프로젝트가 핵심 축으로 제시됐다. 전사에서는 올해 정부 AI 예산 10.1조 원 중 NIPA가 큰 비중을 맡고, 에이전트 사업 경쟁률이 28:1 수준이었다는 언급이 반복된다. AWS는 공공·민간 실증, 글로벌 진출, 공공부문 AI 인재 양성, 클라우드 인프라 활용 측면에서 협력 파트너로 포지셔닝됐다.

**주요 포인트**
- AI 고속도로 관점에서 AI 컴퓨팅 센터, 지역 데이터센터, 수요자 대상 컴퓨팅 자원 제공을 강조.
- 국산 AI 반도체는 공공 조달, 실증 과제 확대, 해외 실증을 통해 생태계 검증과 확산을 추진.
- 피지컬 AI는 제조·로봇·산업 현장과 연결되는 차세대 공공 프로젝트로 제시.
- 공공과 민간이 함께 투자하는 인프라 모델과 해외 AI 교육센터 등 글로벌 확산 계획을 언급.
- "선정/탈락" 중심이 아니라 기업이 실제 과제를 만들고 글로벌 경쟁력을 확보하도록 돕는 파트너 역할을 강조.

**AWS/기술 키워드**  
AWS, 공공 AX, AI G3, AI 컴퓨팅 인프라, 국산 AI 반도체, 파운데이션 모델, 피지컬 AI, 데이터센터, 글로벌 실증

**현장 메모로 남길 점**  
NIPA 발표는 특정 서비스 데모보다 정책·예산·생태계 방향성이 중심이다. 블로그에서는 "공공 AI는 클라우드 인프라와 실증 사업이 결합될 때 산업 정책이 실행력으로 바뀐다"는 메시지가 잘 살아난다.

**블로그용 한줄**  
NIPA는 AI 인프라, 반도체, 피지컬 AI, 글로벌 실증을 묶어 대한민국 AI G3 전략을 실행 가능한 공공 AX 로드맵으로 제시했다.

## sel-ind225

**Title/Time/Track/Speakers**  
- 제목: [삼성전자] 삼성전자의 에이전틱 AI 전략- 개발혁신과 AIOps 여정
- 시간: 2026-05-20 12:50-13:30 KST
- 트랙: Industry Day / Manufacturing & Industrial, Software & Internet / Artificial Intelligence, Open Source
- 발표자: 유현성 그룹장, 삼성전자; 김제민 파트장, 삼성전자

**핵심 요약**  
삼성전자는 Samsung Account처럼 21억 글로벌 사용자와 대규모 EKS 환경을 운영하는 비즈니스 크리티컬 시스템에서 에이전틱 AI를 개발과 운영 양쪽에 적용한 경험을 공유했다. 개발 영역에서는 AI-DLC 방식으로 의도와 실행을 분리하고, Knowledge Base와 Human-in-the-Loop 거버넌스를 결합해 리드타임을 약 70% 단축했다고 설명했다. 운영 영역에서는 AIOps, SecOps, FinOps, 변경관리 분과에 에이전트를 배치해 장애 탐지, 변경 영향도 분석, WAF/로그 분석, 자동 롤백 같은 반복 업무를 줄이는 방향을 제시했다. 발표의 결론은 에이전트를 도입하는 것 자체보다 엔지니어의 판단 구조와 거버넌스를 보존하는 "Human First" 운영 모델이 중요하다는 점이다.

**주요 포인트**
- 삼성계정은 초당 수백만 요청, 수십 개 네임스페이스의 EKS 클러스터를 운영하는 환경으로 소개됨.
- 운영 에이전트와 보안 에이전트는 단순 챗봇이 아니라 도구 선택과 행동 수행을 포함하는 에이전틱 AI로 설명.
- AI-DLC는 요구사항, 계획, 검증, 실행을 분리해 품질 편차와 대기 시간을 줄이는 구조.
- AIOps 목표로 장애 탐지율 개선, MTTR 단축, Human-in-the-Loop 비율 축소가 언급됨.
- Kiro, Amazon Q, Amazon Bedrock AgentCore를 직접 호출하지 않고 보안 검토와 내부 경유 구조를 두는 방식이 강조됨.

**AWS/기술 키워드**  
Amazon EKS, Amazon Bedrock AgentCore, Amazon Q, Kiro, AIOps, SecOps, FinOps, WAF 로그, Knowledge Base, Human-in-the-Loop, RBAC/ABAC

**현장 메모로 남길 점**  
삼성 사례의 핵심은 "AI가 코드를 더 빨리 쓰게 한다"보다 "대규모 운영 조직의 일하는 방식을 다시 설계한다"에 가깝다. 보안·거버넌스·운영 승인 체계를 먼저 세운 뒤 에이전트를 붙이는 순서가 인상적이다.

**블로그용 한줄**  
삼성전자는 에이전틱 AI를 개발 생산성 도구가 아니라 AIOps와 거버넌스를 포함한 엔터프라이즈 운영 체계로 확장하고 있다.

## sel-ind233

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

## sel-ind206

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

## sel-ind212

**Title/Time/Track/Speakers**  
- 제목: [AB180] AB180이 SaaS 에이전틱 AI를 설계하는 방법
- 시간: 2026-05-20 12:50-13:30 KST
- 트랙: Industry Day / Advertising & Marketing / Artificial Intelligence
- 발표자: 김진아 솔루션즈 아키텍트, AWS; 이승헌 프로덕트 오너, AB180

**핵심 요약**  
AB180은 RAG 기반 챗봇 ASK Airbridge에서 출발해 Airbridge Pilot이라는 SaaS 에이전틱 AI로 진화한 과정을 소개했다. 초기 챗봇은 유효 답변율이 30% 미만이어서 사람 개입이 필요했지만, 발표에서는 답변 성공률을 28%에서 91%까지 끌어올렸다고 설명했다. 핵심 설계는 에이전트가 사용자의 목표를 이해하고 Airbridge 데이터와 외부 도구를 MCP로 호출해 실제 작업까지 수행하도록 만드는 것이다. Bedrock AgentCore는 게이트웨이, 런타임, 메모리, 도구 호출, 평가 체계를 묶어 SaaS 사업자가 직접 운영하기 어려운 에이전트 운영 요소를 관리하는 기반으로 제시됐다.

**주요 포인트**
- 에이전틱 AI를 "맥락을 기억하고 필요한 도구를 선택해 환경에 행동을 내보내는 시스템"으로 정의.
- B2B SaaS에서는 단순 답변보다 고객의 KPI, 캠페인 데이터, 설정 상태를 이해하는 제품 내 실행력이 중요.
- MCP를 통해 Airbridge 기능과 외부 도구를 연결하고, CLI나 에이전트 인터페이스에서 SaaS 기능을 호출하는 방향을 제시.
- 정확도, 비용, 속도, 보안, 잘못된 도구 호출 가능성, 데이터 유출 책임 등이 설계 이슈로 다뤄짐.
- 향후 SaaS 경쟁력은 편한 UI뿐 아니라 에이전트가 직접 일할 수 있는 인프라와 API/도구 생태계로 이동한다고 전망.

**AWS/기술 키워드**  
Amazon Bedrock AgentCore, MCP, AgentCore Gateway, AgentCore Runtime, Agent Memory, RAG, Airbridge Pilot, ASK Airbridge, SaaS, GTM, Product-led Growth

**현장 메모로 남길 점**  
AB180 사례는 SaaS의 사용 경험이 "사용자가 화면을 조작"하는 방식에서 "에이전트가 목표를 수행"하는 방식으로 이동하고 있음을 보여준다. 보안과 도구 권한 설계가 제품 경쟁력의 일부가 된다는 점이 중요하다.

**블로그용 한줄**  
AB180은 Bedrock AgentCore와 MCP를 활용해 RAG 챗봇을 실제 마케팅 업무를 수행하는 SaaS 에이전트로 발전시키고 있다.

## sel-ind210

**Title/Time/Track/Speakers**  
- 제목: [포스코] POSCO 광양제철소 설비 예지정비 혁신: AWS Kiro와 MLOps
- 시간: 2026-05-20 12:50-13:30 KST
- 트랙: Industry Day / Manufacturing & Industrial / Artificial Intelligence, Developer Tools, Industry Solutions
- 발표자: 조성철 시니어 솔루션즈 아키텍트, AWS; 조현영 리더, 포스코

**핵심 요약**  
포스코 광양제철소는 설비 예지정비에서 현장 엔지니어가 직접 AI 모델을 만들고 운영할 수 있도록 AWS Kiro와 SageMaker MLOps를 결합한 사례를 발표했다. 기존에는 모델 하나를 만드는 데 워킹데이 기준 약 2주가 필요했고, 배포까지 포함하면 한 달 이상 걸리는 구조였지만, 발표에서는 이노핀스(InnoPince) 기반 프로세스로 약 2주 작업을 2시간 수준으로 줄였다고 설명했다. Kiro는 장애 보고서와 센서 데이터를 분석해 전조 신호와 알고리즘 후보를 제시하고, SageMaker MLOps는 전처리·훈련·평가·배포·모니터링·재학습을 자동화한다. 제조 현장의 도메인 지식이 모델 개발의 핵심 입력이 되도록 만든 점이 세션의 중심 메시지다.

**주요 포인트**
- 예지정비 도입의 장애물로 모델 개발 시간, 수많은 설비 확장성, 대정비 이후 기준치 재조정 문제가 제시됨.
- Kiro는 요구사항 정의, 데이터 분석, 알고리즘 추천, 모델 코드 생성까지 지원하는 AI 에이전트로 설명.
- SageMaker Model Monitor가 드리프트를 감지하면 재학습 파이프라인과 모델 교체가 이어지는 구조를 설계.
- 고장 이전 패턴과 전조 신호를 조기에 탐지해 2시간 이상 라인 정지 가능성이 있는 상황에 선제 대응하는 목표를 제시.
- 향후 모델 공장을 선정하고 AWS 클라우드와 연계해 제조 현장 AI 혁신 범위를 확대할 계획을 공유.

**AWS/기술 키워드**  
AWS Kiro, Amazon SageMaker, SageMaker MLOps, SageMaker Model Monitor, 예지정비, 드리프트 감지, 자동 재학습, 제조 AI, InnoPince

**현장 메모로 남길 점**  
제조 AI의 병목은 모델 알고리즘보다 현장 데이터 해석과 운영 자동화에 있다. 포스코 사례는 현장 엔지니어의 지식을 Kiro가 구조화하고 SageMaker가 운영화하는 조합으로 읽힌다.

**블로그용 한줄**  
포스코는 Kiro와 SageMaker MLOps를 결합해 제철소 예지정비 모델 개발을 현장 주도형 AI 운영 체계로 전환했다.

## sel-ind224

**Title/Time/Track/Speakers**  
- 제목: [Config] 피지컬 AI 기업 Config의 AWS 기반 Robotics Foundation Model 개발 여정
- 시간: 2026-05-20 12:50-13:23 KST
- 트랙: Industry Day / Artificial Intelligence
- 발표자: 손형목 최고 기술 책임자, Config

**핵심 요약**  
Config는 양팔 로봇 작업에 특화된 VLA(Vision Language Action) 기반 Robotics Foundation Model 개발 여정을 소개했다. 발표의 핵심은 로봇 파운데이션 모델의 성능을 좌우하는 것은 단순히 많은 데이터가 아니라 물체, 환경, 액션, 작업 맥락이 다양하게 분포된 고품질 액션 데이터라는 점이다. Config는 서울과 베트남 하노이에 자체 데이터 생산 인프라를 구축하고, 월 2만-3만 시간 수준의 데이터를 만들며 누적 13만 시간 규모를 언급했다. AWS Direct Connect, Amazon S3, DynamoDB, Amazon EKS, GPU 인프라를 조합해 데이터 업로드·처리·학습·추론 비용을 관리하는 방식도 공유했다.

**주요 포인트**
- RFM/로봇 파운데이션 모델은 텍스트·이미지 모델보다 실제 액션 데이터 확보가 훨씬 큰 병목으로 제시됨.
- 좋은 데이터는 다양한 물체, 환경, 작업, 액션을 포함해야 하며 데이터에 없는 상황에 일반화하는 능력이 중요.
- 사람의 액션을 라벨링하고 품질을 자동 평가하는 데이터 파이프라인을 구축했다고 설명.
- Direct Connect를 통해 자체 데이터 생산 시설에서 S3와 DynamoDB로 안정적이고 비용 효율적으로 데이터를 업로드.
- 학습에는 H100/B200급 노드, 추론에는 L40S 같은 상대적으로 저렴한 인스턴스를 쓰는 식으로 역할별 비용 최적화를 언급.

**AWS/기술 키워드**  
Robotics Foundation Model, VLA, Physical AI, AWS Direct Connect, Amazon S3, Amazon DynamoDB, Amazon EKS, SageMaker HyperPod, H100/B200, L40S, Teleoperation Data

**현장 메모로 남길 점**  
피지컬 AI는 모델보다 데이터 생산 공장이 먼저 필요하다는 점이 선명했다. 클라우드는 학습 플랫폼일 뿐 아니라 실제 세계의 액션 데이터를 안정적으로 옮기고 정제하는 운영 인프라다.

**블로그용 한줄**  
Config는 자체 액션 데이터 생산 체계와 AWS 기반 데이터·학습 인프라를 결합해 로봇 파운데이션 모델을 만들고 있다.

## sel-ind302

**Title/Time/Track/Speakers**  
- 제목: [CJ ENM Mnet Plus] K-POP 글로벌 라이브: Mnet+ 4K와 AI 자막
- 시간: 2026-05-20 12:50-13:30 KST
- 트랙: Industry Day / Media & Entertainment / Artificial Intelligence, Cloud Operations, Networking & Content Delivery
- 발표자: 임윤택 솔루션즈 아키텍트, AWS; 박찬규 Platform Engineering, CJ ENM Mnet Plus; 이재황 Platform Engineering, CJ ENM Mnet Plus

**핵심 요약**  
Mnet Plus는 MAMA AWARDS와 KCON 같은 글로벌 K-POP 라이브 이벤트에서 4K 스트리밍과 AI 자막을 운영한 경험을 공유했다. 전사에서는 60만 동시 접속자와 1.6PB 트래픽을 처리하면서 4K 고화질 서비스를 안정적으로 제공했다는 수치가 언급됐다. 라이브 아키텍처는 2개 AWS 리전의 MediaLive, MediaPackage, S3를 독립 구성해 장애 발생 시 백업 리전으로 전환하는 구조로 설명됐다. AI 자막은 S3 이벤트, SQS, STT, LLM, Bedrock 기반 처리, 프롬프트 레이어, 다국어 번역, 비용 최적화와 장애 폴백을 묶은 실시간 파이프라인으로 소개됐다.

**주요 포인트**
- 외부 플랫폼 의존에서 벗어나 자체 라이브 플랫폼을 구축해 DRM, 속기사 자막, 4K, AI 자막까지 단계적으로 확장.
- MediaLive/MediaPackage/S3를 2개 리전에 독립 구성해 한쪽 장애에도 라이브를 지속할 수 있게 설계.
- CloudFront Origin Shield와 ABR 기반 스트리밍으로 글로벌 동시 접속 트래픽이 오리진에 직접 몰리지 않도록 구성.
- 4K 구간은 최신 코덱을 활용해 비트레이트를 30-50% 절감하는 전략을 설명.
- AI 자막은 STT 결과를 바로 번역하지 않고 K-POP 도메인 맥락, 방송 메타데이터, 출력 규칙 프롬프트를 계층화해 환각과 부자연스러운 번역을 줄이는 방향으로 설계.

**AWS/기술 키워드**  
AWS Elemental MediaLive, AWS Elemental MediaPackage, Amazon S3, Amazon CloudFront, Origin Shield, Amazon SQS, Amazon Bedrock, STT, LLM, ABR, 4K Streaming, AI Subtitles

**현장 메모로 남길 점**  
Mnet Plus 사례는 미디어 아키텍처와 생성형 AI가 같은 운영 문제 안에서 만나는 좋은 예다. 라이브 서비스에서는 정확도뿐 아니라 지연, 폴백, 비용, 도메인 용어, 국가별 반응까지 함께 설계해야 한다.

**블로그용 한줄**  
Mnet Plus는 멀티 리전 라이브 스트리밍과 Bedrock 기반 AI 자막을 결합해 글로벌 K-POP 팬에게 4K 라이브 경험을 제공했다.

## sel-ind204

**Title/Time/Track/Speakers**  
- 제목: [놀유니버스] AWS Transform을 통한 놀유니버스의 .NET 현대화
- 시간: 2026-05-20 12:50-13:30 KST
- 트랙: Industry Day / Software & Internet, Travel & Hospitality / Artificial Intelligence, Migration & Modernization
- 발표자: 최준영 테크니컬 어카운트 매니저, AWS; 지윤성 실장, 놀유니버스

**핵심 요약**  
놀유니버스는 28년간 누적된 .NET 레거시 시스템을 AWS Transform for .NET과 Kiro를 활용해 현대화한 사례를 공유했다. 발표에서는 150만 라인, 1,575개 파일을 10시간 만에 분석·전환했고, Kiro로 223개 테스트를 20초 만에 자동 생성했다는 수치가 등장했다. AWS Transform은 프로젝트 전체 의존성 그래프를 분석하고 코드 그룹 단위로 병렬 변환을 오케스트레이션했으며, Kiro는 후속 테스트와 안정화에 쓰인 구조로 설명됐다. 결과적으로 4주 만에 레거시 현대화를 완료하고 컨테이너 기반 AWS 환경, CloudWatch 모니터링, 생산성 3배 향상, 비용 절감 효과를 얻었다고 정리했다.

**주요 포인트**
- 현대화 지연의 이유로 시스템 중단 우려, 비용·리소스 부담, 기술 부채, 복잡한 의존성이 제시됨.
- AWS Transform은 단일 파일 변환이 아니라 전체 프로젝트의 의존성, 변환 순서, 병렬 작업 단위를 잡아주는 에이전틱 AI 시스템으로 소개.
- Kiro는 변환 이후 테스트 자동 생성과 후속 안정화에 투입되어 검증 속도를 높임.
- 컨테이너 기반 배포와 CloudWatch 모니터링으로 운영 체질이 바뀌었다고 설명.
- 발표의 결론은 AI 도구 자체보다 기술 부채 청산을 시작할 실행 체계를 갖추는 것이 중요하다는 메시지.

**AWS/기술 키워드**  
AWS Transform for .NET, Kiro, .NET Framework Modernization, Containers, Amazon CloudWatch, 에이전틱 AI, 의존성 그래프, 테스트 자동화, 기술 부채

**현장 메모로 남길 점**  
현대화는 "코드 변환"보다 "의존성 이해, 검증, 배포, 운영 전환"이 더 큰 과제다. AWS Transform과 Kiro를 역할 분리해 쓴 점이 실제 레거시 전환 사례로 설득력 있다.

**블로그용 한줄**  
놀유니버스는 AWS Transform for .NET과 Kiro로 28년 레거시를 분석·전환·검증하며 .NET 현대화의 실행 속도를 끌어올렸다.
