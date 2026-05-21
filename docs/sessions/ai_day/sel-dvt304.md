# [삼성전자] 200개국 삼성 스마트 TV 앱 데이터를 자연어로 묻다: 에이전틱 AI on AWS

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

## 세션 정보

- 시간: 2026-05-21 14:30-15:10 KST
- 트랙: Track 3
- 레벨: 300 - Advanced
- 발표자: 이혜원(AWS), 이아름(AWS), 임경택(삼성전자)
- 주제: Artificial Intelligence

## 발표 주제

본 세션에서는 Amazon Bedrock AgentCore를 활용하여 LangGraph 멀티 에이전트를 프로덕션 환경에 배포한 실전 사례를 공유합니다. AgentCore Runtime에서 Supervisor 패턴의 멀티 에이전트를 실행하고, MCP(Model Context Protocol)를 통해 내부 API 등 외부 도구를 표준화된 방식으로 연결합니다. Gateway로 MCP 서버를 중앙 관리하고 에이전트 트래픽을 제어하며, Policy & Identity로 자연어 기반 접근 제어와 Okta IdP 연동을 구현한 과정을 다룹니다. 또한 OpenTelemetry 기반 Observability로 Sub-Agent별 계층적 트레이싱을 구성하고, Evaluation을 CI 파이프라인에 통합하여 에이전트 품질을 자동으로 검증하는 방법을 소개합니다.

삼성 스마트 TV 앱 운영 데이터를 자연어로 질의하기 위해 LangGraph 멀티 에이전트를 Amazon Bedrock AgentCore 기반으로 프로덕션에 올린 사례다. 세션은 AgentCore Runtime, Gateway, Identity, Observability, Evaluation을 각각 운영 가능한 에이전트 플랫폼의 구성 요소로 풀어 설명했다. MCP를 통해 내부 API와 외부 도구 연결을 표준화하고, Okta IdP 연동과 자연어 기반 접근 제어, OpenTelemetry 트레이싱, CI 평가 자동화를 적용한 점이 실무적으로 중요했다.

## 주요 내용

- 200개국 TV 앱 데이터 운영 문제를 자연어 질의와 멀티 에이전트로 풀되, 프로덕션 요구사항을 먼저 정의했다.
- AgentCore Runtime은 Supervisor 패턴의 멀티 에이전트를 실행하는 기반으로, Gateway는 MCP 서버와 도구 연결을 중앙 관리한다.
- Identity/Policy 연동으로 사용자의 권한과 에이전트의 도구 호출 권한을 함께 통제했다.
- OpenTelemetry 기반 계층형 트레이싱으로 Sub-Agent별 실행 흐름을 추적하고, Evaluation을 CI에 넣어 품질을 자동 검증했다.

## 세부 내용

### 문제의식과 배경

200개국 TV 앱 데이터 운영 문제를 자연어 질의와 멀티 에이전트로 풀되, 프로덕션 요구사항을 먼저 정의했다. AgentCore Runtime은 Supervisor 패턴의 멀티 에이전트를 실행하는 기반으로, Gateway는 MCP 서버와 도구 연결을 중앙 관리한다.

### 접근 방식과 아키텍처

Identity/Policy 연동으로 사용자의 권한과 에이전트의 도구 호출 권한을 함께 통제했다. OpenTelemetry 기반 계층형 트레이싱으로 Sub-Agent별 실행 흐름을 추적하고, Evaluation을 CI에 넣어 품질을 자동 검증했다.

### 운영 포인트와 확장 방향

관련 기술 키워드는 Amazon Bedrock AgentCore, LangGraph, MCP, AgentCore Runtime, Gateway, Identity, Okta, OpenTelemetry, Evaluation, CI이다.

## 정리

이 세션의 핵심은 [삼성전자] 200개국 삼성 스마트 TV 앱 데이터를 자연어로 묻다: 에이전틱 AI on AWS를 단순한 기능 소개가 아니라 실제 업무와 운영 환경에 적용하기 위한 조건으로 풀어냈다는 점이다. 200개국 TV 앱 데이터 운영 문제를 자연어 질의와 멀티 에이전트로 풀되, 프로덕션 요구사항을 먼저 정의했다.

발표는 AI 활용이 성과로 이어지려면 모델이나 도구 선택뿐 아니라 데이터, 권한, 운영 절차, 관측 가능성을 함께 설계해야 한다는 메시지로 정리된다.
