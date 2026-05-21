# sel-ind232 - [현대지에프홀딩스] SMUS 기반 전사 MLOps 플랫폼으로 실현한 데이터 혁명

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

**제목/시간/트랙/발표자**  
- 제목: [현대지에프홀딩스] SMUS 기반 전사 MLOps 플랫폼으로 실현한 데이터 혁명
- 시간: 2026-05-20 15:30-15:50 KST
- 트랙: Industry Day / Retail & Consumer Goods / Analytics, Artificial Intelligence
- 발표자: 곽영화 Senior Solutions Architect, AWS; 김철중 책임, 현대지에프홀딩스

**핵심 요약**  
AWS는 AI 프로젝트의 실패 원인이 모델이 아니라 AI-ready 데이터 부재에 있다는 문제의식으로 Amazon SageMaker Unified Studio를 소개했다. 현대백화점그룹은 14개 계열사, 1,600만 H.Point 회원, 연간 수십억 건의 데이터를 전사 AI 자산으로 전환하기 위해 SMUS 기반 MLOps 플랫폼을 구축했다. 발표는 인프라 파편화, 분석 환경 부재, 배포 병목을 해결하기 위해 통합 환경 구축, 모델 검증, 거버넌스 설계를 단계적으로 진행한 16개월 여정을 공유했다. 결과적으로 웨딩 예정 지수 등 라이프 스코어를 지속 생성하는 파이프라인과 계열사 확산 가능한 표준 MLOps 운영 모델을 만들었다.

**주요 포인트**
- 엔터프라이즈 AI의 조건으로 분석·AI 통합, 데이터 사일로 해소, 거버넌스, 운영 확장성을 제시했다.
- 현대백화점그룹은 H.Point DW를 중심으로 계열사 데이터를 수집·전처리하고, Redshift Data Sharing으로 복제 없이 필요한 데이터를 연결했다.
- 데이터 카탈로그와 구독·승인 프로세스를 통해 데이터 소유자가 목적과 기간을 검토하고 Lake Formation 기반 권한을 자동 부여하는 구조를 만들었다.
- MLOps 파이프라인은 데이터 ETL, 피처 생성, 학습·평가, 챔피언 모델 선정, 배치 추론, S3/DW 적재, CRM·마케팅 활용까지 자동화했다.
- 웨딩 예정 모델은 변수와 데이터 규모를 3배 이상 확대하고, F1 계열 지표 기준 약 10% 성능 개선과 리콜 향상을 달성했다고 설명했다.

**AWS/기술 키워드**  
Amazon SageMaker Unified Studio, Amazon Redshift Data Sharing, AWS Lake Formation, Amazon S3, Data Catalog, MLOps Pipeline, Batch Inference, AI-ready Data, Data Governance, H.Point DW

**현장 메모로 남길 점**  
현대백화점그룹 사례의 강점은 "모델 하나"보다 조직 확산 구조에 있었다. MVP로 검증하고, 거버넌스를 처음부터 넣고, 계열사 데이터 사이언티스트를 육성한 점이 실무적으로 중요하다.

**블로그용 한줄**  
현대지에프홀딩스는 SageMaker Unified Studio 기반 전사 MLOps 플랫폼으로 그룹 데이터를 AI-ready 자산으로 바꾸고, 마케팅·CRM까지 이어지는 표준 AI 운영 체계를 구축했다.
