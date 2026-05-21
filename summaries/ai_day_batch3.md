# AI Day Batch 3 요약

담당 세션: `sel-aim401`, `sel-ant303`, `sel-dvt304`, `sel-mam202`, `sel-dvt204`, `sel-cmp201`, `sel-sec302`, `sel-biz204`, `sel-dev305`, `sel-aim202`, `sel-prt217-s`, `sel-dvt302`, `sel-prt106-s`, `sel-prt103-s`

대부분 helper script로 생성한 VOD 전사본을 기반으로 요약했습니다. 전사 품질상 일부 고유명사와 제품명은 공식 세션 메타데이터와 대조해 보정했습니다. `sel-prt106-s`는 전사 결과에 발화가 없어 메타데이터 기반 요약으로 작성했습니다.

## sel-aim401 - SageMaker AI MLOps, Nova 2 기반 멀티 에이전트로 한 단계 업그레이드

- 시간/트랙/레벨/발표자: 2026-05-21 14:30-15:10 KST / Track 1 / 400 - Expert / 김지훈(AWS), 최두섭(AWS)
- 요약: SageMaker AI의 ML Pipeline, MLflow, Model Registry 같은 MLOps 기능을 더 잘 쓰기 위해 Nova 2 Lite 기반 멀티 에이전트를 붙이는 실전 접근을 소개했다. 발표는 단일 챗봇이 아니라 역할별 에이전트가 파이프라인 상태, 모델 레지스트리, 운영 지표를 해석하고 개선 후보를 제안하는 구조에 초점을 맞췄다. 에이전트는 자유롭게 패턴을 찾을 수 있지만, 운영 환경에서는 역할 분리와 검증 가능한 피드백 루프가 중요하다는 메시지가 반복됐다.
- 주요 포인트:
  - MLOps 성숙도는 도구 도입만으로 오르지 않고, 파이프라인/레지스트리/실험 관리가 실제 의사결정에 연결되어야 한다.
  - Nova 2 기반 멀티 에이전트는 분석, 진단, 개선 제안처럼 역할을 나누어 MLOps 운영 부담을 줄이는 방향으로 설계된다.
  - 에이전트가 제안한 변경은 사람이 이해할 수 있는 근거와 검증 단계가 있어야 프로덕션 운영에 들어갈 수 있다.
  - 역할 재분배와 자동화 수준 조절을 통해 비용 절감과 운영 품질 개선을 동시에 노릴 수 있다.
- AWS/기술 키워드: Amazon SageMaker AI, MLOps, ML Pipeline, MLflow, Model Registry, Amazon Nova 2 Lite, Multi-Agent, Bedrock
- AX TF 관점/회사 AX 도입 시사점: 사내 ML/LLM 프로젝트도 "모델을 만들었다"에서 끝내지 말고 실험, 배포, 평가, 비용 추적을 에이전트가 읽고 개선 제안을 내는 운영 체계를 목표로 잡을 만하다. Claude Code류 도구를 쓰는 개발팀이라면 코드 생성 에이전트와 MLOps 에이전트를 분리해 변경 제안, 검증, 승인 흐름을 명확히 하는 것이 현실적이다.
- 공유용 한줄: MLOps의 다음 단계는 파이프라인을 자동화하는 것을 넘어, 운영 상태를 이해하고 개선안을 제시하는 멀티 에이전트 체계다.

## sel-ant303 - 밑줄 쫙! AI 성공 네비게이터 SageMaker Catalog

- 시간/트랙/레벨/발표자: 2026-05-21 14:30-15:10 KST / Track 2 / 300 - Advanced / 송규호(AWS), 강성희(AWS)
- 요약: AI 에이전트가 정확한 답을 하려면 모델보다 먼저 데이터의 의미, 품질, 소유권, 계보가 정리되어야 한다는 세션이다. SageMaker Catalog는 정형/비정형 데이터, AI 모델, BI 대시보드까지 메타데이터로 묶어 사람이 보는 데이터 카탈로그와 AI가 참조하는 맥락을 일치시키는 방향으로 설명됐다. 핵심은 데이터 거버넌스를 문서 업무가 아니라 환각을 줄이는 AI 품질 관리 장치로 보는 것이다.
- 주요 포인트:
  - 데이터 거버넌스 부재는 AI 가치 실현 실패의 주요 원인이며, 에이전트 시대에는 메타데이터가 추론 품질을 좌우한다.
  - SageMaker Catalog는 데이터 자산을 검색, 이해, 분류하고 품질/계보/권한 정보를 관리하는 중심 레이어로 소개됐다.
  - 정형 데이터뿐 아니라 모델, 대시보드, 비정형 자산까지 동일한 눈높이로 관리해야 AI와 사람이 같은 의미 체계를 공유한다.
  - 자동 메타데이터 생성과 품질 관리는 AI 환각을 줄이고, 신뢰 가능한 데이터 탐색 경험을 만든다.
