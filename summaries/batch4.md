# Batch 4 요약

작성 기준: 아래 9개 세션은 모두 VOD 음성 전사(`--model base`)를 기반으로 정리했다. 전사상 일부 고유명사와 수치에는 음성 인식 오차 가능성이 있어, 공식 메타데이터의 제목/시간/발표자 정보를 함께 대조했다.

## sel-wps102

**제목/시간/트랙/발표자**  
- 제목: 중앙대의료원_의료진이 직접 만드는 의료 AI
- 시간: 2026-05-20 13:50-14:10 KST
- 트랙: Healthcare & Life Sciences, Professional Services / Artificial Intelligence
- 발표자: 김찬웅 교수, 중앙대학교의료원

**핵심 요약**  
중앙대의료원은 의료 AI를 외부 솔루션 도입 문제가 아니라, 현장 맥락을 가장 잘 아는 의료진과 직원이 직접 문제를 정의하고 도구를 만드는 전환 과제로 다뤘다. 발표자는 코로나 시기 신규 병원 개원과 인력 부족 속에서 RPA/IPA 경험을 쌓은 뒤, AWS와의 프로그램 및 Kiro 기반 바이브 코딩을 통해 비개발자 의료진도 프로토타입을 만들 수 있음을 확인했다고 설명했다. 핵심은 의료 데이터의 민감성과 보안 이슈를 인정하면서도, 반복적 데이터 처리 시간을 줄여 의료진이 환자와 치료 본질에 더 집중하게 만드는 것이다. 실제 예로 복약 이력 정리와 연구 업적 입력 자동화가 소개됐다.

**주요 포인트**
- 중앙대 광명병원 개원 당시 전공의/레지던트 없이 교수와 직원이 반복 업무를 직접 처리해야 했던 경험이 자동화 전환의 출발점이었다.
- 의료기관의 AI 적용 기회는 반복적인 데이터 처리에 있지만, 민감정보 관리와 의료 도메인 지식의 폐쇄성이 큰 장벽으로 제시됐다.
- 약 250명 이상의 의료진과 직원이 참여한 프로그램에서 16개 팀이 프로토타입을 만들었고, 의사뿐 아니라 간호, 영상, 진단검사, 행정 등 다양한 직군이 참여했다.
- Kiro는 요구사항과 스펙을 먼저 구체화하는 방식이 의료진의 가이드라인 중심 사고와 잘 맞는 도구로 소개됐다.
- 복약 이력 정리 도구는 환자의 기존 처방 목록에서 현재 복용 중인 약, 최근 추가/중단된 약을 정리해 휴먼 에러 가능성을 낮추는 사례로 제시됐다.

**AWS/기술 키워드**
- AWS T&C 프로그램, Kiro, 바이브 코딩, RPA/IPA, LLM, 의료 데이터 보안, 비개발자 개발

**현장 메모로 남길 점**
- 의료 AI의 출발점은 “거대한 모델”보다 현장 직원이 매일 부딪히는 작고 구체적인 불편을 정확히 잡아내는 데 있었다.
- 보안은 멈춤의 이유가 아니라 설계의 전제이며, 의료진 주도 개발에는 멘토링과 안전한 실험 환경이 중요하다.

**블로그용 한줄**
- “중앙대의료원 사례는 의료 AI의 장벽을 낮추는 가장 현실적인 방법이 현장을 아는 사람이 직접 작은 도구를 만들 수 있게 하는 것임을 보여줬다.”

## sel-ind227

**제목/시간/트랙/발표자**  
- 제목: [GS 칼텍스] 현장이 만드는 AI 혁신: GS칼텍스의 제조 AI 전환 여정
- 시간: 2026-05-20 14:30-15:10 KST
- 트랙: Energy & Utilities / Artificial Intelligence
- 발표자: 이은주 전무, GS 칼텍스

**핵심 요약**  
GS칼텍스는 제조 AI 전환을 탑다운 솔루션 도입이 아니라 “현업이 직접 배우고, 만들고, 나누는” 바텀업 전환으로 재설계했다. 여수공장처럼 대규모 장치산업 환경에서는 설비와 배관이 복잡하고 운영 인력은 제한적이기 때문에, 데이터와 AI가 보이지 않는 공장을 보이게 하는 핵심 수단이 된다. DAX 아카데미, 플레이그라운드, AIU 플랫폼, Good Risk Taking 문화가 결합되면서 현업이 직접 모델, 대시보드, 에이전트를 만드는 구조가 만들어졌다. 마케팅, 설비관리, 공정운전, 안전, 구매/재무까지 밸류체인 전반에 AI가 확산된 사례가 소개됐다.

