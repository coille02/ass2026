# sel-prt208-s - 다운타임 0의 도전: Agentic AI와 Bedrock으로 완성하는 자율 예지정비 (sponsored by (주)두산 디지털이노베이션BU, Doosan Corporation Digital Innovation BU)

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

- 제목: 다운타임 0의 도전: Agentic AI와 Bedrock으로 완성하는 자율 예지정비 (sponsored by 두산 디지털이노베이션BU)
- 시간: 2026-05-20 13:50-14:10 KST
- 트랙: AWS Summit Seoul - Track 5
- 발표자: 김성진(수석, 두산 디지털이노베이션BU)

### 핵심 요약

두산 DDI 세션은 제조 설비의 다운타임을 줄이기 위한 예지정비를 Agentic AI와 Amazon Bedrock으로 확장한 사례를 소개했다. 기존 예지정비는 센서 데이터, 표준 알고리즘, 전문가 분석에 기반했지만 현장 환경이 바뀌면 고정된 진단 룰이 한계를 보인다. 발표자는 IoT Core로 수신한 데이터를 S3에 저장하고 분석/리포트 흐름을 구성한 뒤, Bedrock 기반 에이전트가 과거 데이터와 진단 기준을 참고해 이상을 분석하고 진단 룰 개선을 추천하는 구조를 설명했다. 단, AI가 바로 운영 룰을 바꾸는 것이 아니라 전문가 승인 후 시스템에 반영되는 폐쇄 루프를 제시했다.

### 주요 포인트

- 예지정비는 설비 다운 전에 고장 가능성을 예측해 생산량, 품질, 운영 안정성 영향을 줄이는 솔루션이다.
- DDI는 진동/온도 기반 데이터, IoT 프로젝트, 데이터 분석, 진단 알고리즘 경험을 제조 솔루션으로 축적해왔다.
- 기존 ISO 20816 기반 규칙과 경험 기반 분석에 생성형 AI 진단/추천을 결합하는 방향으로 확장했다.
- Agentic AI는 진단 룰로 잡히지 않는 데이터나 적중률이 떨어지는 룰을 찾아 개선안을 생성하고, 사용자 승인 후 반영한다.
- 목표는 "다운타임 0"에 가까워지는 지능형 루프이며, 자연어 질의/리포트/정비 일정/부품 추천까지 연결 가능성을 보여줬다.

### AWS/기술 키워드

Amazon Bedrock, AWS IoT Core, Amazon S3, Agentic AI, Predictive Maintenance, ISO 20816, Sensor Data, Diagnostic Rules, Human Approval Loop

### 현장 메모로 남길 점

제조 AI의 가치는 자동 판단 자체보다 현장 전문가의 승인과 축적 데이터로 진단 룰을 계속 개선하는 운영 루프에서 나온다.

### 블로그용 한줄

예지정비의 다음 단계는 고정 룰을 넘어, 설비 데이터로 스스로 개선안을 제안하는 Agentic AI 루프다.
