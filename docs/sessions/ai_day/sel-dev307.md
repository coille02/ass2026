# Kiro Spec 모드 가속 가이드 & 서버리스 CDC 레이크하우스

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

## 세션 정보

- 시간: 2026-05-21 12:50-13:30 KST
- 트랙: Track 9
- 분류: 레벨: 300 - Advanced, 주제: Artificial Intelligence, 주제: Databases
- 발표자: 최지연(AWSKRUG), 강은호(스테이지랩스)

## 발표 주제

모호한 요구사항은 AI의 계층 침범과 구조 붕괴를 야기합니다.

본 세션은 Kiro Spec Mode를 '단일 계약 소스'로 정의하고, BDD의 행동 계약과 FSD 구조를 결합해 LLM의 컨텍스트를 격리한 사례를 공유합니다. 이어서, AWS DMS, AWS Glue, Iceberg — 서버리스로 만드는 CDC 레이크하우스를 구축한 실전 이야기를 소개합니다.

## 주요 내용

- Kiro Spec Mode는 requirements, design, task 단계로 “무엇을 만들지”를 계약처럼 고정한다.
- BDD 시나리오로 행동 기준을 명시하고 FSD 폴더 구조로 코드 위치를 강제하면 AI가 임의 구조를 만들 가능성이 줄어든다.
- CDC 레이크하우스는 DMS Serverless로 변경 데이터를 S3에 적재하고, Glue/Iceberg로 최신 상태를 관리하는 구조다.
- 백필, 신규 테이블 추가, CDC 파일 분류, PK 조합, 최신값 유지 같은 운영 설계가 실제 성공을 좌우한다.
- 주요 기술과 키워드는 Kiro Spec Mode, BDD, Cucumber, FSD, AWS DMS Serverless, Amazon S3, AWS Glue, Apache Iceberg, CDC, Aurora PostgreSQL 중심으로 정리됐다.

## 세부 내용

### 배경과 문제 인식

모호한 요구사항은 AI의 계층 침범과 구조 붕괴를 야기합니다. 본 세션은 Kiro Spec Mode를 '단일 계약 소스'로 정의하고, BDD의 행동 계약과 FSD 구조를 결합해 LLM의 컨텍스트를 격리한 사례를 공유합니다. 이어서, AWS DMS, AWS Glue, Iceberg — 서버리스로 만드는 CDC 레이크하우스를 구축한 실전 이야기를 소개합니다.

발표는 이 배경에서 출발해 실제 서비스나 운영 환경에서 어떤 제약이 있었고, 이를 해결하기 위해 어떤 기술 선택과 구현 방식을 택했는지를 설명했다. 단순한 기능 소개보다 현장에서 마주한 병목, 데이터 흐름, 운영 책임을 어떻게 정리했는지가 핵심 맥락이다.

### 구현 접근

- Kiro Spec Mode는 requirements, design, task 단계로 “무엇을 만들지”를 계약처럼 고정한다.
- BDD 시나리오로 행동 기준을 명시하고 FSD 폴더 구조로 코드 위치를 강제하면 AI가 임의 구조를 만들 가능성이 줄어든다.
- CDC 레이크하우스는 DMS Serverless로 변경 데이터를 S3에 적재하고, Glue/Iceberg로 최신 상태를 관리하는 구조다.
- 백필, 신규 테이블 추가, CDC 파일 분류, PK 조합, 최신값 유지 같은 운영 설계가 실제 성공을 좌우한다.
- 구현을 설명하는 축은 Kiro Spec Mode, BDD, Cucumber, FSD, AWS DMS Serverless, Amazon S3, AWS Glue, Apache Iceberg, CDC, Aurora PostgreSQL 등으로 요약할 수 있다.

### 운영과 확장 관점

- 발표의 초점은 기술 도입 자체보다 반복 가능한 운영 방식, 검증 가능한 성과, 이후 확장 가능한 구조를 만드는 데 있었다.
- 발표에서 남길 만한 메시지는 좋은 AI 코드 품질은 좋은 스펙과 강제된 구조에서 나온다.

## 정리

이 세션은 Kiro Spec 모드 가속 가이드 & 서버리스 CDC 레이크하우스 이라는 주제를 통해, 실제 산업 현장에서 AWS와 AI/클라우드 기술을 어떻게 서비스 개선과 운영 효율로 연결했는지를 보여줬다. 핵심은 새로운 도구의 나열이 아니라 문제를 정의하고, 데이터와 아키텍처를 정리하며, 운영자가 신뢰할 수 있는 방식으로 결과를 만드는 과정에 있었다.