**주요 포인트**
- 초기 탑다운 실험의 한계를 겪은 뒤, 느리더라도 조직에 스며드는 바텀업 전환으로 방향을 전환했다.
- DAX 아카데미는 로코드, 대시보드, 데이터 분석, 에이전트, 온톨로지, 피지컬 AI 등 13개 과정으로 확대됐고, 목표 240명 대비 400명 이상이 교육을 신청했다.
- 데이터 분석 모델은 일부를 현업이 직접 만들고, 대시보드는 대부분 현업 주도로 제작되며, 에이전트는 10개 중 9개 수준을 현업이 직접 만드는 구조가 되었다.
- Amazon Bedrock 기반 사내 생성형 AI 플랫폼 AIU는 사내 지식 기반 질의와 에이전트 제작을 확산시키는 중심 플랫폼으로 소개됐다.
- 고객 VOC 통합 대시보드, Text-to-SQL 기반 마케팅 세그먼트 추출, 배관 부식/회전기계 이상 감지, TBM AI 안전 비서, 구매 에이전트 등이 실제 적용 사례로 제시됐다.

**AWS/기술 키워드**
- Amazon Bedrock, AIU, 데이터 레이크, Text-to-SQL, 온톨로지, MLOps, 대시보드, 생성형 AI 에이전트, Good Risk Taking

**현장 메모로 남길 점**
- 발표의 메시지는 명확했다. 제조 AI의 주역은 IT 전문가만이 아니라 공정과 고객을 아는 현장 SME이며, IT의 역할은 “대신 만들어주기”에서 “현장이 만들 수 있는 기반 제공”으로 이동한다.

**블로그용 한줄**
- “GS칼텍스는 제조 AI 전환의 핵심을 기술 자체보다 현업이 직접 만들고 리더가 좋은 리스크를 감당하는 문화로 정의했다.”

## sel-ind304

**제목/시간/트랙/발표자**  
- 제목: 당근의 CloudHSM/KMS기반 대규모 서명키관리 시스템구축기
- 시간: 2026-05-20 14:30-15:10 KST
- 트랙: Retail & Consumer Goods / Application Integration, Security & Identity
- 발표자: 박진현 솔루션즈 아키텍트(AWS), 조승환 Identity Service Engineer(당근), 최용환 Site Reliability Engineer(당근)

**핵심 요약**  
당근은 월간 활성 사용자 2,000만 명 이상, 하루 평균 6,500만 건 이상의 인증 요청을 처리하는 환경에서 서명키 유출 위험을 줄이고 대규모 JWT 서명을 안정적으로 처리하기 위해 CloudHSM과 KMS 기반 하이브리드 구조를 구축했다. 기존에는 private key가 Secret Manager에 있어 접근 권한이 있으면 추출 가능성이 남아 있었고, 모바일 앱에서 서명 서비스에 직접 연결되는 구조상 더 촘촘한 접근 제어가 필요했다. CloudHSM은 비용, 지연시간, 선형 확장성 측면에서 메인 서명 백엔드로 선택됐고, KMS는 장애 시 fallback을 위한 standby로 구성됐다. 운영 중 HSM 통신 장애 상황에서도 KMS fallback으로 사용자 영향 없이 서비스를 유지한 사례가 핵심 성과로 소개됐다.

**주요 포인트**
- 서명키는 JWT, 코드 서명, TLS 인증서 등 신뢰 체계의 뿌리이며, 유출 시 공급망 전체와 사용자 인증 체계가 무너질 수 있다는 점을 먼저 짚었다.
- 당근은 private key가 절대 외부로 유출되지 않을 것, 6,000 RPS 수준 서명 트래픽을 감당할 것, SPOF가 없을 것, 접근 제어가 촘촘할 것, 담당자도 임의 서명할 수 없을 것을 요구사항으로 잡았다.
- CloudHSM은 VPC 내부 배치, PKCS#11 표준 인터페이스, 싱글 테넌트, 시간당 과금 구조 덕분에 고트래픽 환경에서 유리하다고 판단했다.
- EKS, Istio Authorization Policy, 보안 그룹, mTLS, Secret Manager, IRSA, CloudTrail, Kyverno 정책을 조합해 HSM 접근 경로를 다층으로 제한했다.
- PKCS#11 세션 고정, scale-in 시 in-flight 요청 오류, max sessions 튜닝, 바이너리 로그 관측성 부족 같은 실전 이슈를 테스트와 로그 수집 컴포넌트로 해결했다.
- JWT `kid` 기반 키 로테이션으로 기존 수천만 토큰을 깨지 않고 HSM/KMS/기존 local key를 공존시키며 무중단 전환했다.

