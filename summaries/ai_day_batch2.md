# AI Day Batch 2 요약

## sel-dvt203 - [LG전자] AI 기반 개발 라이프사이클 (AI-DLC) 소개

- 시간/트랙/레벨/발표자: 12:50-13:30 KST / Track 5, Developer Tools / 200 Intermediate / 김수연(AWS), 박태진(LG전자)
- 요약: 단순 코드 생성 도구 도입만으로는 SDLC 전체 생산성이 크게 오르지 않는다는 문제의식에서, 요구사항 정의부터 UX/UI 설계, 기술 의사결정, 코드 생성, 테스트, 배포까지 AI와 사람이 협업하는 AI-DLC 방법론을 소개했다. LG전자는 대규모 코드베이스와 기존 SRS/HLD/LLD 산출물 체계를 반영해 조직 맞춤형 워크플로우를 설계했고, 산출물 간 컨텍스트 단절을 줄이는 데 초점을 뒀다.
- 주요 포인트:
  - AI-DLC는 Inception, Construction, Operation 단계로 요구사항, 설계, 구현, 테스트, 배포를 연결한다.
  - AI가 모든 결정을 대신하는 방식보다, 사람의 의도와 의사결정을 문서화하고 다음 단계 컨텍스트로 넘기는 방식이 중요하다.
  - 대규모 레거시 현대화에서는 기존 의사결정, API 경계, 테스트 케이스, 외부 컨텍스트를 명시적으로 수집해야 한다.
  - LG전자 사례에서는 문서 생성 속도보다 사람이 읽고 판단하는 속도가 병목이 될 수 있어, 리뷰 가능한 산출물 크기와 단계 분리가 중요했다.
- AWS/기술 키워드: AI-DLC, SDLC, AI coding assistant, SRS, HLD, LLD, test case, adaptive workflow, legacy modernization
- AX TF 관점/회사 AX 도입 시사점: Claude Code류 도구를 전사에 뿌리는 것만으로는 생산성 개선이 제한적이다. 우리 회사도 요구사항-설계-코드-테스트-운영 산출물의 표준 템플릿, 단계별 승인 기준, AI가 참조해도 되는 컨텍스트 목록을 먼저 정의해야 한다.
- 공유용 한줄: AI 개발 도입의 핵심은 “코드를 빨리 쓰기”가 아니라 SDLC 전체 컨텍스트를 끊기지 않게 관리하는 것이다.

## sel-cmp202 - 인퍼런스와 모델 퍼포먼스 최적화를 위한 EKS 아키텍처

- 시간/트랙/레벨/발표자: 12:50-13:30 KST / Track 6, Architecture·AI·Cloud Operations / 200 Intermediate / 정영준(AWS)
- 요약: LLM 추론 비용과 지연을 줄이기 위한 Amazon EKS 기반 GPU 운영 전략을 다뤘다. EKS Auto Mode, Karpenter, GPU Operator, Cluster Autoscaler, DRA 등을 워크로드 성숙도에 따라 선택하고, vLLM, KV cache-aware routing, GPU autoscaling, tiered gateway 구성으로 처리량과 GPU utilization을 높이는 방향을 설명했다.
- 주요 포인트:
  - LLM 추론 최적화는 비용 절감과 UX 개선이 동시에 걸린 문제이며, first-token latency와 throughput을 함께 봐야 한다.
  - 시작점은 EKS Auto Mode가 적합하고, 더 세밀한 GPU 분할과 최적화가 필요하면 managed node, Cluster Autoscaler, DRA 조합으로 확장한다.
  - 대규모·MoE 모델은 양자화, 모델 가중치 로딩 최적화, Nitro 기반 네트워크 최적화가 중요하다.
  - 에이전틱 AI 플랫폼은 모델 개발, 평가, 배포, 추론까지 단일 워크플로우로 이어져야 운영 가능하다.
