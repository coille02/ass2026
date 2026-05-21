# AWS Summit Seoul 2026 AI Day 영상 요약

작성 기준: AWS Summit Seoul 2026 Day 2 | AI Day 세션 VOD를 기준으로 정리했습니다. 각 세션은 가능한 경우 VOD 음성 전사를 기반으로 요약하고, 전사나 VOD 접근이 실패한 경우 공식 세션 메타데이터 기반 보조 요약으로 표시합니다.

## 읽는 방법

각 세션은 동일한 형식으로 정리했습니다.

- 세션 정보: 시간, 트랙, 레벨, 발표자, 태그
- 핵심 요약: 발표의 문제의식과 결론
- 주요 포인트: 발표에서 실제로 기억할 만한 내용
- AWS/기술 키워드: 언급된 서비스, 아키텍처, 방법론
- AX TF 관점: 회사 AX 도입 논의와 연결할 수 있는 시사점
- 공유용 한줄: 내부 공유 시 바로 가져다 쓸 수 있는 문장

## 전체 흐름 메모

AI Day의 큰 흐름은 생성형 AI를 실제 프로덕션으로 가져가기 위한 데이터, 개발 방법론, 보안, 인프라, 평가, 운영 체계에 집중되어 있습니다. Industry Day가 산업별 적용 사례를 보여줬다면, AI Day는 그 사례를 가능하게 하는 플랫폼과 운영 원칙을 더 깊게 다룹니다. 특히 AgentCore, Strands Agents, Kiro, SageMaker, Bedrock, AI-ready data, AI 보안, MLOps/AIOps, 추론 인프라 최적화가 반복적으로 등장합니다.

## 세션 인덱스