**AWS/기술 키워드**
- AWS CloudHSM, AWS KMS, AWS Secrets Manager, AWS CloudTrail, EKS, Istio, mTLS, IRSA, Kyverno, PKCS#11, JWT, KID, active-standby fallback

**현장 메모로 남길 점**
- 보안 아키텍처의 좋은 사례였다. 키를 “잘 숨기는” 수준이 아니라 추출 불가능성, 접근 주체 분리, fallback, 관측성, 키 로테이션까지 운영 전체를 설계했다.

**블로그용 한줄**
- “당근의 사례는 대규모 인증 시스템에서 CloudHSM과 KMS를 조합하면 보안성과 고가용성을 동시에 잡을 수 있음을 보여줬다.”

## sel-ind207

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

## sel-ind211

**제목/시간/트랙/발표자**  
- 제목: [바비톡] 바비톡의 AX여정: 에이전틱 AI로 K-beauty를 바꾸다
- 시간: 2026-05-20 14:30-15:10 KST
- 트랙: Advertising & Marketing, Healthcare & Life Sciences, Software & Internet / Architecture, Artificial Intelligence, Cloud Operations
- 발표자: 박민주 솔루션즈 아키텍트(AWS), 최권열 CTO(바비톡)

**핵심 요약**  
바비톡은 AI 도입을 유행이 아니라 비즈니스 문제 해결 수단으로 보고, 리뷰 검수, AI 검색/답변, 뷰티 상담, K-beauty 여행 가이드, 내부 에이전트 스튜디오로 확장해온 AX 여정을 공유했다. AWS 파트에서는 PoC가 프로덕션으로 가지 못하는 이유를 모델 선택/비용, 에이전트 설계 속도, 운영 복잡도로 나누고 Bedrock, Strands SDK, AgentCore, AI-DLC를 해결책으로 제시했다. 바비톡은 use case별로 Claude Sonnet과 Amazon Nova 계열 모델을 나눠 쓰며 비용을 10분의 1로 줄였고, 단일 에이전트를 NLU/DM/NLG 등 역할별 멀티 에이전트로 재구성했다. 특히 K-beauty 여행 가이드는 Kiro, AgentCore, Strands, AI-DLC로 1명의 개발자가 1주일 만에 출시한 사례로 소개됐다.

**주요 포인트**
- 리뷰 검수는 EventBridge와 Lambda, Bedrock 기반 LLM, 운영팀 검수 매뉴얼을 연결해 PoC를 시작했고, 이후 관리자 콘솔까지 통합됐다.
- 운영팀 효율은 50% 증가했고 비정상 게시물 누락률을 0으로 낮춘 사례가 소개됐다.
- 초기 Claude 기반 모델에서 Nova로 전환하며 비용/성능과 모델 교체 유지보수 비용을 최적화했다.
- AI 검색/답변은 단일 LLM 에이전트에서 NLU, Dialogue Manager, NLG 역할을 분리한 멀티 에이전트로 진화했다.
- “공주의 시크릿 상담소”는 1명의 개발자가 3주 안에 frontend, backend, AI, DevOps, 운영 최적화까지 수행한 사례로 소개됐다.
- K-beauty 여행 가이드는 AgentCore Runtime, Strands Agents, Kiro, AI-DLC를 결합해 일정, 시술 상품, 팝업스토어 등 최신성과 실재 여부가 중요한 정보를 다뤘다.
- hallucination 대응을 위해 도구 우선순위, 참조 가능한 정보 범위, 검증 리포트, CI/CD 내 품질 리포트를 함께 설계했다.
- 향후 AI Agent Studio로 비개발자도 업무용 에이전트를 만들고 공유하는 구조를 준비 중이라고 밝혔다.

