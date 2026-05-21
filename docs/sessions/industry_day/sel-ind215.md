# sel-ind215 - [야놀자] Multi-Agent로 AIOps를 혁신하다: 야놀자의 Bedrock AgentCore 구축 사례

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

**title/time/track/speakers**  
- 제목: [야놀자] Multi-Agent로 AIOps를 혁신하다: 야놀자의 Bedrock AgentCore 구축 사례
- 시간: 2026-05-20 16:10:23-16:50:23 KST
- 트랙: AWS Summit Seoul - Track 4
- 발표자: 조현수(솔루션즈 아키텍트, AWS), 신철우(Intelligent Platform Engineering 팀장, 야놀자), 이진태(Intelligent Platform Engineering 팀원, 야놀자)

**핵심 요약**  
야놀자는 글로벌 여행 플랫폼 운영 복잡성을 줄이기 위해 도메인별 전문 에이전트와 코어 에이전트를 조합한 멀티 에이전트 AIOps 플랫폼 “VITA” 구축 사례를 공유했다. AWS 파트에서는 목표, 도구, 컨텍스트를 기반으로 생각-행동-관찰 루프를 반복하는 에이전트 개념과 Strands Agents, Bedrock AgentCore를 소개했다. 야놀자는 반복 인프라 문의, 비용 분석, 장애 대응 같은 단일 에이전트 패턴에서 출발했지만 확장성 문제에 부딪혔고, 코어 에이전트가 전문 도메인 에이전트를 찾아 위임하는 구조로 전환했다. AgentCore Gateway와 A2A 스펙을 활용해 인증, 연결, 도구 품질, 에이전트 확장을 표준화한 점이 핵심이었다.

**주요 포인트**
- 야놀자의 글로벌 인프라 조직은 서비스 규모가 커지지만 운영 인력은 제한적이어서 지능형 운영 전환이 필요했다.
- VITA는 사내 메신저, 개발자 포털, 알림, 웹훅 등 다양한 입력 채널을 게이트웨이에서 통합한다.
- 코어 에이전트는 문제를 해석하고 실행 계획을 세운 뒤, 에이전트 레지스트리의 에이전트 카드를 보고 적절한 도메인 에이전트에 위임한다.
- A2A 프로토콜과 에이전트 카드로 역할, 능력, 입출력, 수행 조건을 표준화했다.
- AgentCore Gateway로 MCP, 서드파티 API, Lambda 기반 커스텀 도구의 인증과 연결 관리를 중앙화했다.

**AWS/기술 키워드**  
Amazon Bedrock AgentCore, Strands Agents, AgentCore Gateway, A2A Protocol, Agent Card, MCP, Lambda, Multi-Agent, AIOps, VITA, Domain Agent, Core Agent

**현장 메모로 남길 점**  
좋은 결론은 “에이전트는 혼자 일하지 않는다”였다. 멀티 에이전트의 성패는 모델보다 역할 경계, 위임 방식, 도구 표준화, 인증/연결 관리에 달려 있다는 방향으로 정리하면 좋다.

**블로그용 한줄**  
야놀자의 VITA는 AIOps 에이전트를 하나 더 만드는 것이 아니라, 에이전트들이 역할을 나누고 함께 운영되는 플랫폼을 만드는 이야기였다.