- AWS/기술 키워드: Amazon EKS, EKS Auto Mode, GPU, NVIDIA, Karpenter, DRA, vLLM, KV cache, autoscaling, tiered gateway, Nitro
- AX TF 관점/회사 AX 도입 시사점: 내부 AI 서비스가 늘면 모델 호출 비용이 빠르게 불어난다. PoC 단계부터 토큰당 비용, GPU utilization, first-token latency, 배치/동시성 정책을 측정 가능한 표준 KPI로 두고 플랫폼팀이 공통 추론 런타임을 제공하는 방향이 좋다.
- 공유용 한줄: LLM 플랫폼의 승부는 모델 선택만이 아니라 GPU를 얼마나 덜 놀리고 지연을 얼마나 낮추느냐에 달려 있다.

## sel-sec201 - Agent-Driven 개발 환경, 보안 강화 전략은?

- 시간/트랙/레벨/발표자: 12:50-13:30 KST / Track 7, Security & Identity / 200 Intermediate / 이지영(AWS), 한태경(AWS)
- 요약: Claude Code, Kiro IDE, GitHub Copilot 같은 Agent-Driven 개발 환경에서는 코드 작성 속도가 보안 검토 속도를 압도하므로, 설계검토, 코드리뷰, 침투테스트를 자동화하는 AWS Security Agent 접근이 필요하다고 설명했다. 보안 요구사항을 조직별로 정의하고, PR 리뷰와 전체 코드 리뷰에서 취약점 탐지와 remediation 제안을 수행하는 흐름을 시연했다.
- 주요 포인트:
  - AI 개발은 취약한 코드가 빠르게 생산·배포될 위험을 키운다.
  - 보안은 배포 전 마지막 관문이 아니라 설계와 코드 작성 시점으로 당겨져야 한다.
  - Security Agent는 설계검토, 코드리뷰, 침투테스트를 각각 수행하고, 취약점 체인과 권한 상승 가능성까지 검증한다.
  - 단순히 “취약점 있음”을 알려주는 수준을 넘어 수정안과 리포트를 생성하는 것이 개발자 경험 측면에서 중요하다.
- AWS/기술 키워드: AWS Security Agent, secure SDLC, PR review, code remediation, penetration testing, OWASP Top 10, vulnerability chaining
- AX TF 관점/회사 AX 도입 시사점: AI 코딩 도구 도입 기준에 “보안 에이전트 리뷰 통과”를 포함해야 한다. 특히 사내 표준 보안 요구사항, 금지 API, 시크릿 처리, 개인정보 처리 기준을 에이전트가 검사할 수 있는 룰셋으로 만들어야 한다.
- 공유용 한줄: AI 개발 속도를 허용하려면 보안 리뷰도 에이전트 속도로 따라붙어야 한다.

## sel-biz202 - Amazon Connect Customer를 활용한 에이전틱 AI 기반 고객 경험 혁신

- 시간/트랙/레벨/발표자: 12:50-13:30 KST / Track 8, Business Applications / 200 Intermediate / 김정곤(AWS), 이일구(AWS)
- 요약: Amazon Connect를 AI 네이티브 고객경험 플랫폼으로 설명하며, 고객 셀프서비스, 상담사 지원, 상담 요약, 채널 통합, 분석까지 모든 접점에 AI를 적용하는 방식을 다뤘다. AI 에이전트는 프롬프트와 도구 연결을 통해 고객 의도를 이해하고, AgentCore와 지식 저장소, 기존 시스템 연계를 통해 실행까지 담당한다.
- 주요 포인트:
  - 고객 경험의 문제는 채널과 도구가 분산되어 맥락이 끊기는 데 있다.
  - Amazon Connect는 음성, 채팅, 이메일 등 모든 채널의 고객 데이터를 통합해 AI가 활용할 수 있게 한다.
  - AI 에이전트는 상담원을 대체하기보다 단계별 가이드, 자동 요약, 양식 작성 등 반복 업무를 맡아 사람의 공감과 판단을 돕는다.
  - 컨택센터 AI는 별도 챗봇을 붙이는 방식보다 기존 고객 여정 안에 자연스럽게 내재화하는 방식이 효과적이다.
