# sel-ind203 - [여기어때컴퍼니] Kiro CLI로 실현한 여기어때의 데이터베이스 현대화

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

- 제목: [여기어때컴퍼니] Kiro CLI로 실현한 여기어때의 데이터베이스 현대화
- 시간: 2026-05-20 11:10-11:50 KST
- 트랙: AWS Summit Seoul - Track 8
- 발표자: 김지훈 (솔루션즈 아키텍트, AWS), 전상학 (플랫폼 엔지니어링 실장, 여기어때컴퍼니)

### 핵심 요약
여기어때컴퍼니는 차세대 항공권 발권 시스템의 데이터베이스를 Oracle에서 Aurora MySQL로 이전하면서 Kiro CLI와 Oracle Modernization Accelerator/Agent 접근을 활용했다. 세션은 이기종 데이터베이스 마이그레이션이 스키마 변환, 데이터 이동, 애플리케이션 SQL 변환, 검증과 성능 테스트를 모두 포함해 큰 공수가 드는 작업이라고 설명했다. 여기어때는 16,000개 SQL, 수백 개 MyBatis 맵 파일, 1,500개 DB 오브젝트를 대상으로 6주 여정을 구성했고, Kiro CLI를 활용해 Oracle 전용 함수와 힌트, 동적 MyBatis 조건문을 Aurora MySQL에 맞게 변환했다. 사람은 반복 변환보다 판단과 검증에 집중하도록 역할을 재배치한 점이 핵심 성과로 제시됐다.

### 주요 포인트
- 이기종 DB 현대화는 대상 DB 지식, 스키마 변경, 데이터 적재, 애플리케이션 SQL 호환성, 검증과 부하 테스트를 모두 요구
- AWS는 Oracle Modernization Accelerator를 발전시켜 에이전트 기반 Oracle Modernization Agent로 확장하는 방향을 소개
- 자동화 대상은 스키마 변환, 데이터 마이그레이션, 애플리케이션 변환, 검증 단계로 구성
- 여기어때 사례는 16,000개 SQL, 수백 개 MyBatis Map 파일, 1,500개 DB 오브젝트를 변환한 대규모 프로젝트
- 6주 동안 분석, 변환, 검증, 보완을 반복하며 수작업 중심의 예상 공수를 줄이고 일정 리스크를 낮춤

### AWS/기술 키워드
- Kiro CLI, Oracle Modernization Accelerator, Oracle Modernization Agent, Amazon Aurora MySQL, MyBatis, SQL 변환, 데이터베이스 현대화, GenAI 기반 마이그레이션

### 현장 메모로 남길 점
- 생성형 AI의 가치는 "SQL을 자동으로 바꾼다"보다 반복 변환을 줄이고 사람이 검증과 의사결정에 집중하게 만든 데 있었다.

### 블로그용 한줄
> 여기어때는 Kiro CLI와 AWS의 DB 현대화 접근을 활용해 1년 이상 걸릴 수 있던 Oracle to Aurora MySQL 전환을 6주 프로젝트로 압축했다.


> Worker 2 assigned sessions: sel-wps105, sel-ind225, sel-ind233, sel-ind206, sel-ind212, sel-ind210, sel-ind224, sel-ind302, sel-ind204. All summaries below are based on generated VOD transcripts plus official session metadata.

### 전사 기반 상세 보강

- 세션 맥락: [여기어때컴퍼니] Kiro CLI로 실현한 여기어때의 데이터베이스 현대화
- 공식 설명 보강: 여기어때는 차세대 항공권 발권 시스템을 Oracle Modernization Accelerator 프로그램을 통해 Oracle에서 Aurora MySQL로 1년 이상 예상되는 16,000개 SQL의 변환을 Kiro CLI를 활용하여 6주만에 완료했습니다. 이 사례는 비용 효율화와 일정 준수를 달성한 Gen AI 기반 레거시 현대화 성공 사례입니다.
- 전사에서 반복적으로 확인된 키워드: 데이터, 에이전트, 전환, 고객, 테스트, 로그, 비용, 운영, 자동화, 인프라
- 발표에서 두드러진 주제 축: data, business, agent, developer

#### 발표 흐름
- 초반: 데이터, 테스트, 자동화, 전환, 로그 중심으로 data, business, agent를 다룬다.
- 중반: 에이전트, 고객, 데이터, 전환, 인프라 중심으로 data, business, agent를 다룬다.
- 후반: 데이터, 전환, 테스트, 로그, 운영 중심으로 data, business, developer를 다룬다.

#### 전사에서 확인할 만한 구간
- 01:39 부근: 고객, 데이터 관련 설명이 나온다. 핵심 문맥은 `6, 7년 정도 기간 동안 많은 데이터베이스 마이 그레이션을 검토하고 계시는 고객분들을 만나 뵙고`
- 05:23 부근: 데이터 관련 설명이 나온다. 핵심 문맥은 `그리고 이게 끝나고 나면 오락크레이는 데이터를 마이 에스쿨으로 이제 옮겨줘야죠`
- 13:52 부근: 에이전트, 자동화 관련 설명이 나온다. 핵심 문맥은 `다 자동화 프로세스, 모든 부분들이 다 에이전트화 돼서`
- 15:07 부근: 고객 관련 설명이 나온다. 핵심 문맥은 `어떤 고객사에 가서 보니까`
- 15:34 부근: 고객 관련 설명이 나온다. 핵심 문맥은 `어떤 고객사회가 또는 맥스 함수를 쓰시지 않으시고, 흰트를 줘가지고,`