- AWS/기술 키워드: Amazon SageMaker Catalog, Data Governance, Metadata, Data Quality, Data Lineage, Analytics, AI-Ready Data
- AX TF 관점/회사 AX 도입 시사점: 사내 AX 과제에서 "챗봇이 사내 데이터를 잘 못 찾는다"는 문제는 RAG 튜닝 이전에 데이터 카탈로그와 의미 관리 문제일 수 있다. 부서별 데이터 사전, 오너, 민감도, 최신성, 대시보드 출처를 표준화하면 개발자용 에이전트와 현업용 에이전트 모두의 신뢰도를 높일 수 있다.
- 공유용 한줄: AI 성공의 네비게이터는 더 큰 모델이 아니라, AI가 믿고 읽을 수 있는 메타데이터 카탈로그다.

## sel-dvt304 - [삼성전자] 200개국 삼성 스마트 TV 앱 데이터를 자연어로 묻다: 에이전틱 AI on AWS

- 시간/트랙/레벨/발표자: 2026-05-21 14:30-15:10 KST / Track 3 / 300 - Advanced / 이혜원(AWS), 이아름(AWS), 임경택(삼성전자)
- 요약: 삼성 스마트 TV 앱 운영 데이터를 자연어로 질의하기 위해 LangGraph 멀티 에이전트를 Amazon Bedrock AgentCore 기반으로 프로덕션에 올린 사례다. 세션은 AgentCore Runtime, Gateway, Identity, Observability, Evaluation을 각각 운영 가능한 에이전트 플랫폼의 구성 요소로 풀어 설명했다. MCP를 통해 내부 API와 외부 도구 연결을 표준화하고, Okta IdP 연동과 자연어 기반 접근 제어, OpenTelemetry 트레이싱, CI 평가 자동화를 적용한 점이 실무적으로 중요했다.
- 주요 포인트:
  - 200개국 TV 앱 데이터 운영 문제를 자연어 질의와 멀티 에이전트로 풀되, 프로덕션 요구사항을 먼저 정의했다.
  - AgentCore Runtime은 Supervisor 패턴의 멀티 에이전트를 실행하는 기반으로, Gateway는 MCP 서버와 도구 연결을 중앙 관리한다.
  - Identity/Policy 연동으로 사용자의 권한과 에이전트의 도구 호출 권한을 함께 통제했다.
  - OpenTelemetry 기반 계층형 트레이싱으로 Sub-Agent별 실행 흐름을 추적하고, Evaluation을 CI에 넣어 품질을 자동 검증했다.
- AWS/기술 키워드: Amazon Bedrock AgentCore, LangGraph, MCP, AgentCore Runtime, Gateway, Identity, Okta, OpenTelemetry, Evaluation, CI
- AX TF 관점/회사 AX 도입 시사점: 사내 데이터 질의형 에이전트를 만들 때도 "데모 챗봇"이 아니라 권한, 도구 게이트웨이, 관측성, 평가 자동화를 처음부터 플랫폼 요구사항으로 잡아야 한다. 내부 API를 MCP로 감싸면 Claude Code류 개발 에이전트와 현업 분석 에이전트가 같은 도구 표준을 공유할 수 있다.
- 공유용 한줄: 삼성 사례의 핵심은 자연어 질의가 아니라, 에이전트를 프로덕션 서비스처럼 배포·통제·관측·평가한 점이다.

## sel-mam202 - 오래된 IT 시스템 현대화, 에이전틱 AI로 쉽게

