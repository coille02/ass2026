# sel-dev308 - [미러] 맥 미니 없이도 서버리스로 만드는 AI Cloud Agent

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

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
