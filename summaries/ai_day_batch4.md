# AI Day Batch 4 요약

## sel-prt212-s - Snowflake + AWS 통합 AI 전략: Cortex Code가 연결하는 데이터와 인텔리전스 (sponsored by Snowflake)

- 시간/트랙/레벨/발표자: 15:30-15:50 KST / Track 6 / 200 - Intermediate / 김현정, Senior Partner Solution Engineer, Snowflake
- 요약: Snowflake와 AWS를 함께 써서 엔터프라이즈 AI용 통합 데이터 파운데이션을 만드는 접근을 소개했다. 발표자는 Snowflake 고객의 상당수가 AWS 리전에서 운영 중이며, S3, Glue Catalog, Iceberg, Bedrock, MCP, Cortex AI/Agent, Amazon Quick, AgentCore 같은 연동으로 데이터 이동 없이 AI 워크플로를 구성할 수 있다고 설명했다.
- 주요 포인트:
  - AI 도입의 과제를 복잡한 파이프라인, 분산된 도구, LLM 통제/보안 요구로 정리하고, Snowflake의 편의성, 연결성, 신뢰성을 해결 축으로 제시했다.
  - AWS Marketplace 원클릭 시작, S3 External Stage, Glue Catalog/Iceberg 통합으로 기존 데이터 레이크와 연결하는 패턴을 강조했다.
  - Bedrock 기반 모델, Cortex AI, Cortex Agent/Code를 통해 자연어 기반 데이터 탐색, 코드 생성, 커스텀 앱/에이전트 개발을 가속하는 흐름을 소개했다.
  - 고객 사례에서는 단일 데이터 소스와 거버넌스 체계를 통해 접근 속도와 전사 데이터 통제를 개선하고 AI 인사이트 탐색까지 확장했다고 설명했다.
- AWS/기술 키워드: Snowflake, AWS Marketplace, Amazon S3, AWS Glue Data Catalog, Apache Iceberg, Amazon Bedrock, MCP, Cortex AI, Cortex Agent, Cortex Code, Amazon Quick, Bedrock AgentCore
- AX TF 관점/회사 AX 도입 시사점: AX 도입은 모델보다 데이터 연결과 거버넌스가 먼저 병목이 된다. 사내 데이터 레이크/웨어하우스에서 데이터를 복사하지 않고 AI 도구가 안전하게 접근하는 표준 경로를 만들고, 개발자는 자연어/코드 생성 도구를 붙여 데이터 분석 앱과 에이전트를 빠르게 실험할 수 있게 해야 한다.
- 공유용 한줄: Snowflake+AWS 조합은 "데이터 이동 없는 AI"와 중앙 거버넌스를 동시에 노리는 엔터프라이즈 AX 데이터 기반 전략이다.

## sel-prt102-s - 3가지 관점으로 살펴보는 Red Hat OpenShift Service on AWS(ROSA)를 활용한 현대화의 새로운 접근 방식 (sponsored by Red Hat)

- 시간/트랙/레벨/발표자: 15:30-15:50 KST / Track 7 / 100 - Foundational / 송찬규, 부장, 한국레드햇
- 요약: 레거시 VM, 컨테이너, 서버리스, AI가 공존하는 복잡한 IT 환경에서 ROSA를 활용해 현대화하는 방식을 설명했다. 발표자는 기존 애플리케이션 운영 지식, 상용 소프트웨어 지원 체계, AI 도구 도입 역량 부족을 장벽으로 보고, AWS와 Red Hat이 제공하는 관리형 OpenShift가 이를 완화한다고 정리했다.
- 주요 포인트:
  - 전통 애플리케이션과 신규 AI 프로젝트를 동시에 지원해야 하는 운영팀의 현실을 문제 정의로 삼았다.
  - OpenShift/ROSA는 컨테이너 플랫폼 표준화, 보안/컴플라이언스, 하이브리드 운영 일관성을 제공하는 현대화 기반으로 소개됐다.
  - VM과 컨테이너를 함께 관리하는 관점, 기존 운영 체계와 클라우드 네이티브 전환을 연결하는 관점, AI 워크로드까지 수용하는 관점을 제시했다.
  - 글로벌 레퍼런스에서는 인프라 운영 부담을 낮추고 배포 시간을 줄이며 비즈니스 집중도를 높인 효과를 언급했다.