- 시간/트랙/레벨/발표자: 2026-05-21 14:30-15:10 KST / Track 4 / 200 - Intermediate / 김윤서(AWS), 임연욱(AWS)
- 요약: 레거시 시스템 현대화를 단순 마이그레이션이 아니라 에이전틱 AI 기반 End-to-End 전환으로 보는 세션이다. AWS Transform으로 기존 시스템을 분석하고 마이그레이션 후보를 도출한 뒤, Kiro로 최신 코드와 설계 산출물을 생성하고, Amazon Quick으로 전환 이후 데이터 분석과 업무 활용까지 연결하는 흐름을 제시했다. 요지는 오래된 시스템이 AI 도입의 병목이 되지 않도록 분석, 변환, 개발, 활용 단계를 자동화해야 한다는 것이다.
- 주요 포인트:
  - AI 도입을 이야기하기 전에 기존 IT 시스템이 AI와 연결될 준비가 되었는지 점검해야 한다.
  - AWS Transform은 레거시 현황 분석과 전환 작업을 자동화해 수작업 중심 현대화의 속도 문제를 줄인다.
  - Kiro는 신규 시스템 개발과 코드 생성 단계에서 프로젝트 맥락을 반영한 자동화 도구로 제시됐다.
  - Amazon Quick은 현대화된 데이터와 대시보드를 업무 분석 흐름으로 연결하는 마지막 사용자 경험으로 소개됐다.
- AWS/기술 키워드: AWS Transform, Kiro, Amazon Quick, Agentic AI, Migration, Modernization, Legacy Analysis
- AX TF 관점/회사 AX 도입 시사점: 회사 AX 로드맵에서 레거시 분석과 전환을 별도 IT 과제로 떼어놓으면 AI 활용이 현업까지 닿기 어렵다. 시스템 분석, 코드 현대화, 데이터 활용까지 한 과제 체인으로 묶고, 각 단계에 에이전트 도구를 붙이는 방식이 더 효과적이다.
- 공유용 한줄: 레거시 현대화의 AX 방향은 "옮기기"가 아니라 분석, 전환, 개발, 활용을 에이전트로 이어 붙이는 것이다.

## sel-dvt204 - 누구나 손쉽게 개발효율 200% 향상시키는 Kiro 활용법

- 시간/트랙/레벨/발표자: 2026-05-21 14:30-15:10 KST / Track 5 / 200 - Intermediate / 전치훈(AWS), 강수희(AWS)
- 요약: Kiro를 단순 코딩 도우미가 아니라 프로젝트 지식과 외부 도구를 연결해 자율 검증 루프를 만드는 개발 에이전트로 활용하는 방법을 다뤘다. 발표는 "에이전트가 코드를 고쳤는데 동작하지 않는다"는 문제를 출발점으로, MCP, Steering, Powers를 통해 팀 규칙, 도메인 문서, 실행 도구, 테스트를 에이전트 컨텍스트에 넣는 방식을 설명했다. 신규 멤버 온보딩과 반복 개발 작업 자동화에도 적용할 수 있다는 점이 강조됐다.
- 주요 포인트:
  - 코딩 에이전트 실패의 흔한 원인은 프로젝트 규칙과 검증 방법을 모르는 상태에서 코드를 수정하는 것이다.
  - Steering은 팀의 개발 규칙, 아키텍처 원칙, 코딩 컨벤션을 에이전트에 지속적으로 주입하는 장치로 소개됐다.
  - MCP와 Powers를 통해 이슈, 문서, 테스트, 외부 API를 연결하면 에이전트가 수정 후 검증까지 수행할 수 있다.
  - 개발 효율은 코드 생성 속도보다 피드백 루프의 짧아짐에서 나온다.
- AWS/기술 키워드: Kiro, MCP, Steering, Powers, Developer Tools, Feedback Loop, AI Coding Agent
- AX TF 관점/회사 AX 도입 시사점: 사내 Claude Code류 도구 도입 시 "프롬프트 잘 쓰기"보다 팀별 steering 문서, 테스트 명령, 배포/검증 도구를 표준화하는 일이 먼저다. 에이전트가 읽을 수 있는 프로젝트 규칙과 실행 가능한 검증 루틴을 갖추면 신규 개발자 온보딩과 레거시 수정에도 바로 효과가 난다.
- 공유용 한줄: Kiro의 생산성은 코드를 빨리 쓰는 데서가 아니라, 프로젝트 지식과 검증 루프를 에이전트에게 연결하는 데서 나온다.

