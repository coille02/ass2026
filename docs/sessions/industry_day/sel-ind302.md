# [CJ ENM Mnet Plus] K-POP 글로벌 라이브: Mnet+ 4K와 AI 자막

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

## 세션 정보

- 시간: 2026-05-20 12:50-13:30 KST
- 트랙: Track 7
- 분류: 레벨: 300 - Advanced, 산업: Media & Entertainment, 주제: Artificial Intelligence, 주제: Cloud Operations, 주제: Networking & Content Delivery
- 발표자: 임윤택 솔루션즈 아키텍트, AWS; 박찬규 Platform Engineering, CJ ENM Mnet Plus; 이재황 Platform Engineering, CJ ENM Mnet Plus

## 발표 주제

Mnet Plus는 MAMA AWARDS와 KCON 같은 글로벌 K-POP 라이브 이벤트에서 4K 스트리밍과 AI 자막을 운영한 경험을 공유했다.

발표에서는 60만 동시 접속자와 1.6PB 트래픽을 처리하면서 4K 고화질 서비스를 안정적으로 제공했다는 수치가 언급됐다. 라이브 아키텍처는 2개 AWS 리전의 MediaLive, MediaPackage, S3를 독립 구성해 장애 발생 시 백업 리전으로 전환하는 구조로 설명됐다.

## 주요 내용

- 외부 플랫폼 의존에서 벗어나 자체 라이브 플랫폼을 구축해 DRM, 속기사 자막, 4K, AI 자막까지 단계적으로 확장.
- MediaLive/MediaPackage/S3를 2개 리전에 독립 구성해 한쪽 장애에도 라이브를 지속할 수 있게 설계.
- CloudFront Origin Shield와 ABR 기반 스트리밍으로 글로벌 동시 접속 트래픽이 오리진에 직접 몰리지 않도록 구성.
- 4K 구간은 최신 코덱을 활용해 비트레이트를 30-50% 절감하는 전략을 설명.
- AI 자막은 STT 결과를 바로 번역하지 않고 K-POP 도메인 맥락, 방송 메타데이터, 출력 규칙 프롬프트를 계층화해 환각과 부자연스러운 번역을 줄이는 방향으로 설계.

## 세부 내용

### 배경과 문제 인식

Mnet+가 MAMA AWARDS에서 수십만 동시접속과 4K 라이브 스트리밍을 성공적으로 운영한 비결을 공유합니다. AWS MediaLive 이중화로 무중단 방송을 보장하고, Amazon Bedrock 기반 실시간 자막 시스템으로 글로벌 팬에게 다국어 자막을 제공합니다. 대규모 라이브 이벤트 아키텍처와 AI 자막 자동화 구축 경험을 다룹니다.

발표는 이 배경에서 출발해 실제 서비스나 운영 환경에서 어떤 제약이 있었고, 이를 해결하기 위해 어떤 기술 선택과 구현 방식을 택했는지를 설명했다. 단순한 기능 소개보다 현장에서 마주한 병목, 데이터 흐름, 운영 책임을 어떻게 정리했는지가 핵심 맥락이다.

### 구현 접근

- 외부 플랫폼 의존에서 벗어나 자체 라이브 플랫폼을 구축해 DRM, 속기사 자막, 4K, AI 자막까지 단계적으로 확장.
- MediaLive/MediaPackage/S3를 2개 리전에 독립 구성해 한쪽 장애에도 라이브를 지속할 수 있게 설계.
- CloudFront Origin Shield와 ABR 기반 스트리밍으로 글로벌 동시 접속 트래픽이 오리진에 직접 몰리지 않도록 구성.
- 4K 구간은 최신 코덱을 활용해 비트레이트를 30-50% 절감하는 전략을 설명.

### 운영과 확장 관점

- AI 자막은 STT 결과를 바로 번역하지 않고 K-POP 도메인 맥락, 방송 메타데이터, 출력 규칙 프롬프트를 계층화해 환각과 부자연스러운 번역을 줄이는 방향으로 설계.

## 정리

이 세션은 [CJ ENM Mnet Plus] K-POP 글로벌 라이브: Mnet+ 4K와 AI 자막 이라는 주제를 통해, 실제 산업 현장에서 AWS와 AI/클라우드 기술을 어떻게 서비스 개선과 운영 효율로 연결했는지를 보여줬다. 핵심은 새로운 도구의 나열이 아니라 문제를 정의하고, 데이터와 아키텍처를 정리하며, 운영자가 신뢰할 수 있는 방식으로 결과를 만드는 과정에 있었다.
