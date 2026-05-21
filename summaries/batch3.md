# AWS Summit Seoul 2026 Industry Day - Batch 3

담당 세션: `sel-wps103`, `sel-prt214-s`, `sel-prt303-s`, `sel-prt205-s`, `sel-prt219-s`, `sel-prt208-s`, `sel-prt304-s`, `sel-prt218-s`, `sel-prt107-s`

모든 세션은 helper script로 생성한 VOD 전사본을 기반으로 요약했습니다. 전사 품질상 일부 고유명사/제품명은 공식 세션 메타데이터와 대조해 보정했습니다.

## sel-wps103

- 제목: [국가인공지능전략위원회 I KIM & CHANG I LIG D&A] 국방 AX: AI와 클라우드로 재편되는 미래 전쟁 구조
- 시간: 2026-05-20 12:50-13:30 KST
- 트랙: AWS Summit Seoul - Track 9
- 발표자: 오순영(수석 솔루션즈 아키텍트, AWS), 이승영(CTO/본부장, LIG D&A), 이상열(위원, KIM & CHANG), 안재희(중령, 국가인공지능전략위원회 지원단 해군AX담당)

### 핵심 요약

이 패널은 국방 AX가 미래의 개념이 아니라 이미 전장에서 진행 중인 변화라는 점에서 출발했다. 무기 중심의 전쟁 이해가 데이터, AI, 클라우드 기반 운영으로 이동하고 있으며, Project Maven 같은 사례를 통해 감시정찰 데이터 분석, 지휘 결심 지원, 클라우드 인프라, AI 모델이 결합되는 구조를 설명했다. 동시에 AI 무기체계는 납품 후 끝나는 하드웨어가 아니라 지속적으로 학습/업데이트되는 소프트웨어 시스템이므로 기존 R&D, 보안 등급, 책임/통제 제도가 함께 바뀌어야 한다고 강조했다. 특히 한국 국방 클라우드는 데이터 민감도별 보안 등급과 통제 체계 정비가 시급하다는 문제의식이 반복됐다.

### 주요 포인트

- 전쟁의 중심이 무기 플랫폼에서 데이터와 AI로 이동하며, 피지컬 AI 투자가 국방 경쟁력의 핵심 축이 될 가능성이 크다.
- Project Maven, Palantir, AWS 클라우드 인프라, Anthropic 모델을 예로 들어 현대 전장 AI가 단일 제품이 아니라 복합 생태계임을 설명했다.
- AI/ML 기반 무기체계는 전통적 4-5년 개발 사이클로는 따라가기 어렵고, 클라우드 기반 실험/시뮬레이션/업데이트 체계가 필요하다.
- 국방 AI 도입의 쟁점은 "어디에 두느냐"보다 "얼마나 정교하게 통제하느냐"로 옮겨가고 있다.
- 법/제도 측면에서는 데이터 분류, 책임 소재, 보안 인증, CMMC류 공급망 보안 요구에 대한 정비가 필요하다.

### AWS/기술 키워드

AWS 클라우드, 국방 AX, Project Maven, Palantir, Anthropic, 피지컬 AI, CMMC, 보안 등급, 데이터 아키텍처, 클라우드 기반 개발 환경

### 현장 메모로 남길 점

국방 클라우드 논의에서 "보안 때문에 못 쓴다"가 아니라 데이터 민감도와 통제 수준을 세분화해 쓰는 방향으로 제도 설계가 필요하다는 메시지가 선명했다.

### 블로그용 한줄

미래 전장은 무기보다 데이터, AI, 클라우드를 얼마나 빠르고 안전하게 통제하느냐의 경쟁으로 재편되고 있다.

## sel-prt214-s

- 제목: 책임감 없는 AI에이전트, 주인은 누구인가 (sponsored by Datadog)
- 시간: 2026-05-20 13:50-14:10 KST
- 트랙: AWS Summit Seoul - Track 1
- 발표자: Mark Hyeonbeom Park(Datadog)

### 핵심 요약