## sel-cmp201 - AWS 차세대 AI 인프라: 리전에서 AI Factory까지

- 시간/트랙/레벨/발표자: 2026-05-21 14:30-15:10 KST / Track 6 / 200 - Intermediate / 강동환(AWS), 신재현(AWS)
- 요약: AWS의 AI 인프라 전략을 리전, 가속 컴퓨팅, 네트워크, AI Factory 관점에서 설명한 세션이다. 대규모 학습과 추론은 GPU/가속기만이 아니라 EFA 같은 네트워크, 배포 단위, 리전 선택, 데이터 주권 요구와 함께 설계해야 한다는 점이 중심이다. AWS AI Factories는 엄격한 주권 요구가 있는 고객에게 완전 관리형 AI 인프라를 제공하면서도 클라우드 운영 편의성을 유지하는 선택지로 소개됐다.
- 주요 포인트:
  - AI 인프라는 컴퓨트 용량, 고성능 네트워크, 스토리지, 운영 자동화가 함께 맞물리는 시스템 문제다.
  - EFA로 연결된 대규모 가속 컴퓨팅 클러스터는 학습/추론 워크로드의 처리량과 지연시간에 직접 영향을 준다.
  - 리전 선택은 거리와 비용뿐 아니라 데이터 주권, 규제, 운영 책임 모델까지 함께 봐야 한다.
  - AI Factory는 고객의 물리적/규제적 요구를 반영하면서 관리형 AI 인프라 경험을 제공하는 방향으로 제시됐다.
- AWS/기술 키워드: AWS AI Factories, Accelerated Computing, GPU, EFA, Region, Sovereignty, AI Infrastructure, Managed Infrastructure
- AX TF 관점/회사 AX 도입 시사점: 회사가 대규모 모델 학습이나 민감 데이터 기반 AI를 검토한다면 "어느 모델을 쓸 것인가"와 별개로 리전, 데이터 위치, 네트워크, 운영 책임을 먼저 정리해야 한다. 내부 AX 플랫폼은 SaaS/API형, 관리형 클라우드형, 전용 인프라형을 워크로드 민감도별로 나누는 전략이 필요하다.
- 공유용 한줄: 차세대 AI 인프라는 GPU 구매가 아니라, 리전·네트워크·주권·운영 모델을 함께 설계하는 일이다.

## sel-sec302 - Amazon Bedrock AgentCore 로 AI 시대의 Zero Trust 구현하기

- 시간/트랙/레벨/발표자: 2026-05-21 14:30-15:10 KST / Track 7 / 300 - Advanced / 이민우(AWS), 황재훈(AWS)
- 요약: AI 에이전트가 도구와 API를 직접 호출하는 시대에 Zero Trust를 어떻게 적용할지 다룬 보안 세션이다. Amazon Bedrock AgentCore Identity와 Gateway를 사용해 에이전트의 신원, 사용자 위임 권한, 도구 접속, 자격 증명 보관을 중앙에서 관리하는 패턴이 소개됐다. 발표는 에이전트의 자율성을 유지하되 API 키나 OAuth 토큰을 안전하게 다루고, MCP 도구 연결을 통제 가능한 경로로 만드는 것이 핵심이라고 설명했다.
- 주요 포인트:
  - AI 에이전트도 사용자, 서비스, 도구와 마찬가지로 명시적 신원과 최소 권한 원칙을 가져야 한다.
  - AgentCore Identity는 에이전트와 사용자 위임 권한을 관리하고, 안전한 credential 저장소와 연계된다.
  - AgentCore Gateway는 MCP, API 등 도구 호출 경로를 중앙화해 보안 정책과 관측성을 적용하기 쉽게 만든다.
  - Zero Trust의 초점은 "에이전트를 막는 것"이 아니라, 어떤 권한으로 어떤 도구를 언제 호출했는지 통제하는 것이다.