- AWS/기술 키워드: Amazon Connect, Amazon Bedrock, AgentCore, knowledge base, customer profile, contact center AI, self-service, agent assist
- AX TF 관점/회사 AX 도입 시사점: 사내 고객·임직원 지원 업무도 단일 문의 채널보다 “맥락 유지”가 더 중요하다. FAQ 봇이 아니라 상담 이력, 사용자 프로필, 업무 시스템 액션을 연결하는 에이전트 설계가 필요하다.
- 공유용 한줄: 고객 AI의 핵심은 답변 자동화가 아니라 채널을 넘어 고객 맥락을 계속 이어가는 것이다.

## sel-dev307 - Kiro Spec 모드 가속 가이드 & 서버리스 CDC 레이크하우스

- 시간/트랙/레벨/발표자: 12:50-13:30 KST / Track 9, AI·Databases / 300 Advanced / 최지연(AWSKRUG), 강은호(스테이지랩스)
- 요약: 1부는 Kiro Spec Mode를 BDD와 FSD 구조에 결합해 LLM 컨텍스트를 격리하고 코드 구조 붕괴를 줄이는 사례를 소개했다. 2부는 AWS DMS Serverless, S3, Glue, Iceberg를 활용해 Aurora PostgreSQL의 변경 데이터를 CDC 방식으로 적재하는 서버리스 레이크하우스 구축 경험을 공유했다.
- 주요 포인트:
  - Kiro Spec Mode는 requirements, design, task 단계로 “무엇을 만들지”를 계약처럼 고정한다.
  - BDD 시나리오로 행동 기준을 명시하고 FSD 폴더 구조로 코드 위치를 강제하면 AI가 임의 구조를 만들 가능성이 줄어든다.
  - CDC 레이크하우스는 DMS Serverless로 변경 데이터를 S3에 적재하고, Glue/Iceberg로 최신 상태를 관리하는 구조다.
  - 백필, 신규 테이블 추가, CDC 파일 분류, PK 조합, 최신값 유지 같은 운영 설계가 실제 성공을 좌우한다.
- AWS/기술 키워드: Kiro Spec Mode, BDD, Cucumber, FSD, AWS DMS Serverless, Amazon S3, AWS Glue, Apache Iceberg, CDC, Aurora PostgreSQL
- AX TF 관점/회사 AX 도입 시사점: AI 코딩 표준에는 “스펙 문서”와 “폴더/아키텍처 경계”를 같이 넣어야 한다. 데이터 AX 과제는 배치성 데이터마트보다 CDC 기반의 최신 데이터 자산화 패턴을 우선 검토할 만하다.
- 공유용 한줄: 좋은 AI 코드 품질은 좋은 스펙과 강제된 구조에서 나온다.

## sel-aim201 - Nova Forge와 Bedrock RFT로 모델 성능 극대화

- 시간/트랙/레벨/발표자: 13:50-14:10 KST / Track 8, AI·Business Applications / 200 Intermediate / 우지환(AWS), 황윤상(AWS)
- 요약: 기업 고유 데이터와 업무 프로세스를 반영한 모델 커스터마이징 방법으로 Nova Forge와 Amazon Bedrock RFT를 소개했다. Nova Forge는 모델 개발 단계별 체크포인트, AWS 큐레이션 데이터, 기업 데이터, 보상 함수를 결합해 기업 맞춤 모델을 만들고, Bedrock RFT는 대규모 라벨 데이터 없이 강화학습 기반으로 정확도와 안전성을 높이는 방법을 제공한다.
- 주요 포인트:
  - 범용 파운데이션 모델은 기업 프로세스와 규제 맥락을 충분히 알지 못하므로 커스텀 모델 수요가 생긴다.
  - Nova Forge는 Nova 모델 개발 단계의 체크포인트를 활용해 기업 데이터와 AWS 데이터셋을 블렌딩한다.
  - 보상 함수는 “좋은 답변”의 기준을 기업별로 반영하는 장치다.
  - Bedrock RFT는 SFT의 데이터 한계를 보완하고, 적은 데이터로도 모델 행동을 강화할 수 있다.
