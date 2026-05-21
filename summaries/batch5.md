# Batch 5 요약

## sel-wps101

**제목/시간/트랙/발표자**  
- 제목: 룰루메딕 의료마이데이터 플랫폼 혁신사례
- 시간: 2026-05-20 14:30-14:55 KST
- 트랙: Industry Day / Healthcare & Life Sciences, Professional Services / Analytics
- 발표자: 김영웅 대표이사, 룰루메딕

**핵심 요약**  
룰루메딕은 의료 마이데이터 플랫폼 `d'state`를 중심으로 흩어진 의료기록을 개인 동의 기반으로 연결하고, 이를 생활·예방·분석 서비스로 확장하는 전략을 소개했다. 발표는 해외 의료 지원 사례를 통해 처방 이력, 예방접종, 복용약 같은 데이터가 국경을 넘어 필요한 순간에 조회되어야 하는 이유를 설명했다. AWS 기반 아키텍처는 보안, 컴플라이언스, 글로벌 확장성, 24시간 가용성을 동시에 달성하기 위한 기반으로 제시됐다. 장기적으로는 업스테이지와의 AI 협력, 에이전틱 AI, 초개인화 헬스케어 서비스로 확장하는 비전을 강조했다.

**주요 포인트**
- 룰루메딕은 보건복지부 지정 보건의료 분야 개인정보관리 전문기관으로, 의료 데이터의 합법적 저장·활용·국외 이전을 핵심 차별점으로 제시했다.
- `d'state`는 병원·기관별 의료기록을 통합 조회하고, 정보주체 동의와 전송 요구 상태 관리를 기반으로 데이터 파이프라인을 만든다.
- 해외 체류 중 처방약 분실, 예방접종 이력 확인, 복용약 성분 확인 같은 사례로 의료 마이데이터 국외 이전의 실무 필요성을 설명했다.
- AWS WAF, Shield, Route 53, ALB, Transit Gateway, Network Firewall, EKS, Aurora, S3, Secrets Manager, CloudWatch 등을 조합해 다층 보안과 운영·개발 분리를 구현했다.
- 의료 마이데이터는 금융 마이데이터처럼 서비스 사업자와 클라우드 인프라가 결합될 때 AI 기반 신시장이 열린다는 관점을 제시했다.

**AWS/기술 키워드**  
Amazon EKS, Amazon Aurora, Amazon S3, AWS WAF, AWS Shield, Amazon Route 53, Elastic Load Balancing, AWS Transit Gateway, AWS Network Firewall, AWS Secrets Manager, Amazon CloudWatch, IAM, KMS, VPC Endpoint, ISMS-P, HIPAA, GDPR, Agentic AI

**현장 메모로 남길 점**  
의료 데이터 세션이지만 기술보다 규제·동의·국외 이전·보안 인증의 조합이 핵심이었다. "데이터를 모으는 앱"이 아니라 의료 AI와 글로벌 바이오데이터 사업의 기반 인프라로 포지셔닝한 점이 인상적이다.

**블로그용 한줄**  
룰루메딕은 AWS 기반 의료 마이데이터 인프라로 국내 의료기록을 안전하게 연결하고, 국외 이전과 초개인화 헬스케어 AI까지 확장하는 로드맵을 제시했다.

## sel-prt401-s

**제목/시간/트랙/발표자**  
- 제목: 복잡함 속의 질서: Beyond AI Adoption in Agentic Era (sponsored by 메가존클라우드)
- 시간: 2026-05-20 15:30-15:50 KST
- 트랙: Industry Day / Financial Services, Retail & Consumer Goods, Software & Internet / Analytics, Architecture, Artificial Intelligence
- 발표자: 공성배 CAIO, MegazoneCloud

**핵심 요약**  
메가존클라우드는 기업 AI가 PoC와 단순 도입 단계를 지나 에이전틱 AI 운영 단계로 넘어가며 더 큰 복잡성에 직면하고 있다고 진단했다. 발표자는 AI 확산의 장벽을 ROI, 거버넌스, 비용, 변화관리, 데이터, 시스템 통합, 하이브리드 환경 등으로 정리하고, 이를 조율하는 "엔터프라이즈 AI의 OS"가 필요하다고 설명했다. 실제 사례로 제약 품질 보고서 자동화와 캐피탈 여신 심사 생산성 개선을 언급하며 버티컬 AI의 실질 성과를 강조했다. 메가존클라우드의 `AI Studio`와 `AI Gateway`는 사용량, 감사 로그, 정책, 비용, 모델 라우팅, MCP 기반 도구 연결을 통제하는 운영 계층으로 소개됐다.