- AWS/기술 키워드: Amazon Bedrock AgentCore, AgentCore Identity, AgentCore Gateway, Zero Trust, MCP, OAuth, API Key, Credential Store, Security
- AX TF 관점/회사 AX 도입 시사점: 사내 에이전트가 Jira, GitHub, DB, 사내 API를 호출하게 되면 토큰 관리와 권한 위임이 즉시 핵심 리스크가 된다. AX TF는 에이전트별 계정, 사용자 위임 범위, 도구 게이트웨이, 감사 로그를 표준 아키텍처로 정하고 개발팀이 임의 토큰을 프롬프트나 설정 파일에 넣지 않도록 해야 한다.
- 공유용 한줄: AI 에이전트 보안의 출발점은 모델 필터가 아니라, 신원·권한·도구 호출을 Zero Trust로 묶는 것이다.

## sel-biz204 - 20만 Amazonian의 AI 내재화 성공 경험, 그리고 Quick Desktop

- 시간/트랙/레벨/발표자: 2026-05-21 14:30-15:10 KST / Track 8 / 200 - Intermediate / 한상훈(AWS), 고지환(AWS)
- 요약: Amazon이 내부적으로 AI를 20만 임직원의 업무에 안착시킨 경험과 Amazon Quick Desktop을 소개한 세션이다. 핵심은 AI가 답변만 하는 단계에서 벗어나 파편화된 데이터, 보안 심사, 변화관리, 사용자 커뮤니티를 거쳐 실제 행동과 업무 수행으로 이어지게 만든 과정이다. Quick Desktop은 회사 데이터와 업무 도구를 연결해 검색, 질문, 실행을 한 곳에서 처리하는 네이티브 AI 팀메이트로 설명됐다.
- 주요 포인트:
  - AI 내재화는 도구 배포보다 데이터 연결, 보안 검토, 사용 습관 형성, 내부 챔피언 육성이 더 중요하다.
  - Amazon 내부 도입은 사용자 커뮤니티와 성공 사례 공유를 통해 현업의 인정을 얻는 방식으로 확산됐다.
  - Quick Desktop은 흩어진 문서, 대화, 티켓, 대시보드 정보를 기반으로 사용자의 업무 맥락을 파악하고 행동을 지원한다.
  - 파일럿에서 일상 업무로 넘어가려면 보안/거버넌스와 사용자 경험을 동시에 설계해야 한다.
- AWS/기술 키워드: Amazon Quick, Quick Desktop, Agentic AI, Enterprise Search, Business Applications, Change Management, AI Adoption
- AX TF 관점/회사 AX 도입 시사점: 사내 AX 확산은 모델 성능 발표보다 실제 사용자 집단, 업무별 플레이북, 커뮤니티, 교육 콘텐츠가 중요하다. 개발자에게는 Claude Code류 도구, 현업에게는 Quick류 업무 에이전트를 제공하되 보안 심사와 성공 사례 공유를 중앙에서 지원해야 확산 속도가 난다.
- 공유용 한줄: AI 내재화는 도구를 여는 날이 아니라, 직원들이 매일 쓰는 업무 흐름에 AI가 들어가는 날 시작된다.

## sel-dev305 - [네오위즈파트너스 | 알고릭스코퍼레이션] IaC 기반 EKS 멀티테넌시와 Sidecar-less 네트워킹

- 시간/트랙/레벨/발표자: 2026-05-21 14:30-15:10 KST / Track 9 / 300 - Advanced / 황우빈(네오위즈파트너스), 이주안(알고릭스코퍼레이션)
- 요약: EKS 기반 서비스 인프라를 단일 클러스터에서 멀티클러스터와 멀티테넌시 구조로 확장한 경험을 공유한 세션이다. Terragrunt 기반 IaC로 프로덕트별 배포와 권한 체계를 만들고, 이후 Cilium과 VPC Lattice를 결합해 사이드카 없이 클러스터 간 서비스 연결을 단순화하는 방향을 제시했다. 마지막 메시지는 연결은 AWS 관리형 기능에 맡기고, 통제와 거버넌스는 조직이 책임지는 선을 명확히 긋자는 것이었다.
- 주요 포인트:
  - EKS 멀티테넌시는 네임스페이스 분리만이 아니라 계정, 권한, 네트워크, 배포 정책을 IaC로 일관되게 관리해야 한다.
  - Terragrunt 기반 구조는 여러 프로덕트와 환경의 공통 규칙을 재사용하고 drift를 줄이는 데 유리하다.
  - Cilium과 VPC Lattice 조합은 서비스 간 연결을 가볍게 만들고 sidecar 운영 부담을 줄이는 선택지로 소개됐다.
  - 멀티클러스터 확장에서는 연결성과 통제성의 경계를 명확히 설계해야 운영 복잡도를 줄일 수 있다.
