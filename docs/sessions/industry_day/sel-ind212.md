# sel-ind212 - [AB180] AB180이 SaaS 에이전틱 AI를 설계하는 방법

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

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
