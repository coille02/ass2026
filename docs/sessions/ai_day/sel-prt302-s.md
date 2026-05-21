# AWS AI와 서버리스로 구축하는 완성차 지능형 상품 전략 플랫폼 (sponsored by 이테크시스템 / ETECH SYSTEM)

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

## 세션 정보

- 시간: 2026-05-21 13:50-14:10 KST
- 트랙: Track 8
- 레벨: 300 - Advanced
- 발표자: 김동희(ETECH SYSTEM)
- 주제: Artificial Intelligence

## 발표 주제

완성차 기업의 PDF/웹 데이터 수집 비효율을 AWS AI와 Serverless로 혁신한 사례를 공유합니다. Bedrock Claude Sonnet 4.5로 차량 정보를 추출하고 S3 Vector 유사도 매핑으로 명칭을 표준화했습니다. Step Functions를 활용한 150개 차종 데이터 지능형 병렬 수집 및 자산화 구현 아키텍처 노하우를 다룹니다.

완성차 기업의 PDF, 웹, 카탈로그 기반 비정형 데이터 수집과 표준화 문제를 AWS AI와 서버리스 아키텍처로 해결한 사례다. Step Functions, EventBridge, Lambda로 수집·크롤링·추출·정규화·저장을 병렬 워크플로우로 만들고, Bedrock 기반 추출과 S3/Glue/Athena 기반 데이터 레이크로 상품 전략 데이터를 자산화했다.

## 주요 내용

- 외부 웹/PDF 데이터는 형식과 명칭이 제각각이라 키워드 검색만으로는 누락과 중복이 생긴다.
- Bedrock은 비정형 텍스트에서 차량 사양을 JSON 구조로 추출하고, 표준화된 데이터로 변환하는 역할을 맡았다.
- Step Functions는 150개 이상 차종의 월별 업데이트를 병렬 처리하고, 수집 리드타임을 크게 줄였다.
- S3, Glue Data Catalog, Athena, 대시보드로 출처와 무결성을 보존하면서 현업이 직접 분석할 수 있게 했다.

## 세부 내용

### 문제의식과 배경

외부 웹/PDF 데이터는 형식과 명칭이 제각각이라 키워드 검색만으로는 누락과 중복이 생긴다. Bedrock은 비정형 텍스트에서 차량 사양을 JSON 구조로 추출하고, 표준화된 데이터로 변환하는 역할을 맡았다.

### 접근 방식과 아키텍처

Step Functions는 150개 이상 차종의 월별 업데이트를 병렬 처리하고, 수집 리드타임을 크게 줄였다. S3, Glue Data Catalog, Athena, 대시보드로 출처와 무결성을 보존하면서 현업이 직접 분석할 수 있게 했다.

### 운영 포인트와 확장 방향

관련 기술 키워드는 Amazon Bedrock, Claude Sonnet 4.5, AWS Step Functions, Amazon EventBridge, AWS Lambda, Amazon S3, AWS Glue, Athena, S3 Vector, serverless이다.

## 정리

이 세션의 핵심은 AWS AI와 서버리스로 구축하는 완성차 지능형 상품 전략 플랫폼 (sponsored by 이테크시스템 / ETECH SYSTEM)를 단순한 기능 소개가 아니라 실제 업무와 운영 환경에 적용하기 위한 조건으로 풀어냈다는 점이다. 외부 웹/PDF 데이터는 형식과 명칭이 제각각이라 키워드 검색만으로는 누락과 중복이 생긴다.

발표는 AI 활용이 성과로 이어지려면 모델이나 도구 선택뿐 아니라 데이터, 권한, 운영 절차, 관측 가능성을 함께 설계해야 한다는 메시지로 정리된다.