- AWS/기술 키워드: Amazon EKS, IaC, Terragrunt, Multi-tenancy, Multi-cluster, Cilium, VPC Lattice, Sidecar-less Networking, Cloud Operations
- AX TF 관점/회사 AX 도입 시사점: AI/AX 서비스가 늘어나면 EKS나 컨테이너 플랫폼 위에서 팀별 격리, 비용 배분, 네트워크 통제가 더 중요해진다. 에이전트/모델 서빙 플랫폼도 IaC 기반 멀티테넌시와 서비스 연결 표준을 먼저 잡아야 팀별 실험이 운영 리스크로 번지지 않는다.
- 공유용 한줄: AX 플랫폼의 확장성은 모델보다 먼저, 팀과 서비스가 안전하게 공존하는 EKS 멀티테넌시에서 갈린다.

## sel-aim202 - [우아한형제들] 우아한형제들의 Nova 2 프로덕션 적용 여정

- 시간/트랙/레벨/발표자: 2026-05-21 15:30-15:50 KST / Track 1 / 200 - Intermediate / 장재주, 남진호, 박경태(우아한형제들)
- 요약: 우아한형제들이 사내 개발자가 쉽게 LLM을 쓰도록 Bedrock LLM Hub를 만들고, Amazon Nova 2 Lite를 다국어 배달 서비스에 프로덕션 적용한 경험을 공유했다. 세션은 원클릭 API 키 발급, 비용 추적, 자바/코틀린 기반 백엔드 아키텍처로 진입 장벽을 낮춘 점과 실제 번역/다국어 처리 서비스에서 모델 선택보다 시스템 설계가 더 중요했다는 교훈을 강조했다. 마지막에는 LLM 성능을 높이는 적절한 아키텍처가 모델 자체보다 중요할 수 있다는 메시지로 마무리됐다.
- 주요 포인트:
  - "모두를 위한 Bedrock LLM Hub"로 사내 개발자 누구나 LLM API를 쉽게 발급받고 비용을 추적할 수 있게 했다.
  - Amazon Nova 2 Lite를 활용해 다국어 배달 서비스 기능을 프로덕션에 적용했다.
  - 백엔드 개발자 친화적인 자바/코틀린 아키텍처로 LLM 도입을 특정 AI 팀의 전유물이 아니게 만들었다.
  - 모델 선정만큼 요청 라우팅, 필드 단위 번역, 이벤트 흐름, 장애 대응 등 시스템 설계가 중요했다.
- AWS/기술 키워드: Amazon Bedrock, Amazon Nova 2 Lite, LLM Hub, Java, Kotlin, Multilingual Service, Production LLM
- AX TF 관점/회사 AX 도입 시사점: 사내 LLM 확산을 위해서는 모델 API를 각 팀이 따로 붙이는 방식보다 중앙 LLM Hub가 효과적이다. API 키 발급, 비용 가시화, 표준 SDK, 샘플 코드, 운영 가이드를 제공하면 백엔드 개발자도 AX 구현의 핵심 인력이 될 수 있다.
- 공유용 한줄: 우아한형제들 사례는 LLM 도입의 병목이 모델 접근이 아니라, 개발자가 안심하고 쓰는 내부 LLM 플랫폼임을 보여준다.

## sel-prt217-s - Oracle AI Database@AWS! AWS는 그대로, Exadata로 더욱 강력하게!(sponsored by Oracle)