**주요 포인트**
- AI는 빅뱅식 전환이 아니라 긴 여정이며, 도입·확산·안정화 단계별 경험과 파트너십이 중요하다고 강조했다.
- 기업의 관심은 TCO에서 ROI로 이동했고, AI 프로젝트는 비용 절감이나 매출 기여 같은 비즈니스 성과를 증명해야 한다.
- 에이전트는 자율성과 의사결정 권한을 갖기 때문에 사람과 마찬가지로 데이터·시스템 접근 권한, 감사, 정책 통제가 필요하다.
- 발표자는 엔터프라이즈 AI의 필수 레이어로 추적성, 규정, 사용자/에이전트 센스, 재사용 가능한 표준화, MCP 기반 툴링을 포함한 Trust Layer를 제시했다.
- AI Gateway를 통해 Gemini, Claude, Amazon Nova 등 여러 모델과 MCP 도구의 트래픽을 한 지점에서 관리하고 비용과 정책을 제어하는 구조를 설명했다.

**AWS/기술 키워드**  
Agentic AI, AI Gateway, MCP, AI Studio, LLM Governance, AI Cost Control, Audit Log, Token Limit, Hybrid AI, Vertical AI, Amazon Nova, Claude, Gemini

**현장 메모로 남길 점**  
스폰서 세션이지만 메시지는 명확했다. AI 자체보다 AI를 운영 가능한 기업 시스템으로 만드는 거버넌스, 비용 통제, 변화관리 체계가 2026년의 핵심 과제라는 점을 반복했다.

**블로그용 한줄**  
메가존클라우드는 에이전틱 AI 시대의 혼란을 줄이려면 모델보다 먼저 거버넌스와 게이트웨이 중심의 엔터프라이즈 AI 운영 체계가 필요하다고 제안했다.

## sel-ind232

**제목/시간/트랙/발표자**  
- 제목: [현대지에프홀딩스] SMUS 기반 전사 MLOps 플랫폼으로 실현한 데이터 혁명
- 시간: 2026-05-20 15:30-15:50 KST
- 트랙: Industry Day / Retail & Consumer Goods / Analytics, Artificial Intelligence
- 발표자: 곽영화 Senior Solutions Architect, AWS; 김철중 책임, 현대지에프홀딩스

**핵심 요약**  
AWS는 AI 프로젝트의 실패 원인이 모델이 아니라 AI-ready 데이터 부재에 있다는 문제의식으로 Amazon SageMaker Unified Studio를 소개했다. 현대백화점그룹은 14개 계열사, 1,600만 H.Point 회원, 연간 수십억 건의 데이터를 전사 AI 자산으로 전환하기 위해 SMUS 기반 MLOps 플랫폼을 구축했다. 발표는 인프라 파편화, 분석 환경 부재, 배포 병목을 해결하기 위해 통합 환경 구축, 모델 검증, 거버넌스 설계를 단계적으로 진행한 16개월 여정을 공유했다. 결과적으로 웨딩 예정 지수 등 라이프 스코어를 지속 생성하는 파이프라인과 계열사 확산 가능한 표준 MLOps 운영 모델을 만들었다.

**주요 포인트**
- 엔터프라이즈 AI의 조건으로 분석·AI 통합, 데이터 사일로 해소, 거버넌스, 운영 확장성을 제시했다.
- 현대백화점그룹은 H.Point DW를 중심으로 계열사 데이터를 수집·전처리하고, Redshift Data Sharing으로 복제 없이 필요한 데이터를 연결했다.
- 데이터 카탈로그와 구독·승인 프로세스를 통해 데이터 소유자가 목적과 기간을 검토하고 Lake Formation 기반 권한을 자동 부여하는 구조를 만들었다.
- MLOps 파이프라인은 데이터 ETL, 피처 생성, 학습·평가, 챔피언 모델 선정, 배치 추론, S3/DW 적재, CRM·마케팅 활용까지 자동화했다.
- 웨딩 예정 모델은 변수와 데이터 규모를 3배 이상 확대하고, F1 계열 지표 기준 약 10% 성능 개선과 리콜 향상을 달성했다고 설명했다.