- AWS/기술 키워드: Red Hat OpenShift Service on AWS, ROSA, OpenShift, Kubernetes, Hybrid Cloud, VM/Container 통합, Migration & Modernization
- AX TF 관점/회사 AX 도입 시사점: AI 프로젝트를 별도 섬처럼 만들면 운영 복잡도가 커진다. 기존 VM/컨테이너 운영 체계와 AI 워크로드 배포 체계를 같은 플랫폼 원칙으로 묶어야 AX 실험이 운영 표준과 충돌하지 않는다.
- 공유용 한줄: ROSA 세션의 핵심은 레거시 현대화와 AI 워크로드 수용을 같은 컨테이너 플랫폼 전략으로 묶자는 것이다.

## sel-prt220-s - 당신의 AI 환경은 안녕하신지요? (sponsored by Zscaler)

- 시간/트랙/레벨/발표자: 15:30-15:50 KST / Track 8 / 200 - Intermediate / 인승진, 전무, Zscaler
- 요약: 직원용 SaaS AI, 사내 AI 서비스, 고객 대상 AI, 에이전트형 AI가 동시에 늘어나는 환경에서 제로 트러스트 기반 보안이 필요하다는 내용이었다. 발표자는 AI 보안이 완전히 새로운 원칙이 아니라 기존 보안의 가시성, 통제, 데이터 보호, 접근 제어를 AI 사용 경로에 맞게 확장하는 것이라고 설명했다.
- 주요 포인트:
  - AI 사용이 확산되며 내부 정보 유출, 모델 학습 데이터 노출, 에이전트 권한 관리, 외부 서비스 접속 통제가 주요 고민으로 부상했다.
  - Bedrock 같은 AWS AI 플랫폼 자체의 보안 기능과 함께, 사용자/앱/API/에이전트 트래픽을 중간에서 관찰하고 통제하는 보안 플랫폼이 필요하다고 설명했다.
  - Zscaler 플랫폼은 AI 사용 트랜잭션 모니터링, 보안 검사, 수정/강화, 통합 가시성을 제공하는 방향으로 소개됐다.
  - 전 세계 보안 클라우드와 통합 컨트롤을 기반으로 AI 사용 현황과 위험을 한 곳에서 운영해야 한다고 강조했다.
- AWS/기술 키워드: Zero Trust, Zscaler, Amazon Bedrock, AI Security, SaaS AI, Private AI, Agentic AI, API 보안, 데이터 유출 방지
- AX TF 관점/회사 AX 도입 시사점: 사내 AX 도구가 늘어나면 "누가 어떤 AI에 어떤 데이터를 보냈는가"를 볼 수 있어야 한다. Claude Code류 도구, 사내 에이전트, 외부 SaaS AI 사용 경로를 정책/로그/차단 관점으로 분류하고 제로 트러스트 원칙을 적용해야 한다.
- 공유용 한줄: AI 보안은 도입 후 감사가 아니라, AI 사용 경로 전체를 보이는 상태로 만드는 것부터 시작한다.

## sel-dev308 - [미러] 맥 미니 없이도 서버리스로 만드는 AI Cloud Agent

- 시간/트랙/레벨/발표자: 15:30-15:50 KST / Track 9 / 300 - Advanced / 이상현, CEO, Serverless Hero, 미러
- 요약: 로컬 Mac mini에서 돌리는 에이전트 루프를 AWS 서버리스 아키텍처로 옮기는 관점을 소개했다. 발표자는 에이전트가 본질적으로 채팅 히스토리, LLM 호출, tool call 실행, 상태 저장, 외부 이벤트 처리로 구성된 일반 소프트웨어이며, Lambda와 DynamoDB 등으로 충분히 클라우드화할 수 있다고 설명했다.
- 주요 포인트:
  - OpenClaw/Claude Code류 로컬 에이전트를 예로 들며, 실제 에이전트 루프 자체는 30줄 안팎의 반복 구조라고 설명했다.
  - 로컬 프로세스에 묶여 있던 상태, 이벤트 큐, 코드 샌드박스, 외부 서비스 연동을 클라우드 컴포넌트로 분리하는 방식이 핵심이다.
  - Lambda 요청, DynamoDB 상태 저장, 외부 이벤트 기반 실행으로 사용한 만큼만 비용을 내는 구조를 제안했다.
  - 에이전트도 웹서버/백그라운드 워커처럼 스테이트리스화, 배포 자동화, 관측성 설계가 필요한 소프트웨어라고 강조했다.
