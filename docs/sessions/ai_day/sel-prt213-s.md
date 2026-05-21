# sel-prt213-s - Amazon Bedrock 기반 GitLab Duo 에이전트 플랫폼으로 혁신 가속화 (sponsored by Gitlab)

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

- 시간/트랙/레벨/발표자: 13:50-14:10 KST / Partner Track / 200 Intermediate / Jimmy Gam(GitLab)
- 요약: GitLab Duo Agent Platform이 Amazon Bedrock과 결합해 SDLC 전반에 에이전틱 AI를 내재화하는 방식을 소개했다. IDE나 CLI에 흩어진 AI 도구가 컨텍스트를 잃는 문제를 지적하며, 계획, 코딩, 코드리뷰, 보안, 컴플라이언스, CI/CD 데이터를 하나의 데이터 모델과 워크플로우 안에서 활용하는 접근을 제시했다.
- 주요 포인트:
  - 코드 작성 속도만 빨라져도 코드리뷰, 보안 스캔, 테스트, 승인 과정이 따라오지 못하면 전체 생산성은 제한된다.
  - GitLab의 통합 데이터 모델은 issue, merge request, pipeline, 취약점, 정책 데이터를 에이전트 컨텍스트로 제공한다.
  - Amazon Bedrock 연동은 IAM, VPC endpoint, 리전 데이터 보관 등 AWS 보안 패턴을 활용해 데이터 레지던시 요구를 맞춘다.
  - 외부 에이전트와의 통합도 지원하되, 승인된 모델과 AI Gateway를 통해 사용량·정책·거버넌스를 통제한다.
- AWS/기술 키워드: GitLab Duo Agent Platform, Amazon Bedrock, AI Gateway, SDLC, DevSecOps, IAM, VPC endpoint, data residency, merge request
- AX TF 관점/회사 AX 도입 시사점: AI 코딩 도구를 개별 IDE 플러그인으로만 보면 거버넌스가 빠진다. 사내 Git 플랫폼의 이슈, MR, CI, 보안 결과를 에이전트 컨텍스트로 연결하는 표준이 필요하다.
- 공유용 한줄: 개발 AI의 생산성은 IDE 안이 아니라 SDLC 전체 데이터 모델 안에서 완성된다.

### 전사 기반 상세 보강

- 세션 맥락: Amazon Bedrock 기반 GitLab Duo 에이전트 플랫폼으로 혁신 가속화 (sponsored by Gitlab)
- 공식 설명 보강: GitLab Duo Agent Platform이 Amazon Bedrock 기반으로 전체 SDLC에 에이전틱 AI를 내재화하는 방법을 살펴보세요 — 데이터를 AWS 환경 또는 고객 내부에 안전하게 유지합니다. AI Gateway로 기획·코딩·보안·컴플라이언스 워크플로우를 오케스트레이션해 데이터 레지던시 충족·AWS 투자 극대화를 실현하세요.
- 전사에서 반복적으로 확인된 키워드: 에이전트, 코드, 개발, 데이터, 고객, 배포, 보안, 감사, 인프라, 승인
- 발표에서 두드러진 주제 축: developer, agent, security, business

#### 발표 흐름
- 초반: 코드, 개발, 에이전트, 리뷰, agent 중심으로 developer, agent, business를 다룬다.
- 중반: 에이전트, 보안, 코드, 데이터, 감사 중심으로 developer, agent, security를 다룬다.
- 후반: 고객, 에이전트, 데이터, 개발, 배포 중심으로 developer, agent, security를 다룬다.

#### 전사에서 확인할 만한 구간
- 04:41 부근: 리뷰, 코드, 테스트 관련 설명이 나온다. 핵심 문맥은 `코드리뷰, 보완 스케닉, 테스트 커버리지,`
- 05:18 부근: 리뷰, 코드 관련 설명이 나온다. 핵심 문맥은 `소프트웨어 라이브 사이크를 각 단계 계획, 코딩, 코드 리뷰, 보완`
- 10:03 부근: 에이전트 관련 설명이 나온다. 핵심 문맥은 `에이전트는 멀티스텝 플랫을 자율적으로 생성하고 실행할 수 있습니다.`
- 15:01 부근: 코드 관련 설명이 나온다. 핵심 문맥은 `코드 수정이나 sasst 취약점 교정.`
- 15:16 부근: 고객 관련 설명이 나온다. 핵심 문맥은 `prompt, code 응답이 절대 지금 고객분들의 환경 밖으로 나가지가 않는`
