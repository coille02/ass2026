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

### 전사 기반 상세 보강

- 세션 맥락: [하이퍼커넥트] 하이퍼커넥트의 HyperPod 기반 Slurm on EKS 도입기
- 공식 설명 보강: 본 세션은 SageMaker HyperPod에서 Slurm 워크플로우를 유지하면서 쿠버네티스의 운영 효율을 확보한 하이퍼커넥트의 Slurm on EKS 도입 사례와 전환 과정의 교훈을 공유합니다. 또한 네트워크 기반 메모리 복제로 2분 내 장애 복구를 실현하고 95% 이상의 Goodput을 유지하는 Checkpointless Training과 Elastic Training 업데이트도 다룹니다.
- 전사에서 반복적으로 확인된 키워드: 데이터, 장애, 로그, S3, 운영, EKS, GPU, 인프라, 비용, 배포
- 발표에서 두드러진 주제 축: data, ops, infra, security

#### 발표 흐름
- 초반: EKS, 데이터, 장애, 운영, GPU 중심으로 data, ops, infra를 다룬다.
- 중반: 데이터, 로그, S3, 인증, 운영 중심으로 data, ops, infra를 다룬다.
- 후반: 장애, 비용, 운영, 데이터, S3 중심으로 data, ops, infra를 다룬다.

#### 전사에서 확인할 만한 구간
- 03:22 부근: 운영, 인프라 관련 설명이 나온다. 핵심 문맥은 `선택에 따라 인프라 운영자들이 좋아하는`
- 06:59 부근: GPU, 인프라 관련 설명이 나온다. 핵심 문맥은 `인프라 관리자 입장에서는 GPU 분할이라든지`
- 13:02 부근: EKS, 아키텍처 관련 설명이 나온다. 핵심 문맥은 `슬럼원 EKS의 아키텍처에 대해서 먼저 간단하게 설명드리겠습니다.`
- 17:06 부근: 데이터, 아키텍처 관련 설명이 나온다. 핵심 문맥은 `메달리온 아키텍처를 따라서 골드레이어로 가공된 데이터들은`
- 17:15 부근: 데이터, 인프라 관련 설명이 나온다. 핵심 문맥은 `데이터브릭스 또한 AWS 인프라를 기반으로 구축되어 있기 때문에`