**AWS/기술 키워드**
- Amazon Bedrock, Claude Sonnet, Amazon Nova Micro/Lite/Pro, AWS Lambda, Amazon EventBridge, Bedrock AgentCore Runtime, AgentCore Gateway, AgentCore Observability, Strands Agents SDK, AWS Kiro, AI-DLC, CI/CD

**현장 메모로 남길 점**
- 바비톡의 강조점은 “작게, 빠르게, 비즈니스 문제부터”였다. 정식 기능보다 pocket service처럼 열고 닫으며 실험하는 방식이 스타트업형 AI 도입 전략으로 인상적이었다.

**블로그용 한줄**
- “바비톡은 AI 에이전트를 거창한 플랫폼이 아니라 빠르게 실험하고 검증하며 비즈니스 플라이휠로 키우는 방식으로 접근했다.”

## sel-ind217

**제목/시간/트랙/발표자**  
- 제목: LG전자, 에이전틱 AI 기반 멀티에이전트 플랫폼 구축을 통한 업무혁신
- 시간: 2026-05-20 14:30-15:10 KST
- 트랙: Manufacturing & Industrial / Industry Solutions
- 발표자: 문필재 팀장, LG전자 한국영업본부 AX플랫폼

**핵심 요약**  
LG전자 한국영업본부는 고객 데이터 플랫폼과 대시보드 AI에서 출발해, 정형/비정형/멀티모달 데이터를 다루는 멀티 에이전트 플랫폼 “Agent One”으로 AX를 확장했다. 영업본부는 오프라인 매장, 온라인 판매, B2B 영업, 마케팅, 물류, 신제품 지원 등 다양한 업무를 수행하기 때문에 AI 에이전트도 데이터 분석을 넘어 교육, CRM, GEO 모니터링, 상담 기록, 유튜브/뉴스 분석, 실적 분석, CAD 도면 자동화로 넓어졌다. 플랫폼은 개별 에이전트를 포털처럼 호출하거나 planner가 적합한 에이전트를 선택하고, collector/coder/reporter 등 역할을 나눠 리포트를 생성하는 구조로 설명됐다. 향후에는 에이전트 워크플로 빌더와 영업본부 온톨로지를 통해 현업 담당자가 직접 에이전트들을 연결하는 방향을 준비하고 있다.

**주요 포인트**
- 기존 DX 조직은 CDP와 경영 지표 대시보드를 운영했고, 2024년에는 자연어로 고객 조건을 입력해 세그먼트를 추출하는 챗인사이트/챗봇 형태를 만들었다.
- 2025년에는 내부/외부 데이터, API, 검색을 결합해 분석 리포트를 만드는 멀티 에이전트 “Deep Analyst” 형태로 확장했다.
- Agent One은 AWS 인프라, Redshift, Aurora, RAG, vector search, Amazon Bedrock, Amazon Transcribe, Amazon IVS, Amazon Q/QuickSight 계열 기능을 조합해 멀티모달 업무를 처리한다.
- Role Playing Agent는 판매 매니저 교육 영상을 Amazon IVS로 녹화해 S3에 저장하고, 영상/표정/제스처와 음성을 분리 분석한 뒤 Bedrock으로 평가 기준표 기반 피드백을 생성한다.
- 구독 대시보드/챗봇 사례는 QuickSight 필터 맥락을 에이전트가 이해해 현재 보고 있는 지역의 판매 트렌드나 지도 분석을 이어서 답변하는 방식이었다.
- AutoGen CRM은 캠페인 기획, CDP 기반 타게팅, 세그먼트 생성, 카피라이팅, 이미지 생성, 발송, 성과 분석까지 CRM 흐름을 여러 에이전트가 나눠 처리한다.
- GEO 모니터링은 AI 검색/추천 시대에 LG전자 제품이 어떤 질문에서 어떻게 인용되고 추천되는지를 직접 수집/분석하는 사례였다.
- CAD 도면 자동화는 공간 면적 산출, 제품 스펙 선정, 배치, 검토 자동화를 목표로 하며 전문점 설계 검토의 80% 이상 자동화를 추진 중이라고 소개됐다.

**AWS/기술 키워드**
- Amazon Bedrock, Amazon Transcribe, Amazon IVS, Amazon S3, Amazon Aurora, Amazon Redshift, Amazon QuickSight, RAG, vector search, 멀티모달 AI, agent orchestration, ontology, CAD automation

