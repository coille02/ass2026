# sel-ind224 - [Config] 피지컬 AI 기업 Config의 AWS 기반 Robotics Foundation Model 개발 여정

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

**Title/Time/Track/Speakers**  
- 제목: [Config] 피지컬 AI 기업 Config의 AWS 기반 Robotics Foundation Model 개발 여정
- 시간: 2026-05-20 12:50-13:23 KST
- 트랙: Industry Day / Artificial Intelligence
- 발표자: 손형목 최고 기술 책임자, Config

**핵심 요약**  
Config는 양팔 로봇 작업에 특화된 VLA(Vision Language Action) 기반 Robotics Foundation Model 개발 여정을 소개했다. 발표의 핵심은 로봇 파운데이션 모델의 성능을 좌우하는 것은 단순히 많은 데이터가 아니라 물체, 환경, 액션, 작업 맥락이 다양하게 분포된 고품질 액션 데이터라는 점이다. Config는 서울과 베트남 하노이에 자체 데이터 생산 인프라를 구축하고, 월 2만-3만 시간 수준의 데이터를 만들며 누적 13만 시간 규모를 언급했다. AWS Direct Connect, Amazon S3, DynamoDB, Amazon EKS, GPU 인프라를 조합해 데이터 업로드·처리·학습·추론 비용을 관리하는 방식도 공유했다.

**주요 포인트**
- RFM/로봇 파운데이션 모델은 텍스트·이미지 모델보다 실제 액션 데이터 확보가 훨씬 큰 병목으로 제시됨.
- 좋은 데이터는 다양한 물체, 환경, 작업, 액션을 포함해야 하며 데이터에 없는 상황에 일반화하는 능력이 중요.
- 사람의 액션을 라벨링하고 품질을 자동 평가하는 데이터 파이프라인을 구축했다고 설명.
- Direct Connect를 통해 자체 데이터 생산 시설에서 S3와 DynamoDB로 안정적이고 비용 효율적으로 데이터를 업로드.
- 학습에는 H100/B200급 노드, 추론에는 L40S 같은 상대적으로 저렴한 인스턴스를 쓰는 식으로 역할별 비용 최적화를 언급.

**AWS/기술 키워드**  
Robotics Foundation Model, VLA, Physical AI, AWS Direct Connect, Amazon S3, Amazon DynamoDB, Amazon EKS, SageMaker HyperPod, H100/B200, L40S, Teleoperation Data

**현장 메모로 남길 점**  
피지컬 AI는 모델보다 데이터 생산 공장이 먼저 필요하다는 점이 선명했다. 클라우드는 학습 플랫폼일 뿐 아니라 실제 세계의 액션 데이터를 안정적으로 옮기고 정제하는 운영 인프라다.

**블로그용 한줄**  
Config는 자체 액션 데이터 생산 체계와 AWS 기반 데이터·학습 인프라를 결합해 로봇 파운데이션 모델을 만들고 있다.

### 전사 기반 상세 보강

- 세션 맥락: [Config] 피지컬 AI 기업 Config의 AWS 기반 Robotics Foundation Model 개발 여정
- 공식 설명 보강: 한국의 대표적인 피지컬 AI 스타트업 Config는 양팔 작업에 특화된 자체 VLA(Vision Language Action)모델을 개발해 다양한 엔터프라이즈 기업과 협업하고 있습니다. Config는 Robot Foundation 모델 제작에 필수인 고품질 액션 데이터를 확보하기 위해, 국내 및 베트남에 자체 데이터 생산 및 검수 시설을 구축하여 월 20,000시간 이상의 액션 데이터를 수집하고 있습니다. 확보한 데이터는 AWS Direct Connect를...
- 전사에서 반복적으로 확인된 키워드: 데이터, 테스트, 고객, 비용, 자동화, 개발, S3, 감사, 인프라, 품질
- 발표에서 두드러진 주제 축: data, developer, governance, business

#### 발표 흐름
- 초반: 데이터, 고객, 개발, 장애, 비용 중심으로 data, developer, governance를 다룬다.
- 중반: 데이터, 테스트, 자동화, 고객, 품질 중심으로 data, developer, governance를 다룬다.
- 후반: 데이터, 비용, S3, 감사, 개발 중심으로 data, developer, governance를 다룬다.

#### 전사에서 확인할 만한 구간
- 00:13 부근: 개발 관련 설명이 나온다. 핵심 문맥은 `로고틱스 파운데이션 모델 개발 여정이라는 주제로`
- 01:31 부근: 고객 관련 설명이 나온다. 핵심 문맥은 `저희는 이제 여러 고객들이 본인들이`
- 13:13 부근: 고객, 테스트 관련 설명이 나온다. 핵심 문맥은 `고객들이 원하는 타겟 테스트가 정의가 됐을 때`
- 20:22 부근: S3, 데이터, 비용 관련 설명이 나온다. 핵심 문맥은 `또 비용 효율적으로 s3라든지 DynamoDB 데이터를 업로드할 수 있었는데`
- 28:18 부근: 개발, 데이터 관련 설명이 나온다. 핵심 문맥은 `인크, 폼팩터도 우리가 지원할 수 있는 데이터를 현재 개발 중에 있습니다.`