| 시간 | 트랙 | ID | 세션 |
|---|---|---|---|
| 09:30 | Keynote | sel-key002 | 기조연설 - AI Day |
| 11:10 | Track 1 | sel-aim301 | Superb AI의 HyperPod 기반 비전 파운데이션 모델 구축 여정 |
| 11:10 | Track 2 | sel-ant305 | 에이전틱 AI를 위한 데이터 실무 가이드 |
| 11:10 | Track 3 | sel-aim305 | [삼성전자] 21억 사용자규모 삼성 어카운트의 에이전틱 AIOps on AWS |
| 11:10 | Track 4 | sel-mam201 | 기술 부채의 한계를 넘어 AI-Ready 비즈니스로: AWS가 제안하는 에이전틱 AI 마이그레이션 |
| 11:10 | Track 5 | sel-dvt201 | 에이전틱 AI로 완전히 달라지는 소프트웨어와 개발 방법 |
| 11:10 | Track 6 | sel-cmp401 | 대규모 분산 학습 AWS ParallelCluster 로 시작하기 |
| 11:10 | Track 7 | sel-sec301 | AI 보안심화: AI 워크로드에 대한 심층방어 체계 구축 |
| 11:10 | Track 8 | sel-biz203 | Amazon Connect Customer AI Agent가 다시 쓰는 고객 경험 : 불만을 감동으로 |
| 11:10 | Track 9 | sel-dev304 | [당근 I CJ 올리브영] 장애에 강한 팀: 서버리스 온콜과 서비스 모니터링 |
| 12:50 | Track 1 | sel-aim302 | [하이퍼커넥트] 하이퍼커넥트의 HyperPod 기반 Slurm on EKS 도입기 |
| 12:50 | Track 2 | sel-ant201 | AI-Ready Data: 에이전틱 AI 시대, 데이터가 답이다 |
| 12:50 | Track 3 | sel-dvt205 | Strands Agents와 함께 스스로 진화하는 AI 에이전트 |
| 12:50 | Track 4 | sel-mam301 | [LG전자] AI 에이전트, AgentCore로 프로덕션까지 |
| 12:50 | Track 5 | sel-dvt203 | [LG전자] AI 기반 개발 라이프사이클 
(AI-DLC) 소개 |
| 12:50 | Track 6 | sel-cmp202 | 인퍼런스와 모델 퍼포먼스 최적화를 위한 EKS 아키텍처 |
| 12:50 | Track 7 | sel-sec201 | Agent-Driven 개발 환경, 보안 강화 전략은? |
| 12:50 | Track 8 | sel-biz202 | Amazon Connect Customer를 활용한 에이전틱 AI 기반 고객 경험 혁신 |
| 12:50 | Track 9 | sel-dev307 | Kiro Spec 모드 가속 가이드 & 서버리스 CDC 레이크하우스 |
| 13:50 | Track 1 | sel-aim201 | Nova Forge와 Bedrock RFT로 모델 성능 극대화 |
| 13:50 | Track 2 | sel-prt221-s | Enterprise AI Transformation: Agentic AI로 만드는 실질적인 비즈니스 성과 (sponsored by LG CNS) |
| 13:50 | Track 3 | sel-prt201-s | SK AX가 구현한 SageMaker 기반 분석가와 현업의 통합 AI 환경 (sponsored by SK AX) |
| 13:50 | Track 4 | sel-prt215-s | Unlocking Cost-Efficient Cloud and AI Performance on AWS with AMD EPYC (sponsored by AMD) |
| 13:50 | Track 5 | sel-prt207-s | LLM 애플리케이션 프로덕션 운영, Observability로 풀다 (sponsored by 와탭, WhaTap) |
| 13:50 | Track 6 | sel-prt213-s | Amazon Bedrock 기반 GitLab Duo 에이전트 플랫폼으로 혁신 가속화 (sponsored by Gitlab) |
| 13:50 | Track 7 | sel-prt301-s | Secure AI by Design (sponsored by Palo Alto Networks) |
| 13:50 | Track 8 | sel-prt302-s | AWS AI와 서버리스로 구축하는 완성차 지능형 상품 전략 플랫폼 (sponsored by 이테크시스템 / ETECH SYSTEM) |
| 13:50 | Track 9 | sel-prt206-s | 속도와 제어를 동시에 - Cloudflare에서 AI 에이전트 구축하기 (sponsored by 클라우드플레어/Cloudflare) |
| 14:30 | Track 1 | sel-aim401 | SageMaker AI MLOps, Nova 2 기반 멀티 에이전트로 한 단계 업그레이드 |
| 14:30 | Track 2 | sel-ant303 | 밑줄 쫙! AI 성공 네비게이터 SageMaker Catalog |
| 14:30 | Track 3 | sel-dvt304 | [삼성전자] 200개국 삼성 스마트 TV 앱 데이터를 자연어로 묻다: 에이전틱 AI on AWS |
| 14:30 | Track 4 | sel-mam202 | 오래된 IT 시스템 현대화, 에이전틱 AI로 쉽게 |
| 14:30 | Track 5 | sel-dvt204 | 누구나 손쉽게 개발효율 200% 향상시키는 Kiro 활용법 |
| 14:30 | Track 6 | sel-cmp201 | AWS 차세대 AI 인프라: 리전에서 AI Factory까지 |
| 14:30 | Track 7 | sel-sec302 | Amazon Bedrock AgentCore 로 AI 시대의 Zero Trust 구현하기 |
| 14:30 | Track 8 | sel-biz204 | 20만 Amazonian의 AI 내재화 성공 경험, 그리고 Quick Desktop |
| 14:30 | Track 9 | sel-dev305 | [네오위즈파트너스 | 알고릭스코퍼레이션] IaC 기반 EKS 멀티테넌시와 Sidecar-less 네트워킹 |
| 15:30 | Track 1 | sel-aim202 | [우아한형제들] 우아한형제들의 Nova 2 프로덕션 적용 여정 |
| 15:30 | Track 2 | sel-prt217-s | Oracle AI Database@AWS! AWS는 그대로, Exadata로 더욱 강력하게!(sponsored by Oracle) |
| 15:30 | Track 3 | sel-dvt302 | 에이전트 성능 평가와 개선: 개발부터 운영까지 |
| 15:30 | Track 4 | sel-prt106-s | Notion: API를 넘어 플랫폼으로 (sponsored by 노션, Notion) |
| 15:30 | Track 5 | sel-prt103-s | MUSINSA - ClickHouse Cloud를 활용한 Audience Engine 및 다각적 비즈니스 확장을 위한 전략 (sponsored by ClickHouse) |
| 15:30 | Track 6 | sel-prt212-s | Snowflake + AWS 통합 AI 전략: Cortex Code가 연결하는 데이터와 인텔리전스 (sponsored by Snowflake) |
| 15:30 | Track 7 | sel-prt102-s | 3가지 관점으로 살펴보는 Red Hat OpenShift Service on AWS(ROSA)를 활용한 현대화의 새로운 접근 방식 (sponsored by Red Hat) |
| 15:30 | Track 8 | sel-prt220-s | 당신의 AI 환경은 안녕하신지요? (sponsored by Zscaler) |
| 15:30 | Track 9 | sel-dev308 | [미러] 맥 미니 없이도 서버리스로 만드는 AI Cloud Agent |
| 16:10 | Track 1 | sel-aim303 | 40분 완성! SageMaker AI 기반 에이전틱 모델 구축 및 배포 |
| 16:10 | Track 2 | sel-ant202 | 나야, 차세대 OpenSearch: 에이전틱 AI를 곁들인 |
| 16:10 | Track 3 | sel-dvt303 | 프로덕션으로 가기 위한 에이전틱 AI 아키텍처 설계하기 |
| 16:10 | Track 4 | sel-mam302 | AIOps 도전과 실전: AI SecOps에서 DevOps 에이전트까지 |
| 16:10 | Track 5 | sel-dvt305 | Nova Act & Strands Agent 실전: AI 에이전트로 개발 워크플로 자동화하기 |
| 16:10 | Track 6 | sel-cmp301 | AWS Trainium 기반 LLM 추론 A to Z: Neuron 환경 이해부터 성능 최적화까지 |
| 16:10 | Track 7 | sel-sec202 | 신뢰할 수 있는 KMS 아키텍처의 진화와 서명키 관리 전략 |
| 16:10 | Track 8 | sel-aim205 | 당신의 새로운 AI 업무 파트너, Amazon Quick |
| 16:10 | Track 9 | sel-dev306 | [LG유플러스] AWS Kiro로 가속하는 IaC 혁신과 레거시 전환 |