**현장 메모로 남길 점**
- LG전자의 사례는 “에이전트 하나”가 아니라 영업본부 업무 전체에 작은 에이전트들을 깔고, 이후 워크플로로 연결해 실제 생산성으로 묶어내려는 플랫폼 접근이었다.

**블로그용 한줄**
- “LG전자는 Agent One을 통해 데이터 분석을 넘어 매장 교육, CRM, B2B 도면 업무까지 현업형 멀티 에이전트로 확장하고 있었다.”

## sel-ind230

**제목/시간/트랙/발표자**  
- 제목: [위로보틱스 I RLWRLD] AWS 위에서 만드는 로봇의 미래: 리얼월드의 RFM 학습과 위로보틱스의 휴머노이드 조작기능 구현
- 시간: 2026-05-20 14:30-15:10 KST
- 트랙: Aerospace & Satellite, Federal Government, Manufacturing & Industrial / Artificial Intelligence, Business Applications, Industry Solutions
- 발표자: 김용재 CTO(위로보틱스), 배재경 CTO(RLWRLD)

**핵심 요약**  
RLWRLD와 위로보틱스는 피지컬 AI에서 로봇 파운데이션 모델과 하드웨어 플랫폼이 어떻게 함께 발전해야 하는지를 보여줬다. RLWRLD는 VLA 기반 Robot Foundation Model에 motion, physics, memory module을 더해 움직이는 물체 예측, 촉각/힘 정보 활용, 장기 맥락 기억을 강화했고, 이를 AWS의 대규모 GPU/스토리지 인프라로 학습했다. 학습에는 S3, FSx for Lustre, ParallelCluster, H200 GPU 64 nodes, L4S 기반 렌더링/시뮬레이션, Elastic Fabric Adapter 등이 활용됐다. 위로보틱스는 힘과 접촉을 잘 느끼는 휴머노이드 Alex를 소개하며, AWS Physical AI Fellowship에서 드릴/볼팅 조작 파이프라인을 6주 안에 구축한 여정을 공유했다.

**주요 포인트**
- RLWRLD의 모델은 VLA 구조에 액션 헤드를 붙인 형태이며, 기존 VLA가 약한 움직임 예측, 촉각/힘 정보, 기억 기반 작업을 보완하는 세 모듈을 강조했다.
- 데이터는 teleoperation, human demonstration, synthetic/augmented data, open data로 구성되며, 비디오 생성 모델과 IDM 기반 pseudo action, filtering으로 증강했다.
- human data는 wearable 없이 multi-camera로 사람 손 관절 정보를 추출하고 로봇으로 retargeting한 뒤 simulation 렌더링을 통해 학습 데이터로 만들었다.
- pretrain/mid-train/fine-tuning 구조로 학습했고, H200 GPU 64 nodes에서 pretrain은 약 8일 이상, mid-train은 하루 미만이 걸렸다고 설명했다.
- ParallelCluster는 Slurm 기반으로 활용됐고, 원본 데이터는 S3, 빠른 접근이 필요한 학습 데이터와 checkpoint는 FSx for Lustre에 두었다.
- 모방학습 후 병목 구간에 추가 데이터를 모으고, 강화학습으로 손잡이를 돌리는 작업의 속도를 기존 대비 약 3배 높인 사례가 소개됐다.
- 위로보틱스 Alex는 15자유도 hand, 전신 force sensing, 높은 backdrivability/compliance, 30kg 수준 payload를 강조했다.
- Physical AI Fellowship에서는 Amazon Kinesis, S3, Glue, EC2, NVIDIA Isaac Lab/물리 엔진을 활용해 데이터 수집, 정제, 강화학습, 배포 파이프라인을 구축했다.

**AWS/기술 키워드**
- AWS ParallelCluster, Slurm, Amazon S3, Amazon FSx for Lustre, Amazon EC2 H200/L4S, Elastic Fabric Adapter, AWS Glue, Amazon Kinesis, AWS HyperPod, Bedrock 구상, NVIDIA Isaac Lab, VLA, RFM, teleoperation, reinforcement learning

**현장 메모로 남길 점**
- 피지컬 AI는 모델만의 문제가 아니라 데이터 수집, 시뮬레이션, 실시간 제어, 하드웨어 감각, 학습 인프라가 한꺼번에 맞물려야 하는 전체 시스템 문제라는 점이 선명했다.