- 시간/트랙/레벨/발표자: 2026-05-21 15:30-15:50 KST / Track 2 / 200 - Intermediate / 조경진(Oracle Korea)
- 요약: Oracle AI Database@AWS를 통해 AWS 환경에서 Oracle Exadata와 Oracle AI Database 26ai를 활용하는 방안을 소개한 스폰서 세션이다. 온프레미스와 클라우드가 분리된 구조에서 생기는 데이터 이동, 운영 복잡도, 성능 요구를 줄이고, AWS 서비스와 Oracle 데이터베이스의 강점을 함께 쓰는 구성이 중심이었다. AI 관점에서는 데이터베이스 안의 데이터, 벡터/AI 기능, 보안과 운영을 함께 묶어 활용하는 메시지가 강조됐다.
- 주요 포인트:
  - Oracle AI Database@AWS는 AWS 안에서 Exadata 기반 Oracle 데이터베이스 성능과 운영 모델을 쓰는 선택지로 소개됐다.
  - Oracle AI Database 26ai는 AI 개발과 데이터 활용을 데이터베이스 레이어에서 지원하는 방향을 제시한다.
  - 온프레미스-클라우드 분리로 인한 데이터 이동과 운영 부담을 줄이는 것이 주요 가치다.
  - AI가 데이터를 스스로 활용하려면 데이터가 있는 위치의 성능, 보안, 운영 통제가 함께 보장되어야 한다.
- AWS/기술 키워드: Oracle AI Database@AWS, Oracle AI Database 26ai, Exadata, Autonomous Database, Databases, Cloud Operations
- AX TF 관점/회사 AX 도입 시사점: 핵심 업무 데이터가 Oracle에 남아 있는 조직은 AI를 위해 무조건 데이터를 이동하기보다, DB 근처에서 AI 기능과 클라우드 서비스를 결합하는 아키텍처를 검토할 필요가 있다. AX TF는 데이터 이동 비용, 권한, 성능, 기존 DBA 운영 모델을 포함해 AI 데이터 접근 전략을 세워야 한다.
- 공유용 한줄: Oracle 기반 핵심 데이터를 가진 조직의 AX는 데이터 이관보다, 기존 DB 성능과 AWS AI 생태계를 함께 쓰는 경로가 현실적일 수 있다.

## sel-dvt302 - 에이전트 성능 평가와 개선: 개발부터 운영까지

- 시간/트랙/레벨/발표자: 2026-05-21 15:30-15:50 KST / Track 3 / 300 - Advanced / 김무현(AWS)
- 요약: 에이전트가 단순 생성형 응답에서 툴콜, 계획, 멀티 에이전트로 진화하면서 평가 방식도 개발 단계와 운영 단계 모두에 필요해졌다는 세션이다. AgentCore Evaluation과 Strands Evaluation을 이용해 개발 중 성능을 측정하고, 운영 중에는 프로덕션 에이전트를 지속적으로 모니터링하고 개선하는 흐름을 설명했다. LLM 기반 평가만 고집할 필요는 없으며, 중요한 케이스를 반복 평가하는 파이프라인을 만들어야 한다는 메시지가 실용적이었다.
- 주요 포인트:
  - 에이전트는 입력-출력 평가만으로 부족하며, 도구 선택, 계획, 실행 경로, 최종 결과를 함께 봐야 한다.
  - 개발 단계에서는 AgentCore Evaluation과 Strands Evaluation으로 기능별/케이스별 성능을 측정한다.
  - 운영 단계에서는 실제 영향 없이 평가를 돌리고, 중요한 케이스의 품질을 지속적으로 보장하는 파이프라인이 필요하다.
  - LLM-as-a-judge뿐 아니라 규칙 기반, 참조 답변, 재시도/비교 평가를 조합할 수 있다.
- AWS/기술 키워드: AgentCore Evaluation, Strands Evaluation, Agent Observability, LLM Evaluation, AI Function, Production Monitoring
- AX TF 관점/회사 AX 도입 시사점: 사내 에이전트 PoC가 늘어날수록 "잘 되는 것 같다"는 데모 평가를 벗어나 표준 평가셋, 회귀 테스트, 운영 모니터링이 필요하다. Claude Code류 개발 에이전트도 PR 품질, 테스트 통과율, 보안 규칙 위반, 재작업률 같은 평가 지표를 CI에 넣어야 한다.
- 공유용 한줄: 에이전트 품질은 출시 전에 한 번 보는 점수가 아니라, 개발부터 운영까지 계속 도는 평가 파이프라인이다.

## sel-prt106-s - Notion: API를 넘어 플랫폼으로 (sponsored by 노션, Notion)

