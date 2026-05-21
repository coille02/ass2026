# sel-ind211 - [바비톡] 바비톡의 AX여정: 에이전틱 AI로 K-beauty를 바꾸다

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

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

### 전사 기반 상세 보강

- 세션 맥락: [바비톡] 바비톡의 AX여정: 에이전틱 AI로 K-beauty를 바꾸다
- 공식 설명 보강: 1,000만 유저의 바비톡은 AI 특공대와 Monthly PoC로 AX를 추진하고 있습니다. 본 세션에서는 Amazon Bedrock 기반 K-Beauty 어시스턴트 등 Agentic AI 도입 사례와, AI-DLC(AI Development Life Cycle)를 사용해 마케팅팀과 개발팀 협업 모델 변화를 통한 개발 문화 및 생산성 혁신 경험을 공유합니다.
- 전사에서 반복적으로 확인된 키워드: 에이전트, 개발, 운영, 비용, 워크플로, 코드, 비즈니스, 배포, 감사, 추천
- 발표에서 두드러진 주제 축: agent, developer, business, governance

#### 발표 흐름
- 초반: 에이전트, 개발, 비용, 운영, 비즈니스 중심으로 agent, developer, business를 다룬다.
- 중반: 에이전트, 개발, 운영, 비용, 상담 중심으로 agent, developer, business를 다룬다.
- 후반: 에이전트, 개발, 워크플로, 코드, 배포 중심으로 agent, developer, business를 다룬다.

#### 전사에서 확인할 만한 구간
- 02:37 부근: 개발, 에이전트 관련 설명이 나온다. 핵심 문맥은 `에이전트를 개발하는 것을 넘어서서`
- 06:24 부근: 코드, 테스트, 품질 관련 설명이 나온다. 핵심 문맥은 `상세 설계를 하고 코드 생성하고 테스트까지 진행하면서 품질까지 높이고 있습니다.`
- 12:08 부근: 비용, 에이전트 관련 설명이 나온다. 핵심 문맥은 `성능과 비용을 체직하기에 여러 에이전트로`
- 15:34 부근: 비용, 전략 관련 설명이 나온다. 핵심 문맥은 `모델 교체 유지보수 비용을 전략할 수 있었습니다`
- 21:28 부근: 개발, 품질 관련 설명이 나온다. 핵심 문맥은 `그래서 소프트웨어 개발에 속도가 빨라지고 품질 또한 더 높아지고 있습니다.`

### 직접 들은 뒤 메모

바비톡의 AX 여정은 작게 만들고 빠르게 검증하는 방식이 가장 기억에 남았다. 처음부터 거대한 플랫폼을 만들기보다 리뷰 검수, 검색, 상담, 여행 가이드처럼 실제 고객 문제와 내부 업무 문제를 하나씩 풀어가며 에이전트를 키웠다. AI를 유행처럼 붙인 것이 아니라, 비즈니스 문제를 정하고 그 문제를 해결하는 pocket service를 빠르게 실험하는 방식이었다.

우리 회사에서도 AX TF가 처음부터 완성형 플랫폼을 목표로 잡으면 속도가 느려질 수 있다. 고객센터 상담 보조, 가맹점 문의 분류, 내부 정책 검색, 장애 회고 초안, 개발자 업무 보조처럼 효과가 보이는 작은 단위부터 시작하는 것이 현실적이다. 작은 성공이 쌓여야 스킬허브와 Agent Builder의 요구사항도 구체화된다.