**블로그용 한줄**
- “RLWRLD와 위로보틱스 세션은 피지컬 AI가 거대 모델 학습과 로봇 하드웨어 감각이 만나는 지점에서 현실화되고 있음을 보여줬다.”

## sel-ind303

**제목/시간/트랙/발표자**  
- 제목: LG U+의 에이전틱 AI 기반 대규모 마이그레이션 여정
- 시간: 2026-05-20 14:30-15:10 KST
- 트랙: Telecommunications / Artificial Intelligence, Developer Tools, Migration & Modernization
- 발표자: 문승제 딜리버리 컨설턴트(AWS), 우건희 책임(LG U+)

**핵심 요약**  
LG U+는 100개 이상의 온프레미스 애플리케이션을 클라우드로 전환하면서, assessment, design, migration, scale-out 단계 전반에 에이전틱 AI를 적용했다. 목표는 단순 이전이 아니라 운영 표준화, 보안 강화, 마이그레이션 속도/품질 확보, AX 기반 혁신 환경 마련이었다. UCMP에 내재화한 인터뷰 에이전트와 코드 분석 에이전트가 표준화된 입력을 만들고, design agent가 목표 AWS native architecture와 refactoring action item을 생성했다. migration 단계에서는 AWS Transform Custom이 대규모 규칙 기반 변환을 맡고, Kiro IDE와 Utopia 플랫폼이 복잡한 리팩터링 패턴과 조직 표준을 재사용 가능한 지식으로 축적했다.

**주요 포인트**
- 대규모 온프레미스 환경은 서비스별 인프라/로그/보안/외주 개발사가 분산되어 있어 통합 모니터링, 패치, 보안 대응, AI 도입이 느려지는 문제가 있었다.
- Assessment 단계의 인터뷰 에이전트는 AWS 마이그레이션 경험이 담긴 61개 질문을 기반으로 답변 품질을 검증하고, 부족하면 재질문해 표준화된 리포트와 JSON을 생성했다.
- 코드 분석에는 AWS Transform Custom을 활용해 framework/runtime, security/compliance, dependency/CVE, cloud readiness 관점으로 코드를 진단했다.
- Design 단계는 인터뷰 결과와 코드 분석 결과를 입력으로 목표 아키텍처와 리팩터링 action item을 자동 생성하고 Confluence에 기록했다.
- Migration 단계에서 Java version upgrade 같은 반복/규칙 기반 대규모 변경은 AWS Transform Custom이 변환, build, validation을 반복하며 PR 형태로 결과를 만들었다.
- 복잡한 리팩터링은 Kiro IDE의 steering, skill, powers를 활용했고, Utopia 플랫폼이 검증된 기술 표준과 전환 패턴을 중앙 관리했다.
- LG CTL CLI는 프로젝트 세팅, action item 선택, requirement 생성, Kiro 개발 흐름, 테스트, 문서화, Confluence 업로드, 신규 skill/steering 생성까지 연결했다.
- 성과는 리드타임 단축, application 품질 향상, immutable/declarative/self-healing 원칙 기반 운영 표준 확립, 여러 개발사가 같은 기준으로 확장 가능한 전환 기반 마련으로 요약됐다.

**AWS/기술 키워드**
- AWS Transform Custom, Kiro IDE, Bedrock AgentCore Runtime, UCMP, Utopia, LG CTL, Confluence, Amazon S3, AWS native architecture, Elasticache 전환, steering/skills/powers, MCP, agentic migration

**현장 메모로 남길 점**
- 마이그레이션 자동화의 핵심은 AI가 코드를 바꾸는 것보다 “분석 결과, 설계 판단, 전환 패턴, 조직 표준”을 재사용 가능한 지식으로 축적하는 데 있었다.

**블로그용 한줄**
- “LG U+는 대규모 마이그레이션을 에이전틱 AI 워크플로로 재구성해, 전환 작업 자체를 조직 학습 시스템으로 바꾸고 있었다.”

## sel-ind222