Datadog 세션은 AI 에이전트가 업무 효율을 높이는 동시에 책임 소재와 승인 체계를 흐릴 수 있다는 문제를 다뤘다. 발표자는 기업의 AI 활용이 이미 사람을 대신해 의사결정과 실행에 들어서고 있지만, AI의 판단도 결국 조직이 책임져야 한다는 사례를 소개했다. 그래서 AI를 사람을 대체하는 존재가 아니라 업무를 돕는 도구로 재정의하고, 실행 전 승인과 관찰 가능한 텔레메트리를 갖춘 구조가 필요하다고 설명했다. Datadog Agent Builder는 Datadog 콘솔 안에서 액션, 스킬, 트리거, 외부 시스템 연동, human-in-the-loop 승인을 구성하는 방식으로 제시됐다.

### 주요 포인트

- AI 에이전트는 이미 업무 자동화와 의사결정에 들어왔지만, 잘못된 액션의 책임은 AI가 아니라 조직과 사람이 져야 한다.
- 코드/데이터 유출, 잘못된 예약/취소, 승인 없는 자동 실행 등 AI 사용 사례의 리스크를 통해 거버넌스 필요성을 설명했다.
- 에이전트가 실행할 수 있는 액션과 스킬을 제한하고, 실행 전 사람이 확인하는 승인 구조가 핵심이다.
- Datadog Agent Builder는 Datadog 내 텔레메트리뿐 아니라 외부 시스템 데이터까지 참조해 자동화 흐름을 구성할 수 있다고 소개됐다.
- 마지막 메시지는 "AI는 사람을 대체하는 것이 아니라 도와주는 도구"이며, 업무 방식도 그 전제에 맞게 바뀌어야 한다는 점이었다.

### AWS/기술 키워드

AI Agent, Datadog Agent Builder, Observability, Telemetry, Human-in-the-loop, Workflow Automation, Approval Flow, Governance

### 현장 메모로 남길 점

AI 에이전트 도입의 관건은 "무엇을 할 수 있느냐"보다 "무엇을 하면 안 되는지와 누가 승인하는지"를 제품/운영 흐름에 내장하는 것이다.

### 블로그용 한줄

AI 에이전트의 주인은 모델이 아니라, 액션과 책임을 설계하는 사람과 조직이다.

## sel-prt303-s

- 제목: LLM and Agent Workloads with DRA GPU를 더 잘게, 더 똑똑하게 - DRAmatic하게 (sponsored by GS네오텍)
- 시간: 2026-05-20 13:50-14:10 KST
- 트랙: AWS Summit Seoul - Track 2
- 발표자: 김성혁(AI Research Engineer, GS Neotek)

### 핵심 요약

GS네오텍 세션은 AI 인프라 문제가 GPU 확보량이 아니라 GPU를 워크로드 조건에 맞게 배치하고 공유하는 문제로 바뀌었다는 점을 짚었다. LLM/에이전트 워크로드는 요청 패턴이 동적이고 idle, 과점유, 토폴로지 불일치가 비용과 성능 병목을 만든다. 발표자는 Kubernetes/EKS 환경에서 기존 디바이스 플러그인 방식이 GPU 개수 중심이라 메모리, 공유 정책, 토폴로지 표현에 한계가 있다고 설명하고, DRA를 통해 "어떤 조건의 GPU가 필요한가"를 리소스 클레임으로 선언하는 구조를 소개했다. MPS, MIG, time slicing, exclusive GPU 사용 등 공유/격리 전략을 워크로드별로 선택해야 한다는 운영 관점도 강조했다.

### 주요 포인트

- 에이전트 시대의 GPU 운영은 정적인 GPU 개수 할당에서 워크로드 속성 기반 스케줄링으로 이동한다.
- 기존 Kubernetes device plugin은 GPU를 주로 개수로 다뤄 메모리, 토폴로지, 격리 수준을 세밀하게 표현하기 어렵다.
- DRA는 GPU 모델, 메모리, 드라이버, 공유 방식, 토폴로지 요구사항을 resource claim으로 선언하게 해준다.
- MPS는 다중 프로세스 공유, MIG는 하드웨어 격리, time slicing은 개발/검증, exclusive는 대규모 학습에 적합하다고 구분했다.
- EKS/Kubernetes 최신 버전의 DRA 지원 흐름과 GPU 공급 정책/서비스 요구사항의 분리 운영이 핵심 설계 포인트다.

### AWS/기술 키워드

