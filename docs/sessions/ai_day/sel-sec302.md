# Amazon Bedrock AgentCore 로 AI 시대의 Zero Trust 구현하기

[AI Day 세션 목록으로 돌아가기](../../ai_day_sessions.md)

## 세션 정보

- 시간: 2026-05-21 14:30-15:10 KST
- 트랙: Track 7
- 레벨: 300 - Advanced
- 발표자: 이민우(AWS), 황재훈(AWS)
- 주제: Security & Identity

## 발표 주제

이 세션에서는 Amazon Bedrock AgentCore Identity와 Gateway를 활용하여 AI 시대의 Zero Trust 보안 모델을 구현하는 방법을 다룹니다. AgentCore Identity와 Gateway를 사용하여 중앙화된 에이전트 신원 관리, 안전한 자격 증명 저장소를 통한 AI 에이전트의 인증 및 권한 부여, 안전한 도구(MCP, API 등) 연결을 지원하는 방법을 배웁니다. 이를 통해 참석자는 AI 에이전트의 자율성을 유지하면서도 강력한 보안을 확보하는 실용적인 아키텍처 패턴을 학습하고, 엔터프라이즈 환경에서 신뢰할 수 있는 AI 에이전트 시스템을 구축할 수 있습니다.

AI 에이전트가 도구와 API를 직접 호출하는 시대에 Zero Trust를 어떻게 적용할지 다룬 보안 세션이다. Amazon Bedrock AgentCore Identity와 Gateway를 사용해 에이전트의 신원, 사용자 위임 권한, 도구 접속, 자격 증명 보관을 중앙에서 관리하는 패턴이 소개됐다. 발표는 에이전트의 자율성을 유지하되 API 키나 OAuth 토큰을 안전하게 다루고, MCP 도구 연결을 통제 가능한 경로로 만드는 것이 핵심이라고 설명했다.

## 주요 내용

- AI 에이전트도 사용자, 서비스, 도구와 마찬가지로 명시적 신원과 최소 권한 원칙을 가져야 한다.
- AgentCore Identity는 에이전트와 사용자 위임 권한을 관리하고, 안전한 credential 저장소와 연계된다.
- AgentCore Gateway는 MCP, API 등 도구 호출 경로를 중앙화해 보안 정책과 관측성을 적용하기 쉽게 만든다.
- Zero Trust의 초점은 "에이전트를 막는 것"이 아니라, 어떤 권한으로 어떤 도구를 언제 호출했는지 통제하는 것이다.

## 세부 내용

### 문제의식과 배경

AI 에이전트도 사용자, 서비스, 도구와 마찬가지로 명시적 신원과 최소 권한 원칙을 가져야 한다. AgentCore Identity는 에이전트와 사용자 위임 권한을 관리하고, 안전한 credential 저장소와 연계된다.

### 접근 방식과 아키텍처

AgentCore Gateway는 MCP, API 등 도구 호출 경로를 중앙화해 보안 정책과 관측성을 적용하기 쉽게 만든다. Zero Trust의 초점은 "에이전트를 막는 것"이 아니라, 어떤 권한으로 어떤 도구를 언제 호출했는지 통제하는 것이다.

### 운영 포인트와 확장 방향

관련 기술 키워드는 Amazon Bedrock AgentCore, AgentCore Identity, AgentCore Gateway, Zero Trust, MCP, OAuth, API Key, Credential Store, Security이다.

## 정리

이 세션의 핵심은 Amazon Bedrock AgentCore 로 AI 시대의 Zero Trust 구현하기를 단순한 기능 소개가 아니라 실제 업무와 운영 환경에 적용하기 위한 조건으로 풀어냈다는 점이다. AI 에이전트도 사용자, 서비스, 도구와 마찬가지로 명시적 신원과 최소 권한 원칙을 가져야 한다.

발표는 AI 활용의 속도를 높이더라도 보안, 접근 제어, 감사, 데이터 보호를 같은 수준으로 설계해야 한다는 메시지로 정리된다.
