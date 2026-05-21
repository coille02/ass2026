# sel-ind230 - [위로보틱스 I RLWRLD] AWS 위에서 만드는 로봇의 미래: 리얼월드의 RFM 학습과 위로보틱스의 휴머노이드 조작기능 구현

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

**제목/시간/트랙/발표자**  
- 제목: [위로보틱스 I RLWRLD] AWS 위에서 만드는 로봇의 미래: 리얼월드의 RFM 학습과 위로보틱스의 휴머노이드 조작기능 구현
- 시간: 2026-05-20 14:30-15:10 KST
- 트랙: Aerospace & Satellite, Federal Government, Manufacturing & Industrial / Artificial Intelligence, Business Applications, Industry Solutions
- 발표자: 김용재 CTO(위로보틱스), 배재경 CTO(RLWRLD)

**핵심 요약**  
RLWRLD와 위로보틱스는 피지컬 AI에서 로봇 파운데이션 모델과 하드웨어 플랫폼이 어떻게 함께 발전해야 하는지를 보여줬다. RLWRLD는 VLA 기반 Robot Foundation Model에 motion, physics, memory module을 더해 움직이는 물체 예측, 촉각/힘 정보 활용, 장기 맥락 기억을 강화했고, 이를 AWS의 대규모 GPU/스토리지 인프라로 학습했다. 학습에는 S3, FSx for Lustre, ParallelCluster, H200 GPU 64 nodes, L4S 기반 렌더링/시뮬레이션, Elastic Fabric Adapter 등이 활용됐다. 위로보틱스는 힘과 접촉을 잘 느끼는 휴머노이드 Alex를 소개하며, AWS Physical AI Fellowship에서 드릴/볼팅 조작 파이프라인을 6주 안에 구축한 여정을 공유했다.

**주요 포인트**
- RLWRLD의 모델은 VLA 구조에 액션 헤드를 붙인 형태이며, 기존 VLA가 약한 움직임 예측, 촉각/힘 정보, 기억 기반 작업을 보완하는 세 모듈을 강조했다.
- 데이터는 teleoperation, human demonstration, synthetic/augmented data, open data로 구성되며, 비디오 생성 모델과 IDM 기반 pseudo action, filtering으로 증강했다.
- human data는 wearable 없이 multi-camera로 사람 손 관절 정보를 추출하고 로봇으로 retargeting한 뒤 simulation 렌더링을 통해 학습 데이터로 만들었다.
- pretrain/mid-train/fine-tuning 구조로 학습했고, H200 GPU 64 nodes에서 pretrain은 약 8일 이상, mid-train은 하루 미만이 걸렸다고 설명했다.
- ParallelCluster는 Slurm 기반으로 활용됐고, 원본 데이터는 S3, 빠른 접근이 필요한 학습 데이터와 checkpoint는 FSx for Lustre에 두었다.
- 모방학습 후 병목 구간에 추가 데이터를 모으고, 강화학습으로 손잡이를 돌리는 작업의 속도를 기존 대비 약 3배 높인 사례가 소개됐다.
- 위로보틱스 Alex는 15자유도 hand, 전신 force sensing, 높은 backdrivability/compliance, 30kg 수준 payload를 강조했다.
- Physical AI Fellowship에서는 Amazon Kinesis, S3, Glue, EC2, NVIDIA Isaac Lab/물리 엔진을 활용해 데이터 수집, 정제, 강화학습, 배포 파이프라인을 구축했다.

**AWS/기술 키워드**
- AWS ParallelCluster, Slurm, Amazon S3, Amazon FSx for Lustre, Amazon EC2 H200/L4S, Elastic Fabric Adapter, AWS Glue, Amazon Kinesis, AWS HyperPod, Bedrock 구상, NVIDIA Isaac Lab, VLA, RFM, teleoperation, reinforcement learning

**현장 메모로 남길 점**
- 피지컬 AI는 모델만의 문제가 아니라 데이터 수집, 시뮬레이션, 실시간 제어, 하드웨어 감각, 학습 인프라가 한꺼번에 맞물려야 하는 전체 시스템 문제라는 점이 선명했다.

**블로그용 한줄**
- “RLWRLD와 위로보틱스 세션은 피지컬 AI가 거대 모델 학습과 로봇 하드웨어 감각이 만나는 지점에서 현실화되고 있음을 보여줬다.”