- AWS/기술 키워드: Amazon Nova Forge, Amazon Bedrock, RFT, RLVR, RLAIF, reward function, S3, custom model, fine-tuning
- AX TF 관점/회사 AX 도입 시사점: RAG만으로 해결되지 않는 전문 업무는 커스텀 모델 또는 RFT 후보로 분류해야 한다. 단, “좋은 답변”의 평가 기준과 보상 함수를 업무 부서가 함께 정의할 수 있어야 한다.
- 공유용 한줄: 모델 커스터마이징은 데이터만 넣는 일이 아니라 회사가 원하는 답의 기준을 학습시키는 일이다.

## sel-prt221-s - Enterprise AI Transformation: Agentic AI로 만드는 실질적인 비즈니스 성과 (sponsored by LG CNS)

- 시간/트랙/레벨/발표자: 13:50-14:10 KST / Partner Track / 200 Intermediate / 이상원(LG CNS)
- 요약: “AI를 아는가”에서 “AI가 어떤 비즈니스 지표를 바꾸는가”로 질문을 바꿔야 한다는 메시지의 세션이었다. LG CNS는 제조, 여행, 제약 등 사례를 통해 에이전틱 AI를 단순 자동화, 휴먼 인 더 루프 자동화, 풀 에이전틱 AI로 구분하고 업무 유형별 도입 방식을 설명했다.
- 주요 포인트:
  - 에이전틱 AI의 목표는 모델 도입이 아니라 매출, 생산성, 비용, 고객경험 같은 지표 변화다.
  - 반복적이고 프로세스가 명확한 제조 업무는 자동화 효과가 크며, 한 사례에서는 80시간 업무를 16시간 수준으로 줄였다고 설명했다.
  - 여행 서비스처럼 고객 영향이 큰 업무는 사람의 승인과 안전장치를 남겨야 한다.
  - 제약처럼 전문성이 높은 영역은 데이터 수집, 분석, 추천까지 AI가 수행하되 리스크 관리와 의사결정 체계를 함께 설계해야 한다.
- AWS/기술 키워드: Agentic AI, workflow automation, human-in-the-loop, business KPI, enterprise AI transformation
- AX TF 관점/회사 AX 도입 시사점: AX 과제 선정 기준은 “AI 적용 가능성”보다 “움직일 KPI”여야 한다. 업무 유형별로 완전 자동화, 보조 자동화, 승인형 자동화를 구분하는 포트폴리오가 필요하다.
- 공유용 한줄: AX 과제는 모델이 아니라 병목 KPI에서 출발해야 한다.

## sel-prt201-s - SK AX가 구현한 SageMaker 기반 분석가와 현업의 통합 AI 환경 (sponsored by SK AX)

- 시간/트랙/레벨/발표자: 13:50-14:10 KST / Partner Track / 200 Intermediate / 조진선(SK AX)
- 요약: SK Innovation E&S의 통합 데이터·AI 플랫폼 구축 사례를 통해 AI 실패의 본질을 데이터 사일로, 현업 접근성 부족, 불안한 보안/비용 구조에서 찾았다. 3-Layer 레이크하우스, 비즈니스 메타데이터 카탈로그, Bedrock 기반 메타데이터 검색, SageMaker Unified Studio로 분석가와 현업이 함께 쓰는 환경을 구성했다.
- 주요 포인트:
  - AI 프로젝트가 실패하는 이유는 모델보다 데이터에 닿지 못하는 구조인 경우가 많다.
  - Lake, DW, Mart 계층으로 원천 데이터, 정제/실험 데이터, LLM·BI 활용 데이터를 구분했다.
  - IT 메타데이터와 비즈니스 메타데이터를 분리해 현업이 IT 용어 없이 데이터를 찾을 수 있게 했다.
  - Lake Formation 기반 권한관리와 SageMaker Unified Studio로 데이터 엔지니어, 분석가, 현업의 작업 환경을 통합했다.
- AWS/기술 키워드: Amazon SageMaker Unified Studio, Amazon Bedrock Knowledge Bases, AWS Lake Formation, Amazon S3, AWS Glue, Athena, lakehouse, metadata catalog
- AX TF 관점/회사 AX 도입 시사점: 사내 AX 플랫폼은 “챗봇”보다 데이터 탐색성과 권한 거버넌스가 먼저다. 현업 용어 기반 메타데이터와 AI 검색을 제공해야 분석/GenAI 활용률이 올라간다.
- 공유용 한줄: AI 활용률은 모델 성능보다 현업이 안전하게 데이터를 찾고 쓸 수 있는 구조에서 갈린다.

