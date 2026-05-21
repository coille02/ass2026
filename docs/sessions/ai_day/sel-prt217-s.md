# sel-prt217-s - Oracle AI Database@AWS! AWS는 그대로, Exadata로 더욱 강력하게!(sponsored by Oracle)

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

- 시간/트랙/레벨/발표자: 2026-05-21 15:30-15:50 KST / Track 2 / 200 - Intermediate / 조경진(Oracle Korea)
- 요약: Oracle AI Database@AWS를 통해 AWS 환경에서 Oracle Exadata와 Oracle AI Database 26ai를 활용하는 방안을 소개한 스폰서 세션이다. 온프레미스와 클라우드가 분리된 구조에서 생기는 데이터 이동, 운영 복잡도, 성능 요구를 줄이고, AWS 서비스와 Oracle 데이터베이스의 강점을 함께 쓰는 구성이 중심이었다. AI 관점에서는 데이터베이스 안의 데이터, 벡터/AI 기능, 보안과 운영을 함께 묶어 활용하는 메시지가 강조됐다.
- 주요 포인트:
  - Oracle AI Database@AWS는 AWS 안에서 Exadata 기반 Oracle 데이터베이스 성능과 운영 모델을 쓰는 선택지로 소개됐다.
  - Oracle AI Database 26ai는 AI 개발과 데이터 활용을 데이터베이스 레이어에서 지원하는 방향을 제시한다.
  - 온프레미스-클라우드 분리로 인한 데이터 이동과 운영 부담을 줄이는 것이 주요 가치다.
  - AI가 데이터를 스스로 활용하려면 데이터가 있는 위치의 성능, 보안, 운영 통제가 함께 보장되어야 한다.
- AWS/기술 키워드: Oracle AI Database@AWS, Oracle AI Database 26ai, Exadata, Autonomous Database, Databases, Cloud Operations
- AX TF 관점/회사 AX 도입 시사점: 핵심 업무 데이터가 Oracle에 남아 있는 조직은 AI를 위해 무조건 데이터를 이동하기보다, DB 근처에서 AI 기능과 클라우드 서비스를 결합하는 아키텍처를 검토할 필요가 있다. AX TF는 데이터 이동 비용, 권한, 성능, 기존 DBA 운영 모델을 포함해 AI 데이터 접근 전략을 세워야 한다.
- 공유용 한줄: Oracle 기반 핵심 데이터를 가진 조직의 AX는 데이터 이관보다, 기존 DB 성능과 AWS AI 생태계를 함께 쓰는 경로가 현실적일 수 있다.

### 전사 기반 상세 보강

- 세션 맥락: Oracle AI Database@AWS! AWS는 그대로, Exadata로 더욱 강력하게!(sponsored by Oracle)
- 공식 설명 보강: AWS에서 Oracle Exadata 서비스를 활용할 수 있는 Oracle AI Database@AWS를 소개합니다. Oracle AI Database 26ai를 기반으로 Exadata 서비스 및 자율운영 데이터베이스로 제공되는 오라클 데이터베이스의 핵심 기능과 성능을 이제 AWS에서도 바로 활용하세요.
- 전사에서 반복적으로 확인된 키워드: 데이터, 에이전트, 운영, 개발, 권한, 감사, 인프라, MCP, 보안, 인가
- 발표에서 두드러진 주제 축: data, agent, security, ops

#### 발표 흐름
- 초반: 데이터, 운영, 인프라, 개발, 인가 중심으로 data, security, ops를 다룬다.
- 중반: 데이터, 에이전트, MCP, 개발, 인가 중심으로 data, agent, security를 다룬다.
- 후반: 데이터, 권한, 감사, 보안, 운영 중심으로 data, agent, security를 다룬다.

#### 전사에서 확인할 만한 구간
- 01:19 부근: 데이터, 운영 관련 설명이 나온다. 핵심 문맥은 `운영하고 계시지만 사실 중요한 데이터베이스가`
- 07:43 부근: 데이터, 에이전트 관련 설명이 나온다. 핵심 문맥은 `에이전트를 만들거나 또는 자연어로다가 데이터로 조회하거나 하는 여러 가지`
- 12:51 부근: 데이터, 인가 관련 설명이 나온다. 핵심 문맥은 `이제 AI가 어떤 데이터를 정확히 접근하고 뽑아낼 것인가에 대한 것들을 판단을 할 수 있겠죠.`
- 15:06 부근: 권한, 데이터 관련 설명이 나온다. 핵심 문맥은 `AI가 데이터를 처리하기 위해서 굉장히 많은 권한을 갖게 됩니다.`
- 15:20 부근: 권한, 에이전트 관련 설명이 나온다. 핵심 문맥은 `그렇기 때문에 에이전트가 굉장히 높은 수준에 권한을 갖게 되는 경우가 많이 있습니다.`
