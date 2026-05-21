# AIOps 도전과 실전: AI SecOps에서 DevOps 에이전트까지

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

## 세션 정보

- 시간: 2026-05-21 16:10-16:50 KST
- 트랙: Track 4
- 레벨: 300 - Advanced
- 발표자: 이연수, 테크니컬 어카운트 매니저, AWS; 박종진, 테크니컬 어카운트 매니저, AWS; 현승열, 선임 엔지니어, 삼성전자
- 주제: Artificial Intelligence, Cloud Operations

## 발표 주제

장애 대응과 보안 로그 수동 분석에서 벗어나 생산적 업무에 집중하고자 AIOps에 주목하고 있습니다. 이 세션에서는 삼성전자가 Amazon Bedrock과 Strands Agents SDK로 WAF 위협을 탐지한 AI SecOps 여정을 공유하고, 근본 원인 분석부터 배포 롤백, 사전 예방까지 제공하는 AWS DevOps 에이전트를 소개합니다.

삼성전자 계정 서비스의 WAF 로그 분석 AI SecOps 사례와 AWS DevOps Agent를 소개했다. 삼성전자 사례는 대규모 트래픽과 하루 TB급 보안 로그를 사람이 분석하는 한계를 Bedrock, Strands Agents, 멀티 에이전트 구조로 해결하려는 여정이었다.

## 주요 내용

- 삼성 계정은 21억 사용자와 초당 대규모 트래픽을 처리하며, WAF 로그 기반 악성 트래픽 분석을 수행한다.
- AI로 공격 패턴이 빠르게 바뀌면서 고정 룰과 수동 로그 분석만으로는 대응이 어렵고, 자연어 질의로 WAF 로그를 조회/분석/리포트화하는 필요가 커졌다.
- Bedrock Agent Builder로 빠르게 시작했지만 복잡한 질의와 해석 품질에 한계가 있어 Strands Agents와 멀티 에이전트 구조로 확장했다.
- 후반부 AWS DevOps Agent 데모는 조사, 완화, MCP 서버 연동, 스킬/채팅, 사전 예방 권장사항을 통해 장애 대응과 예방 조치를 자동화하는 흐름을 보여줬다.

## 세부 내용

### 문제의식과 배경

삼성 계정은 21억 사용자와 초당 대규모 트래픽을 처리하며, WAF 로그 기반 악성 트래픽 분석을 수행한다. AI로 공격 패턴이 빠르게 바뀌면서 고정 룰과 수동 로그 분석만으로는 대응이 어렵고, 자연어 질의로 WAF 로그를 조회/분석/리포트화하는 필요가 커졌다.

### 접근 방식과 아키텍처

Bedrock Agent Builder로 빠르게 시작했지만 복잡한 질의와 해석 품질에 한계가 있어 Strands Agents와 멀티 에이전트 구조로 확장했다. 후반부 AWS DevOps Agent 데모는 조사, 완화, MCP 서버 연동, 스킬/채팅, 사전 예방 권장사항을 통해 장애 대응과 예방 조치를 자동화하는 흐름을 보여줬다.

### 운영 포인트와 확장 방향

관련 기술 키워드는 Amazon Bedrock, Bedrock Agent Builder, Strands Agents SDK, AWS WAF, Amazon EKS, Amazon CloudWatch, MCP, DevOps Agent, AI SecOps, AIOps이다.

## 정리

이 세션의 핵심은 AIOps 도전과 실전: AI SecOps에서 DevOps 에이전트까지를 단순한 기능 소개가 아니라 실제 업무와 운영 환경에 적용하기 위한 조건으로 풀어냈다는 점이다. 삼성 계정은 21억 사용자와 초당 대규모 트래픽을 처리하며, WAF 로그 기반 악성 트래픽 분석을 수행한다.

발표는 AI 활용이 성과로 이어지려면 모델이나 도구 선택뿐 아니라 데이터, 권한, 운영 절차, 관측 가능성을 함께 설계해야 한다는 메시지로 정리된다.
