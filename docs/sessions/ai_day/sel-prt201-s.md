# sel-prt201-s - SK AX가 구현한 SageMaker 기반 분석가와 현업의 통합 AI 환경 (sponsored by SK AX)

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

- 시간/트랙/레벨/발표자: 13:50-14:10 KST / Partner Track / 200 Intermediate / 조진선(SK AX)
- 요약: SK Innovation E&S의 통합 데이터·AI 플랫폼 구축 사례를 통해 AI 실패의 본질을 데이터 사일로, 현업 접근성 부족, 불안한 보안/비용 구조에서 찾았다. 3-Layer 레이크하우스, 비즈니스 메타데이터 카탈로그, Bedrock 기반 메타데이터 검색, SageMaker Unified Studio로 분석가와 현업이 함께 쓰는 환경을 구성했다.
- 주요 포인트:
  - AI 프로젝트가 실패하는 이유는 모델보다 데이터에 닿지 못하는 구조인 경우가 많다.
  - Lake, DW, Mart 계층으로 원천 데이터, 정제/실험 데이터, LLM·BI 활용 데이터를 구분했다.
  - IT 메타데이터와 비즈니스 메타데이터를 분리해 현업이 IT 용어 없이 데이터를 찾을 수 있게 했다.
  - Lake Formation 기반 권한관리와 SageMaker Unified Studio로 데이터 엔지니어, 분석가, 현업의 작업 환경을 통합했다.
- AWS/기술 키워드: Amazon SageMaker Unified Studio, Amazon Bedrock Knowledge Bases, AWS Lake Formation, Amazon S3, AWS Glue, Athena, lakehouse, metadata catalog
- AX TF 관점/회사 AX 도입 시사점: 사내 AX 플랫폼은 “챗봇”보다 데이터 탐색성과 권한 거버넌스가 먼저다. 현업 용어 기반 메타데이터와 AI 검색을 제공해야 분석/GenAI 활용률이 올라간다.
- 공유용 한줄: AI 활용률은 모델 성능보다 현업이 안전하게 데이터를 찾고 쓸 수 있는 구조에서 갈린다.