Amazon EKS, Kubernetes DRA, GPU Scheduling, ResourceClaim, NVIDIA GPU, MPS, MIG, Time Slicing, LLM Serving, Agent Workloads, Topology-aware Scheduling

### 현장 메모로 남길 점

GPU 최적화는 "더 많이"가 아니라 "필요한 속성의 GPU를 필요한 워크로드에 정확히 매칭"하는 문제로 바뀌고 있다.

### 블로그용 한줄

LLM/에이전트 시대의 GPU 운영은 카드 수가 아니라 워크로드 요구 조건을 코드로 선언하는 능력에서 갈린다.

## sel-prt205-s

- 제목: 생성형 AI의 신뢰성 확보 전략: 매경AX의 환각 통제 사례 (sponsored by 스마일샤크, SmileShark)
- 시간: 2026-05-20 13:50-14:10 KST
- 트랙: AWS Summit Seoul - Track 3
- 발표자: 최병주(Solution Architect, 스마일샤크)

### 핵심 요약

스마일샤크 세션은 매경AX와 구축한 AI 팟캐스트/콘텐츠 생성 사례를 통해 생성형 AI의 환각을 운영 수준에서 통제하는 방법을 설명했다. 초기 워크플로우는 기사 선별, 대본 생성, 통합, TTS 변환으로 구성됐고 AWS Step Functions로 전체 흐름을 제어했다. 가장 큰 병목은 대본 생성에서 원문의 사실 관계가 바뀌는 문제였으며, 이를 해결하기 위해 생성 모델 뒤에 LLM 기반 평가 모델을 붙여 기사와 대본을 문장 단위로 비교했다. 발표자는 평가 모델도 틀릴 수 있으므로 교차 모델 평가, 기준 분리, 사람 검수 피드백으로 평가 모델을 지속 보정해야 한다고 강조했다.

### 주요 포인트

- 운영 가능한 GenAI 서비스의 핵심은 자연스러운 문장보다 원문 사실의 정확성 유지다.
- 코드 기반 평가는 빠르지만 의미 보존을 보기 어렵고, 사람 기반 평가는 정확하지만 대량 운영에 부담이 크다.
- LLM 기반 평가를 도입해 문장 단위 pass/fail과 근거를 생성하고, 해결되지 않는 항목만 사람에게 검수 요청하도록 설계했다.
- 생성 모델과 평가 모델을 같은 계열로만 쓰면 같은 편향을 놓칠 수 있어 교차 모델 평가로 사각지대를 줄였다.
- 사람과 평가 모델의 차이 데이터를 수집해 평가 기준을 보정하고, 비용/복잡도 증가를 감수해 안정적 품질을 확보했다.

### AWS/기술 키워드

Amazon Bedrock, AWS Step Functions, LLM-as-a-Judge, Claude, Cross-model Evaluation, TTS, Human Review, Hallucination Control, LLMOps

### 현장 메모로 남길 점

환각 통제는 한 번의 프롬프트 튜닝이 아니라 생성-평가-재생성-사람 검수 데이터를 반복하는 운영 시스템에 가깝다.

### 블로그용 한줄

생성형 AI 품질은 모델이 만든 답을 또 다른 모델과 사람이 함께 검증하는 운영 루프에서 나온다.

## sel-prt219-s

- 제목: 에이전트의 진화 (sponsored by Anthropic)
- 시간: 2026-05-20 13:50-14:10 KST
- 트랙: AWS Summit Seoul - Track 4
- 발표자: 장동진(Applied AI Architect, Anthropic)

### 핵심 요약

Anthropic 세션은 소프트웨어가 도구에서 함께 일하는 동료로 바뀌고 있다는 관찰로 시작했다. 발표자는 LLM이 단순 질의응답을 넘어 planning, action, reflection을 수행하는 에이전트 구조가 되면서 실제 업무 단위의 결과물을 낼 수 있게 됐다고 설명했다. 가장 성공적인 적용 분야로 코딩을 들며 Claude Code가 터미널에서 코드 작성, 파일 수정, 작업 실행을 도와 개인 생산성을 넘어 조직 생산성에 영향을 주기 시작했다고 말했다. 이후 데스크톱 에이전트, 디자인 워크플로우, 제품 내 에이전트 적용으로 확장되는 흐름을 제시했다.

