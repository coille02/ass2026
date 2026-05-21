# sel-prt214-s - 책임감 없는 AI에이전트, 주인은 누구인가 (sponsored by Datadog)

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

- 제목: 책임감 없는 AI에이전트, 주인은 누구인가 (sponsored by Datadog)
- 시간: 2026-05-20 13:50-14:10 KST
- 트랙: AWS Summit Seoul - Track 1
- 발표자: Mark Hyeonbeom Park(Datadog)

### 핵심 요약

Datadog 세션은 AI 에이전트가 업무 효율을 높이는 동시에 책임 소재와 승인 체계를 흐릴 수 있다는 문제를 다뤘다. 발표자는 기업의 AI 활용이 이미 사람을 대신해 의사결정과 실행에 들어서고 있지만, AI의 판단도 결국 조직이 책임져야 한다는 사례를 소개했다. 그래서 AI를 사람을 대체하는 존재가 아니라 업무를 돕는 도구로 재정의하고, 실행 전 승인과 관찰 가능한 텔레메트리를 갖춘 구조가 필요하다고 설명했다. Datadog Agent Builder는 Datadog 콘솔 안에서 액션, 스킬, 트리거, 외부 시스템 연동, human-in-the-loop 승인을 구성하는 방식으로 제시됐다.

### 주요 포인트

- AI 에이전트는 이미 업무 자동화와 의사결정에 들어왔지만, 잘못된 액션의 책임은 AI가 아니라 조직과 사람이 져야 한다.
- 코드/데이터 유출, 잘못된 예약/취소, 승인 없는 자동 실행 등 AI 사용 사례의 리스크를 통해 거버넌스 필요성을 설명했다.
- 에이전트가 실행할 수 있는 액션과 스킬을 제한하고, 실행 전 사람이 확인하는 승인 구조가 핵심이다.
- Datadog Agent Builder는 Datadog 내 텔레메트리뿐 아니라 외부 시스템 데이터까지 참조해 자동화 흐름을 구성할 수 있다고 소개됐다.
- 마지막 메시지는 "AI는 사람을 대체하는 것이 아니라 도와주는 도구"이며, 업무 방식도 그 전제에 맞게 바뀌어야 한다는 점이었다.

### AWS/기술 키워드

AI Agent, Datadog Agent Builder, Observability, Telemetry, Human-in-the-loop, Workflow Automation, Approval Flow, Governance

### 현장 메모로 남길 점

AI 에이전트 도입의 관건은 "무엇을 할 수 있느냐"보다 "무엇을 하면 안 되는지와 누가 승인하는지"를 제품/운영 흐름에 내장하는 것이다.

### 블로그용 한줄

AI 에이전트의 주인은 모델이 아니라, 액션과 책임을 설계하는 사람과 조직이다.
