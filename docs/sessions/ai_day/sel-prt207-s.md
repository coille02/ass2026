# LLM 애플리케이션 프로덕션 운영, Observability로 풀다 (sponsored by 와탭, WhaTap)

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

## 세션 정보

- 시간: 2026-05-21 13:50-14:10 KST
- 트랙: Track 5
- 분류: 레벨: 200 - Intermediate, 산업: Professional Services, 산업: Software & Internet, 주제: Artificial Intelligence, 주제: Business Applications, 주제: Developer Tools
- 발표자: 신민철(WhaTap)

## 발표 주제

LLM 서비스는 구축보다

안정적 운영이 더 어렵습니다. 기존 APM/RUM으로는 커버할 수 없는 토큰 비용 폭발, 응답 지연, 할루시네이션 등 LLM 특유의 과제를 살펴보고, 이를 감지·대응하기 위한 LLM 옵저버빌리티 핵심 메트릭과 아키텍처를 소개합니다.

## 주요 내용

- LLM 앱은 단순 API 호출처럼 보여도 실제 프로덕션 파이프라인은 여러 LLM 호출과 도구 호출을 포함한다.
- 토큰 사용량은 비용과 직결되며 모델별 가격 차이 때문에 비용이 비선형적으로 증가할 수 있다.
- Provider LLM은 API 영역 중심으로, Local LLM은 인프라 영역까지 포함해 관측 지점을 다르게 봐야 한다.
- 프롬프트, 응답 품질, 지연, 토큰, 비용, 로그, 트레이스가 함께 연결되어야 운영자가 원인을 찾을 수 있다.
- 주요 기술과 키워드는 LLM observability, Amazon Bedrock, APM, RUM, token cost, latency, prompt/response trace, monitoring 중심으로 정리됐다.

## 세부 내용

### 배경과 문제 인식

LLM 서비스는 구축보다 안정적 운영이 더 어렵습니다. 기존 APM/RUM으로는 커버할 수 없는 토큰 비용 폭발, 응답 지연, 할루시네이션 등 LLM 특유의 과제를 살펴보고, 이를 감지·대응하기 위한 LLM 옵저버빌리티 핵심 메트릭과 아키텍처를 소개합니다. AWS Bedrock 기반 실제 사례를 통해 엔터프라이즈 환경의 LLM 모니터링 전략을 공유합니다.

발표는 이 배경에서 출발해 실제 서비스나 운영 환경에서 어떤 제약이 있었고, 이를 해결하기 위해 어떤 기술 선택과 구현 방식을 택했는지를 설명했다. 단순한 기능 소개보다 현장에서 마주한 병목, 데이터 흐름, 운영 책임을 어떻게 정리했는지가 핵심 맥락이다.

### 구현 접근

- LLM 앱은 단순 API 호출처럼 보여도 실제 프로덕션 파이프라인은 여러 LLM 호출과 도구 호출을 포함한다.
- 토큰 사용량은 비용과 직결되며 모델별 가격 차이 때문에 비용이 비선형적으로 증가할 수 있다.
- Provider LLM은 API 영역 중심으로, Local LLM은 인프라 영역까지 포함해 관측 지점을 다르게 봐야 한다.
- 프롬프트, 응답 품질, 지연, 토큰, 비용, 로그, 트레이스가 함께 연결되어야 운영자가 원인을 찾을 수 있다.
- 구현을 설명하는 축은 LLM observability, Amazon Bedrock, APM, RUM, token cost, latency, prompt/response trace, monitoring 등으로 요약할 수 있다.

### 운영과 확장 관점

- 발표의 초점은 기술 도입 자체보다 반복 가능한 운영 방식, 검증 가능한 성과, 이후 확장 가능한 구조를 만드는 데 있었다.
- 발표에서 남길 만한 메시지는 LLM 앱은 배포 후부터 진짜 비용과 품질 문제가 시작된다.

## 정리

이 세션은 LLM 애플리케이션 프로덕션 운영, Observability로 풀다 (sponsored by 와탭, WhaTap) 이라는 주제를 통해, 실제 산업 현장에서 AWS와 AI/클라우드 기술을 어떻게 서비스 개선과 운영 효율로 연결했는지를 보여줬다. 핵심은 새로운 도구의 나열이 아니라 문제를 정의하고, 데이터와 아키텍처를 정리하며, 운영자가 신뢰할 수 있는 방식으로 결과를 만드는 과정에 있었다.