- AWS/기술 키워드: AWS Lambda, Amazon DynamoDB, Serverless, Agent Loop, Tool Calling, Event Queue, Code Sandbox, Claude Code-like Agent
- AX TF 관점/회사 AX 도입 시사점: 사내 개발 에이전트를 개인 PC에만 두면 권한, 비용, 재현성, 배포 통제가 어렵다. 반복 실행되는 업무 에이전트는 서버리스 백엔드로 빼고, 상태/권한/로그를 중앙화하면 팀 단위 AX 자동화 자산으로 운영할 수 있다.
- 공유용 한줄: 에이전트는 신비한 별도 장르가 아니라 서버리스로 운영 가능한 상태ful 업무 소프트웨어다.

## sel-aim303 - 40분 완성! SageMaker AI 기반 에이전틱 모델 구축 및 배포

- 시간/트랙/레벨/발표자: 16:10-16:50 KST / Track 1 / 300 - Advanced / 박지윤, 솔루션즈 아키텍트, AWS; 강광일, 테크니컬 어카운트 매니저, AWS
- 요약: SageMaker AI로 에이전틱 AI에 필요한 모델 커스터마이징, 배포, AgentCore 연동까지 엔드투엔드로 구현하는 흐름을 다뤘다. 발표자는 생성형 AI에서 에이전틱 AI로 넘어가며 추론 컴퓨팅 요구가 커지고, 업무별 모델을 비용 효율적으로 커스터마이징/서빙하는 역량이 중요해졌다고 설명했다.
- 주요 포인트:
  - 에이전틱 워크플로는 다단계 추론과 tool call 때문에 토큰/컴퓨팅 수요가 급증하며, 모델 커스터마이징과 쿼터/용량 관리가 중요해진다.
  - Salesforce 사례를 들어 오픈소스 모델 기반 사전학습/파인튜닝/고품질 답변 튜닝으로 hallucination을 줄이고 특화 모델을 운영하는 패턴을 소개했다.
  - SageMaker AI의 파인튜닝 환경, 멀티 모델/멀티 컨테이너/Inference Component 기반 배포, 비용 효율적 엔드포인트 운영을 설명했다.
  - 데모에서는 의료 상담 모델을 배포하고 Bedrock AgentCore Runtime에 Docker 기반 에이전트를 배포해 증상 질의, 병원 추천, 예약 흐름까지 연결했다.
- AWS/기술 키워드: Amazon SageMaker AI, Fine-tuning, Open-source LLM, vLLM DLC, Inference Component, Multi-model Endpoint, Amazon Bedrock AgentCore Runtime, AWS CodeBuild
- AX TF 관점/회사 AX 도입 시사점: 범용 모델 호출만으로 끝내지 말고, 업무 도메인별 특화 모델을 만들고 이를 에이전트 런타임에 연결하는 표준 파이프라인이 필요하다. 특히 비용 추적, 엔드포인트 배포 방식, 평가 기준을 초기에 잡아야 AX 서비스가 실험 단계에서 운영 단계로 넘어갈 수 있다.
- 공유용 한줄: SageMaker AI는 특화 모델을 만들고 AgentCore에 붙이는 AX 모델 운영 파이프라인의 좋은 기준점이다.

## sel-ant202 - 나야, 차세대 OpenSearch: 에이전틱 AI를 곁들인

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

## sel-dvt303 - 프로덕션으로 가기 위한 에이전틱 AI 아키텍처 설계하기

