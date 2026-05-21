# sel-aim205 - 당신의 새로운 AI 업무 파트너, Amazon Quick

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

- 시간/트랙/레벨/발표자: 16:10-16:50 KST / Track 8 / 200 - Intermediate / 채정희, 솔루션즈 아키텍트, AWS; 이지연, 솔루션즈 아키텍트, AWS
- 요약: Amazon Quick을 회사 데이터와 업무 시스템에 연결된 AI 업무 파트너로 소개했다. 발표자는 직원들이 여러 앱을 오가며 정보를 찾고 정리하는 데 많은 시간을 쓰는 문제를 짚고, Quick이 자연어 검색, 맥락 있는 답변, 실행, 보안/거버넌스를 한 경험으로 묶는다고 설명했다.
- 주요 포인트:
  - 소비자 AI는 편하지만 회사 데이터, 권한, 내부 정책을 모르기 때문에 업무 적용에는 한계가 있다.
  - Quick은 문서, 데이터베이스, 이메일, Slack, 대시보드, Jira 등 회사 시스템에 연결되어 질문과 실행을 한 곳에서 처리하도록 설계됐다.
  - 데모 흐름에서는 마케팅 팀원이 대시보드/문서/웹 페이지를 참고해 인사이트를 얻고 반복 작업을 자동화하는 방식을 보여줬다.
  - VPC 엔드포인트, 데이터 리전 내 보관, 모델 학습 미사용, IAM/IAM Identity Center/SAML/AD 연동, CloudWatch/CloudTrail 감사 로그를 보안/거버넌스 근거로 제시했다.
  - 발표자는 Quick의 핵심을 모든 데이터 연결, 답변 이후 실행, 엔터프라이즈 보안/AI 거버넌스로 정리했다.
- AWS/기술 키워드: Amazon Quick, Amazon QuickSight, Slack, Jira, VPC Endpoint, IAM, IAM Identity Center, SAML, Active Directory, Amazon CloudWatch, AWS CloudTrail, AI Governance
- AX TF 관점/회사 AX 도입 시사점: 사내 AX 포털은 단순 Q&A보다 "찾기-판단-실행"을 연결해야 한다. 단, 기존 권한 체계를 그대로 존중하고 감사 로그를 남기는 방식이어야 조직 내 확산이 가능하다.
- 공유용 한줄: Amazon Quick은 흩어진 사내 정보를 한 AI 업무 동료로 묶고, 답변에서 실행까지 이어가려는 업무 AX 플랫폼이다.
