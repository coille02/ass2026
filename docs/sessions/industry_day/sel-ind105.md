# sel-ind105 - AWS 피지컬 AI로 실현하는 기업의 차세대 혁신 전략

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

- 제목: AWS 피지컬 AI로 실현하는 기업의 차세대 혁신 전략
- 시간: 2026-05-20 11:10-11:50 KST
- 트랙: AWS Summit Seoul - Track 6
- 발표자: David Randle (Worldwide Head GTM - Physical AI, AWS)

### 핵심 요약
이 세션은 피지컬 AI를 디지털 모델이 실제 세계를 감지하고, 시뮬레이션하고, 검증한 뒤 물리 시스템의 행동으로 이어지게 하는 흐름으로 설명했다. 발표자는 노동력 부족과 생산성 압박이 물리 세계의 자동화와 자율성을 가속하는 배경이라고 짚었다. 핵심 구성은 센서와 물리 상태 데이터, 디지털 트윈, 클라우드 기반 대규모 시뮬레이션, 엣지 디바이스의 자율 실행, 운영 데이터의 재학습 루프로 이어지는 AWS Physical AI Framework다. 제조, 자동차, 자율주행, 로보틱스 같은 영역에서 클라우드와 엣지가 함께 피지컬 AI 플라이휠을 만든다는 메시지가 중심이었다.

### 주요 포인트
- 피지컬 AI는 물리 세계를 이해하고 행동을 결정하는 AI를 로봇, 공장, 자동차, 엣지 시스템에 적용하는 개념
- 디지털 트윈은 실제 환경에서 테스트하기 어려운 조건을 시뮬레이션하고 사전 검증하는 핵심 수단
- 클라우드는 온프레미스나 사람이 직접 수행하기 어려운 대규모 컴퓨팅 시뮬레이션을 가능하게 함
- 학습된 정책과 스킬은 엣지 디바이스로 이동해 현장에서 자율적으로 동작하고, 결과 데이터는 다시 모델 개선에 활용
- AWS Physical AI Framework는 감지, 추론, 시뮬레이션, 배포, 운영 피드백을 하나의 플라이휠로 묶는 구조로 제시됨

### AWS/기술 키워드
- AWS Physical AI Framework, Amazon EKS, Digital Twin, Simulation, Edge AI, Robotics, IoT sensing, Autonomous systems, Physical AI flywheel

### 현장 메모로 남길 점
- 피지컬 AI의 핵심은 "클라우드에서 똑똑해진 모델"이 아니라 시뮬레이션과 엣지 실행, 운영 피드백이 계속 순환하는 구조였다.

### 블로그용 한줄
> AWS 피지컬 AI 전략은 디지털 트윈과 클라우드 시뮬레이션을 엣지의 자율 행동으로 연결해 제조와 로보틱스 혁신을 가속한다.

### 전사 기반 상세 보강

- 세션 맥락: AWS 피지컬 AI로 실현하는 기업의 차세대 혁신 전략
- 공식 설명 보강: 2030년, 7조 달러 규모의 자율 경제 시대가 열릴 것으로 예상되는 가운데 IoT 센싱부터 엣지 자율성까지의 AWS 피지컬 AI의 6단계 아키텍처를 통해 한국 제조업이 글로벌 경쟁력을 확보하고, 생산성을 극대화하며 새로운 비즈니스 가치를 실현하는 방법을 소개합니다.
- 전사에서 반복적으로 확인된 키워드: 정책, RAG, agent, 데이터, S3, 감사, DevOps, 전략, 비즈니스, EKS
- 발표에서 두드러진 주제 축: governance, data, infra, agent

#### 발표 흐름
- 초반: RAG, 감사, 전략, 비즈니스, 아키텍처 중심으로 data, infra를 다룬다.
- 중반: 정책, RAG, agent, 데이터, S3 중심으로 governance, data, infra를 다룬다.
- 후반: agent, RAG, DevOps 중심으로 data, agent를 다룬다.

#### 전사에서 확인할 만한 구간
- 00:21 부근: 아키텍처 관련 설명이 나온다. 핵심 문맥은 `AWS 피지컬 AI에 6단계 아키텍처를 통해 한국 제조업이 글로벌 경쟁력을 확보하고`
- 17:04 부근: EKS 관련 설명이 나온다. 핵심 문맥은 `EKS,`
- 20:24 부근: HyperPod, S3 관련 설명이 나온다. 핵심 문맥은 `again using SageMaker HyperPod S3`
- 27:32 부근: agent 관련 설명이 나온다. 핵심 문맥은 `Think about agents operating simulation environments,`
- 32:28 부근: agent 관련 설명이 나온다. 핵심 문맥은 `through an agentex workflow`
