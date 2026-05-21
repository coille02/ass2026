# sel-cmp301 - AWS Trainium 기반 LLM 추론 A to Z: Neuron 환경 이해부터 성능 최적화까지

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

- 시간/트랙/레벨/발표자: 16:10-16:50 KST / Track 6 / 300 - Advanced / 이수지, GTM 가속 컴퓨팅 전문 솔루션즈 아키텍트, AWS; 차수정, 딥러닝 아키텍트, AWS
- 요약: AWS Trainium과 Neuron SDK를 활용해 LLM 추론을 비용 효율적으로 운영하고 성능을 최적화하는 방법을 다뤘다. 발표는 LLM 추론의 비용 증가, 디코드 병목, 이기종 하드웨어 전환 부담을 문제로 제시하고 Trainium2, Neuron, vLLM/PyTorch 연동, NKI 최적화로 해결하는 흐름을 설명했다.
- 주요 포인트:
  - 생성형 AI 인프라 비용은 토큰 가격 하락보다 사용량 증가가 빨라 최적화 없이는 부담이 커진다.
  - LLM 추론은 KV cache와 디코드 병목 때문에 메모리/대역폭이 중요하며, Trainium2의 대용량 HBM과 멀티코어 구조를 해결책으로 소개했다.
  - Neuron은 익숙한 Python, PyTorch, vLLM 생태계와 연동되어 새 하드웨어 진입 장벽을 낮춘다고 설명했다.
  - Qwen3 8B 데모에서 NKI attention kernel 적용 후 처리량은 약 5.4배 증가, 지연시간은 2.84초에서 0.53초로 약 81% 감소했다고 정리했다.
- AWS/기술 키워드: AWS Trainium, Trainium2, AWS Neuron SDK, Neuron Kernel Interface, NKI, NKI Library, Neuron Explorer, vLLM, PyTorch, Qwen3, LLM Inference, HBM
- AX TF 관점/회사 AX 도입 시사점: AX 서비스가 많아지면 모델 API 비용만 볼 것이 아니라 자체/전용 추론 인프라 최적화도 검토해야 한다. 특히 내부 반복 워크로드나 대규모 배치/온라인 추론은 Trainium 같은 대안 가속기와 커널 최적화가 비용 차이를 만들 수 있다.
- 공유용 한줄: Trainium+Neuron은 LLM 추론 비용과 지연시간을 낮추기 위한 AWS 전용 가속기 선택지다.

### 전사 기반 상세 보강

- 세션 맥락: AWS Trainium 기반 LLM 추론 A to Z: Neuron 환경 이해부터 성능 최적화까지
- 공식 설명 보강: 생성형 AI의 빠른 확산과 함께 대규모 언어 모델(LLM)의 효율적인 추론은 기업들의 핵심 과제가 되었습니다. 본 세션에서는 AWS 전용 AI 칩인 Trainium과 Neuron SDK 생태계를 활용하여 LLM 추론의 전체 파이프라인을 체계적으로 다룹니다. 실습 데모에서는 Qwen3 모델에 NKI(Neuron Kernel Interface) 최적화 커널을 적용하여 처리량과 지연시간 모두에서 의미 있는 성능 향상을 달성하는 과정을 단계별로 시연합니다. 또한...
- 전사에서 반복적으로 확인된 키워드: 코드, 데이터, 배포, 비용, 감사, 모니터링, 전략, GPU, 아키텍처, 개발
- 발표에서 두드러진 주제 축: developer, data, infra, security

#### 발표 흐름
- 초반: 비용, 코드, GPU, 감사, 고객 중심으로 developer, data, infra를 다룬다.
- 중반: 코드, 배포, 데이터, 모니터링, 전략 중심으로 developer, data, infra를 다룬다.
- 후반: 데이터, 코드, 아키텍처, 배포, 감사 중심으로 developer, data, infra를 다룬다.

#### 전사에서 확인할 만한 구간
- 01:02 부근: 인프라 관련 설명이 나온다. 핵심 문맥은 `네 안녕하세요. 저희 AI 인프라 트랙의 마지막 세션인데요.`
- 05:05 부근: 아키텍처 관련 설명이 나온다. 핵심 문맥은 `아키텍처와 멀티코어 활용으로써 해결하실 수 있습니다.`
- 10:00 부근: 코드 관련 설명이 나온다. 핵심 문맥은 `세컨드입니다. lm 출연의 디코드 단계는 컴퓨트가 아니라 메모리 속도가 병목입니다.`
- 10:15 부근: GPU 관련 설명이 나온다. 핵심 문맥은 `네, AWS에서 활용 가능한 GPU 기반 인스턴스와의 비교입니다.`
- 30:25 부근: 데이터, 테스트 관련 설명이 나온다. 핵심 문맥은 `여기서 주의하실 부분은 테스트 데이터세세의 인플드 아웃 길이를 모델을 디플로이하실 때 쓰셨던`
