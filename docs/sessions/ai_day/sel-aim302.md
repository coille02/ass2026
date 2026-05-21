# sel-aim302 - [하이퍼커넥트] 하이퍼커넥트의 HyperPod 기반 Slurm on EKS 도입기

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

- 시간/트랙/레벨/발표자: 12:50-13:30 / Track 1 / 300 Advanced / 오준석(AWS), 현륜식(AWS), 윤보현(하이퍼커넥트)
- 요약: SageMaker HyperPod에서 기존 Slurm 워크플로우를 유지하면서 EKS의 운영 효율을 확보한 하이퍼커넥트 사례. Slurm on EKS 전환 과정과 Checkpointless Training, Elastic Training 등 대규모 학습 운영의 최신 개선점을 소개했다.
- 주요 포인트:
  - HyperPod는 대규모 모델 훈련/배포를 위한 맞춤형 인프라와 노드 복원력을 제공.
  - Slurm 사용자 경험을 유지하면서 Kubernetes/EKS 기반 운영 자동화와 리소스 관리를 결합.
  - 하이퍼커넥트는 동일 인프라에서 Slurm과 EKS를 활용하며 운영 효율과 전환 리스크를 함께 관리.
  - 네트워크 기반 메모리 복제로 2분 내 장애 복구와 95% 이상 Goodput을 지향하는 Checkpointless Training도 다룸.
- AWS/기술 키워드: SageMaker HyperPod, Slurm on EKS, Amazon EKS, Checkpointless Training, Elastic Training, Goodput, 분산 학습
- AX TF 관점/회사 AX 도입 시사점: 기존 개발/ML 워크플로우를 한 번에 갈아엎기보다 익숙한 도구를 유지하면서 운영 기반을 현대화하는 방식이 현실적이다. 사내 AX도 IDE, Git, 이슈 흐름은 유지하되 에이전트와 자동화를 옆에 붙이는 전환 전략이 유효하다.
- 공유용 한줄: 성공적인 AI 인프라 전환은 기존 워크플로우를 존중하면서 운영 자동화 계층을 점진적으로 얹는 방식이 강하다.