**AWS/기술 키워드**  
Amazon SageMaker Unified Studio, Amazon Redshift Data Sharing, AWS Lake Formation, Amazon S3, Data Catalog, MLOps Pipeline, Batch Inference, AI-ready Data, Data Governance, H.Point DW

**현장 메모로 남길 점**  
현대백화점그룹 사례의 강점은 "모델 하나"보다 조직 확산 구조에 있었다. MVP로 검증하고, 거버넌스를 처음부터 넣고, 계열사 데이터 사이언티스트를 육성한 점이 실무적으로 중요하다.

**블로그용 한줄**  
현대지에프홀딩스는 SageMaker Unified Studio 기반 전사 MLOps 플랫폼으로 그룹 데이터를 AI-ready 자산으로 바꾸고, 마케팅·CRM까지 이어지는 표준 AI 운영 체계를 구축했다.

## sel-ind235

**제목/시간/트랙/발표자**  
- 제목: [퀀팃] 퀀트 개발 혁신: Bedrock 기반 자율형 AI 알파 팩토리
- 시간: 2026-05-20 15:30-15:50 KST
- 트랙: Industry Day / Financial Services, Professional Services / Artificial Intelligence, Developer Tools, Security & Identity
- 발표자: 한덕희 CEO, 퀀팃

**핵심 요약**  
퀀팃은 투자 아이디어를 실제 백테스트 가능한 퀀트 전략으로 바꾸는 과정을 Amazon Bedrock 기반 멀티 에이전트 시스템으로 자동화한 `Arkraft` 여정을 소개했다. 발표는 알파 발굴이 아이디어 정리, 데이터 조달, 코딩, 패턴 분석, 백테스트, 리스크 검토까지 수작업에 오래 걸리는 병목을 갖고 있다고 설명했다. 퀀팃은 리서치 플랜 생성, 데이터 분석, Python 코드 작성, 백테스트, 통계·경제적 타당성 평가를 에이전트 워크플로로 연결해 한 시간 안에 알파 후보를 생산하는 구조를 만들었다. 이후 RAG 기반 아이디어 축적, 데이터 조달 에이전트, 운영 모니터링 에이전트까지 확장하며 "무인 알파 공장"에 가까운 방향을 제시했다.

**주요 포인트**
- 알파는 시장 베타와 무관하게 수익 기회를 만드는 투자 신호이며, 다양한 데이터와 팩터 분석이 필요하다고 설명했다.
- 단순 텍스트 요청을 리서치 명세로 바꾸고, 관련 데이터를 추출·분석한 뒤 Python 전략 코드와 백테스트 결과를 생성하는 데 LLM과 에이전트를 활용했다.
- 포트폴리오 매니저, 데이터 엔지니어, 퀀트 개발자 등 역할별 에이전트를 워크플로로 연결해 리서치 파이프라인을 구성했다.
- 코딩 병목을 푼 뒤에는 아이디어 생성이 병목이 되었고, 기존 알파 아이디어와 성공·실패 결과를 RAG 형태로 축적해 새 아이디어 생성에 재활용했다.
- AWS와 Bedrock은 컴퓨팅, 스토리지, 거버넌스, 모니터링, 확장성, 권한·보안 관리를 금융기관 친화적인 공통 인프라로 제공한다는 점이 장점으로 제시됐다.

**AWS/기술 키워드**  
Amazon Bedrock, Claude, Multi-agent Workflow, RAG, Python Backtesting, Quant Research, Alpha Factory, OpenSearch, Amazon EKS, Sandbox Execution, Financial AI

**현장 메모로 남길 점**  
퀀팃 사례는 생성형 AI가 "문서 요약"을 넘어 고부가 전문 워크플로를 자동화하는 예로 좋다. 특히 코딩 자동화 다음 병목이 아이디어와 데이터 조달로 이동했다는 설명이 현실적이었다.