## sel-prt215-s - Unlocking Cost-Efficient Cloud and AI Performance on AWS with AMD EPYC (sponsored by AMD)

- 시간/트랙/레벨/발표자: 13:50-14:10 KST / Partner Track / 200 Intermediate / 송성운(AMD Korea)
- 요약: AMD EPYC 기반 AWS EC2 인스턴스가 클라우드와 AI 워크로드에서 성능과 비용 효율을 제공하는 방식을 소개했다. 최신 M8a, C8a, R8a 계열과 데이터베이스, AI 추론, HPC, 미디어 처리 워크로드 사례를 통해 CPU 기반 AI 추론과 범용 워크로드 최적화 포인트를 설명했다.
- 주요 포인트:
  - AI 워크로드가 모두 GPU만 필요한 것은 아니며, CPU 기반 추론과 전처리·데이터 처리도 비용 최적화 여지가 크다.
  - C8a는 전세대 대비 처리시간 개선, M8a는 여러 워크로드에서 실행 성능 향상과 비용 절감 사례를 강조했다.
  - PostgreSQL 등 데이터베이스 워크로드에서는 인스턴스 크기와 CPU 특성 선택이 TCO에 직접 영향을 준다.
  - Netflix, Pinterest 등 사례를 통해 성능 예측성과 비용 대비 성능을 강조했다.
- AWS/기술 키워드: AMD EPYC, Amazon EC2, M8a, C8a, R8a, PostgreSQL, CPU inference, HPC, TCO, workload optimization
- AX TF 관점/회사 AX 도입 시사점: AX 인프라 비용 최적화는 GPU만 보지 말고 CPU 추론, 임베딩 전처리, ETL, 벡터 구축, 데이터베이스까지 워크로드별 인스턴스 벤치마크가 필요하다.
- 공유용 한줄: AI 비용 최적화는 GPU 구매 전략이 아니라 워크로드별 컴퓨트 선택 전략이다.

## sel-prt207-s - LLM 애플리케이션 프로덕션 운영, Observability로 풀다 (sponsored by 와탭, WhaTap)

- 시간/트랙/레벨/발표자: 13:50-14:10 KST / Partner Track / 200 Intermediate / 신민철(WhaTap)
- 요약: LLM 애플리케이션은 만들기는 쉬워졌지만 프로덕션 운영에서는 토큰 비용 폭증, 예측 어려운 응답 지연, 품질 저하, 할루시네이션 문제가 발생한다고 설명했다. 기존 APM/RUM만으로는 LLM API 호출, 프롬프트, 응답, 토큰 사용량, 모델 품질을 충분히 관측할 수 없으므로 LLM 전용 옵저버빌리티가 필요하다는 내용이다.
- 주요 포인트:
  - LLM 앱은 단순 API 호출처럼 보여도 실제 프로덕션 파이프라인은 여러 LLM 호출과 도구 호출을 포함한다.
  - 토큰 사용량은 비용과 직결되며 모델별 가격 차이 때문에 비용이 비선형적으로 증가할 수 있다.
  - Provider LLM은 API 영역 중심으로, Local LLM은 인프라 영역까지 포함해 관측 지점을 다르게 봐야 한다.
  - 프롬프트, 응답 품질, 지연, 토큰, 비용, 로그, 트레이스가 함께 연결되어야 운영자가 원인을 찾을 수 있다.
- AWS/기술 키워드: LLM observability, Amazon Bedrock, APM, RUM, token cost, latency, prompt/response trace, monitoring
- AX TF 관점/회사 AX 도입 시사점: 사내 LLM 앱 표준에 토큰 예산, 호출 트레이스, 프롬프트/응답 로깅 정책, 품질 평가 지표를 포함해야 한다. 운영 대시보드 없이 배포된 챗봇은 비용과 품질 리스크를 숨긴다.
- 공유용 한줄: LLM 앱은 배포 후부터 진짜 비용과 품질 문제가 시작된다.