### 주요 포인트

- 에이전트는 태스크를 잘게 나누고, 실행하고, 결과를 검증/반성하는 planning-action-reflection 구조로 동작한다.
- LLM은 더 이상 질문에 답하는 모델만이 아니라 특정 업무 결과를 산출하는 실행 주체로 진화하고 있다.
- Claude Code 사례를 통해 복사/붙여넣기식 코드 보조에서 터미널 기반 파일 수정과 작업 수행으로 사용성이 이동했다고 설명했다.
- 개발자 개인 생산성 향상을 넘어 조직 단위 생산성, 업무 인터페이스, 제품 경험까지 에이전트가 확장될 수 있다.
- 실제 제품에 에이전트를 넣을 때는 모델 능력뿐 아니라 유저 인터페이스, 툴 권한, 피드백 루프, AWS와의 운영 환경이 함께 설계돼야 한다.

### AWS/기술 키워드

Claude, Claude Code, AI Agent, Planning, Action, Reflection, Tool Use, Desktop Agent, Product Agent, Applied AI, AWS

### 현장 메모로 남길 점

에이전트의 첫 승전지는 코딩이었지만, 다음 단계는 업무용 제품 안에서 사용자가 자연스럽게 맡기는 "일 단위"의 자동화다.

### 블로그용 한줄

LLM은 답변하는 도구에서 계획하고 실행하고 되돌아보는 동료형 소프트웨어로 진화하고 있다.

## sel-prt208-s

- 제목: 다운타임 0의 도전: Agentic AI와 Bedrock으로 완성하는 자율 예지정비 (sponsored by 두산 디지털이노베이션BU)
- 시간: 2026-05-20 13:50-14:10 KST
- 트랙: AWS Summit Seoul - Track 5
- 발표자: 김성진(수석, 두산 디지털이노베이션BU)

### 핵심 요약

두산 DDI 세션은 제조 설비의 다운타임을 줄이기 위한 예지정비를 Agentic AI와 Amazon Bedrock으로 확장한 사례를 소개했다. 기존 예지정비는 센서 데이터, 표준 알고리즘, 전문가 분석에 기반했지만 현장 환경이 바뀌면 고정된 진단 룰이 한계를 보인다. 발표자는 IoT Core로 수신한 데이터를 S3에 저장하고 분석/리포트 흐름을 구성한 뒤, Bedrock 기반 에이전트가 과거 데이터와 진단 기준을 참고해 이상을 분석하고 진단 룰 개선을 추천하는 구조를 설명했다. 단, AI가 바로 운영 룰을 바꾸는 것이 아니라 전문가 승인 후 시스템에 반영되는 폐쇄 루프를 제시했다.

### 주요 포인트

- 예지정비는 설비 다운 전에 고장 가능성을 예측해 생산량, 품질, 운영 안정성 영향을 줄이는 솔루션이다.
- DDI는 진동/온도 기반 데이터, IoT 프로젝트, 데이터 분석, 진단 알고리즘 경험을 제조 솔루션으로 축적해왔다.
- 기존 ISO 20816 기반 규칙과 경험 기반 분석에 생성형 AI 진단/추천을 결합하는 방향으로 확장했다.
- Agentic AI는 진단 룰로 잡히지 않는 데이터나 적중률이 떨어지는 룰을 찾아 개선안을 생성하고, 사용자 승인 후 반영한다.
- 목표는 "다운타임 0"에 가까워지는 지능형 루프이며, 자연어 질의/리포트/정비 일정/부품 추천까지 연결 가능성을 보여줬다.

### AWS/기술 키워드

Amazon Bedrock, AWS IoT Core, Amazon S3, Agentic AI, Predictive Maintenance, ISO 20816, Sensor Data, Diagnostic Rules, Human Approval Loop

### 현장 메모로 남길 점

제조 AI의 가치는 자동 판단 자체보다 현장 전문가의 승인과 축적 데이터로 진단 룰을 계속 개선하는 운영 루프에서 나온다.

### 블로그용 한줄

예지정비의 다음 단계는 고정 룰을 넘어, 설비 데이터로 스스로 개선안을 제안하는 Agentic AI 루프다.

## sel-prt304-s