- 시간/트랙/레벨/발표자: 16:10-16:50 KST / Track 3 / 300 - Advanced / 이유정, AI/ML 전문 솔루션즈 아키텍트, AWS; 류하선, AI/ML 전문 솔루션즈 아키텍트, AWS
- 요약: POC 수준 에이전트를 프로덕션으로 확장하려면 모델, 도구, 메모리, 게이트웨이, 관측성, 평가, 운영 체계를 갖춘 파운데이션이 필요하다는 세션이었다. 발표자는 에이전틱 AI의 실패는 잘못된 답변을 넘어 잘못된 행동으로 이어질 수 있으므로 중앙 통제와 AgentOps가 필수라고 강조했다.
- 주요 포인트:
  - 생성형 AI는 모델 응답 중심이었지만 에이전틱 AI는 계획, 추론, 행동, 도구 사용, 메모리, 오케스트레이션이 결합된 복합 시스템이다.
  - 모델/에이전트/도구 레지스트리, 게이트웨이, 런타임, 데이터/벡터/메모리 레이어, 오케스트레이션 레이어, 운영/보안/관측성을 공통 파운데이션으로 제시했다.
  - 게이트웨이는 인증, 비용 관리, 가드레일, 모델/도구 접근을 일관된 진입점에서 제어하는 역할을 한다.
  - AgentCore Evaluation과 관측성을 활용해 세션별 추적, 실시간/오프라인 평가, 프롬프트 최적화, 일부 배포 후 전체 배포 같은 운영 루프를 구성할 수 있다고 설명했다.
- AWS/기술 키워드: Agentic AI, AgentOps, Amazon Bedrock AgentCore, AgentCore Gateway, AgentCore Evaluation, Model Registry, Tool Registry, Guardrails, Observability, Evaluation Loop
- AX TF 관점/회사 AX 도입 시사점: 사내 에이전트가 많아질수록 개별 팀이 알아서 만드는 방식은 위험하다. AX TF는 중앙 게이트웨이, 도구 등록소, 모델 접근 정책, 비용/토큰 추적, 평가 루프를 공통 기반으로 제공해야 한다.
- 공유용 한줄: POC 에이전트를 프로덕션으로 보내려면 "에이전트 앱"보다 먼저 AgentOps 파운데이션이 필요하다.

## sel-mam302 - AIOps 도전과 실전: AI SecOps에서 DevOps 에이전트까지

- 시간/트랙/레벨/발표자: 16:10-16:50 KST / Track 4 / 300 - Advanced / 이연수, 테크니컬 어카운트 매니저, AWS; 박종진, 테크니컬 어카운트 매니저, AWS; 현승열, 선임 엔지니어, 삼성전자
- 요약: 삼성전자 계정 서비스의 WAF 로그 분석 AI SecOps 사례와 AWS DevOps Agent를 소개했다. 삼성전자 사례는 대규모 트래픽과 하루 TB급 보안 로그를 사람이 분석하는 한계를 Bedrock, Strands Agents, 멀티 에이전트 구조로 해결하려는 여정이었다.
- 주요 포인트:
  - 삼성 계정은 21억 사용자와 초당 대규모 트래픽을 처리하며, WAF 로그 기반 악성 트래픽 분석을 수행한다.
  - AI로 공격 패턴이 빠르게 바뀌면서 고정 룰과 수동 로그 분석만으로는 대응이 어렵고, 자연어 질의로 WAF 로그를 조회/분석/리포트화하는 필요가 커졌다.
  - Bedrock Agent Builder로 빠르게 시작했지만 복잡한 질의와 해석 품질에 한계가 있어 Strands Agents와 멀티 에이전트 구조로 확장했다.
  - 후반부 AWS DevOps Agent 데모는 조사, 완화, MCP 서버 연동, 스킬/채팅, 사전 예방 권장사항을 통해 장애 대응과 예방 조치를 자동화하는 흐름을 보여줬다.
- AWS/기술 키워드: Amazon Bedrock, Bedrock Agent Builder, Strands Agents SDK, AWS WAF, Amazon EKS, Amazon CloudWatch, MCP, DevOps Agent, AI SecOps, AIOps
- AX TF 관점/회사 AX 도입 시사점: 운영/보안 영역은 AX 효과가 바로 보이는 영역이다. 로그 조회 SQL 생성에 그치지 말고, 탐지, 분석, 원인 요약, 대응 제안, 재발 방지 권고까지 역할을 나눈 멀티 에이전트 워크플로로 설계해야 한다.
- 공유용 한줄: AIOps의 현실적 출발점은 "사람이 보던 로그"를 에이전트가 질의, 해석, 조치 제안까지 이어주는 것이다.

