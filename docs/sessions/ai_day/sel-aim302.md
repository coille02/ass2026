# [하이퍼커넥트] 하이퍼커넥트의 HyperPod 기반 Slurm on EKS 도입기

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

## 세션 정보

- 시간: 2026-05-21 12:50-13:30 KST
- 트랙: Track 1
- 레벨: 300 - Advanced
- 발표자: 오준석(AWS), 현륜식(AWS), 윤보현(하이퍼커넥트)
- 주제: Architecture, Artificial Intelligence, Compute

## 발표 주제

본 세션은 SageMaker HyperPod에서 Slurm 워크플로우를 유지하면서 쿠버네티스의 운영 효율을 확보한 하이퍼커넥트의 Slurm on EKS 도입 사례와 전환 과정의 교훈을 공유합니다. 또한 네트워크 기반 메모리 복제로 2분 내 장애 복구를 실현하고 95% 이상의 Goodput을 유지하는 Checkpointless Training과 Elastic Training 업데이트도 다룹니다.

SageMaker HyperPod에서 기존 Slurm 워크플로우를 유지하면서 EKS의 운영 효율을 확보한 하이퍼커넥트 사례. Slurm on EKS 전환 과정과 Checkpointless Training, Elastic Training 등 대규모 학습 운영의 최신 개선점을 소개했다.

## 주요 내용

- HyperPod는 대규모 모델 훈련/배포를 위한 맞춤형 인프라와 노드 복원력을 제공.
- Slurm 사용자 경험을 유지하면서 Kubernetes/EKS 기반 운영 자동화와 리소스 관리를 결합.
- 하이퍼커넥트는 동일 인프라에서 Slurm과 EKS를 활용하며 운영 효율과 전환 리스크를 함께 관리.
- 네트워크 기반 메모리 복제로 2분 내 장애 복구와 95% 이상 Goodput을 지향하는 Checkpointless Training도 다룸.

## 세부 내용

### 문제의식과 배경

HyperPod는 대규모 모델 훈련/배포를 위한 맞춤형 인프라와 노드 복원력을 제공. Slurm 사용자 경험을 유지하면서 Kubernetes/EKS 기반 운영 자동화와 리소스 관리를 결합.

### 접근 방식과 아키텍처

하이퍼커넥트는 동일 인프라에서 Slurm과 EKS를 활용하며 운영 효율과 전환 리스크를 함께 관리. 네트워크 기반 메모리 복제로 2분 내 장애 복구와 95% 이상 Goodput을 지향하는 Checkpointless Training도 다룸.

### 운영 포인트와 확장 방향

관련 기술 키워드는 SageMaker HyperPod, Slurm on EKS, Amazon EKS, Checkpointless Training, Elastic Training, Goodput, 분산 학습이다.

## 정리

이 세션의 핵심은 [하이퍼커넥트] 하이퍼커넥트의 HyperPod 기반 Slurm on EKS 도입기를 단순한 기능 소개가 아니라 실제 업무와 운영 환경에 적용하기 위한 조건으로 풀어냈다는 점이다. HyperPod는 대규모 모델 훈련/배포를 위한 맞춤형 인프라와 노드 복원력을 제공.

발표는 AI 인프라의 성능을 확보하려면 컴퓨팅 자원뿐 아니라 네트워크, 스토리지, 장애 복구, 운영 자동화를 함께 봐야 한다는 메시지로 정리된다.
