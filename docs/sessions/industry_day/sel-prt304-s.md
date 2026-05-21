# sel-prt304-s - Agentic 시대에 필요한 machine data 관리 전략 (sponsored by Splunk)

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

- 제목: Agentic 시대에 필요한 machine data 관리 전략 (sponsored by Splunk)
- 시간: 2026-05-20 13:50-14:10 KST
- 트랙: AWS Summit Seoul - Track 6
- 발표자: 김현준(전무, Splunk)

### 핵심 요약

Splunk 세션은 Agentic AI의 성패가 모델이나 GPU만이 아니라 AI가 읽을 수 있는 machine data 통합에 달려 있다고 설명했다. 발표자는 로그, 트레이스, 메트릭 같은 운영 데이터를 machine data로 정의하고, 에이전트가 장애 원인과 영향도를 판단하려면 이 데이터가 정상적으로 수집, 검색, 연결돼야 한다고 강조했다. 기업들은 AI를 도입하면서도 보안/개발/운영 도메인별로 데이터가 흩어져 있어 문제가 보안 이슈인지 시스템 이슈인지 빠르게 판단하기 어렵다. Splunk는 schema-on-read, SPL, Cisco Data Fabric, machine data lake 등을 통해 데이터 위치와 형식이 달라도 분석 가능한 구조를 제안했다.

### 주요 포인트

- AI 에이전트가 정상적으로 의사결정하려면 로그, 메트릭, 트레이스 등 machine data를 볼 수 있어야 한다.
- Kubernetes 노드나 VPC Flow Logs처럼 현대 인프라는 막대한 로그를 생성하지만, 이를 AI가 활용 가능한 상태로 관리하는 조직은 제한적이다.
- 보안, 애플리케이션, 개발, 운영 데이터가 도메인별로 분리되면 장애 원인과 영향도 판단이 느려진다.
- Splunk의 schema-on-read는 먼저 저장하고 필요할 때 스키마를 적용해 다양한 형식의 machine data에서 인사이트를 뽑는 접근이다.
- Cisco Data Fabric과 machine data lake는 S3, Snowflake, Databricks 등 데이터 위치와 무관하게 분석/렌딩/검색할 수 있는 구조로 소개됐다.

### AWS/기술 키워드

Splunk, Machine Data, Logs, Metrics, Traces, Schema-on-read, SPL, Cisco Data Fabric, Machine Data Lake, Amazon S3, VPC Flow Logs, Kubernetes Logs

### 현장 메모로 남길 점

Agentic AI를 운영에 쓰려면 먼저 데이터 통합과 관찰 가능성이 되어 있어야 하며, "AI가 볼 수 없는 데이터"는 곧 "AI가 판단할 수 없는 업무"가 된다.

### 블로그용 한줄

에이전트 시대의 숨은 인프라는 GPU가 아니라 로그, 메트릭, 트레이스를 연결하는 machine data 전략이다.
