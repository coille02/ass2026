# sel-wps201 - 규제 환경에서의 통제 가능한 AI 에이전트 아키텍처

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

**title/time/track/speakers**  
- 제목: 규제 환경에서의 통제 가능한 AI 에이전트 아키텍처
- 시간: 2026-05-20 16:10-16:50 KST
- 트랙: AWS Summit Seoul - Track 9
- 발표자: 최인영(시니어 솔루션즈 아키텍트 매니저, AWS)

**핵심 요약**  
이 세션은 공공, 헬스케어 등 규제 환경에서 AI 에이전트를 도입할 때 개인정보, 분리, 감사 대응을 어떻게 아키텍처에 내재화할지 설명했다. 발표자는 AI 에이전트의 자율성이 생산성을 높이지만 동시에 규제 리스크를 키우므로, 거버넌스를 체크리스트가 아니라 설계 입력값으로 봐야 한다고 강조했다. Bedrock 기반 관리형 접근과 EKS 기반 셀프 매니지드 접근을 비교하며, 운영 부담을 줄일지 세밀한 통제권을 확보할지에 따라 선택이 달라진다고 정리했다. 모델 입출력은 Bedrock Guardrails로, 에이전트 행동은 AgentCore Policy로 통제하는 이중 구조가 핵심이었다.

**주요 포인트**
- 규제 환경의 AI 논의는 개인정보, 분리, 감사로 귀결되며 이를 피하는 것이 아니라 설계 요구사항으로 받아들여야 한다.
- 고영향 AI는 설명 가능성, 사람의 개입, 위험관리체계, 활용 고지 등을 아키텍처에 반영해야 한다.
- Bedrock 관리형 접근은 배포와 운영 부담을 줄이고, EKS 셀프 매니지드 접근은 모델/인프라 통제권을 더 세밀하게 제공한다.
- Bedrock은 고객 데이터가 모델 학습에 사용되지 않는다는 점, 고객 간 데이터 격리, 리전 선택을 통한 데이터 레지던시를 기반으로 제시했다.
- Cross-account Bedrock Guardrails와 AgentCore Policy를 통해 조직 전체의 모델 호출과 에이전트 행동 규칙을 중앙에서 강제할 수 있다.

**AWS/기술 키워드**  
Amazon Bedrock, Amazon EKS, Bedrock Guardrails, Cross-account Guardrails, Bedrock AgentCore Runtime, AgentCore Identity, AgentCore Policy, Strands Agents, MCP, API, Governance, Data Residency

**현장 메모로 남길 점**  
세션의 핵심은 “책임질 수 있는 에이전트”다. 규제 대응을 문서 작업으로 따로 떼지 않고, 모델 입출력/행동 권한/운영 검증을 아키텍처 계층으로 표현하면 좋다.

**블로그용 한줄**  
규제 환경의 AI 에이전트는 더 똑똑한 답보다, 누가 무엇을 왜 했는지 증명할 수 있는 설계가 먼저다.
