# 3주차: AWS Summit Seoul 2026 AI Day VOD 기반 사례 정리

## 위키 작성안

### 활동 단계

- 발굴
- 자산화
- 전파

### 진행 내용

이번 주에는 AWS Summit Seoul 2026 AI Day 세션을 VOD 기반으로 확인하고, AX TF에서 참고할 만한 사례와 플랫폼 관점을 정리했다.

AI Day에서는 Industry Day보다 플랫폼과 운영에 가까운 내용이 많았다. Bedrock, AgentCore, Strands Agents, Kiro, SageMaker, OpenSearch, Amazon Quick, 보안, AIOps, 추론 인프라, AI-ready data 등 AI를 실제 업무와 운영 환경에 지속적으로 적용하기 위한 기반 요소가 반복적으로 등장했다.

### 주요 정리 내용

- 에이전트는 데모보다 운영이 어렵고, 관측성, 권한, 비용, 실패 대응이 함께 필요함
- Agent Builder를 만들기 전에 AI-ready data, 데이터 카탈로그, 권한 체계가 선행되어야 함
- 개발자 AI 도구 활용은 AI-DLC 관점에서 요구사항, 설계, 코드 생성, 테스트, 리뷰, 배포, 운영 피드백으로 연결될 수 있음
- 업무형 AI는 별도 챗봇보다 기존 문서, 메일, 일정, 메시지, 대시보드와 연결될 때 실질적인 효과가 커짐
- 서버리스와 이벤트 기반 구조는 내부 업무 자동화와 반복 리포트 생성에 적합함
- 보안, 비용, 로그, 관측성은 AX 플랫폼의 기본 기능으로 설계되어야 함

### 참고한 사례

- 삼성 어카운트 AIOps
- 20만 Amazonian의 AI 내재화와 Amazon Quick Desktop
- 완성차 지능형 상품 전략 플랫폼
- LG전자 AI-DLC
- Kiro 기반 개발 효율화
- AI-ready data / OpenSearch / 데이터 플랫폼 관련 세션
- Bedrock AgentCore / Strands Agents 관련 세션

### 느낀 점 / AX TF에 가져갈 점

AI Day VOD를 보면서 가장 인상 깊었던 점은, AI를 실제 업무에 계속 쓰게 만들려면 모델보다 운영 체계가 더 중요하다는 점이었다. 여러 세션에서 AgentCore, Strands Agents, Kiro, SageMaker, OpenSearch, 보안, 관측성, 비용 관리가 반복적으로 등장했다. 이것은 에이전트가 데모를 넘어 실제 서비스가 되려면 플랫폼 요구사항을 갖춰야 한다는 의미로 보였다.

특히 AI-ready data 관련 세션을 보면서 Agent Builder보다 먼저 데이터 카탈로그와 권한 체계가 필요하다고 느꼈다. 데이터의 위치, 의미, 최신성, 소유자, 접근 권한이 정리되지 않으면 에이전트는 답변은 할 수 있어도 실무에서 신뢰받기 어렵다.

Amazon Quick Desktop 사례도 계속 생각이 남았다. AX TF에서 사무직 업무 효율화를 고민한다면 “사내 챗봇”보다 기존 업무 도구와 연결된 AI 업무 환경을 상상해야 할 것 같다. 아침에 주요 이슈를 요약하고, 회의 전 관련 문서를 모아주고, 퇴근 후 반복 작업을 이어서 수행하는 흐름은 실제 업무 시간을 줄이는 데 더 직접적일 수 있다.

AI Day를 보고 나니 AX TF의 역할은 AI 기능을 많이 만드는 것이 아니라, 에이전트가 안전하게 데이터와 도구를 사용할 수 있는 기반을 만드는 쪽에 더 가깝다고 느꼈다.

### 추가로 검토할 주제: Strands Agents SDK