## 세션별 요약

# AI Day Batch 1 요약

## sel-key002 - 기조연설 - AI Day

- 시간/트랙/레벨/발표자: 09:30-10:40 / Keynote / 100 Foundational / 안종훈(아모레퍼시픽), 신재현(우아한형제들), 김민태(우아한형제들), 윤석찬(AWS)
- 요약: AWS 서울 리전 이후 10년의 클라우드 도입 흐름과 앞으로의 AI 네이티브 전환을 고객 사례 중심으로 정리한 키노트. 개발자는 더 이상 인프라 조립자가 아니라 AI를 활용해 제품 가설, 구현, 운영을 빠르게 반복하는 역할로 이동하고 있음을 강조했다.
- 주요 포인트:
  - 서울 리전, Lambda, 커뮤니티 경험을 통해 한국 개발 생태계가 빠르게 실험하고 확장한 과정을 회고.
  - AI는 뷰티, 엔터테인먼트, 피지컬 AI 등 산업별 현실 문제를 푸는 새 컴퓨팅 빌딩 블록으로 제시.
  - 개발 주기는 요구사항 작성, 코드 생성, 테스트, 운영 피드백까지 AI 보조가 들어가는 형태로 재편.
  - 기업은 AI 도입을 단발 PoC가 아니라 데이터, 보안, 운영, 인재 역량이 연결된 장기 전환 과제로 봐야 함.
- AWS/기술 키워드: AWS 서울 리전, Lambda, Amazon Bedrock, SageMaker, 생성형 AI, AI 기반 개발 사이클, 산업별 AI
- AX TF 관점/회사 AX 도입 시사점: 사내 AX는 특정 챗봇 도입이 아니라 개발/운영/업무 프로세스 전반의 반복 속도를 높이는 체계로 설계해야 한다. Claude Code류 도구도 개인 생산성 도구에 머물지 않도록 코드 리뷰, 배포, 보안 가드레일, 지식 재사용까지 연결하는 운영 모델이 필요하다.
- 공유용 한줄: AI Day 키노트의 핵심은 "AI를 도구가 아니라 개발과 비즈니스 운영 방식 자체를 바꾸는 새 클라우드 빌딩 블록으로 보라"는 메시지다.

## sel-aim301 - Superb AI의 HyperPod 기반 비전 파운데이션 모델 구축 여정

- 시간/트랙/레벨/발표자: 11:10-11:50 / Track 1 / 300 Advanced / 유용환(AWS), 차문수(Superb AI)
- 요약: 제조 도메인용 비전 파운데이션 모델을 직접 학습해야 하는 이유와 SageMaker HyperPod 기반 대규모 분산 학습 운영 방식을 Superb AI 사례로 설명했다. GPU 클러스터 운영, 장애 복구, 병렬화, 비용 최적화가 모델 경쟁력의 핵심 인프라 역량으로 다뤄졌다.
- 주요 포인트:
  - 범용 모델만으로는 제조, 의료, 자율주행 같은 도메인 정밀도를 만족하기 어려워 자체 학습/커스터마이징 수요가 증가.
  - HyperPod는 장시간 분산 학습에서 노드 상태 모니터링, 장애 노드 교체, 체크포인트 복구를 지원.
  - Superb AI는 ZERO 비전 파운데이션 모델 구축 과정에서 데이터/학습 파이프라인과 GPU 활용률을 함께 최적화.
  - 학습 시간 단축과 비용 절감은 단순 인스턴스 선택보다 클러스터 안정성, 네트워크, 작업 재시작 전략에 좌우됨.
- AWS/기술 키워드: Amazon SageMaker HyperPod, 분산 학습, 비전 파운데이션 모델, GPU 클러스터, 체크포인트, 제조 AI
- AX TF 관점/회사 AX 도입 시사점: 사내 도메인 모델을 검토한다면 "모델 선택"보다 먼저 데이터 품질, 학습 인프라, 재학습 운영비를 산정해야 한다. 개발자용 AX도 사내 코드/문서 기반 특화 모델이나 RAG를 붙일 경우 지속 학습과 평가 체계를 비용 항목으로 잡아야 한다.
- 공유용 한줄: 특화 AI 경쟁력은 좋은 모델 API만이 아니라 안정적으로 학습하고 재학습할 수 있는 인프라 역량에서 나온다.

