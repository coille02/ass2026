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
