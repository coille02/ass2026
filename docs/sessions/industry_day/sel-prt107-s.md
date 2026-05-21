# sel-prt107-s - AWS All-in 마이그레이션으로 실현한 SM하이플러스의 AI 모빌리티 전략 (sponsored by NDS)

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

- 제목: AWS All-in 마이그레이션으로 실현한 SM하이플러스의 AI 모빌리티 전략 (sponsored by NDS)
- 시간: 2026-05-20 13:50-14:10 KST
- 트랙: AWS Summit Seoul - Track 8
- 발표자: 김성수(CTO, SM 하이플러스), 김완상(Data Engineer, NDS)

### 핵심 요약

SM하이플러스/NDS 세션은 하이패스 카드 1위 사업자가 종합 모빌리티 결제 플랫폼으로 확장하기 위해 AWS All-in 마이그레이션을 추진한 사례를 공유했다. 기존 전산센터, 높은 라이선스 비용, 노후 인프라, 보안 강화 요구를 단순 서버 이전이 아니라 클라우드 기반 IT 모더나이제이션으로 해결했다. 발표에서는 카드망, 구름망, 콜센터를 포함해 6개월 만에 대규모 서버/소스코드를 AWS로 이전하고 Oracle을 Aurora PostgreSQL/RDS Oracle 19c로 전환한 과정이 소개됐다. 이후 AWS Connect, Bedrock, Redshift, QuickSight를 기반으로 AI 컨택센터와 모빌리티 데이터 플랫폼을 추진하며 AX 여정으로 확장하고 있다고 설명했다.

### 주요 포인트

- SM하이플러스는 하이패스 카드 사업을 넘어 차량 내 종합 결제/모빌리티 플랫폼 기업으로 진화하려는 비전을 제시했다.
- 레거시 전산센터 이전, 유지보수 리스크, 라이선스 비용, 보안 강화 요구가 전면 AWS 마이그레이션의 배경이었다.
- Oracle에서 Aurora PostgreSQL 및 RDS Oracle 19c로 전환하고, 오래된 Unix 환경을 클라우드 네이티브에 맞는 AWS Linux 환경으로 전환했다.
- NDS는 AWS DMS CDC, 암호화, KMS 키 관리, 해시 기반 전수 검증 등으로 금융 데이터 정합성과 보안을 보장하는 전략을 설명했다.
- 구축된 기반 위에 AWS Connect 기반 AI 컨택센터, Bedrock 에이전트, Redshift/QuickSight 데이터 플랫폼으로 AX를 확장하고 있다.

### AWS/기술 키워드

AWS All-in Migration, Amazon Aurora PostgreSQL, Amazon RDS for Oracle 19c, AWS DMS CDC, AWS KMS, Amazon Connect, Amazon Bedrock, Amazon Redshift, Amazon QuickSight, AWS Linux

### 현장 메모로 남길 점

마이그레이션 성공이 곧 끝이 아니라, AI 컨택센터와 데이터 플랫폼을 얹을 수 있는 AX 기반을 만든 것이 이 사례의 핵심이다.

### 블로그용 한줄

SM하이플러스의 AWS All-in 마이그레이션은 레거시 비용 절감에서 출발해 AI 모빌리티 플랫폼의 데이터 기반으로 이어졌다.


작성 기준: 아래 9개 세션은 모두 VOD 음성 전사(`--model base`)를 기반으로 정리했다. 전사상 일부 고유명사와 수치에는 음성 인식 오차 가능성이 있어, 공식 메타데이터의 제목/시간/발표자 정보를 함께 대조했다.
