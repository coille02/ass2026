# sel-prt103-s - MUSINSA - ClickHouse Cloud를 활용한 Audience Engine 및 다각적 비즈니스 확장을 위한 전략 (sponsored by ClickHouse)

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

- 시간/트랙/레벨/발표자: 2026-05-21 15:30-15:50 KST / Track 5 / 100 - Foundational / 이기훈(ClickHouse), 최민영(무신사), 박병길(무신사)
- 요약: 무신사가 AWS 기반 ClickHouse Cloud로 Audience Engine을 구축하고, Vector Search 룩어라이크 타겟팅, OLAP 기반 AI 분석, 실시간 로그 서빙 등으로 데이터 활용 범위를 넓힌 사례다. 발표는 ClickPipes와 Materialized View를 활용해 데이터 파이프라인과 집계 처리를 단순화하고, 셀프호스팅 ClickHouse 운영 부담을 줄이기 위해 ClickHouse Cloud를 검토한 경험을 공유했다. 패션 플랫폼의 고객 세그먼트, 로그, 추천/타겟팅 데이터를 빠르게 분석하는 것이 핵심 가치였다.
- 주요 포인트:
  - Audience Engine은 대규모 고객 행동 데이터를 세그먼트화하고 타겟팅/분석/서빙에 활용하는 데이터 기반이다.
  - ClickPipes와 Materialized View로 실시간성 있는 데이터 적재와 집계를 구성했다.
  - Vector Search를 활용한 룩어라이크 타겟팅과 OLAP 분석을 함께 다루며 AI 활용 범위를 넓혔다.
  - 셀프호스팅 운영 부담을 줄이고 데이터 팀이 제품 가치에 집중하기 위해 ClickHouse Cloud를 선택지로 제시했다.
- AWS/기술 키워드: ClickHouse Cloud, ClickPipes, Materialized View, Vector Search, OLAP, Audience Engine, Real-time Logs, AWS
- AX TF 관점/회사 AX 도입 시사점: AX 서비스가 개인화, 추천, 영업/마케팅 자동화로 확장되려면 빠른 분석 DB와 실시간 이벤트 파이프라인이 필요하다. 기존 DW만으로 어렵다면 ClickHouse류 OLAP/Vector Search 기반을 별도 서빙·분석 계층으로 두는 아키텍처를 검토할 만하다.
- 공유용 한줄: 무신사 사례는 AX 개인화의 기반이 모델만이 아니라, 빠르게 세그먼트화하고 서빙할 수 있는 실시간 분석 엔진임을 보여준다.

### 전사 기반 상세 보강

- 세션 맥락: MUSINSA - ClickHouse Cloud를 활용한 Audience Engine 및 다각적 비즈니스 확장을 위한 전략 (sponsored by ClickHouse)
- 공식 설명 보강: 국내 최대 패션 플랫폼 무신사는 AWS 기반 ClickHouse Cloud의 ClickPipes와 Materialized View로 Audience Engine을 구축했습니다. Vector Search 룩어라이크 타겟팅, OLAP 기반 AI 분석, 실시간 로그 서빙 등 다양한 활용 사례와 데이터 플랫폼 설계 및 도입 과정을 소개합니다.
- 전사에서 반복적으로 확인된 키워드: 데이터, 운영, 비용, 보안, 감사, 비즈니스, 인프라, 로그, 아키텍처, 평가
- 발표에서 두드러진 주제 축: data, ops, governance, security

#### 발표 흐름
- 초반: 데이터, 운영, 비즈니스, 개발, 감사 중심으로 data, ops, security를 다룬다.
- 중반: 운영, 데이터, 비용, 평가, S3 중심으로 data, ops, governance를 다룬다.
- 후반: 비용, 운영, 데이터, 보안, 인프라 중심으로 data, ops, governance를 다룬다.

#### 전사에서 확인할 만한 구간
- 00:23 부근: 로그 관련 설명이 나온다. 핵심 문맥은 `백터 썼지 루거라이크 타게팅, 오랫기반 AI 분석, 실시간 로그 서빙 등`
- 05:49 부근: 운영 관련 설명이 나온다. 핵심 문맥은 `채널을 또 운영하고 있습니다.`
- 05:57 부근: 운영 관련 설명이 나온다. 핵심 문맥은 `CDP 플랫폼 운영하면서 고민 중에 하나가`
- 10:42 부근: 비용, 운영 관련 설명이 나온다. 핵심 문맥은 `운영적인 효율이나 비용적으로 저희가 절감을 많이 할 수 있었고요.`
- 18:50 부근: 데이터, 비용 관련 설명이 나온다. 핵심 문맥은 `원래 사용하던 데이터를 보관하던 비용에`
