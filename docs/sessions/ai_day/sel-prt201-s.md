# SK AX가 구현한 SageMaker 기반 분석가와 현업의 통합 AI 환경 (sponsored by SK AX)

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

## 세션 정보

- 시간: 2026-05-21 13:50-14:10 KST
- 트랙: Track 3
- 레벨: 200 - Intermediate
- 발표자: 조진선(SK AX)
- 주제: Analytics, Architecture, Artificial Intelligence

## 발표 주제

SKI E&S 분석가의 모델 개발과 현업의 GenAI 활용을 위한 통합 데이터 플랫폼 구축 전략을 소개합니다. 국내 최초로 SageMaker Unified Studio를 도입해 데이터와 AI 모델을 통합하고, 3-Layer 레이크하우스와 메타데이터 챗봇을 결합해 현업이 필요한 데이터를 스스로 탐색, 분석할 수 있는 Self-Service환경을 구현했습니다.

SK Innovation E&S의 통합 데이터·AI 플랫폼 구축 사례를 통해 AI 실패의 본질을 데이터 사일로, 현업 접근성 부족, 불안한 보안/비용 구조에서 찾았다. 3-Layer 레이크하우스, 비즈니스 메타데이터 카탈로그, Bedrock 기반 메타데이터 검색, SageMaker Unified Studio로 분석가와 현업이 함께 쓰는 환경을 구성했다.

## 주요 내용

- AI 프로젝트가 실패하는 이유는 모델보다 데이터에 닿지 못하는 구조인 경우가 많다.
- Lake, DW, Mart 계층으로 원천 데이터, 정제/실험 데이터, LLM·BI 활용 데이터를 구분했다.
- IT 메타데이터와 비즈니스 메타데이터를 분리해 현업이 IT 용어 없이 데이터를 찾을 수 있게 했다.
- Lake Formation 기반 권한관리와 SageMaker Unified Studio로 데이터 엔지니어, 분석가, 현업의 작업 환경을 통합했다.

## 세부 내용

### 문제의식과 배경

AI 프로젝트가 실패하는 이유는 모델보다 데이터에 닿지 못하는 구조인 경우가 많다. Lake, DW, Mart 계층으로 원천 데이터, 정제/실험 데이터, LLM·BI 활용 데이터를 구분했다.

### 접근 방식과 아키텍처

IT 메타데이터와 비즈니스 메타데이터를 분리해 현업이 IT 용어 없이 데이터를 찾을 수 있게 했다. Lake Formation 기반 권한관리와 SageMaker Unified Studio로 데이터 엔지니어, 분석가, 현업의 작업 환경을 통합했다.

### 운영 포인트와 확장 방향

관련 기술 키워드는 Amazon SageMaker Unified Studio, Amazon Bedrock Knowledge Bases, AWS Lake Formation, Amazon S3, AWS Glue, Athena, lakehouse, metadata catalog이다.

## 정리

이 세션의 핵심은 SK AX가 구현한 SageMaker 기반 분석가와 현업의 통합 AI 환경 (sponsored by SK AX)를 단순한 기능 소개가 아니라 실제 업무와 운영 환경에 적용하기 위한 조건으로 풀어냈다는 점이다. AI 프로젝트가 실패하는 이유는 모델보다 데이터에 닿지 못하는 구조인 경우가 많다.

발표는 AI 품질을 높이기 위해 데이터의 의미, 출처, 품질, 접근 권한을 함께 관리해야 한다는 메시지로 정리된다.
