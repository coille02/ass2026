# MUSINSA - ClickHouse Cloud를 활용한 Audience Engine 및 다각적 비즈니스 확장을 위한 전략 (sponsored by ClickHouse)

[AI Day 세션 목록으로 돌아가기](../../ai_day_sessions.md)

## 세션 정보

- 시간: 2026-05-21 15:30-15:50 KST
- 트랙: Track 5
- 분류: 레벨: 100 - Foundational, 산업: Financial Services, 산업: Retail & Consumer Goods, 산업: Software & Internet, 주제: Analytics, 주제: Artificial Intelligence, 주제: Databases
- 발표자: 이기훈(ClickHouse), 최민영(무신사), 박병길(무신사)

## 발표 주제

국내 최대 패션 플랫폼 무신사는 AWS 기반 ClickHouse Cloud의 ClickPipes와 Materialized View로 Audience Engine을 구축했습니다.

Vector Search 룩어라이크 타겟팅, OLAP 기반 AI 분석, 실시간 로그 서빙 등 다양한 활용 사례와 데이터 플랫폼 설계 및 도입 과정을 소개합니다.

## 주요 내용

- Audience Engine은 대규모 고객 행동 데이터를 세그먼트화하고 타겟팅/분석/서빙에 활용하는 데이터 기반이다.
- ClickPipes와 Materialized View로 실시간성 있는 데이터 적재와 집계를 구성했다.
- Vector Search를 활용한 룩어라이크 타겟팅과 OLAP 분석을 함께 다루며 AI 활용 범위를 넓혔다.
- 셀프호스팅 운영 부담을 줄이고 데이터 팀이 제품 가치에 집중하기 위해 ClickHouse Cloud를 선택지로 제시했다.
- 주요 기술과 키워드는 ClickHouse Cloud, ClickPipes, Materialized View, Vector Search, OLAP, Audience Engine, Real-time Logs, AWS 중심으로 정리됐다.

## 세부 내용

### 배경과 문제 인식

국내 최대 패션 플랫폼 무신사는 AWS 기반 ClickHouse Cloud의 ClickPipes와 Materialized View로 Audience Engine을 구축했습니다. Vector Search 룩어라이크 타겟팅, OLAP 기반 AI 분석, 실시간 로그 서빙 등 다양한 활용 사례와 데이터 플랫폼 설계 및 도입 과정을 소개합니다.

발표는 이 배경에서 출발해 실제 서비스나 운영 환경에서 어떤 제약이 있었고, 이를 해결하기 위해 어떤 기술 선택과 구현 방식을 택했는지를 설명했다. 단순한 기능 소개보다 현장에서 마주한 병목, 데이터 흐름, 운영 책임을 어떻게 정리했는지가 핵심 맥락이다.

### 구현 접근

- Audience Engine은 대규모 고객 행동 데이터를 세그먼트화하고 타겟팅/분석/서빙에 활용하는 데이터 기반이다.
- ClickPipes와 Materialized View로 실시간성 있는 데이터 적재와 집계를 구성했다.
- Vector Search를 활용한 룩어라이크 타겟팅과 OLAP 분석을 함께 다루며 AI 활용 범위를 넓혔다.
- 셀프호스팅 운영 부담을 줄이고 데이터 팀이 제품 가치에 집중하기 위해 ClickHouse Cloud를 선택지로 제시했다.
- 구현을 설명하는 축은 ClickHouse Cloud, ClickPipes, Materialized View, Vector Search, OLAP, Audience Engine, Real-time Logs, AWS 등으로 요약할 수 있다.

### 운영과 확장 관점

- 발표의 초점은 기술 도입 자체보다 반복 가능한 운영 방식, 검증 가능한 성과, 이후 확장 가능한 구조를 만드는 데 있었다.
- 발표에서 남길 만한 메시지는 무신사 사례는 AX 개인화의 기반이 모델만이 아니라, 빠르게 세그먼트화하고 서빙할 수 있는 실시간 분석 엔진임을 보여준다.

## 정리

이 세션은 MUSINSA - ClickHouse Cloud를 활용한 Audience Engine 및 다각적 비즈니스 확장을 위한 전략 (sponsored by ClickHouse) 이라는 주제를 통해, 실제 산업 현장에서 AWS와 AI/클라우드 기술을 어떻게 서비스 개선과 운영 효율로 연결했는지를 보여줬다. 핵심은 새로운 도구의 나열이 아니라 문제를 정의하고, 데이터와 아키텍처를 정리하며, 운영자가 신뢰할 수 있는 방식으로 결과를 만드는 과정에 있었다.