**블로그용 한줄**  
퀀팃은 Bedrock 기반 멀티 에이전트로 퀀트 리서치, 코드 생성, 백테스트, 데이터 조달을 연결해 알파 전략 개발 시간을 극단적으로 단축하는 AI 알파 팩토리를 구현했다.

## sel-ind214

**제목/시간/트랙/발표자**  
- 제목: [요기요] 요기요의 AIOps: SRE 운영의 콘솔 탈출기
- 시간: 2026-05-20 15:30-15:50 KST
- 트랙: Industry Day / Retail & Consumer Goods, Software & Internet / Artificial Intelligence, Cloud Operations
- 발표자: 최낙권 Account Manager, AWS; 김예준 선임연구원, 위대한상상

**핵심 요약**  
AWS는 AIOps를 관찰, 이해, 행동으로 이어지는 운영 자동화 흐름으로 설명하며 Amazon Bedrock AgentCore를 소개했다. 요기요는 30개 이상 AWS 계정과 60개 이상 마이크로서비스를 운영하면서 Datadog, Argo CD, Grafana, Elasticsearch, CDN 로그 등 여러 도구를 오가야 하는 SRE 업무 부담을 겪고 있었다. 위대한상상은 AgentCore 기반 운영 포털을 만들고, 자연어 질문으로 서비스 영향도 분석, 리소스 최적화, 이벤트 리포트를 생성하는 구조를 구현했다. 핵심 성과는 모든 판단을 자동화한 것이 아니라 탐색 시간을 줄이고 근거를 정량화해 운영자가 더 중요한 의사결정에 집중하도록 만든 점이었다.

**주요 포인트**
- Bedrock AgentCore의 Runtime, Identity, Memory, Gateway를 활용해 에이전트 배포, 권한, 대화 맥락, 운영 도구 연결을 통합했다.
- 운영 포털은 CloudFront, ALB, Cognito, Lambda Authorizer를 거쳐 AgentCore로 요청을 보내고, MCP 형태의 Lambda 도구가 AWS·외부 관측 데이터를 조회한다.
- 연결 데이터에는 AWS 컴퓨트·네트워크·DB·스토리지·보안·모니터링·비용 지표와 Prometheus, Loki, Datadog, CDN 로그 등이 포함됐다.
- AI Assistant는 Elasticache 대역폭 병목과 read replica 증설 필요성 같은 판단을 콘솔 5개를 오가던 작업보다 빠르게 정리했다.
- 리소스 최적화는 피크 구간 기준 병목 시뮬레이션으로 Graviton 전환, 다운사이징, 세대 교체를 비교했고 Elasticache 비용 55% 절감, 작업 효율 10배 이상 향상을 확인했다.

**AWS/기술 키워드**  
Amazon Bedrock AgentCore, AgentCore Runtime, AgentCore Identity, AgentCore Memory, AgentCore Gateway, AWS Lambda, MCP, Amazon CloudFront, ALB, Amazon Cognito, Amazon Aurora, Amazon DynamoDB, ElastiCache, Prometheus, Loki, Datadog, Grafana, Argo CD

**현장 메모로 남길 점**  
요기요가 얻은 교훈은 "전문 에이전트를 많이 나누는 것"보다 단일 에이전트가 하나의 판단 맥락 안에서 원본 데이터를 해석하는 방식이 더 자연스럽고 정확했다는 점이다.

**블로그용 한줄**  
요기요는 Bedrock AgentCore 기반 AIOps로 흩어진 운영 지표를 자연어 분석과 표준 리포트로 묶어 SRE의 콘솔 탐색 시간을 크게 줄였다.

## sel-prt101-s

**제목/시간/트랙/발표자**  
- 제목: The Platform for AI Success: Enterprise AI와 Agent 전략 (sponsored by 데이터이쿠)
- 시간: 2026-05-20 15:30-15:50 KST
- 트랙: Industry Day / Artificial Intelligence
- 발표자: 김영석 상무, Dataiku

