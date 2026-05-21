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

### 전사 기반 상세 보강

- 세션 맥락: Unlocking Cost-Efficient Cloud and AI Performance on AWS with AMD EPYC (sponsored by AMD)
- 공식 설명 보강: 본 세션에서는 AMD EPYC 프로세서 기반 AWS EC2 인스턴스를 통해 클라우드 및 AI 워크로드의 성능을 극대화하고 비용을 최적화하는 방법을 소개합니다. 최신 M8a·C8a·R8a 인스턴스와 실제 고객 사례를 통해 데이터베이스, AI 추론, HPC 등 다양한 워크로드에서의 성능 향상과 TCO 절감 전략을 살펴봅니다.
- 전사에서 반복적으로 확인된 키워드: 비용, 테스트, 데이터, GPU, 코드, 보안, 감사, 운영, 추천, 자동화
- 발표에서 두드러진 주제 축: governance, developer, data, business

#### 발표 흐름
- 초반: 비용, GPU, 보안, 자동화, 데이터 중심으로 governance, data, business를 다룬다.
- 중반: 비용, 테스트, 데이터, 비즈니스 중심으로 governance, developer, data를 다룬다.
- 후반: 비용, 테스트, 코드, 데이터, 감사 중심으로 governance, developer, data를 다룬다.

#### 전사에서 확인할 만한 구간
- 00:22 부근: 비용 관련 설명이 나온다. 핵심 문맥은 `오늘 AWS, AINSTANCE, 즉, AMD 인스터를 통해서 성능을 극대화하고 동시에 비용을`
- 05:15 부근: 데이터 관련 설명이 나온다. 핵심 문맥은 `AI 출원, 백터연산, 데이터 분석연산을 가속하는`
- 11:35 부근: 데이터, 추천 관련 설명이 나온다. 핵심 문맥은 `추천, 인코딩, 데이터 처리`
- 15:50 부근: 코드 관련 설명이 나온다. 핵심 문맥은 `때문에 코드 수정이나 컴파일을 다시 할 필요가 없이 그대로 이전이`
- 16:02 부근: 비용 관련 설명이 나온다. 핵심 문맥은 `스타를 단순하게 바꾸고 줄이는 방법으로 비용을`
