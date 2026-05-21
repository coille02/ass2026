# Amazon Bedrock 기반 GitLab Duo 에이전트 플랫폼으로 혁신 가속화 (sponsored by Gitlab)

[AI Day 세션 목록으로 돌아가기](../../ai_day_sessions.md)

## 세션 정보

- 시간: 2026-05-21 13:50-14:10 KST
- 트랙: Track 6
- 레벨: 200 - Intermediate
- 발표자: Jimmy Gam(GitLab)
- 주제: Artificial Intelligence, Developer Tools, Industry Solutions

## 발표 주제

GitLab Duo Agent Platform이 Amazon Bedrock 기반으로 전체 SDLC에 에이전틱 AI를 내재화하는 방법을 살펴보세요 — 데이터를 AWS 환경 또는 고객 내부에 안전하게 유지합니다. AI Gateway로 기획·코딩·보안·컴플라이언스 워크플로우를 오케스트레이션해 데이터 레지던시 충족·AWS 투자 극대화를 실현하세요.

GitLab Duo Agent Platform이 Amazon Bedrock과 결합해 SDLC 전반에 에이전틱 AI를 내재화하는 방식을 소개했다. IDE나 CLI에 흩어진 AI 도구가 컨텍스트를 잃는 문제를 지적하며, 계획, 코딩, 코드리뷰, 보안, 컴플라이언스, CI/CD 데이터를 하나의 데이터 모델과 워크플로우 안에서 활용하는 접근을 제시했다.

## 주요 내용

- 코드 작성 속도만 빨라져도 코드리뷰, 보안 스캔, 테스트, 승인 과정이 따라오지 못하면 전체 생산성은 제한된다.
- GitLab의 통합 데이터 모델은 issue, merge request, pipeline, 취약점, 정책 데이터를 에이전트 컨텍스트로 제공한다.
- Amazon Bedrock 연동은 IAM, VPC endpoint, 리전 데이터 보관 등 AWS 보안 패턴을 활용해 데이터 레지던시 요구를 맞춘다.
- 외부 에이전트와의 통합도 지원하되, 승인된 모델과 AI Gateway를 통해 사용량·정책·거버넌스를 통제한다.

## 세부 내용

### 문제의식과 배경

코드 작성 속도만 빨라져도 코드리뷰, 보안 스캔, 테스트, 승인 과정이 따라오지 못하면 전체 생산성은 제한된다. GitLab의 통합 데이터 모델은 issue, merge request, pipeline, 취약점, 정책 데이터를 에이전트 컨텍스트로 제공한다.

### 접근 방식과 아키텍처

Amazon Bedrock 연동은 IAM, VPC endpoint, 리전 데이터 보관 등 AWS 보안 패턴을 활용해 데이터 레지던시 요구를 맞춘다. 외부 에이전트와의 통합도 지원하되, 승인된 모델과 AI Gateway를 통해 사용량·정책·거버넌스를 통제한다.

### 운영 포인트와 확장 방향

관련 기술 키워드는 GitLab Duo Agent Platform, Amazon Bedrock, AI Gateway, SDLC, DevSecOps, IAM, VPC endpoint, data residency, merge request이다.

## 정리

이 세션의 핵심은 Amazon Bedrock 기반 GitLab Duo 에이전트 플랫폼으로 혁신 가속화 (sponsored by Gitlab)를 단순한 기능 소개가 아니라 실제 업무와 운영 환경에 적용하기 위한 조건으로 풀어냈다는 점이다. 코드 작성 속도만 빨라져도 코드리뷰, 보안 스캔, 테스트, 승인 과정이 따라오지 못하면 전체 생산성은 제한된다.

발표는 AI 활용이 성과로 이어지려면 모델이나 도구 선택뿐 아니라 데이터, 권한, 운영 절차, 관측 가능성을 함께 설계해야 한다는 메시지로 정리된다.