**핵심 요약**  
Dataiku는 많은 기업이 AI를 사용하고 있지만 실제 가치를 만드는 기업은 소수에 그친다는 문제의식에서 출발했다. 발표자는 엔터프라이즈 AI 성공의 핵심을 사용자, 특히 현업 도메인 전문가가 직접 주도할 수 있는 플랫폼에 두었다. Dataiku는 기존 MLops 기반 위에 생성형 AI와 에이전틱 AI를 통합하고, 여러 데이터·모델·애플리케이션을 연결하는 오케스트레이션 레이어로 자신들의 플랫폼을 설명했다. 특히 엔터프라이즈 환경에서는 완전 자율 에이전트보다 결정론적 프로세스, 휴먼 인 더 루프, 거버넌스가 결합된 구조화된 에이전트가 필요하다고 강조했다.

**주요 포인트**
- AI 실패 원인으로 현업과 AI 엔지니어의 소통 괴리, 불명확한 유스케이스, 데이터 파편화, 조직문화 경직성, 보안·규제·거버넌스 부재를 제시했다.
- 데이터 플랫폼을 완전히 새로 만들 때까지 기다리기보다, 현재 흩어진 데이터를 연결해 AI를 실행하는 cross-platform orchestration이 필요하다고 말했다.
- Dataiku는 노코드·로코드·하이코드 사용자를 모두 지원하고, 데이터 연결부터 모델 개발·배포·에이전트화까지 단일 UX로 제공한다고 소개했다.
- 엔터프라이즈 에이전트는 확률적 LLM 호출만으로 충분하지 않으며, 미리 정의된 워크플로와 분기, 루프, 메모리, 병렬 처리가 포함된 결정론적 흐름이 필요하다고 설명했다.
- 제조 유지보수 스케줄링 사례에서는 센서 데이터, 설비 정보, 보고서, 예측 모델, 벡터 DB, 멀티 에이전트를 결합해 예방정비 의사결정을 지원하는 구조를 제시했다.

**AWS/기술 키워드**  
Dataiku, MLOps, AgentOps, Structured Agent, Deterministic Workflow, Human-in-the-loop, Cross-platform Orchestration, Vector DB, Predictive Maintenance, No-code/Low-code/High-code, AWS Bedrock Agent 연계 예정

**현장 메모로 남길 점**  
발표의 중심 문장은 "사용자가 쓰지 않는 AI는 성공할 수 없다"에 가까웠다. 엔터프라이즈 AI는 모델 성능보다 현업 채택, 통제, 반복 가능한 운영 흐름이 더 큰 병목이라는 메시지가 강했다.

**블로그용 한줄**  
Dataiku는 현업 도메인 전문가가 데이터, 모델, 에이전트를 한 플랫폼에서 오케스트레이션하고 통제할 수 있어야 엔터프라이즈 AI가 실제 성과로 이어진다고 강조했다.

## sel-prt105-s

**제목/시간/트랙/발표자**  
- 제목: AI ‘개발’에서 ‘운영’으로: 엔터프라이즈 AI 전환 (sponsored by 베스핀글로벌)
- 시간: 2026-05-20 15:30-15:50 KST
- 트랙: Industry Day / Financial Services, Manufacturing & Industrial, Retail & Consumer Goods, Telecommunications / Application Integration, Artificial Intelligence, Business Applications
- 발표자: 장형화 AXT 본부 이사, 베스핀글로벌

**핵심 요약**  
베스핀글로벌은 기업 AI가 PoC와 해커톤 중심의 개발 단계를 지나 운영 책임을 져야 하는 단계에 들어섰다고 진단했다. 발표자는 AI가 실제 비즈니스에 적용되지 못하는 이유를 거버넌스, 변화관리, 프로세스 통합, 모델·팀별 파편화에서 찾았다. `HelpNow AI Foundry`는 현업이 직접 에이전트를 만들고, 멀티 LLM과 다양한 데이터 소스를 연결하며, 운영·모니터링·감사까지 제공하는 플랫폼으로 소개됐다. 데모에서는 자연어 기반 에이전트 생성, 블록형 워크플로, S3 문서 파싱·청킹·임베딩, 그래프 레이크, 비용·사용량 대시보드가 시연됐다.

