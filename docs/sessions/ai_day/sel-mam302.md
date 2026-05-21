# sel-mam302 - AIOps 도전과 실전: AI SecOps에서 DevOps 에이전트까지

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

- 시간/트랙/레벨/발표자: 16:10-16:50 KST / Track 4 / 300 - Advanced / 이연수, 테크니컬 어카운트 매니저, AWS; 박종진, 테크니컬 어카운트 매니저, AWS; 현승열, 선임 엔지니어, 삼성전자
- 요약: 삼성전자 계정 서비스의 WAF 로그 분석 AI SecOps 사례와 AWS DevOps Agent를 소개했다. 삼성전자 사례는 대규모 트래픽과 하루 TB급 보안 로그를 사람이 분석하는 한계를 Bedrock, Strands Agents, 멀티 에이전트 구조로 해결하려는 여정이었다.
- 주요 포인트:
  - 삼성 계정은 21억 사용자와 초당 대규모 트래픽을 처리하며, WAF 로그 기반 악성 트래픽 분석을 수행한다.
  - AI로 공격 패턴이 빠르게 바뀌면서 고정 룰과 수동 로그 분석만으로는 대응이 어렵고, 자연어 질의로 WAF 로그를 조회/분석/리포트화하는 필요가 커졌다.
  - Bedrock Agent Builder로 빠르게 시작했지만 복잡한 질의와 해석 품질에 한계가 있어 Strands Agents와 멀티 에이전트 구조로 확장했다.
  - 후반부 AWS DevOps Agent 데모는 조사, 완화, MCP 서버 연동, 스킬/채팅, 사전 예방 권장사항을 통해 장애 대응과 예방 조치를 자동화하는 흐름을 보여줬다.
- AWS/기술 키워드: Amazon Bedrock, Bedrock Agent Builder, Strands Agents SDK, AWS WAF, Amazon EKS, Amazon CloudWatch, MCP, DevOps Agent, AI SecOps, AIOps
- AX TF 관점/회사 AX 도입 시사점: 운영/보안 영역은 AX 효과가 바로 보이는 영역이다. 로그 조회 SQL 생성에 그치지 말고, 탐지, 분석, 원인 요약, 대응 제안, 재발 방지 권고까지 역할을 나눈 멀티 에이전트 워크플로로 설계해야 한다.
- 공유용 한줄: AIOps의 현실적 출발점은 "사람이 보던 로그"를 에이전트가 질의, 해석, 조치 제안까지 이어주는 것이다.