## sel-ant305 - 에이전틱 AI를 위한 데이터 실무 가이드

- 시간/트랙/레벨/발표자: 11:10-11:50 / Track 2 / 300 Advanced / 김기영(AWS), 이종혁(AWS)
- 요약: 챗봇, RAG, MCP, 자율 에이전트로 이어지는 변화 속에서 에이전트가 실제 업무를 수행하려면 데이터 접근, 맥락, 권한, 거버넌스가 함께 설계되어야 한다는 실무 가이드. 보험사 예시를 통해 에이전틱 애플리케이션을 데이터 기반으로 구성하는 흐름을 설명했다.
- 주요 포인트:
  - 2023년 챗봇/벡터 중심에서 RAG, MCP, 자율 에이전트로 빠르게 이동 중.
  - 에이전트는 도구 호출과 데이터 접근을 하기 때문에 단순 검색 품질보다 권한, 출처, 품질 관리가 중요.
  - Aurora, OpenSearch, 데이터 레이크, SageMaker Unified Studio 등을 조합해 분석과 검색 기반을 구성.
  - Bedrock AgentCore 통합 시 데이터 거버넌스와 도구 호출 정책을 함께 설계해야 함.
- AWS/기술 키워드: MCP, RAG, Aurora, Amazon OpenSearch Service, SageMaker Unified Studio, Data Lake, Bedrock AgentCore, 데이터 거버넌스
- AX TF 관점/회사 AX 도입 시사점: 사내 에이전트가 "검색은 되지만 처리하지 못하는" 상태에 머물지 않으려면 업무 데이터의 소유자, 권한, 메타데이터, API 도구 목록을 먼저 정리해야 한다. Claude Code류 도구에도 코드베이스, 이슈, 문서, 배포 로그 접근권한을 역할별로 나누는 설계가 필요하다.
- 공유용 한줄: 에이전틱 AI의 성패는 모델보다 "에이전트가 믿고 행동할 수 있는 데이터와 권한 구조"가 좌우한다.

## sel-aim305 - [삼성전자] 21억 사용자규모 삼성 어카운트의 에이전틱 AIOps on AWS

- 시간/트랙/레벨/발표자: 11:10-11:50 / Track 3 / 300 Advanced / 박규태(AWS), 이준영(삼성전자)
- 요약: AI PoC의 상당수가 프로덕션에 도달하지 못하는 이유를 운영 우수성, 데이터, 신뢰, 안정성의 4개 축으로 설명하고, 삼성 어카운트 규모의 AIOps 사례로 프로덕션 전환 방법을 제시했다. Bedrock AgentCore 기반의 운영형 에이전트 구축 관점이 핵심이다.
- 주요 포인트:
  - PoC에서는 단일 사용자, 낮은 비용 민감도, 제한된 입력으로 동작하지만 프로덕션은 예측 불가능한 입력과 컴플라이언스를 요구.
  - 에이전틱 AI 운영에는 관찰성, 비용 통제, 권한 관리, 예외 처리, 지속 개선 루프가 필요.
  - 삼성 어카운트 사례는 대규모 사용자 서비스에서 장애 탐지/분석/대응 흐름에 에이전트를 적용하는 방향을 보여줌.
  - 데모 성공보다 운영 지표와 실패 대응 설계가 프로덕션 판단 기준이 되어야 함.
- AWS/기술 키워드: Amazon Bedrock, Bedrock AgentCore, AIOps, 운영 우수성, Observability, 프로덕션 에이전트, 삼성 어카운트
- AX TF 관점/회사 AX 도입 시사점: AX TF가 사내 에이전트를 배포할 때는 "답변 정확도" 외에 누가 실행 권한을 갖는지, 실패 시 어떻게 롤백/에스컬레이션하는지, 비용과 로그를 어떻게 볼지까지 체크리스트화해야 한다. 개발 에이전트도 CI/CD와 연결되는 순간 운영 시스템으로 취급해야 한다.
- 공유용 한줄: 프로덕션 에이전트는 잘 말하는 AI가 아니라 관찰, 통제, 복구가 가능한 운영 시스템이어야 한다.

## sel-mam201 - 기술 부채의 한계를 넘어 AI-Ready 비즈니스로: AWS가 제안하는 에이전틱 AI 마이그레이션