## sel-dvt305 - Nova Act & Strands Agent 실전: AI 에이전트로 개발 워크플로 자동화하기

- 시간/트랙/레벨/발표자: 16:10-16:50 KST / Track 5 / 300 - Advanced / 김예진, 솔루션즈 아키텍트, AWS; 안수진, 클라우드 서포트 엔지니어, AWS
- 요약: Amazon Nova Act로 브라우저 기반 QA 자동화 에이전트를 만들고, Strands Agents SDK로 코드 어시스턴트와 멀티 에이전트 개발 자동화 파이프라인을 만드는 방법을 소개했다. 발표는 에이전트 성숙도를 RPA식 follow, 생성형 AI assist, 협업형 collaborate, 자율형 pioneer 단계로 설명하고, 현재는 assist에서 collaborate로 빠르게 이동 중이라고 봤다.
- 주요 포인트:
  - MCP는 도구 호출, Skills는 능력 정의, A2A는 에이전트 간 통신의 언어로 소개되며 에이전트 생태계의 연결 표준으로 설명됐다.
  - Nova Act는 브라우저 UI를 이해하고 조작하는 QA/웹 워크플로 자동화 에이전트로 제시됐다.
  - Strands Agents는 원하는 형태의 에이전트를 빠르게 만들 수 있는 오픈소스 SDK로 소개됐다.
  - 데모에서는 보안/성능/코드리뷰 에이전트가 교차 검증하고, 오케스트레이터가 코드 수정, 테스트, Lambda 배포, 최종 리포트까지 수행했다.
  - 하드코딩 민감정보 제거, SQL 인젝션 방어, 입력 검증, 예외 처리 개선처럼 개발자가 실제로 기대하는 코드 품질 개선을 보여줬다.
- AWS/기술 키워드: Amazon Nova Act, Strands Agents SDK, MCP, Skills, A2A, Multi-agent, Swarm, Graph, Workflow, AWS Lambda, QA Automation, Code Review Agent
- AX TF 관점/회사 AX 도입 시사점: 개발 AX는 단일 챗봇보다 역할 기반 멀티 에이전트가 더 실용적이다. 코드 리뷰, 보안 점검, 성능 분석, 배포 검증을 분리하고, 최종 승인/배포는 정책화된 그래프나 워크플로로 묶는 구조가 필요하다.
- 공유용 한줄: Nova Act와 Strands는 개발자의 브라우저 QA부터 코드 수정/배포까지 에이전트 협업으로 확장하는 실전 도구다.

## sel-cmp301 - AWS Trainium 기반 LLM 추론 A to Z: Neuron 환경 이해부터 성능 최적화까지

- 시간/트랙/레벨/발표자: 16:10-16:50 KST / Track 6 / 300 - Advanced / 이수지, GTM 가속 컴퓨팅 전문 솔루션즈 아키텍트, AWS; 차수정, 딥러닝 아키텍트, AWS
- 요약: AWS Trainium과 Neuron SDK를 활용해 LLM 추론을 비용 효율적으로 운영하고 성능을 최적화하는 방법을 다뤘다. 발표는 LLM 추론의 비용 증가, 디코드 병목, 이기종 하드웨어 전환 부담을 문제로 제시하고 Trainium2, Neuron, vLLM/PyTorch 연동, NKI 최적화로 해결하는 흐름을 설명했다.
- 주요 포인트:
  - 생성형 AI 인프라 비용은 토큰 가격 하락보다 사용량 증가가 빨라 최적화 없이는 부담이 커진다.
  - LLM 추론은 KV cache와 디코드 병목 때문에 메모리/대역폭이 중요하며, Trainium2의 대용량 HBM과 멀티코어 구조를 해결책으로 소개했다.
  - Neuron은 익숙한 Python, PyTorch, vLLM 생태계와 연동되어 새 하드웨어 진입 장벽을 낮춘다고 설명했다.
  - Qwen3 8B 데모에서 NKI attention kernel 적용 후 처리량은 약 5.4배 증가, 지연시간은 2.84초에서 0.53초로 약 81% 감소했다고 정리했다.
