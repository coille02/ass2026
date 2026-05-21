# sel-ind302 - [CJ ENM Mnet Plus] K-POP 글로벌 라이브: Mnet+ 4K와 AI 자막

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

**Title/Time/Track/Speakers**  
- 제목: [CJ ENM Mnet Plus] K-POP 글로벌 라이브: Mnet+ 4K와 AI 자막
- 시간: 2026-05-20 12:50-13:30 KST
- 트랙: Industry Day / Media & Entertainment / Artificial Intelligence, Cloud Operations, Networking & Content Delivery
- 발표자: 임윤택 솔루션즈 아키텍트, AWS; 박찬규 Platform Engineering, CJ ENM Mnet Plus; 이재황 Platform Engineering, CJ ENM Mnet Plus

**핵심 요약**  
Mnet Plus는 MAMA AWARDS와 KCON 같은 글로벌 K-POP 라이브 이벤트에서 4K 스트리밍과 AI 자막을 운영한 경험을 공유했다. 전사에서는 60만 동시 접속자와 1.6PB 트래픽을 처리하면서 4K 고화질 서비스를 안정적으로 제공했다는 수치가 언급됐다. 라이브 아키텍처는 2개 AWS 리전의 MediaLive, MediaPackage, S3를 독립 구성해 장애 발생 시 백업 리전으로 전환하는 구조로 설명됐다. AI 자막은 S3 이벤트, SQS, STT, LLM, Bedrock 기반 처리, 프롬프트 레이어, 다국어 번역, 비용 최적화와 장애 폴백을 묶은 실시간 파이프라인으로 소개됐다.

**주요 포인트**
- 외부 플랫폼 의존에서 벗어나 자체 라이브 플랫폼을 구축해 DRM, 속기사 자막, 4K, AI 자막까지 단계적으로 확장.
- MediaLive/MediaPackage/S3를 2개 리전에 독립 구성해 한쪽 장애에도 라이브를 지속할 수 있게 설계.
- CloudFront Origin Shield와 ABR 기반 스트리밍으로 글로벌 동시 접속 트래픽이 오리진에 직접 몰리지 않도록 구성.
- 4K 구간은 최신 코덱을 활용해 비트레이트를 30-50% 절감하는 전략을 설명.
- AI 자막은 STT 결과를 바로 번역하지 않고 K-POP 도메인 맥락, 방송 메타데이터, 출력 규칙 프롬프트를 계층화해 환각과 부자연스러운 번역을 줄이는 방향으로 설계.

**AWS/기술 키워드**  
AWS Elemental MediaLive, AWS Elemental MediaPackage, Amazon S3, Amazon CloudFront, Origin Shield, Amazon SQS, Amazon Bedrock, STT, LLM, ABR, 4K Streaming, AI Subtitles

**현장 메모로 남길 점**  
Mnet Plus 사례는 미디어 아키텍처와 생성형 AI가 같은 운영 문제 안에서 만나는 좋은 예다. 라이브 서비스에서는 정확도뿐 아니라 지연, 폴백, 비용, 도메인 용어, 국가별 반응까지 함께 설계해야 한다.

**블로그용 한줄**  
Mnet Plus는 멀티 리전 라이브 스트리밍과 Bedrock 기반 AI 자막을 결합해 글로벌 K-POP 팬에게 4K 라이브 경험을 제공했다.

### 직접 들은 뒤 메모

K-POP 글로벌 라이브 세션은 대규모 실시간 트래픽과 AI 자막을 함께 운영한 사례라 인상적이었다. AI 자막 자체도 흥미로웠지만, 더 크게 보인 것은 멀티 리전, 장애 전환, 비용 통제, 품질 폴백까지 포함한 운영 설계였다. 라이브 서비스에서 AI 기능은 별도 부가 기능이 아니라 서비스 안정성과 함께 설계되어야 한다는 점이 남았다.

카카오페이에서도 이벤트성 트래픽, 대규모 알림, 실시간 상담, 장애 상황 공지처럼 순간적으로 부하가 몰리는 흐름이 많다. AI가 고객 안내 문구를 만들거나 상담 답변을 보조하더라도 장애 시 안전하게 멈추고, 잘못된 답변을 막고, 사람에게 넘기는 폴백이 필요하다. AI 자막에서 도메인 맥락과 출력 규칙을 넣어 품질을 잡은 것처럼, 금융 약관이나 고객 안내 문구에도 도메인별 규칙과 검증 기준이 필요하다.