- 시간/트랙/레벨/발표자: 2026-05-21 15:30-15:50 KST / Track 4 / 100 - Foundational / Eric Goldman(Notion)
- 요약: 메타데이터 기반 요약. VOD 전사 결과에 발화가 없어 공식 세션 설명을 기반으로 정리했다. Notion은 단순 CRUD API나 CLI, MCP를 넘어 에이전트가 실제 업무를 수행할 수 있는 공유 워크스페이스 플랫폼으로 진화하고 있다는 메시지를 제시했다. 핵심은 데이터를 동기화하고, 툴을 구축하고, 에이전트를 공동 작업 공간에 연결해 사람이 쓰는 업무 맥락과 AI가 실행하는 작업 맥락을 같은 공간에 두는 것이다.
- 주요 포인트:
  - 에이전트는 단순 API 호출보다 문서, 데이터, 권한, 협업 맥락이 통합된 업무 공간을 필요로 한다.
  - Notion은 어떤 데이터도 동기화하고 어떤 툴도 구축할 수 있는 플랫폼 인프라를 지향한다.
  - 공유 워크스페이스는 에이전트 결과를 사람이 검토하고 이어서 실행하기 좋은 표면이 될 수 있다.
  - MCP와 API는 연결 수단이고, 실제 업무 완결성은 사용자가 일하는 공간과 연결될 때 높아진다.
- AWS/기술 키워드: Notion, API, MCP, Workspace, Agent Platform, Collaboration, Knowledge Management
- AX TF 관점/회사 AX 도입 시사점: 사내 AX 도구는 모델과 API만으로는 부족하고, 결과가 쌓이고 검토되고 재사용되는 업무 공간이 필요하다. Notion류 지식 베이스를 사용한다면 에이전트가 문서를 읽고 쓰는 권한, 변경 이력, 승인 흐름을 표준화하는 것이 중요하다.
- 공유용 한줄: 업무 에이전트의 진짜 목적지는 API가 아니라, 사람이 함께 일하는 공유 워크스페이스다.

## sel-prt103-s - MUSINSA - ClickHouse Cloud를 활용한 Audience Engine 및 다각적 비즈니스 확장을 위한 전략 (sponsored by ClickHouse)

- 시간/트랙/레벨/발표자: 2026-05-21 15:30-15:50 KST / Track 5 / 100 - Foundational / 이기훈(ClickHouse), 최민영(무신사), 박병길(무신사)
- 요약: 무신사가 AWS 기반 ClickHouse Cloud로 Audience Engine을 구축하고, Vector Search 룩어라이크 타겟팅, OLAP 기반 AI 분석, 실시간 로그 서빙 등으로 데이터 활용 범위를 넓힌 사례다. 발표는 ClickPipes와 Materialized View를 활용해 데이터 파이프라인과 집계 처리를 단순화하고, 셀프호스팅 ClickHouse 운영 부담을 줄이기 위해 ClickHouse Cloud를 검토한 경험을 공유했다. 패션 플랫폼의 고객 세그먼트, 로그, 추천/타겟팅 데이터를 빠르게 분석하는 것이 핵심 가치였다.
- 주요 포인트:
  - Audience Engine은 대규모 고객 행동 데이터를 세그먼트화하고 타겟팅/분석/서빙에 활용하는 데이터 기반이다.
  - ClickPipes와 Materialized View로 실시간성 있는 데이터 적재와 집계를 구성했다.
  - Vector Search를 활용한 룩어라이크 타겟팅과 OLAP 분석을 함께 다루며 AI 활용 범위를 넓혔다.
  - 셀프호스팅 운영 부담을 줄이고 데이터 팀이 제품 가치에 집중하기 위해 ClickHouse Cloud를 선택지로 제시했다.
- AWS/기술 키워드: ClickHouse Cloud, ClickPipes, Materialized View, Vector Search, OLAP, Audience Engine, Real-time Logs, AWS
- AX TF 관점/회사 AX 도입 시사점: AX 서비스가 개인화, 추천, 영업/마케팅 자동화로 확장되려면 빠른 분석 DB와 실시간 이벤트 파이프라인이 필요하다. 기존 DW만으로 어렵다면 ClickHouse류 OLAP/Vector Search 기반을 별도 서빙·분석 계층으로 두는 아키텍처를 검토할 만하다.
- 공유용 한줄: 무신사 사례는 AX 개인화의 기반이 모델만이 아니라, 빠르게 세그먼트화하고 서빙할 수 있는 실시간 분석 엔진임을 보여준다.
