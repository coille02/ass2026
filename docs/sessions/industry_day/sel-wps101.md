# sel-wps101 - 룰루메딕 의료마이데이터 플랫폼 혁신사례

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

**제목/시간/트랙/발표자**  
- 제목: 룰루메딕 의료마이데이터 플랫폼 혁신사례
- 시간: 2026-05-20 14:30-14:55 KST
- 트랙: Industry Day / Healthcare & Life Sciences, Professional Services / Analytics
- 발표자: 김영웅 대표이사, 룰루메딕

**핵심 요약**  
룰루메딕은 의료 마이데이터 플랫폼 `d'state`를 중심으로 흩어진 의료기록을 개인 동의 기반으로 연결하고, 이를 생활·예방·분석 서비스로 확장하는 전략을 소개했다. 발표는 해외 의료 지원 사례를 통해 처방 이력, 예방접종, 복용약 같은 데이터가 국경을 넘어 필요한 순간에 조회되어야 하는 이유를 설명했다. AWS 기반 아키텍처는 보안, 컴플라이언스, 글로벌 확장성, 24시간 가용성을 동시에 달성하기 위한 기반으로 제시됐다. 장기적으로는 업스테이지와의 AI 협력, 에이전틱 AI, 초개인화 헬스케어 서비스로 확장하는 비전을 강조했다.

**주요 포인트**
- 룰루메딕은 보건복지부 지정 보건의료 분야 개인정보관리 전문기관으로, 의료 데이터의 합법적 저장·활용·국외 이전을 핵심 차별점으로 제시했다.
- `d'state`는 병원·기관별 의료기록을 통합 조회하고, 정보주체 동의와 전송 요구 상태 관리를 기반으로 데이터 파이프라인을 만든다.
- 해외 체류 중 처방약 분실, 예방접종 이력 확인, 복용약 성분 확인 같은 사례로 의료 마이데이터 국외 이전의 실무 필요성을 설명했다.
- AWS WAF, Shield, Route 53, ALB, Transit Gateway, Network Firewall, EKS, Aurora, S3, Secrets Manager, CloudWatch 등을 조합해 다층 보안과 운영·개발 분리를 구현했다.
- 의료 마이데이터는 금융 마이데이터처럼 서비스 사업자와 클라우드 인프라가 결합될 때 AI 기반 신시장이 열린다는 관점을 제시했다.

**AWS/기술 키워드**  
Amazon EKS, Amazon Aurora, Amazon S3, AWS WAF, AWS Shield, Amazon Route 53, Elastic Load Balancing, AWS Transit Gateway, AWS Network Firewall, AWS Secrets Manager, Amazon CloudWatch, IAM, KMS, VPC Endpoint, ISMS-P, HIPAA, GDPR, Agentic AI

**현장 메모로 남길 점**  
의료 데이터 세션이지만 기술보다 규제·동의·국외 이전·보안 인증의 조합이 핵심이었다. "데이터를 모으는 앱"이 아니라 의료 AI와 글로벌 바이오데이터 사업의 기반 인프라로 포지셔닝한 점이 인상적이다.

**블로그용 한줄**  
룰루메딕은 AWS 기반 의료 마이데이터 인프라로 국내 의료기록을 안전하게 연결하고, 국외 이전과 초개인화 헬스케어 AI까지 확장하는 로드맵을 제시했다.