- 시간/트랙/레벨/발표자: 11:10-11:50 / Track 4 / 200 Intermediate / 전소영(AWS), 김세진(AWS)
- 요약: 클라우드 마이그레이션을 단순 서버 이전이 아니라 AI를 빠르게 적용할 수 있는 비즈니스 기반으로 전환하는 과정으로 정의했다. AWS의 에이전틱 AI 마이그레이션 접근을 통해 평가, 설계, 실행, 현대화의 반복 선순환을 설명했다.
- 주요 포인트:
  - 마이그레이션의 가치는 이동 자체가 아니라 현대화, 운영 효율, 혁신 투자로 이어지는 선순환에 있음.
  - AI 시대에는 레거시 기술 부채가 AI 적용 속도와 비용을 직접 제한.
  - 에이전틱 AI는 워크로드 분석, 의존성 파악, 전환 계획 수립, 실행 자동화에 활용 가능.
  - 설계 원칙과 운영 모델 없이 이전만 하면 AI-Ready 상태에 도달하기 어렵다.
- AWS/기술 키워드: Migration & Modernization, AI-Ready Business, 에이전틱 AI 마이그레이션, AWS 마이그레이션 전략, 현대화
- AX TF 관점/회사 AX 도입 시사점: AX 도입 대상 업무를 고를 때 레거시 시스템의 API화, 로그 표준화, 문서화 수준을 함께 평가해야 한다. 개발 생산성 AX도 오래된 빌드/배포/권한 구조를 그대로 두면 도구 효과가 제한된다.
- 공유용 한줄: AI 도입 속도는 모델보다 레거시 기술 부채를 얼마나 줄였는지에 크게 좌우된다.

## sel-dvt201 - 에이전틱 AI로 완전히 달라지는 소프트웨어와 개발 방법

- 시간/트랙/레벨/발표자: 11:10-11:50 / Track 5 / 200 Intermediate / 구태훈(AWS)
- 요약: 에이전틱 AI가 소프트웨어 개발 방식을 요구사항 작성, 설계, 코드 생성, 검증, 운영 자동화까지 확장한다는 내용을 다뤘다. Kiro와 AWS의 에이전트 구축 서비스를 중심으로 개발자가 AI와 협업하는 새로운 작업 방식을 소개했다.
- 주요 포인트:
  - 에이전트는 단순 코드 자동완성이 아니라 목표를 이해하고 계획, 도구 호출, 결과 검증까지 수행.
  - Kiro는 스펙 기반 개발 흐름을 통해 요구사항과 구현 사이의 간극을 줄이는 도구로 소개.
  - 소프트웨어를 위한 에이전트는 코드, 문서, 테스트, 배포 시스템과 연결될 때 실질적 가치가 커짐.
  - 개발자는 프롬프트 작성자가 아니라 문제 정의, 제약 조건, 검증 기준을 설계하는 역할이 중요해짐.
- AWS/기술 키워드: Kiro, Agentic AI, Developer Tools, Amazon Bedrock, 소프트웨어 개발 생명주기, 스펙 기반 개발
- AX TF 관점/회사 AX 도입 시사점: Claude Code류 도구 도입은 개인별 사용법 교육보다 팀 단위 "스펙 작성-코드 생성-리뷰-테스트" 표준을 만드는 쪽이 효과적이다. 사내 저장소 템플릿, PR 체크리스트, 테스트 기준을 AI가 이해하기 좋게 정리해야 한다.
- 공유용 한줄: 개발 AX의 핵심은 코드를 빨리 쓰는 것이 아니라 요구사항부터 검증까지 AI와 함께 닫힌 루프를 만드는 것이다.

## sel-cmp401 - 대규모 분산 학습 AWS ParallelCluster로 시작하기

- 시간/트랙/레벨/발표자: 11:10-11:50 / Track 6 / 400 Expert / 조소현(AWS), 이수정(AWS)
- 요약: 대규모 분산 학습 인프라를 AWS ParallelCluster와 Slurm 중심으로 구성하고 운영하는 실전 세션. GPU 노드, EFA 네트워크, AMI/컨테이너 전략, 모니터링, 장애 복구까지 HPC형 학습 클러스터 운영 포인트를 다뤘다.
- 주요 포인트:
  - 분산 학습은 GPU 계산만큼 GPU 간 통신 성능이 중요하며, EFA가 OS 우회 통신으로 지연과 오버헤드를 줄임.
  - ParallelCluster는 헤드 노드, 컴퓨트 노드, 로그인 노드와 Slurm 스케줄러 기반으로 작업을 관리.
  - AMI 빌드, 컨테이너 경량화, 외부 스토리지 마운트, 버전 릴리즈 노트 확인이 운영 안정성의 핵심.
  - 클러스터 배포 후 EFA, NCCL/런타임, 노드 상태, 모니터링 지표를 반드시 검증해야 함.