## sel-prt213-s - Amazon Bedrock 기반 GitLab Duo 에이전트 플랫폼으로 혁신 가속화 (sponsored by Gitlab)

- 시간/트랙/레벨/발표자: 13:50-14:10 KST / Partner Track / 200 Intermediate / Jimmy Gam(GitLab)
- 요약: GitLab Duo Agent Platform이 Amazon Bedrock과 결합해 SDLC 전반에 에이전틱 AI를 내재화하는 방식을 소개했다. IDE나 CLI에 흩어진 AI 도구가 컨텍스트를 잃는 문제를 지적하며, 계획, 코딩, 코드리뷰, 보안, 컴플라이언스, CI/CD 데이터를 하나의 데이터 모델과 워크플로우 안에서 활용하는 접근을 제시했다.
- 주요 포인트:
  - 코드 작성 속도만 빨라져도 코드리뷰, 보안 스캔, 테스트, 승인 과정이 따라오지 못하면 전체 생산성은 제한된다.
  - GitLab의 통합 데이터 모델은 issue, merge request, pipeline, 취약점, 정책 데이터를 에이전트 컨텍스트로 제공한다.
  - Amazon Bedrock 연동은 IAM, VPC endpoint, 리전 데이터 보관 등 AWS 보안 패턴을 활용해 데이터 레지던시 요구를 맞춘다.
  - 외부 에이전트와의 통합도 지원하되, 승인된 모델과 AI Gateway를 통해 사용량·정책·거버넌스를 통제한다.
- AWS/기술 키워드: GitLab Duo Agent Platform, Amazon Bedrock, AI Gateway, SDLC, DevSecOps, IAM, VPC endpoint, data residency, merge request
- AX TF 관점/회사 AX 도입 시사점: AI 코딩 도구를 개별 IDE 플러그인으로만 보면 거버넌스가 빠진다. 사내 Git 플랫폼의 이슈, MR, CI, 보안 결과를 에이전트 컨텍스트로 연결하는 표준이 필요하다.
- 공유용 한줄: 개발 AI의 생산성은 IDE 안이 아니라 SDLC 전체 데이터 모델 안에서 완성된다.

## sel-prt301-s - Secure AI by Design (sponsored by Palo Alto Networks)

- 시간/트랙/레벨/발표자: 13:50-14:10 KST / Partner Track / 300 Advanced / 김범수(Palo Alto Networks)
- 요약: AI 사용과 AI 개발을 모두 설계 단계부터 보안 내재화해야 한다는 메시지의 세션이었다. Prisma Browser는 임직원의 외부 생성형 AI 사용을 발견·평가·통제하고, Prisma AIRS는 AI 애플리케이션과 에이전트 생태계의 모델, 데이터, 플러그인, 런타임, 프롬프트 인젝션, 데이터 유출 위험을 보호하는 플랫폼으로 소개됐다.
- 주요 포인트:
  - 승인되지 않은 AI 서비스 사용과 민감정보 입력은 이미 현실적인 Shadow AI 리스크다.
  - 브라우저 계층에서 어떤 AI 도구를 누가 쓰는지 발견하고, 리스크와 데이터 정책을 적용해야 한다.
  - AI 앱은 모델, 데이터셋, 플러그인, 에이전트, 런타임이 연결된 생태계라 포인트 솔루션만으로는 복잡도가 커진다.
  - AI red teaming, model security, posture management, runtime security, prompt injection 탐지, 데이터 유출 차단이 함께 필요하다.
- AWS/기술 키워드: Prisma Browser, Prisma AIRS, AI governance, Shadow AI, AI red teaming, prompt injection, model security, runtime security, DLP
- AX TF 관점/회사 AX 도입 시사점: AX TF는 사내 AI 사용 가시성부터 확보해야 한다. 승인 AI 도구 목록, 민감정보 입력 차단, 자체 AI 앱 보안 점검, 에이전트 권한 관리가 함께 설계되어야 한다.
- 공유용 한줄: AI 보안은 차단 정책이 아니라 발견, 허용, 통제, 보호를 한 번에 설계하는 일이다.

