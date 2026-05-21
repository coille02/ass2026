# sel-ind303 - LG U+의 에이전틱 AI 기반 대규모 마이그레이션 여정

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

**제목/시간/트랙/발표자**  
- 제목: LG U+의 에이전틱 AI 기반 대규모 마이그레이션 여정
- 시간: 2026-05-20 14:30-15:10 KST
- 트랙: Telecommunications / Artificial Intelligence, Developer Tools, Migration & Modernization
- 발표자: 문승제 딜리버리 컨설턴트(AWS), 우건희 책임(LG U+)

**핵심 요약**  
LG U+는 100개 이상의 온프레미스 애플리케이션을 클라우드로 전환하면서, assessment, design, migration, scale-out 단계 전반에 에이전틱 AI를 적용했다. 목표는 단순 이전이 아니라 운영 표준화, 보안 강화, 마이그레이션 속도/품질 확보, AX 기반 혁신 환경 마련이었다. UCMP에 내재화한 인터뷰 에이전트와 코드 분석 에이전트가 표준화된 입력을 만들고, design agent가 목표 AWS native architecture와 refactoring action item을 생성했다. migration 단계에서는 AWS Transform Custom이 대규모 규칙 기반 변환을 맡고, Kiro IDE와 Utopia 플랫폼이 복잡한 리팩터링 패턴과 조직 표준을 재사용 가능한 지식으로 축적했다.

**주요 포인트**
- 대규모 온프레미스 환경은 서비스별 인프라/로그/보안/외주 개발사가 분산되어 있어 통합 모니터링, 패치, 보안 대응, AI 도입이 느려지는 문제가 있었다.
- Assessment 단계의 인터뷰 에이전트는 AWS 마이그레이션 경험이 담긴 61개 질문을 기반으로 답변 품질을 검증하고, 부족하면 재질문해 표준화된 리포트와 JSON을 생성했다.
- 코드 분석에는 AWS Transform Custom을 활용해 framework/runtime, security/compliance, dependency/CVE, cloud readiness 관점으로 코드를 진단했다.
- Design 단계는 인터뷰 결과와 코드 분석 결과를 입력으로 목표 아키텍처와 리팩터링 action item을 자동 생성하고 Confluence에 기록했다.
- Migration 단계에서 Java version upgrade 같은 반복/규칙 기반 대규모 변경은 AWS Transform Custom이 변환, build, validation을 반복하며 PR 형태로 결과를 만들었다.
- 복잡한 리팩터링은 Kiro IDE의 steering, skill, powers를 활용했고, Utopia 플랫폼이 검증된 기술 표준과 전환 패턴을 중앙 관리했다.
- LG CTL CLI는 프로젝트 세팅, action item 선택, requirement 생성, Kiro 개발 흐름, 테스트, 문서화, Confluence 업로드, 신규 skill/steering 생성까지 연결했다.
- 성과는 리드타임 단축, application 품질 향상, immutable/declarative/self-healing 원칙 기반 운영 표준 확립, 여러 개발사가 같은 기준으로 확장 가능한 전환 기반 마련으로 요약됐다.

**AWS/기술 키워드**
- AWS Transform Custom, Kiro IDE, Bedrock AgentCore Runtime, UCMP, Utopia, LG CTL, Confluence, Amazon S3, AWS native architecture, Elasticache 전환, steering/skills/powers, MCP, agentic migration

**현장 메모로 남길 점**
- 마이그레이션 자동화의 핵심은 AI가 코드를 바꾸는 것보다 “분석 결과, 설계 판단, 전환 패턴, 조직 표준”을 재사용 가능한 지식으로 축적하는 데 있었다.

**블로그용 한줄**
- “LG U+는 대규모 마이그레이션을 에이전틱 AI 워크플로로 재구성해, 전환 작업 자체를 조직 학습 시스템으로 바꾸고 있었다.”

### 전사 기반 상세 보강

- 세션 맥락: LG U+의 에이전틱 AI 기반 대규모 마이그레이션 여정
- 공식 설명 보강: LG U+ 대규모 애플리케이션 마이그레이션 사례를 기반으로, AWS Transform과 Kiro IDE를 활용한 에이전틱 AI 기반 마이그레이션 방법론을 소개합니다. 코드 분석, 리팩터링, 검증 자동화를 통해 엔터프라이즈 클라우드 마이그레이션의 속도와 품질을 동시에 향상시킨 실제 경험을 공유합니다.
- 전사에서 반복적으로 확인된 키워드: 개발, 전환, 에이전트, 코드, 표준, 운영, 테스트, 품질, 데이터, 보안
- 발표에서 두드러진 주제 축: developer, business, governance, agent

#### 발표 흐름
- 초반: 에이전트, 운영, 코드, 전환, 표준 중심으로 developer, business, governance를 다룬다.
- 중반: 에이전트, 코드, 전환, 운영, 표준 중심으로 developer, business, governance를 다룬다.
- 후반: 개발, 전환, 테스트, 표준, 에이전트 중심으로 developer, business, governance를 다룬다.

#### 전사에서 확인할 만한 구간
- 00:55 부근: 고객, 전환 관련 설명이 나온다. 핵심 문맥은 `저는 주로 엔터프라이즈 고객분들의 클라우드 전환을 돋고`
- 06:04 부근: 에이전트, 워크플로, 전환 관련 설명이 나온다. 핵심 문맥은 `저는 클라우드 전환 가속화를 위한 에이전트와 워크플로우를 설계하고 구현한 역할을 수행하고 있습니다.`
- 10:03 부근: 전환, 코드, 평가 관련 설명이 나온다. 핵심 문맥은 `이 단계에서는 실제 코드랩에서 전환의 가능성과 난이도를 평가하게 됩니다.`
- 19:08 부근: 코드, 테스트 관련 설명이 나온다. 핵심 문맥은 `어색스만 테스트 단계에서 S3에 적재된 두 결과물, 인터뷰 결과와 또 코드`
- 21:14 부근: 개발, 리뷰 관련 설명이 나온다. 핵심 문맥은 `벨드의 브렌치의 피할 형태로 생성되어서 개발자가 바로 리뷰를`
