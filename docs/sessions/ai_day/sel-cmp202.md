# sel-cmp202 - 인퍼런스와 모델 퍼포먼스 최적화를 위한 EKS 아키텍처

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

- 시간/트랙/레벨/발표자: 12:50-13:30 KST / Track 6, Architecture·AI·Cloud Operations / 200 Intermediate / 정영준(AWS)
- 요약: LLM 추론 비용과 지연을 줄이기 위한 Amazon EKS 기반 GPU 운영 전략을 다뤘다. EKS Auto Mode, Karpenter, GPU Operator, Cluster Autoscaler, DRA 등을 워크로드 성숙도에 따라 선택하고, vLLM, KV cache-aware routing, GPU autoscaling, tiered gateway 구성으로 처리량과 GPU utilization을 높이는 방향을 설명했다.
- 주요 포인트:
  - LLM 추론 최적화는 비용 절감과 UX 개선이 동시에 걸린 문제이며, first-token latency와 throughput을 함께 봐야 한다.
  - 시작점은 EKS Auto Mode가 적합하고, 더 세밀한 GPU 분할과 최적화가 필요하면 managed node, Cluster Autoscaler, DRA 조합으로 확장한다.
  - 대규모·MoE 모델은 양자화, 모델 가중치 로딩 최적화, Nitro 기반 네트워크 최적화가 중요하다.
  - 에이전틱 AI 플랫폼은 모델 개발, 평가, 배포, 추론까지 단일 워크플로우로 이어져야 운영 가능하다.
- AWS/기술 키워드: Amazon EKS, EKS Auto Mode, GPU, NVIDIA, Karpenter, DRA, vLLM, KV cache, autoscaling, tiered gateway, Nitro
- AX TF 관점/회사 AX 도입 시사점: 내부 AI 서비스가 늘면 모델 호출 비용이 빠르게 불어난다. PoC 단계부터 토큰당 비용, GPU utilization, first-token latency, 배치/동시성 정책을 측정 가능한 표준 KPI로 두고 플랫폼팀이 공통 추론 런타임을 제공하는 방향이 좋다.
- 공유용 한줄: LLM 플랫폼의 승부는 모델 선택만이 아니라 GPU를 얼마나 덜 놀리고 지연을 얼마나 낮추느냐에 달려 있다.

### 전사 기반 상세 보강

- 세션 맥락: 인퍼런스와 모델 퍼포먼스 최적화를 위한 EKS 아키텍처
- 공식 설명 보강: Amazon EKS 에서 NVIDIA GPU 기반의 인퍼런스 및 GPU 워크로드 최적화 기법을 다룹니다. Opex가 매우 높은 클라우드 AI 플렛폼을 최적화하고, 처리량은 높이고 지연을 최소화하여 Agentic AI 워크로드를 통한 변화를 가속화 하는 EKS 기반의 아키텍처에 대하여 설명합니다.
- 전사에서 반복적으로 확인된 키워드: GPU, EKS, 운영, 고객, 인프라, 아키텍처, 개발, 비용, 코드, 전략
- 발표에서 두드러진 주제 축: infra, business, developer, ops

#### 발표 흐름
- 초반: GPU, EKS, 운영, 인프라, 개발 중심으로 infra, business, developer를 다룬다.
- 중반: GPU, EKS, 인프라, 비용, 코드 중심으로 infra, business, developer를 다룬다.
- 후반: GPU, 고객, EKS, 전략, 아키텍처 중심으로 infra, business, developer를 다룬다.

#### 전사에서 확인할 만한 구간
- 00:12 부근: EKS, 아키텍처 관련 설명이 나온다. 핵심 문맥은 `EKS 아키텍처라는 주제로`
- 08:29 부근: 고객, 상품 관련 설명이 나온다. 핵심 문맥은 `향후에 저희가 고객사분들을 만나서 저희가 쓰고 있는 여러 가지 플랫폼 형상들을 비투비 상품으로 만들어서 제공한 계획도 있으니 많은 관심을 바라겠고`
- 12:01 부근: EKS, 운영, 추천 관련 설명이 나온다. 핵심 문맥은 `어쨌든 지금 EKS 위에서 A-SUN TGRI를 운영하는 것에 최고의 옵션은 EKS 오토 모드에서 시작하시는 것을 추천을 드리고`
- 16:57 부근: 고객, 전략 관련 설명이 나온다. 핵심 문맥은 `여러분들 지금 제가 만나는 대형 고객들, 전략고객분들이 실제로`
- 17:02 부근: 개발, 운영 관련 설명이 나온다. 핵심 문맥은 `에이전틱 AI를 도입할 때 개발팀이나 운영팀한테 동시에 영향을 줘`