- 제목: Agentic 시대에 필요한 machine data 관리 전략 (sponsored by Splunk)
- 시간: 2026-05-20 13:50-14:10 KST
- 트랙: AWS Summit Seoul - Track 6
- 발표자: 김현준(전무, Splunk)

### 핵심 요약

Splunk 세션은 Agentic AI의 성패가 모델이나 GPU만이 아니라 AI가 읽을 수 있는 machine data 통합에 달려 있다고 설명했다. 발표자는 로그, 트레이스, 메트릭 같은 운영 데이터를 machine data로 정의하고, 에이전트가 장애 원인과 영향도를 판단하려면 이 데이터가 정상적으로 수집, 검색, 연결돼야 한다고 강조했다. 기업들은 AI를 도입하면서도 보안/개발/운영 도메인별로 데이터가 흩어져 있어 문제가 보안 이슈인지 시스템 이슈인지 빠르게 판단하기 어렵다. Splunk는 schema-on-read, SPL, Cisco Data Fabric, machine data lake 등을 통해 데이터 위치와 형식이 달라도 분석 가능한 구조를 제안했다.

### 주요 포인트

- AI 에이전트가 정상적으로 의사결정하려면 로그, 메트릭, 트레이스 등 machine data를 볼 수 있어야 한다.
- Kubernetes 노드나 VPC Flow Logs처럼 현대 인프라는 막대한 로그를 생성하지만, 이를 AI가 활용 가능한 상태로 관리하는 조직은 제한적이다.
- 보안, 애플리케이션, 개발, 운영 데이터가 도메인별로 분리되면 장애 원인과 영향도 판단이 느려진다.
- Splunk의 schema-on-read는 먼저 저장하고 필요할 때 스키마를 적용해 다양한 형식의 machine data에서 인사이트를 뽑는 접근이다.
- Cisco Data Fabric과 machine data lake는 S3, Snowflake, Databricks 등 데이터 위치와 무관하게 분석/렌딩/검색할 수 있는 구조로 소개됐다.

### AWS/기술 키워드

Splunk, Machine Data, Logs, Metrics, Traces, Schema-on-read, SPL, Cisco Data Fabric, Machine Data Lake, Amazon S3, VPC Flow Logs, Kubernetes Logs

### 현장 메모로 남길 점

Agentic AI를 운영에 쓰려면 먼저 데이터 통합과 관찰 가능성이 되어 있어야 하며, "AI가 볼 수 없는 데이터"는 곧 "AI가 판단할 수 없는 업무"가 된다.

### 블로그용 한줄

에이전트 시대의 숨은 인프라는 GPU가 아니라 로그, 메트릭, 트레이스를 연결하는 machine data 전략이다.

## sel-prt218-s

- 제목: VMware 종속을 넘어 자율로, 삼성SDS와 함께하는 AX 전략 (sponsored by Samsung SDS)
- 시간: 2026-05-20 13:50-14:10 KST
- 트랙: AWS Summit Seoul - Track 7
- 발표자: 김현기(그룹장, 삼성SDS)

### 핵심 요약

삼성SDS 세션은 VMware 라이선스 정책 변화와 비용 상승을 계기로 AI Ready 인프라 전환의 골든타임을 강조했다. 발표자는 생성형 AI와 에이전트 도입이 늘면서 GPU 효율, 비정형 데이터 활용, 최신 AI 서비스 접근성, 예측 가능한 비용 구조를 갖춘 인프라가 필요하다고 설명했다. 모든 워크로드를 한 번에 퍼블릭 클라우드로 옮기는 것이 답은 아니며, 안정적 전환이 필요한 영역은 Nutanix 기반 하이브리드 통합 플랫폼으로, 클라우드 네이티브/AI 최적화가 필요한 영역은 AWS 전환 전략으로 접근하는 선택지를 제시했다. AWS Transform 등 에이전트 기반 자동화를 활용하면 VM/네트워크 분석과 마이그레이션 효율을 높일 수 있다고 소개했다.

### 주요 포인트

