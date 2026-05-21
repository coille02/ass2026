# [위로보틱스 I RLWRLD] AWS 위에서 만드는 로봇의 미래: 리얼월드의 RFM 학습과 위로보틱스의 휴머노이드 조작기능 구현

[Industry Day 세션 목록으로 돌아가기](../../industry_day_sessions.md)

## 세션 정보

- 시간: 2026-05-20 14:30-15:10 KST
- 트랙: Track 6
- 발표자: 김용재(CTO, 위로보틱스), 배재경(CTO, RLWRLD)

## 발표 주제

이 세션은 피지컬 AI 시대에 로봇 파운데이션 모델과 휴머노이드 하드웨어가 어떻게 함께 발전해야 하는지 보여준 발표다. RLWRLD는 AWS 기반 대규모 인프라에서 Robot Foundation Model을 학습한 과정을 소개했고, 위로보틱스는 휴머노이드 Alex를 통해 실제 조작 기능을 구현한 6주간의 Physical AI Fellowship 여정을 공유했다.

발표의 중심은 로봇 AI가 모델만으로 완성되지 않는다는 점이다. 데이터 수집, 시뮬레이션, 렌더링, 대규모 GPU 학습, 강화학습, 하드웨어 감각, 실시간 제어가 하나의 시스템으로 연결되어야 실제 작업을 수행하는 피지컬 AI가 된다.

## 주요 내용

- RLWRLD는 VLA 기반 Robot Foundation Model에 motion, physics, memory module을 더해 움직임 예측, 촉각과 힘 정보, 장기 맥락 기억을 보강했다고 설명했다.
- 학습 데이터는 teleoperation, human demonstration, synthetic/augmented data, open data로 구성됐다.
- multi-camera 기반 human data에서 손 관절 정보를 추출하고 로봇 동작으로 retargeting한 뒤, simulation rendering을 통해 학습 데이터로 확장하는 흐름이 소개됐다.
- 학습 인프라는 AWS ParallelCluster, Slurm, Amazon S3, Amazon FSx for Lustre, EC2 H200/L4S, Elastic Fabric Adapter 등을 활용했다.
- 원본 데이터는 S3에 두고 빠른 접근이 필요한 학습 데이터와 checkpoint는 FSx for Lustre에 두는 구조로 설명됐다.
- 위로보틱스 Alex는 15자유도 hand, 전신 force sensing, 높은 backdrivability와 compliance, 30kg 수준 payload를 특징으로 소개됐다.
- 드릴 작업 구현 과정에서는 데이터 수집, 정제, 시뮬레이션, 강화학습, 배포까지 이어지는 파이프라인이 설명됐다.

## 세부 내용

### Robot Foundation Model 학습

RLWRLD는 로봇이 실제 환경에서 작업하려면 시각 정보와 언어 명령만으로는 부족하다고 설명했다. 움직이는 물체를 예측하고, 접촉과 힘을 이해하며, 이전 맥락을 기억하는 능력이 필요하다. 이를 위해 기존 VLA 구조에 motion, physics, memory module을 더한 Robot Foundation Model 접근을 제시했다.

데이터 전략도 중요하게 다뤄졌다. teleoperation과 human demonstration, synthetic data, open data를 조합하고, 비디오 생성 모델과 pseudo action, filtering을 통해 학습 데이터를 보강한다. 사람의 동작 데이터를 로봇 동작으로 옮기는 retargeting 과정도 핵심 단계로 설명됐다.

### AWS 기반 학습 인프라

대규모 로봇 모델 학습에는 GPU와 스토리지, 네트워크가 함께 필요하다. 발표에서는 ParallelCluster와 Slurm 기반 클러스터, H200 GPU 노드, L4S 기반 렌더링과 시뮬레이션, Elastic Fabric Adapter가 소개됐다.

스토리지 구조는 원본 데이터와 고속 학습 데이터를 분리했다. S3는 원본 학습 데이터 저장소로, FSx for Lustre는 학습 중 빠르게 접근해야 하는 데이터와 checkpoint 저장소로 활용됐다. 이 구조는 로봇 모델 학습에서 데이터 이동과 I/O 병목을 줄이기 위한 설계로 설명됐다.

### 휴머노이드 Alex와 조작 기능

위로보틱스는 휴머노이드 Alex를 통해 피지컬 AI가 실제 물체와 접촉하며 작업을 수행하는 데 필요한 하드웨어 조건을 설명했다. 손의 자유도, 전신 force sensing, backdrivability, compliance 같은 특성은 로봇이 도구를 잡고 힘을 조절하는 데 중요하다.

Physical AI Fellowship에서는 드릴과 볼팅 작업을 대상으로 데이터 수집, 정제, 시뮬레이션 환경 구성, 강화학습, 배포까지 이어지는 파이프라인을 만들었다. 모방학습 후 병목 구간의 데이터를 추가로 모으고 강화학습으로 작업 속도를 개선한 사례도 소개됐다.

## 정리

이 세션의 핵심은 피지컬 AI가 모델, 데이터, 시뮬레이션, 하드웨어, 인프라의 결합으로 현실화된다는 점이다. RLWRLD는 대규모 학습 인프라와 데이터 전략을, 위로보틱스는 실제 로봇 조작과 하드웨어 감각의 중요성을 보여줬다.

로봇의 미래는 단순히 더 큰 모델을 학습하는 것만으로 오지 않는다. 실제 세계에서 움직이고 접촉하는 로봇을 만들려면 AWS 기반 학습 인프라, 시뮬레이션, 강화학습, 정교한 하드웨어 설계가 함께 맞물려야 한다는 메시지가 발표의 중심이었다.