## sel-prt302-s - AWS AI와 서버리스로 구축하는 완성차 지능형 상품 전략 플랫폼 (sponsored by 이테크시스템 / ETECH SYSTEM)

- 시간/트랙/레벨/발표자: 13:50-14:10 KST / Partner Track / 300 Advanced / 김동희(ETECH SYSTEM)
- 요약: 완성차 기업의 PDF, 웹, 카탈로그 기반 비정형 데이터 수집과 표준화 문제를 AWS AI와 서버리스 아키텍처로 해결한 사례다. Step Functions, EventBridge, Lambda로 수집·크롤링·추출·정규화·저장을 병렬 워크플로우로 만들고, Bedrock 기반 추출과 S3/Glue/Athena 기반 데이터 레이크로 상품 전략 데이터를 자산화했다.
- 주요 포인트:
  - 외부 웹/PDF 데이터는 형식과 명칭이 제각각이라 키워드 검색만으로는 누락과 중복이 생긴다.
  - Bedrock은 비정형 텍스트에서 차량 사양을 JSON 구조로 추출하고, 표준화된 데이터로 변환하는 역할을 맡았다.
  - Step Functions는 150개 이상 차종의 월별 업데이트를 병렬 처리하고, 수집 리드타임을 크게 줄였다.
  - S3, Glue Data Catalog, Athena, 대시보드로 출처와 무결성을 보존하면서 현업이 직접 분석할 수 있게 했다.
- AWS/기술 키워드: Amazon Bedrock, Claude Sonnet 4.5, AWS Step Functions, Amazon EventBridge, AWS Lambda, Amazon S3, AWS Glue, Athena, S3 Vector, serverless
- AX TF 관점/회사 AX 도입 시사점: 외부 PDF/웹 기반 리서치 업무는 AX 우선 후보가 될 수 있다. 단순 크롤링보다 출처 추적, 표준 명칭 매핑, JSON 스키마화, 오류율 모니터링을 포함해야 실무 의사결정에 쓸 수 있다.
- 공유용 한줄: 비정형 데이터 자동화의 가치는 수집 속도보다 표준화와 출처 검증에서 나온다.

## sel-prt206-s - 속도와 제어를 동시에 - Cloudflare에서 AI 에이전트 구축하기 (sponsored by 클라우드플레어/Cloudflare)

- 시간/트랙/레벨/발표자: 13:50-14:10 KST / Partner Track / 100 Foundational / 조성윤(Cloudflare)
- 요약: AI 에이전트가 코드를 작성하고 실행하며 DB 조회와 API 호출까지 수행하는 시대에는 “빠른 배포”와 “권한·감사·격리”가 함께 필요하다고 설명했다. Cloudflare AI Gateway, MCP 서버 포털, 샌드박스 실행 환경을 통해 에이전트의 LLM 호출, 도구 접근, 데이터 유출, 무한 루프, 권한 남용을 통제하는 접근을 제시했다.
- 주요 포인트:
  - 2023년의 AI가 텍스트 생성 도구였다면 2026년의 AI 에이전트는 실행 주체에 가깝다.
  - 에이전트에는 직원처럼 신원, 최소 권한, 정책, 감사 로그, 격리된 실행 환경이 필요하다.
  - MCP 서버 포털은 승인된 도구만 사용하게 하는 관문 역할을 한다.
  - AI Gateway는 LLM 트래픽의 제어 지점으로 DLP, 사용량 제한, 루프 탐지, 소스코드/PII 유출 방지에 활용된다.
- AWS/기술 키워드: Cloudflare AI Gateway, MCP server portal, AI agent sandbox, DLP, policy control, audit log, least privilege
- AX TF 관점/회사 AX 도입 시사점: 사내 에이전트 실험은 “개발자 편의”만 보고 열면 위험하다. 도구 호출을 승인 목록으로 제한하고, 에이전트별 권한과 로그, 샌드박스 실행 정책을 먼저 잡아야 한다.
- 공유용 한줄: AI 에이전트는 도구가 아니라 실행 주체이므로 사람처럼 권한과 감사가 필요하다.