- VMware 비용/TCO 상승과 기술 종속은 단순 비용 문제가 아니라 AI 도입 타이밍을 놓치게 하는 리스크로 제시됐다.
- AI Ready 인프라는 GPU 효율, 비정형 데이터 소화, 최신 AI 서비스 활용, 예측 가능한 비용 통제가 필요하다.
- Nutanix 전환 전략은 기존 설정 복제, 하이퍼바이저 비용 부담 완화, 하이브리드 확장을 통해 안정적 전환을 목표로 한다.
- 삼성SDS는 사전 진단, 인프라 세팅, 자동 전환, 검증/운영 안정화의 절차로 리스크를 낮추는 접근을 설명했다.
- AWS 전환은 클라우드 네이티브와 AI 최적화가 필요한 워크로드를 대상으로 AWS Transform 같은 자동화 도구와 결합하는 전략이다.

### AWS/기술 키워드

AWS Transform, VMware Migration, Nutanix, Hybrid Cloud, Cloud Native, AI Ready Infrastructure, TCO, AOS, Prism Central, MSP, Migration Automation

### 현장 메모로 남길 점

VMware 대안 논의는 "탈 VMware" 자체보다 안정적 전환과 AI 네이티브 확장을 어느 워크로드에 어떻게 나눌지의 포트폴리오 전략으로 봐야 한다.

### 블로그용 한줄

AX 인프라 전략은 VMware를 벗어나는 문제가 아니라 안정성과 AI 확장성을 동시에 확보하는 전환 설계의 문제다.

## sel-prt107-s

- 제목: AWS All-in 마이그레이션으로 실현한 SM하이플러스의 AI 모빌리티 전략 (sponsored by NDS)
- 시간: 2026-05-20 13:50-14:10 KST
- 트랙: AWS Summit Seoul - Track 8
- 발표자: 김성수(CTO, SM 하이플러스), 김완상(Data Engineer, NDS)

### 핵심 요약

SM하이플러스/NDS 세션은 하이패스 카드 1위 사업자가 종합 모빌리티 결제 플랫폼으로 확장하기 위해 AWS All-in 마이그레이션을 추진한 사례를 공유했다. 기존 전산센터, 높은 라이선스 비용, 노후 인프라, 보안 강화 요구를 단순 서버 이전이 아니라 클라우드 기반 IT 모더나이제이션으로 해결했다. 발표에서는 카드망, 구름망, 콜센터를 포함해 6개월 만에 대규모 서버/소스코드를 AWS로 이전하고 Oracle을 Aurora PostgreSQL/RDS Oracle 19c로 전환한 과정이 소개됐다. 이후 AWS Connect, Bedrock, Redshift, QuickSight를 기반으로 AI 컨택센터와 모빌리티 데이터 플랫폼을 추진하며 AX 여정으로 확장하고 있다고 설명했다.

### 주요 포인트

- SM하이플러스는 하이패스 카드 사업을 넘어 차량 내 종합 결제/모빌리티 플랫폼 기업으로 진화하려는 비전을 제시했다.
- 레거시 전산센터 이전, 유지보수 리스크, 라이선스 비용, 보안 강화 요구가 전면 AWS 마이그레이션의 배경이었다.
- Oracle에서 Aurora PostgreSQL 및 RDS Oracle 19c로 전환하고, 오래된 Unix 환경을 클라우드 네이티브에 맞는 AWS Linux 환경으로 전환했다.
- NDS는 AWS DMS CDC, 암호화, KMS 키 관리, 해시 기반 전수 검증 등으로 금융 데이터 정합성과 보안을 보장하는 전략을 설명했다.
- 구축된 기반 위에 AWS Connect 기반 AI 컨택센터, Bedrock 에이전트, Redshift/QuickSight 데이터 플랫폼으로 AX를 확장하고 있다.

### AWS/기술 키워드

AWS All-in Migration, Amazon Aurora PostgreSQL, Amazon RDS for Oracle 19c, AWS DMS CDC, AWS KMS, Amazon Connect, Amazon Bedrock, Amazon Redshift, Amazon QuickSight, AWS Linux

### 현장 메모로 남길 점

마이그레이션 성공이 곧 끝이 아니라, AI 컨택센터와 데이터 플랫폼을 얹을 수 있는 AX 기반을 만든 것이 이 사례의 핵심이다.

### 블로그용 한줄

SM하이플러스의 AWS All-in 마이그레이션은 레거시 비용 절감에서 출발해 AI 모빌리티 플랫폼의 데이터 기반으로 이어졌다.