- AWS/기술 키워드: AWS Trainium, Trainium2, AWS Neuron SDK, Neuron Kernel Interface, NKI, NKI Library, Neuron Explorer, vLLM, PyTorch, Qwen3, LLM Inference, HBM
- AX TF 관점/회사 AX 도입 시사점: AX 서비스가 많아지면 모델 API 비용만 볼 것이 아니라 자체/전용 추론 인프라 최적화도 검토해야 한다. 특히 내부 반복 워크로드나 대규모 배치/온라인 추론은 Trainium 같은 대안 가속기와 커널 최적화가 비용 차이를 만들 수 있다.
- 공유용 한줄: Trainium+Neuron은 LLM 추론 비용과 지연시간을 낮추기 위한 AWS 전용 가속기 선택지다.

## sel-sec202 - 신뢰할 수 있는 KMS 아키텍처의 진화와 서명키 관리 전략

- 시간/트랙/레벨/발표자: 16:10-16:50 KST / Track 7 / 200 - Intermediate / 정관진, 보안 전문 솔루션즈 아키텍트, AWS; 문민아, 테크니컬 어카운트 매니저, AWS
- 요약: AWS KMS가 보안, 내구성, 가용성을 원칙으로 어떻게 발전했는지와 서명키 관리 전략을 설명했다. 발표자는 암호화의 기본 개념부터 시작해 클라우드 키 관리가 필요한 이유, 규제 대응, 감사/운영 통제, 포스트 양자 서명 준비까지 다뤘다.
- 주요 포인트:
  - 암호화는 데이터 보호의 기본이며, 키가 유출되면 보호가 무력화되기 때문에 키 관리가 핵심이라고 설명했다.
  - AWS의 "Everything starts with security" 철학처럼 설계 단계부터 보안과 다중 암호화를 고려해야 한다고 강조했다.
  - KMS는 서비스별로 흩어졌던 키 관리를 중앙화하고, 고객 관리형 키와 클라우드 확장 키 관리 요구를 지원하기 위해 발전했다.
  - 서명키는 사용량 감사, 이상 요청량 모니터링, 키 정책/권한 통제가 중요하며, RSA 2048/ECC 계열의 장기적 전환 이슈도 고려해야 한다.
  - KMS는 ML-DSA 등 포스트 양자 전자서명을 지원하며, 알고리즘을 코드에 고정하지 말고 데이터/설정으로 선택 가능하게 만드는 암호 민첩성을 제안했다.
- AWS/기술 키워드: AWS KMS, HSM, Customer Managed Key, Encryption, Digital Signature, RSA, ECC, Post-Quantum Cryptography, ML-DSA, CloudTrail, Audit, Crypto Agility
- AX TF 관점/회사 AX 도입 시사점: AI/에이전트가 사내 데이터와 액션 권한을 다루게 되면 키 관리와 서명 체계가 더 중요해진다. 모델/에이전트 호출, 아티팩트 서명, 배포 승인, 감사 로그에 KMS 기반 서명과 키 로테이션 전략을 연결해야 한다.
- 공유용 한줄: AX 보안의 하부에는 결국 신뢰할 수 있는 키 관리, 감사, 서명 체계가 있어야 한다.

## sel-aim205 - 당신의 새로운 AI 업무 파트너, Amazon Quick

