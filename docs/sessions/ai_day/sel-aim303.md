# sel-aim303 - 40분 완성! SageMaker AI 기반 에이전틱 모델 구축 및 배포

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

- 시간/트랙/레벨/발표자: 16:10-16:50 KST / Track 1 / 300 - Advanced / 박지윤, 솔루션즈 아키텍트, AWS; 강광일, 테크니컬 어카운트 매니저, AWS
- 요약: SageMaker AI로 에이전틱 AI에 필요한 모델 커스터마이징, 배포, AgentCore 연동까지 엔드투엔드로 구현하는 흐름을 다뤘다. 발표자는 생성형 AI에서 에이전틱 AI로 넘어가며 추론 컴퓨팅 요구가 커지고, 업무별 모델을 비용 효율적으로 커스터마이징/서빙하는 역량이 중요해졌다고 설명했다.
- 주요 포인트:
  - 에이전틱 워크플로는 다단계 추론과 tool call 때문에 토큰/컴퓨팅 수요가 급증하며, 모델 커스터마이징과 쿼터/용량 관리가 중요해진다.
  - Salesforce 사례를 들어 오픈소스 모델 기반 사전학습/파인튜닝/고품질 답변 튜닝으로 hallucination을 줄이고 특화 모델을 운영하는 패턴을 소개했다.
  - SageMaker AI의 파인튜닝 환경, 멀티 모델/멀티 컨테이너/Inference Component 기반 배포, 비용 효율적 엔드포인트 운영을 설명했다.
  - 데모에서는 의료 상담 모델을 배포하고 Bedrock AgentCore Runtime에 Docker 기반 에이전트를 배포해 증상 질의, 병원 추천, 예약 흐름까지 연결했다.
- AWS/기술 키워드: Amazon SageMaker AI, Fine-tuning, Open-source LLM, vLLM DLC, Inference Component, Multi-model Endpoint, Amazon Bedrock AgentCore Runtime, AWS CodeBuild
- AX TF 관점/회사 AX 도입 시사점: 범용 모델 호출만으로 끝내지 말고, 업무 도메인별 특화 모델을 만들고 이를 에이전트 런타임에 연결하는 표준 파이프라인이 필요하다. 특히 비용 추적, 엔드포인트 배포 방식, 평가 기준을 초기에 잡아야 AX 서비스가 실험 단계에서 운영 단계로 넘어갈 수 있다.
- 공유용 한줄: SageMaker AI는 특화 모델을 만들고 AgentCore에 붙이는 AX 모델 운영 파이프라인의 좋은 기준점이다.