**주요 포인트**
- AI는 더 이상 연구 프로젝트나 PoC가 아니라 운영 대상이며, 운영 책임은 결국 기업에게 돌아온다고 강조했다.
- HelpNow AI Foundry의 핵심은 현업이 직접 만드는 AI 에이전트 환경, 어떤 모델이든 연결하는 멀티 LLM 통합, 운영에 필요한 모니터링·거버넌스·감사 기능이다.
- 플랫폼은 비정형 데이터를 AI-ready 데이터로 만드는 RAGOps, 에이전트 오케스트레이션, 운영·관리·거버넌스 영역으로 구성된다.
- 자연어 프롬프트로 에이전트 워크플로를 생성하고, 블록을 드래그해 AWS 및 비즈니스 시스템을 연결하는 노코드 경험을 강조했다.
- 내부 사용 사례에서는 사용자별 에이전트, 사용 모델, 비용, 로그를 확인해 감사와 비용 통제가 가능하다고 설명했다.

**AWS/기술 키워드**  
HelpNow AI Foundry, AWS Marketplace, Multi-LLM, LLMOps, RAGOps, Agent Orchestration, Graph Lake, Amazon S3, Parsing, Chunking, Embedding, No-code Agent Builder, Audit Log, Governance Dashboard

**현장 메모로 남길 점**  
기술 세부보다 "AI 플랫폼을 어떤 기준으로 선택할 것인가"에 집중한 세션이었다. 만들기 쉬운 에이전트보다 운영, 통제, 비용 가시성, 감사 대응이 되는 에이전트 플랫폼을 강조했다.

**블로그용 한줄**  
베스핀글로벌은 HelpNow AI Foundry를 통해 기업 AI의 초점을 개발에서 운영으로 옮기고, 현업 주도 에이전트 생성과 LLMOps·거버넌스를 한 플랫폼으로 묶는 전략을 제시했다.

## sel-prt211-s

**제목/시간/트랙/발표자**  
- 제목: AI 컨시어지: 기억하는 AI가 만드는 다음 세대 고객 경험 (sponsored by 센드버드)
- 시간: 2026-05-20 15:30-15:50 KST
- 트랙: Industry Day / Retail & Consumer Goods, Software & Internet / Artificial Intelligence, Business Applications
- 발표자: 이상희 대표이사, 센드버드

**핵심 요약**  
센드버드는 AI 챗봇과 컨택센터 현대화 프로젝트가 PoC에서는 성공해도 실제 고객 경험과 비즈니스 성과로 이어지지 못한 이유를 "고객을 기억하지 못하는 AI"에서 찾았다. 발표는 CRM의 정적 데이터와 티켓팅 시스템의 사후 대응 방식만으로는 고객의 맥락, 감정, 의도, 채널 간 연속성을 제공하기 어렵다고 설명했다. `delight.ai`는 장기 메모리, 맞춤형 대화, 옴니프레즌스, Trust OS를 기반으로 고객 여정 전체에서 개인화된 AI 컨시어지를 제공하는 방향으로 소개됐다. 실제 사례로 창고형 리테일러, 쿠팡이츠 일본, 한샘, Norse Atlantic Airways의 빠른 도입과 구매 단가 상승, CS 자동화, 고객 만족도 개선을 공유했다.

**주요 포인트**
- 샌드버드는 4,000개 이상 엔터프라이즈, 월 70억 건 이상 메시지, 3.2억 명 이상 사용자를 처리해온 커뮤니케이션 인프라 위에 AI 컨시어지를 구축했다고 설명했다.
- 기존 AI 상담은 세션·채널을 넘어 고객 맥락을 기억하지 못해 반복 설명, 사람 상담사 핸드오프, 중복 투자를 초래한다고 진단했다.
- delight.ai의 핵심 축은 장기 고객 메모리, 구매 이력·선호도 기반 선제적 대화, 웹·앱·문자·이메일을 넘나드는 옴니프레즌스, 엔터프라이즈급 Trust OS다.
- 미국 창고형 리테일러 사례에서는 AI 쇼핑 어시스턴트와 대화한 고객의 평균 구매 단가가 20% 상승하고 특정 페르소나에서는 최대 6배 상승했다고 소개했다.
- 쿠팡이츠 일본은 약 29일 만에 AI 상담을 출시했고, 한샘은 3주 도입 후 고객 상담의 90%를 AI가 종결하는 수준을 보였다고 설명했다.

**AWS/기술 키워드**  
delight.ai, AI Concierge, Agent Memory Platform, Omnipresence, Trust OS, AI Contact Center, Customer Experience AI, Long-term Memory, Personalization, Agent Economy