- AWS/기술 키워드: AWS ParallelCluster, Slurm, EFA, GPU 분산 학습, AMI, 컨테이너, 모니터링, HPC
- AX TF 관점/회사 AX 도입 시사점: 사내에서 대규모 모델 학습을 직접 운영할 가능성이 있다면 MLOps 이전에 HPC 운영 역량을 현실적으로 평가해야 한다. 대부분의 AX 과제는 관리형 서비스나 API로 시작하되, 자체 학습이 필요한 영역은 인프라 전문성을 별도 확보해야 한다.
- 공유용 한줄: 대규모 학습은 모델 코드보다 클러스터, 네트워크, 버전, 장애 복구 운영력이 병목이 된다.

## sel-sec301 - AI 보안심화: AI 워크로드에 대한 심층방어 체계 구축

- 시간/트랙/레벨/발표자: 11:10-11:50 / Track 7 / 300 Advanced / 신은수(AWS), 신안셀모(AWS)
- 요약: AI 워크로드를 안전하게 운영하기 위한 심층 방어 구조를 AWS 네이티브 서비스와 오픈소스 프레임워크 관점에서 설명했다. 프롬프트 인젝션, 유해 콘텐츠, RAG 권한 필터링, MCP 인증/인가까지 에이전틱 AI 보안의 실전 쟁점을 다뤘다.
- 주요 포인트:
  - 자연어 입력은 모델 내부에서 해석되므로 보안 통제는 모델 외부에서 강제해야 함.
  - Amazon Bedrock Guardrails는 책임 있는 AI 정책, 콘텐츠 필터, 민감정보 차단, 주제 차단에 활용.
  - RAG는 검색 후 필터링, 사용자/그룹별 데이터 분리, 메타데이터 기반 검색 전 필터링 등 권한 전략이 필요.
  - MCP 환경에서는 OAuth 기반 2-legged/3-legged 인증 패턴으로 도구 접근을 안전하게 위임해야 함.
- AWS/기술 키워드: Amazon Bedrock Guardrails, RAG 보안, MCP, OAuth, 데이터 거버넌스, Prompt Injection, 심층 방어
- AX TF 관점/회사 AX 도입 시사점: 사내 AX는 "AI가 보면 안 되는 데이터"와 "AI가 실행하면 안 되는 도구"를 명확히 구분해야 한다. 개발 에이전트에 repo, 이슈, 배포 권한을 줄 때도 사용자 권한 위임과 감사 로그를 기본 요구사항으로 둬야 한다.
- 공유용 한줄: AI 보안은 모델에게 조심하라고 말하는 것이 아니라 모델 밖에서 권한과 정책을 강제하는 것이다.

## sel-biz203 - Amazon Connect Customer AI Agent가 다시 쓰는 고객 경험 : 불만을 감동으로

- 시간/트랙/레벨/발표자: 11:10-11:50 / Track 8 / 200 Intermediate / 이석원(AWS), 배경완(AWS)
- 요약: Amazon Connect Customer를 중심으로 고객 여정 전반에 AI를 내재화해 셀프서비스, 상담원 지원, 후처리 자동화를 연결하는 방법을 소개했다. 항공편 변경 데모를 통해 AI 에이전트가 고객 맥락을 이해하고 업무 처리를 보조하는 흐름을 보여줬다.
- 주요 포인트:
  - 컨택센터의 과제는 높아진 고객 기대, 파편화된 경험, 자동화와 사람 상담 사이의 극단적 선택, 분산 비용.
  - AI는 빠른 자동화를 담당하고 사람 상담원은 감동과 예외 처리에 집중하는 구조가 필요.
  - 데모에서는 고객의 일정 변경 상황을 파악하고 대체 항공편 확인, 선택, 변경 처리까지 대화로 진행.
  - 상담원 워크스페이스에서는 이전 대화 요약, 고객 정보, 응대 가이드, 에스컬레이션 판단, 후처리 노트 생성을 지원.
- AWS/기술 키워드: Amazon Connect Customer, Customer AI Agent, Contact Center, 상담원 워크스페이스, 대화 요약, 후처리 자동화
- AX TF 관점/회사 AX 도입 시사점: 내부 헬프데스크나 IT 지원에도 유사한 패턴을 적용할 수 있다. 단순 FAQ 봇보다 티켓 맥락 요약, 담당자 추천, 처리 절차 안내, 후처리 기록 자동화부터 시작하면 실효성이 높다.
- 공유용 한줄: 고객 경험 AX는 사람을 대체하기보다 반복 처리와 맥락 정리를 AI가 맡아 상담 품질을 높이는 방향이 현실적이다.

## sel-dev304 - [당근 | CJ 올리브영] 장애에 강한 팀: 서버리스 온콜과 서비스 모니터링

