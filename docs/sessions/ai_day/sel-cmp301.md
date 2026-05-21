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
