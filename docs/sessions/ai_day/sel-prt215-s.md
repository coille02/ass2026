# sel-prt215-s - Unlocking Cost-Efficient Cloud and AI Performance on AWS with AMD EPYC (sponsored by AMD)

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

- 시간/트랙/레벨/발표자: 13:50-14:10 KST / Partner Track / 200 Intermediate / 송성운(AMD Korea)
- 요약: AMD EPYC 기반 AWS EC2 인스턴스가 클라우드와 AI 워크로드에서 성능과 비용 효율을 제공하는 방식을 소개했다. 최신 M8a, C8a, R8a 계열과 데이터베이스, AI 추론, HPC, 미디어 처리 워크로드 사례를 통해 CPU 기반 AI 추론과 범용 워크로드 최적화 포인트를 설명했다.
- 주요 포인트:
  - AI 워크로드가 모두 GPU만 필요한 것은 아니며, CPU 기반 추론과 전처리·데이터 처리도 비용 최적화 여지가 크다.
  - C8a는 전세대 대비 처리시간 개선, M8a는 여러 워크로드에서 실행 성능 향상과 비용 절감 사례를 강조했다.
  - PostgreSQL 등 데이터베이스 워크로드에서는 인스턴스 크기와 CPU 특성 선택이 TCO에 직접 영향을 준다.
  - Netflix, Pinterest 등 사례를 통해 성능 예측성과 비용 대비 성능을 강조했다.
- AWS/기술 키워드: AMD EPYC, Amazon EC2, M8a, C8a, R8a, PostgreSQL, CPU inference, HPC, TCO, workload optimization
- AX TF 관점/회사 AX 도입 시사점: AX 인프라 비용 최적화는 GPU만 보지 말고 CPU 추론, 임베딩 전처리, ETL, 벡터 구축, 데이터베이스까지 워크로드별 인스턴스 벤치마크가 필요하다.
- 공유용 한줄: AI 비용 최적화는 GPU 구매 전략이 아니라 워크로드별 컴퓨트 선택 전략이다.
