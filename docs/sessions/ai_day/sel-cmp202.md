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