- 시간/트랙/레벨/발표자: 16:10-16:50 KST / Track 8 / 200 - Intermediate / 채정희, 솔루션즈 아키텍트, AWS; 이지연, 솔루션즈 아키텍트, AWS
- 요약: Amazon Quick을 회사 데이터와 업무 시스템에 연결된 AI 업무 파트너로 소개했다. 발표자는 직원들이 여러 앱을 오가며 정보를 찾고 정리하는 데 많은 시간을 쓰는 문제를 짚고, Quick이 자연어 검색, 맥락 있는 답변, 실행, 보안/거버넌스를 한 경험으로 묶는다고 설명했다.
- 주요 포인트:
  - 소비자 AI는 편하지만 회사 데이터, 권한, 내부 정책을 모르기 때문에 업무 적용에는 한계가 있다.
  - Quick은 문서, 데이터베이스, 이메일, Slack, 대시보드, Jira 등 회사 시스템에 연결되어 질문과 실행을 한 곳에서 처리하도록 설계됐다.
  - 데모 흐름에서는 마케팅 팀원이 대시보드/문서/웹 페이지를 참고해 인사이트를 얻고 반복 작업을 자동화하는 방식을 보여줬다.
  - VPC 엔드포인트, 데이터 리전 내 보관, 모델 학습 미사용, IAM/IAM Identity Center/SAML/AD 연동, CloudWatch/CloudTrail 감사 로그를 보안/거버넌스 근거로 제시했다.
  - 발표자는 Quick의 핵심을 모든 데이터 연결, 답변 이후 실행, 엔터프라이즈 보안/AI 거버넌스로 정리했다.
- AWS/기술 키워드: Amazon Quick, Amazon QuickSight, Slack, Jira, VPC Endpoint, IAM, IAM Identity Center, SAML, Active Directory, Amazon CloudWatch, AWS CloudTrail, AI Governance
- AX TF 관점/회사 AX 도입 시사점: 사내 AX 포털은 단순 Q&A보다 "찾기-판단-실행"을 연결해야 한다. 단, 기존 권한 체계를 그대로 존중하고 감사 로그를 남기는 방식이어야 조직 내 확산이 가능하다.
- 공유용 한줄: Amazon Quick은 흩어진 사내 정보를 한 AI 업무 동료로 묶고, 답변에서 실행까지 이어가려는 업무 AX 플랫폼이다.

## sel-dev306 - [LG유플러스] AWS Kiro로 가속하는 IaC 혁신과 레거시 전환

- 시간/트랙/레벨/발표자: 16:10-16:50 KST / Track 9 / 300 - Advanced / 양승만, 데브옵스 엔지니어, LG유플러스; 윤병찬, 데브옵스 엔지니어, LG유플러스
- 요약: LG유플러스가 AWS Kiro를 활용해 Terraform IaC 컨벤션을 정리하고 레거시 코드를 표준화한 경험을 공유했다. 발표자는 AI 에이전트가 코드 생성 속도는 높였지만, 컨벤션이 정리되지 않은 코드베이스에서는 스타일 혼란, 리뷰 부담, 온보딩 난이도, 영향도 파악 문제가 더 커졌다고 설명했다.
- 주요 포인트:
  - Terraform은 멀티 클라우드/네트워크 리소스 관리, 선언형 언어, 상태/의존성/실행 계획 장점이 있지만 작성자별 스타일 차이가 누적되기 쉽다.
  - AI 에이전트 도입 이후 코드와 디렉터리 구조가 더 빠르게 생성되면서 일관성 없는 IaC가 기술 부채로 확대됐다.
  - 해결책으로 흩어진 컨벤션과 작업 히스토리를 README 등 에이전트와 사람이 모두 읽는 문서로 통합하고, 반복 가능한 운영 루프를 만들었다.
  - Kiro를 활용해 Terraform 코드 패턴 분석, 컨벤션 정립, IaC 작성/수정/정리 자동화를 수행하고, GitHub PR 단계에서 Amazon Q Developer 리뷰로 컨벤션 준수를 확인했다.
  - 발표자는 AI 결과물을 맹신하지 말고 결정론적 테스트, 절차적 파이프라인, 사람이 이해하고 검증할 수 있는 책임 구조가 필요하다고 강조했다.
- AWS/기술 키워드: AWS Kiro, Terraform, IaC, HCL, Amazon Q Developer, GitHub PR Review, DevOps, Convention, Legacy Modernization, Deterministic Test
- AX TF 관점/회사 AX 도입 시사점: Claude Code류 도구를 도입하기 전에 코드베이스 컨벤션과 테스트 체계가 정리되어 있어야 한다. 에이전트가 읽을 문서, 자동 리뷰, 결정론적 테스트, PR 게이트를 갖추면 AI가 기술 부채를 증폭시키지 않고 표준화를 가속한다.
- 공유용 한줄: AI 코딩 도구의 생산성은 컨벤션과 검증 루프가 있는 코드베이스에서만 안정적으로 커진다.
