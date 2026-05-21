# Unlocking Cost-Efficient Cloud and AI Performance on AWS with AMD EPYC (sponsored by AMD)

[AI Day 세션 목록으로 돌아가기](../../ai_day_sessions.md)

## 세션 정보

- 시간: 2026-05-21 13:50-14:10 KST
- 트랙: Track 4
- 분류: 레벨: 200 - Intermediate, 주제: Application Integration, 주제: Compute, 주제: Migration & Modernization
- 발표자: 송성운(AMD Korea)

## 발표 주제

본 세션에서는 AMD EPYC 프로세서 기반 AWS EC2 인스턴스를 통해 클라우드 및 AI 워크로드의 성능을 극대화하고 비용을 최적화하는 방법을 소개합니다.

최신 M8a·C8a·R8a 인스턴스와 실제 고객 사례를 통해 데이터베이스, AI 추론, HPC 등 다양한 워크로드에서의 성능 향상과 TCO 절감 전략을 살펴봅니다.

## 주요 내용

- AI 워크로드가 모두 GPU만 필요한 것은 아니며, CPU 기반 추론과 전처리·데이터 처리도 비용 최적화 여지가 크다.
- C8a는 전세대 대비 처리시간 개선, M8a는 여러 워크로드에서 실행 성능 향상과 비용 절감 사례를 강조했다.
- PostgreSQL 등 데이터베이스 워크로드에서는 인스턴스 크기와 CPU 특성 선택이 TCO에 직접 영향을 준다.
- Netflix, Pinterest 등 사례를 통해 성능 예측성과 비용 대비 성능을 강조했다.
- 주요 기술과 키워드는 AMD EPYC, Amazon EC2, M8a, C8a, R8a, PostgreSQL, CPU inference, HPC, TCO, workload optimization 중심으로 정리됐다.

## 세부 내용

### 배경과 문제 인식

본 세션에서는 AMD EPYC 프로세서 기반 AWS EC2 인스턴스를 통해 클라우드 및 AI 워크로드의 성능을 극대화하고 비용을 최적화하는 방법을 소개합니다. 최신 M8a·C8a·R8a 인스턴스와 실제 고객 사례를 통해 데이터베이스, AI 추론, HPC 등 다양한 워크로드에서의 성능 향상과 TCO 절감 전략을 살펴봅니다.

발표는 이 배경에서 출발해 실제 서비스나 운영 환경에서 어떤 제약이 있었고, 이를 해결하기 위해 어떤 기술 선택과 구현 방식을 택했는지를 설명했다. 단순한 기능 소개보다 현장에서 마주한 병목, 데이터 흐름, 운영 책임을 어떻게 정리했는지가 핵심 맥락이다.

### 구현 접근

- AI 워크로드가 모두 GPU만 필요한 것은 아니며, CPU 기반 추론과 전처리·데이터 처리도 비용 최적화 여지가 크다.
- C8a는 전세대 대비 처리시간 개선, M8a는 여러 워크로드에서 실행 성능 향상과 비용 절감 사례를 강조했다.
- PostgreSQL 등 데이터베이스 워크로드에서는 인스턴스 크기와 CPU 특성 선택이 TCO에 직접 영향을 준다.
- Netflix, Pinterest 등 사례를 통해 성능 예측성과 비용 대비 성능을 강조했다.
- 구현을 설명하는 축은 AMD EPYC, Amazon EC2, M8a, C8a, R8a, PostgreSQL, CPU inference, HPC, TCO, workload optimization 등으로 요약할 수 있다.

### 운영과 확장 관점

- 발표의 초점은 기술 도입 자체보다 반복 가능한 운영 방식, 검증 가능한 성과, 이후 확장 가능한 구조를 만드는 데 있었다.
- 발표에서 남길 만한 메시지는 AI 비용 최적화는 GPU 구매 전략이 아니라 워크로드별 컴퓨트 선택 전략이다.

## 정리

이 세션은 Unlocking Cost-Efficient Cloud and AI Performance on AWS with AMD EPYC (sponsored by AMD) 이라는 주제를 통해, 실제 산업 현장에서 AWS와 AI/클라우드 기술을 어떻게 서비스 개선과 운영 효율로 연결했는지를 보여줬다. 핵심은 새로운 도구의 나열이 아니라 문제를 정의하고, 데이터와 아키텍처를 정리하며, 운영자가 신뢰할 수 있는 방식으로 결과를 만드는 과정에 있었다.