AI Day에서 Agent AI 관련 세션을 보며 Strands Agents SDK가 여러 번 등장했다. 에이전트를 단순 데모가 아니라 실제 업무 흐름과 운영 환경에 연결하려면 도구 호출, 상태 관리, 메모리, 평가, 관측성, 배포 방식이 중요해진다. Strands Agents SDK는 이 영역에서 반복적으로 언급된 개발 기반이었다.

아직 직접 사용해보지 않았기 때문에, 별도 학습과 실습이 필요하다고 느꼈다. 이후 간단한 PoC를 통해 다음 내용을 확인해보면 좋겠다.

- 에이전트가 외부 도구와 API를 호출하는 방식
- MCP 또는 사내 도구와 연결할 수 있는 구조
- 메모리나 컨텍스트를 관리하는 방식
- 실행 로그와 관측성을 확보하는 방식
- Bedrock, AgentCore와 함께 사용할 때의 개발 경험
- 사내 Agent Builder나 Skill Hub와 연결 가능한지 여부

### 산출물

- GitHub: https://github.com/coille02/ass2026
- AI Day 세션별 정리 문서
- AI Day AX 플랫폼 관점 정리
- AWS Summit Seoul 2026 AX 관점 통합 정리

### 정리

3주간 AWS Summit Seoul 2026 사례를 나누어 정리하면서, AX는 단순 AI 도구 도입이 아니라 스킬, 데이터, 권한, 운영, 보안, 변화관리를 함께 설계하는 일이라는 점을 확인했다.

## Jira 코멘트

```markdown
이번 주에는 AWS Summit Seoul 2026 AI Day 세션을 VOD 기반으로 확인하고, AX TF에서 참고할 만한 플랫폼 관점을 정리했습니다.

활동 단계는 발굴 / 자산화 / 전파에 해당합니다.

주요 내용:
- 에이전트는 데모보다 운영이 어렵고, 관측성, 권한, 비용, 실패 대응이 함께 필요함
- Agent Builder를 위해서는 AI-ready data, 데이터 카탈로그, 권한 체계가 선행되어야 함
- AI-DLC 관점에서는 요구사항, 설계, 코드 생성, 테스트, 리뷰, 배포, 운영 피드백을 하나의 흐름으로 연결하는 것이 중요함
- Amazon Quick Desktop 사례처럼 기존 문서, 메일, 일정, 메시지, 대시보드와 AI를 연결하는 방식이 업무형 AI에 참고가 될 수 있음
- 보안, 비용, 로그, 관측성은 AX 플랫폼의 기본 기능으로 설계되어야 함

느낀 점:
AI Day 사례를 보면서 AI를 실제 업무에 계속 쓰게 만들려면 모델보다 운영 체계가 더 중요하다고 느꼈습니다. AgentCore, Strands Agents, Kiro, SageMaker, OpenSearch, 보안, 관측성, 비용 관리가 반복적으로 등장한 점이 인상적이었습니다.

특히 Agent Builder를 고민하기 전에 AI-ready data, 데이터 카탈로그, 권한 체계가 먼저 필요하다고 느꼈습니다. 또한 Amazon Quick Desktop 사례처럼 기존 문서, 메일, 일정, 메시지, 대시보드와 AI를 연결하는 방식이 사무직 AX에 더 현실적일 수 있다고 생각했습니다.

추가로 여러 Agent AI 세션에서 Strands Agents SDK가 반복적으로 등장한 점이 인상 깊었습니다. 아직 직접 사용해보지 않았기 때문에, 이후 문서를 찾아보고 간단한 예제를 만들어보며 도구 호출, 메모리, 관측성, Bedrock/AgentCore 연동 방식 등을 확인해볼 필요가 있다고 느꼈습니다.

산출물:
- https://github.com/coille02/ass2026

3주간 AWS Summit Seoul 2026 사례를 나누어 정리하면서, AX는 단순 AI 도구 도입이 아니라 스킬, 데이터, 권한, 운영, 보안, 변화관리를 함께 설계하는 일이라는 점을 확인했습니다.
```
