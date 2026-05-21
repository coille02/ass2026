# Nova Act & Strands Agent 실전: AI 에이전트로 개발 워크플로 자동화하기

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

## 세션 정보

- 시간: 2026-05-21 16:10-16:50 KST
- 트랙: Track 5
- 레벨: 300 - Advanced
- 발표자: 김예진, 솔루션즈 아키텍트, AWS; 안수진, 클라우드 서포트 엔지니어, AWS
- 주제: Architecture, Artificial Intelligence, Developer Tools

## 발표 주제

AI 에이전트 도입을 고려하지만 어디서부터 시작해야 할지 막막한 개발자가 많습니다. 이 세션에서는 Amazon Nova Act를 활용한 브라우저 기반 QA 자동화 에이전트와 Strands Agents SDK를 활용한 AI 코드 어시스턴트 구축 방법을 다룹니다. 나아가 Swarm, Graph, Workflow 등 멀티 에이전트 협업 패턴을 적용하여 코드 리뷰부터 AWS Lambda 배포까지 자동화하는 파이프라인을 3개의 라이브 데모와 함께 소개합니다. 이 세션을 통해 실무에 바로 적용 가능한 에이전트 활용 사례를 살펴봅니다.

Amazon Nova Act로 브라우저 기반 QA 자동화 에이전트를 만들고, Strands Agents SDK로 코드 어시스턴트와 멀티 에이전트 개발 자동화 파이프라인을 만드는 방법을 소개했다. 발표는 에이전트 성숙도를 RPA식 follow, 생성형 AI assist, 협업형 collaborate, 자율형 pioneer 단계로 설명하고, 현재는 assist에서 collaborate로 빠르게 이동 중이라고 봤다.

## 주요 내용

- MCP는 도구 호출, Skills는 능력 정의, A2A는 에이전트 간 통신의 언어로 소개되며 에이전트 생태계의 연결 표준으로 설명됐다.
- Nova Act는 브라우저 UI를 이해하고 조작하는 QA/웹 워크플로 자동화 에이전트로 제시됐다.
- Strands Agents는 원하는 형태의 에이전트를 빠르게 만들 수 있는 오픈소스 SDK로 소개됐다.
- 데모에서는 보안/성능/코드리뷰 에이전트가 교차 검증하고, 오케스트레이터가 코드 수정, 테스트, Lambda 배포, 최종 리포트까지 수행했다.
- 하드코딩 민감정보 제거, SQL 인젝션 방어, 입력 검증, 예외 처리 개선처럼 개발자가 실제로 기대하는 코드 품질 개선을 보여줬다.

## 세부 내용

### 문제의식과 배경

MCP는 도구 호출, Skills는 능력 정의, A2A는 에이전트 간 통신의 언어로 소개되며 에이전트 생태계의 연결 표준으로 설명됐다. Nova Act는 브라우저 UI를 이해하고 조작하는 QA/웹 워크플로 자동화 에이전트로 제시됐다.

### 접근 방식과 아키텍처

Strands Agents는 원하는 형태의 에이전트를 빠르게 만들 수 있는 오픈소스 SDK로 소개됐다. 데모에서는 보안/성능/코드리뷰 에이전트가 교차 검증하고, 오케스트레이터가 코드 수정, 테스트, Lambda 배포, 최종 리포트까지 수행했다. 하드코딩 민감정보 제거, SQL 인젝션 방어, 입력 검증, 예외 처리 개선처럼 개발자가 실제로 기대하는 코드 품질 개선을 보여줬다.

### 운영 포인트와 확장 방향

관련 기술 키워드는 Amazon Nova Act, Strands Agents SDK, MCP, Skills, A2A, Multi-agent, Swarm, Graph, Workflow, AWS Lambda, QA Automation, Code Review Agent이다.

## 정리

이 세션의 핵심은 Nova Act & Strands Agent 실전: AI 에이전트로 개발 워크플로 자동화하기를 단순한 기능 소개가 아니라 실제 업무와 운영 환경에 적용하기 위한 조건으로 풀어냈다는 점이다. MCP는 도구 호출, Skills는 능력 정의, A2A는 에이전트 간 통신의 언어로 소개되며 에이전트 생태계의 연결 표준으로 설명됐다.

발표는 AI 활용이 성과로 이어지려면 모델이나 도구 선택뿐 아니라 데이터, 권한, 운영 절차, 관측 가능성을 함께 설계해야 한다는 메시지로 정리된다.
