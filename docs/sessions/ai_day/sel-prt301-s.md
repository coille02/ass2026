# sel-prt301-s - Secure AI by Design (sponsored by Palo Alto Networks)

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

- 시간/트랙/레벨/발표자: 13:50-14:10 KST / Partner Track / 300 Advanced / 김범수(Palo Alto Networks)
- 요약: AI 사용과 AI 개발을 모두 설계 단계부터 보안 내재화해야 한다는 메시지의 세션이었다. Prisma Browser는 임직원의 외부 생성형 AI 사용을 발견·평가·통제하고, Prisma AIRS는 AI 애플리케이션과 에이전트 생태계의 모델, 데이터, 플러그인, 런타임, 프롬프트 인젝션, 데이터 유출 위험을 보호하는 플랫폼으로 소개됐다.
- 주요 포인트:
  - 승인되지 않은 AI 서비스 사용과 민감정보 입력은 이미 현실적인 Shadow AI 리스크다.
  - 브라우저 계층에서 어떤 AI 도구를 누가 쓰는지 발견하고, 리스크와 데이터 정책을 적용해야 한다.
  - AI 앱은 모델, 데이터셋, 플러그인, 에이전트, 런타임이 연결된 생태계라 포인트 솔루션만으로는 복잡도가 커진다.
  - AI red teaming, model security, posture management, runtime security, prompt injection 탐지, 데이터 유출 차단이 함께 필요하다.
- AWS/기술 키워드: Prisma Browser, Prisma AIRS, AI governance, Shadow AI, AI red teaming, prompt injection, model security, runtime security, DLP
- AX TF 관점/회사 AX 도입 시사점: AX TF는 사내 AI 사용 가시성부터 확보해야 한다. 승인 AI 도구 목록, 민감정보 입력 차단, 자체 AI 앱 보안 점검, 에이전트 권한 관리가 함께 설계되어야 한다.
- 공유용 한줄: AI 보안은 차단 정책이 아니라 발견, 허용, 통제, 보호를 한 번에 설계하는 일이다.

### 전사 기반 상세 보강

- 세션 맥락: Secure AI by Design (sponsored by Palo Alto Networks)
- 공식 설명 보강: "설계 단계부터 안전한 AI를 구축하는" 접근 방식은 AI 시대에 있어 모든 조직에게 매우 중요합니다. 외부 AI 거버넌스를 위한 Prisma Browser와 안전한 애플리케이션 개발 및 에이전트 제어를 위한 Prisma AIRS를 통해 혁신에 대한 두려움을 없애고, 현대 기업의 위험에 맞춰 설계된 통합 플랫폼으로 AI 생태계를 안전하게 보호하십시오.
- 전사에서 반복적으로 확인된 키워드: 데이터, 개발, 보안, 에이전트, 리스크, 평가, 코드, 운영, 정책, 배포
- 발표에서 두드러진 주제 축: data, developer, security, ops

#### 발표 흐름
- 초반: 보안, 데이터, 운영, 에이전트, 개발 중심으로 data, developer, security를 다룬다.
- 중반: 데이터, 보안, 에이전트, 개발, 코드 중심으로 data, developer, security를 다룬다.
- 후반: 데이터, 개발, 평가, 리스크, 에이전트 중심으로 data, developer, security를 다룬다.

#### 전사에서 확인할 만한 구간
- 01:48 부근: 데이터, 운영 관련 설명이 나온다. 핵심 문맥은 `AI 코딩 도구가 운영 데이터베이스를 삭제한 사례.`
- 05:36 부근: 데이터 관련 설명이 나온다. 핵심 문맥은 `또한 약 15%의 직원들은 이미 민감한 회사의 데이터를 공개된 AI 도구에 입력한 경험이 있다고 합니다.`
- 14:27 부근: 데이터, 인가 관련 설명이 나온다. 핵심 문맥은 `비인가 접근차단 데이터함이 모델 변조시도를`
- 15:05 부근: 데이터 관련 설명이 나온다. 핵심 문맥은 `데이터 모델에 노란불이 하나 들어와 있습니다.`
- 15:07 부근: 리스크 관련 설명이 나온다. 핵심 문맥은 `가시성 안에서 리스크 평가를 해서 지금 어떤 위험 도가 있는지 확인을 해 보일 수 있고요.`
