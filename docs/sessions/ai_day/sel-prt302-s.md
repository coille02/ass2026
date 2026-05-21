# sel-prt302-s - AWS AI와 서버리스로 구축하는 완성차 지능형 상품 전략 플랫폼 (sponsored by 이테크시스템 / ETECH SYSTEM)

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

- 시간/트랙/레벨/발표자: 13:50-14:10 KST / Partner Track / 300 Advanced / 김동희(ETECH SYSTEM)
- 요약: 완성차 기업의 PDF, 웹, 카탈로그 기반 비정형 데이터 수집과 표준화 문제를 AWS AI와 서버리스 아키텍처로 해결한 사례다. Step Functions, EventBridge, Lambda로 수집·크롤링·추출·정규화·저장을 병렬 워크플로우로 만들고, Bedrock 기반 추출과 S3/Glue/Athena 기반 데이터 레이크로 상품 전략 데이터를 자산화했다.
- 주요 포인트:
  - 외부 웹/PDF 데이터는 형식과 명칭이 제각각이라 키워드 검색만으로는 누락과 중복이 생긴다.
  - Bedrock은 비정형 텍스트에서 차량 사양을 JSON 구조로 추출하고, 표준화된 데이터로 변환하는 역할을 맡았다.
  - Step Functions는 150개 이상 차종의 월별 업데이트를 병렬 처리하고, 수집 리드타임을 크게 줄였다.
  - S3, Glue Data Catalog, Athena, 대시보드로 출처와 무결성을 보존하면서 현업이 직접 분석할 수 있게 했다.
- AWS/기술 키워드: Amazon Bedrock, Claude Sonnet 4.5, AWS Step Functions, Amazon EventBridge, AWS Lambda, Amazon S3, AWS Glue, Athena, S3 Vector, serverless
- AX TF 관점/회사 AX 도입 시사점: 외부 PDF/웹 기반 리서치 업무는 AX 우선 후보가 될 수 있다. 단순 크롤링보다 출처 추적, 표준 명칭 매핑, JSON 스키마화, 오류율 모니터링을 포함해야 실무 의사결정에 쓸 수 있다.
- 공유용 한줄: 비정형 데이터 자동화의 가치는 수집 속도보다 표준화와 출처 검증에서 나온다.

### 직접 들은 뒤 메모

완성차 지능형 상품 전략 플랫폼 세션은 AI와 서버리스가 업무 의사결정 플랫폼으로 연결되는 모습을 보여줬다. 자동차 상품 전략이라는 도메인은 다르지만, 여러 데이터 소스를 묶어 시장 변화와 상품 전략을 빠르게 분석한다는 구조는 핀테크에도 맞다. 카카오페이에서는 금융 상품, 혜택, 가맹점, 사용자 행동, 리스크 지표를 연결해 상품/마케팅/제휴 담당자가 직접 탐색할 수 있는 내부 전략 에이전트로 확장해볼 수 있다.