**제목/시간/트랙/발표자**  
- 제목: [하나투어 I AK아이에스] AI가 바꾸는 여행 산업의 무대 뒤: 하나투어, 제주항공의 업무혁신
- 시간: 2026-05-20 14:30-15:10 KST
- 트랙: Aerospace & Satellite, Travel & Hospitality / Artificial Intelligence, Industry Solutions, Migration & Modernization
- 발표자: 주혜령 솔루션즈 아키텍트(AWS), 이길주 온라인개발 랩장(하나투어), 박수호 항공IT기획팀 팀장(AK아이에스)

**핵심 요약**  
이 세션은 여행 산업의 백오피스 혁신을 하나투어의 여행 상품 기획 에이전트와 AK아이에스/제주항공의 항공 정비 데이터 AI 전환 사례로 나눠 보여줬다. 하나투어는 초기 LLM loop 방식이 느리고 비싸며 MD가 선택하지 않는 결과를 만든 실패를 겪은 뒤, 여행 데이터를 knowledge graph로 재구성하고 AgentCore와 Neptune 기반 구조로 전환했다. 그 결과 10분 이상 걸리던 상품 초안 생성이 1분 이내로 줄고, 비용도 80% 이상 절감될 것으로 소개됐다. AK아이에스는 MEL 문서와 정비 이력 데이터를 검색 가능한 구조로 만들고, Textract 기반 AI OCR로 종이 정비 기록을 시스템 안으로 들여와 항공 안전과 정비 의사결정 속도를 높이는 방향을 제시했다.

**주요 포인트**
- AWS 파트는 여행 상품 기획 텍스트를 knowledge graph로, 항공 정비 종이 문서를 구조화된 디지털 데이터로 바꾸는 것이 AI 활용의 전제라고 설명했다.
- 하나투어의 1차 LLM 반복 구조는 10-20분 이상 걸리고 토큰/EC2 비용이 컸으며, 결과도 MD의 상품 기획 품질에는 미치지 못했다.
- 외부 지도/검색 기반 LLM을 활용한 2차 시도는 20-30초까지 빨라졌지만, 하나투어 고유 자산과 MD 노하우가 빠져 선택받지 못했다.
- 최종 구조는 Amazon Neptune에 여행 graph를 저장하고, AgentCore Runtime에 배포된 Claude 기반 agent가 AgentCore Gateway를 통해 graph 저장/검색 tool을 호출하는 방식이다.
- “그래프에 없는 데이터는 사용하지 말라”는 원칙으로 hallucination을 줄였고, MD 피드백을 자연어로 받아 Cypher query로 변환해 준실시간으로 graph를 업데이트하는 loop를 만들었다.
- AK아이에스는 MEL 문서와 MRO 정비 이력 데이터를 S3에 적재하고, OpenSearch index와 Bedrock Claude 기반 chatbot agent가 MEL search와 정비 이력 search tool을 호출하는 구조를 소개했다.
- 항공 정비 AI는 hallucination이 안전 리스크가 되므로 신뢰도 scoring, golden dataset 기반 정기 검증, 직급별 사용 권한과 human final decision 원칙을 세웠다.
- AI OCR은 정비사가 모바일로 종이 문서를 촬영하면 S3에 저장하고 Amazon Textract가 표와 손글씨를 읽어 정비 업무 시스템에 입력하는 흐름으로 설명됐다.
- 네트워크/서버 장애 시를 대비해 원본 종이 문서를 일정 기간 보관하고, 디지털 저장 완료 후 데이터 원장이 원본을 대체한다는 절차도 함께 설계했다.

**AWS/기술 키워드**
- Amazon Bedrock, Claude, Bedrock AgentCore Runtime, AgentCore Gateway, Amazon Neptune, Amazon DynamoDB, Amazon OpenSearch Service, Amazon Textract, Amazon S3, API Gateway, knowledge graph, Cypher, RAG, AI OCR

**현장 메모로 남길 점**
- 하나투어 사례는 “AI에게 긴 텍스트 대신 지도, 즉 도메인 그래프를 주라”는 메시지가 강했다.
- 제주항공/AK아이에스 사례는 기술보다 변화관리와 안전 거버넌스가 중요했다. 정비 현장에서는 AI가 답을 해도 숙련자가 최종 책임을 지는 구조가 필수다.

**블로그용 한줄**
- “하나투어와 AK아이에스는 AI 혁신의 핵심이 모델 호출이 아니라 도메인 데이터를 AI가 믿고 쓸 수 있는 구조로 바꾸는 데 있음을 보여줬다.”