- 시간/트랙/레벨/발표자: 11:10-11:50 / Track 9 / 300 Advanced / 김수빈(당근), 이태근(CJ 올리브영)
- 요약: CJ 올리브영의 Amazon Connect 기반 서버리스 온콜 시스템과 당근의 CloudFront/MSK 모니터링 개선 사례를 공유했다. 장애 인지, 알림 품질, 담당자 라우팅, 대시보드 구조화가 운영 효율을 어떻게 높이는지 실무 중심으로 다뤘다.
- 주요 포인트:
  - 올리브영은 이메일 기반 알림을 Lambda 등으로 처리해 Amazon Connect 전화 알림으로 연결하는 온콜 PoC를 구성.
  - 스팸 메일로 불필요한 전화가 발생한 사례를 통해 알림 입력 검증과 방어 로직의 중요성을 설명.
  - 당근은 플랫폼 엔지니어링 관점에서 지표 통합, 온오너 데이터 구조화, 셀프서비스 모니터링을 추진.
  - CloudFront 가시성, MSK 브로커/컨슈머 랙 대시보드와 알림을 구축해 장애 인지와 대응 흐름을 개선.
- AWS/기술 키워드: Amazon Connect, AWS Lambda, Amazon CloudFront, Amazon MSK, 서버리스 온콜, Observability, 플랫폼 엔지니어링
- AX TF 관점/회사 AX 도입 시사점: AX 도입 전 운영 알림과 로그 품질을 개선하면 AI가 장애 맥락을 요약하고 조치 후보를 제안하기 쉬워진다. 개발 에이전트보다 먼저 "깨끗한 이벤트와 책임자 매핑"을 만드는 것도 높은 ROI의 AX 기반 작업이다.
- 공유용 한줄: 장애 대응 자동화는 AI 이전에 알림 입력, 소유자, 지표 구조를 정리하는 것에서 출발한다.

## sel-aim302 - [하이퍼커넥트] 하이퍼커넥트의 HyperPod 기반 Slurm on EKS 도입기

- 시간/트랙/레벨/발표자: 12:50-13:30 / Track 1 / 300 Advanced / 오준석(AWS), 현륜식(AWS), 윤보현(하이퍼커넥트)
- 요약: SageMaker HyperPod에서 기존 Slurm 워크플로우를 유지하면서 EKS의 운영 효율을 확보한 하이퍼커넥트 사례. Slurm on EKS 전환 과정과 Checkpointless Training, Elastic Training 등 대규모 학습 운영의 최신 개선점을 소개했다.
- 주요 포인트:
  - HyperPod는 대규모 모델 훈련/배포를 위한 맞춤형 인프라와 노드 복원력을 제공.
  - Slurm 사용자 경험을 유지하면서 Kubernetes/EKS 기반 운영 자동화와 리소스 관리를 결합.
  - 하이퍼커넥트는 동일 인프라에서 Slurm과 EKS를 활용하며 운영 효율과 전환 리스크를 함께 관리.
  - 네트워크 기반 메모리 복제로 2분 내 장애 복구와 95% 이상 Goodput을 지향하는 Checkpointless Training도 다룸.
- AWS/기술 키워드: SageMaker HyperPod, Slurm on EKS, Amazon EKS, Checkpointless Training, Elastic Training, Goodput, 분산 학습
- AX TF 관점/회사 AX 도입 시사점: 기존 개발/ML 워크플로우를 한 번에 갈아엎기보다 익숙한 도구를 유지하면서 운영 기반을 현대화하는 방식이 현실적이다. 사내 AX도 IDE, Git, 이슈 흐름은 유지하되 에이전트와 자동화를 옆에 붙이는 전환 전략이 유효하다.
- 공유용 한줄: 성공적인 AI 인프라 전환은 기존 워크플로우를 존중하면서 운영 자동화 계층을 점진적으로 얹는 방식이 강하다.

## sel-ant201 - AI-Ready Data: 에이전틱 AI 시대, 데이터가 답이다

- 시간/트랙/레벨/발표자: 12:50-13:30 / Track 2 / 200 Intermediate / 유철민(AWS), 김지애(AWS)
- 요약: 에이전틱 AI가 기대만큼 답하지 못하는 원인을 모델이 아니라 데이터 준비 부족에서 찾고, AI-Ready Data와 시맨틱 레이어 구축 방법을 설명했다. 라이브 데모를 통해 데이터 맥락과 의미 계층이 응답 품질을 어떻게 바꾸는지 보여줬다.
- 주요 포인트:
  - 에이전틱 AI는 답변 생성에서 판단과 행동 단계로 넘어가고 있으며, 이때 데이터 맥락이 핵심.
  - "분석할 수 없습니다"만 반복하는 에이전트는 모델 문제가 아니라 데이터 의미, 권한, 품질 문제일 가능성이 큼.
  - 시맨틱 레이어는 업무 용어, 지표 정의, 관계를 AI가 이해할 수 있는 형태로 제공.
  - 프로덕션 전환에는 데이터 품질, 거버넌스, 접근 제어, 평가 기준이 함께 필요.
