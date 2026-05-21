# sel-dev307 - Kiro Spec 모드 가속 가이드 & 서버리스 CDC 레이크하우스

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

- 시간/트랙/레벨/발표자: 12:50-13:30 KST / Track 9, AI·Databases / 300 Advanced / 최지연(AWSKRUG), 강은호(스테이지랩스)
- 요약: 1부는 Kiro Spec Mode를 BDD와 FSD 구조에 결합해 LLM 컨텍스트를 격리하고 코드 구조 붕괴를 줄이는 사례를 소개했다. 2부는 AWS DMS Serverless, S3, Glue, Iceberg를 활용해 Aurora PostgreSQL의 변경 데이터를 CDC 방식으로 적재하는 서버리스 레이크하우스 구축 경험을 공유했다.
- 주요 포인트:
  - Kiro Spec Mode는 requirements, design, task 단계로 “무엇을 만들지”를 계약처럼 고정한다.
  - BDD 시나리오로 행동 기준을 명시하고 FSD 폴더 구조로 코드 위치를 강제하면 AI가 임의 구조를 만들 가능성이 줄어든다.
  - CDC 레이크하우스는 DMS Serverless로 변경 데이터를 S3에 적재하고, Glue/Iceberg로 최신 상태를 관리하는 구조다.
  - 백필, 신규 테이블 추가, CDC 파일 분류, PK 조합, 최신값 유지 같은 운영 설계가 실제 성공을 좌우한다.
- AWS/기술 키워드: Kiro Spec Mode, BDD, Cucumber, FSD, AWS DMS Serverless, Amazon S3, AWS Glue, Apache Iceberg, CDC, Aurora PostgreSQL
- AX TF 관점/회사 AX 도입 시사점: AI 코딩 표준에는 “스펙 문서”와 “폴더/아키텍처 경계”를 같이 넣어야 한다. 데이터 AX 과제는 배치성 데이터마트보다 CDC 기반의 최신 데이터 자산화 패턴을 우선 검토할 만하다.
- 공유용 한줄: 좋은 AI 코드 품질은 좋은 스펙과 강제된 구조에서 나온다.

### 전사 기반 상세 보강

- 세션 맥락: Kiro Spec 모드 가속 가이드 & 서버리스 CDC 레이크하우스
- 공식 설명 보강: 모호한 요구사항은 AI의 계층 침범과 구조 붕괴를 야기합니다. 본 세션은 Kiro Spec Mode를 '단일 계약 소스'로 정의하고, BDD의 행동 계약과 FSD 구조를 결합해 LLM의 컨텍스트를 격리한 사례를 공유합니다. 이어서, AWS DMS, AWS Glue, Iceberg — 서버리스로 만드는 CDC 레이크하우스를 구축한 실전 이야기를 소개합니다.
- 전사에서 반복적으로 확인된 키워드: 데이터, 개발, 운영, 코드, S3, 비용, 에이전트, 로그, 아키텍처, 테스트
- 발표에서 두드러진 주제 축: data, developer, ops, governance

#### 발표 흐름
- 초반: 개발, 코드, 운영, 아키텍처, 테스트 중심으로 data, developer, ops를 다룬다.
- 중반: 데이터, 운영, 개발, 코드, 아키텍처 중심으로 data, developer, ops를 다룬다.
- 후반: 데이터, 에이전트, S3, 비용, IaC 중심으로 data, developer, ops를 다룬다.

#### 전사에서 확인할 만한 구간
- 06:15 부근: 코드, 테스트 관련 설명이 나온다. 핵심 문맥은 `이를 코드와 테스트를 연결하는 방식입니다.`
- 19:40 부근: Glue, S3 관련 설명이 나온다. 핵심 문맥은 `A2bless DNS, Amazon S3, A2bless Glue,`
- 20:08 부근: 데이터, 운영 관련 설명이 나온다. 핵심 문맥은 `AI가 자율적으로 작성한 SQL를 과연 운영 데이터 베이스에서`
- 29:03 부근: 개발, 코드 관련 설명이 나온다. 핵심 문맥은 `개발자는 그냥 파이 스파크 그리고 스칼라로 코드를 작성해서 제출만 해줘면 되죠.`
- 29:09 부근: 데이터, 카탈로그 관련 설명이 나온다. 핵심 문맥은 `두 번째는 글로 데이터 카탈로그입니다.`
