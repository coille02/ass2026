# sel-dvt305 - Nova Act & Strands Agent 실전: AI 에이전트로 개발 워크플로 자동화하기

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

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