**현장 메모로 남길 점**  
AI 상담의 성패를 자동화율만이 아니라 구매 단가, 업셀, 고객 만족도, 브랜드 데이터 소유권으로 확장해 본 점이 좋았다. 앞으로 브랜드가 자체 AI 컨시어지를 갖는 것이 고객 관계 주도권의 문제가 될 수 있다는 메시지가 강했다.

**블로그용 한줄**  
센드버드는 고객을 기억하고 채널을 넘어 맥락을 이어가는 AI 컨시어지가 다음 세대 고객 경험과 브랜드 데이터 주도권의 핵심이 될 것이라고 제시했다.

## sel-prt209-s

**제목/시간/트랙/발표자**  
- 제목: 에버랜드의 VMware에서 Nutanix 클라우드 클러스터로 마이그레이션 여정 (sponsored by Nutanix)
- 시간: 2026-05-20 15:30-15:50 KST
- 트랙: Industry Day / Cloud Operations, Hybrid Cloud & Multicloud, Migration & Modernization
- 발표자: 김상우 상무, Nutanix

**핵심 요약**  
Nutanix는 엔터프라이즈가 클라우드의 유연성을 원하지만 기존 운영 모델과 애플리케이션을 한 번에 바꾸는 데 큰 리스크를 느낀다는 문제에서 출발했다. 발표는 `Nutanix Cloud Clusters(NC2) on AWS`가 온프레미스 Nutanix 운영 환경을 AWS로 확장해 동일한 관리 방식으로 프라이빗 클라우드와 퍼블릭 클라우드를 연결한다고 설명했다. 단순 마이그레이션뿐 아니라 DR, 온디맨드 클린룸, 데이터 보호, 사이버 복구, VM·컨테이너·AI 워크로드까지 단일 운영 모델로 확장할 수 있음을 강조했다. 에버랜드 사례에서는 VMC on AWS에서 NC2 on AWS로 제한된 일정 안에 이전하며 안정성, 비용 리스크 완화, 운영 연속성을 확보한 여정을 공유했다.

**주요 포인트**
- 기업의 클라우드 여정은 프라이빗, 하이브리드, 클라우드 퍼스트 단계로 이어지며, 핵심은 어느 위치에서든 일관된 운영 모델을 유지하는 것이다.
- NC2는 기존 Nutanix Prism 기반 관리 방식, 네트워크·보안 정책, 자동화 운영 프로세스를 AWS 위에서도 유지하게 해준다.
- AWS 서비스와의 연동을 통해 S3, RDS, Load Balancer, Bedrock 같은 서비스를 필요 시 활용하면서 기존 업무 환경은 안정적으로 이전할 수 있다고 설명했다.
- 온디맨드 클린룸은 평상시 NC2 클러스터를 대기 상태로 두고, 변경 불가능한 스냅샷을 S3에 저장했다가 비상 시 자동 복구 환경을 구성하는 방식이다.
- 삼성물산 리조트/에버랜드 사례는 VMC 라이선스 비용 리스크를 줄이고, Multi-AZ 기반 액티브-액티브 운영과 Nutanix Move 자동화 도구로 3개월 내 이전을 완료한 사례로 제시됐다.

**AWS/기술 키워드**  
Nutanix Cloud Clusters(NC2) on AWS, VMware Cloud on AWS, Nutanix Move, Multi-AZ, Active-Active, Amazon S3, Amazon RDS, Elastic Load Balancing, Amazon Bedrock, Hybrid Cloud, Disaster Recovery, Immutable Snapshot, On-demand Clean Room, Cyber Recovery

**현장 메모로 남길 점**  
마이그레이션 세션이지만 "클라우드 네이티브로 전면 재설계"가 아니라 시간·리스크·비용의 현실적 균형을 찾는 증검다리 전략이 핵심이었다. 에버랜드처럼 다운타임이 고객 경험에 직결되는 환경에서는 운영 모델 유지가 큰 가치로 제시됐다.

**블로그용 한줄**  
Nutanix는 NC2 on AWS로 기존 VMware 기반 운영 모델을 유지하면서 에버랜드 워크로드를 안정적으로 이전하고, DR·데이터 보호·하이브리드 확장까지 이어지는 현실적 클라우드 전환 방식을 제시했다.