- AWS/기술 키워드: AI-Ready Data, Semantic Layer, Analytics, Agentic AI, 데이터 품질, 데이터 거버넌스
- AX TF 관점/회사 AX 도입 시사점: 사내 업무 에이전트는 문서만 많이 넣는다고 좋아지지 않는다. KPI 정의, 조직별 용어, 데이터 소유권, 최신성 기준을 시맨틱 레이어처럼 정리해야 신뢰할 만한 답과 행동이 가능하다.
- 공유용 한줄: 에이전틱 AI의 품질은 모델 크기보다 회사 데이터가 의미와 맥락을 갖고 준비되어 있는지에 달려 있다.

## sel-dvt205 - Strands Agents와 함께 스스로 진화하는 AI 에이전트

- 시간/트랙/레벨/발표자: 12:50-13:30 / Track 3 / 200 Intermediate / 김제삼(AWS), 박경수(AWS)
- 요약: AWS가 공개한 Strands Agents SDK를 활용해 자율 AI 에이전트를 구축하고, 지식 격차 식별, 추론 전략 수정, 동적 도구 생성 등 스스로 개선하는 패턴을 소개했다. 단순 에이전트 생성에서 한 단계 나아가 장기간 독립 운영되는 에이전트 시스템을 다뤘다.
- 주요 포인트:
  - AI 에이전트는 목표를 받으면 계획을 세우고 도구/API를 호출해 실제 행동하는 소프트웨어.
  - Strands Agents SDK는 에이전트 구축 패턴을 오픈소스로 제공해 도구 연결과 실행 흐름을 단순화.
  - 자가 개선 에이전트는 실패/지식 격차를 감지하고 프롬프트, 도구, 추론 전략을 갱신하는 방식으로 발전.
  - 완전 자율부터 human-in-the-loop까지 업무 위험도에 따라 자율성 수준을 조절해야 함.
- AWS/기술 키워드: Strands Agents, AI Agent SDK, 자율 에이전트, 동적 도구 생성, 실시간 스트리밍, Human-in-the-loop
- AX TF 관점/회사 AX 도입 시사점: 사내 에이전트가 스스로 개선되려면 실패 로그, 사용자 피드백, 평가 데이터가 구조화되어야 한다. 개발 에이전트도 "수정했다"에서 끝내지 말고 테스트 실패, 리뷰 코멘트, 배포 결과를 다음 실행의 학습 신호로 쓰는 루프가 필요하다.
- 공유용 한줄: 다음 단계의 에이전트는 실행만 하는 것이 아니라 실패를 기록하고 자신의 도구와 전략을 개선하는 시스템이다.

## sel-mam301 - [LG전자] AI 에이전트, AgentCore로 프로덕션까지

- 시간/트랙/레벨/발표자: 12:50-13:30 / Track 4 / 300 Advanced / 이광우(AWS), 송민지(AWS), 김영곤(LG전자)
- 요약: Amazon Bedrock AgentCore 기반으로 엔터프라이즈급 AI 에이전트를 프로덕션에 올리기 위한 핵심 패턴을 설명하고 LG전자 사례로 적용 방식을 보여줬다. 신뢰성, 확장성, 도구 공유, 에이전트 간 협업, 메모리, 접근 제어, 관찰성이 주요 체크리스트로 제시됐다.
- 주요 포인트:
  - PoC 에이전트는 일부 기능만 만족해도 되지만 프로덕션은 일관성, 예외 대응, 추적, 확장성을 요구.
  - AgentCore는 게이트웨이, 도구 공유, A2A 협업, 공유 메모리, ID 기반 접근 제어, 옵저버빌리티 패턴을 지원.
  - 엔터프라이즈 에이전트는 LLM 응답뿐 아니라 어떤 도구를 언제 어떤 권한으로 호출했는지 추적 가능해야 함.
  - LG전자 사례는 실제 제품/서비스 환경에서 거버넌스와 자율성을 함께 만족시키는 에이전트 인프라 설계의 예시.
- AWS/기술 키워드: Amazon Bedrock AgentCore, Gateway, A2A, Shared Memory, Identity-based Access Control, Observability, LG전자
- AX TF 관점/회사 AX 도입 시사점: 사내 AX 플랫폼은 에이전트별 독립 구현을 방치하지 말고 공통 게이트웨이, 도구 레지스트리, 인증/인가, 로그 표준을 먼저 제공해야 한다. 그래야 각 팀이 빠르게 실험하면서도 보안과 운영 기준을 유지할 수 있다.
- 공유용 한줄: 엔터프라이즈 에이전트의 승부처는 모델 성능보다 공통 도구, 권한, 메모리, 관찰성을 갖춘 운영 기반이다.

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
