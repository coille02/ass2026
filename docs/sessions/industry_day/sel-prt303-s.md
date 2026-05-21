# sel-prt303-s - LLM and Agent Workloads with DRA GPU를 더 잘게, 더 똑똑하게 — DRAmatic하게(sponsored by GS네오텍)

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

- 제목: LLM and Agent Workloads with DRA GPU를 더 잘게, 더 똑똑하게 - DRAmatic하게 (sponsored by GS네오텍)
- 시간: 2026-05-20 13:50-14:10 KST
- 트랙: AWS Summit Seoul - Track 2
- 발표자: 김성혁(AI Research Engineer, GS Neotek)

### 핵심 요약

GS네오텍 세션은 AI 인프라 문제가 GPU 확보량이 아니라 GPU를 워크로드 조건에 맞게 배치하고 공유하는 문제로 바뀌었다는 점을 짚었다. LLM/에이전트 워크로드는 요청 패턴이 동적이고 idle, 과점유, 토폴로지 불일치가 비용과 성능 병목을 만든다. 발표자는 Kubernetes/EKS 환경에서 기존 디바이스 플러그인 방식이 GPU 개수 중심이라 메모리, 공유 정책, 토폴로지 표현에 한계가 있다고 설명하고, DRA를 통해 "어떤 조건의 GPU가 필요한가"를 리소스 클레임으로 선언하는 구조를 소개했다. MPS, MIG, time slicing, exclusive GPU 사용 등 공유/격리 전략을 워크로드별로 선택해야 한다는 운영 관점도 강조했다.

### 주요 포인트

- 에이전트 시대의 GPU 운영은 정적인 GPU 개수 할당에서 워크로드 속성 기반 스케줄링으로 이동한다.
- 기존 Kubernetes device plugin은 GPU를 주로 개수로 다뤄 메모리, 토폴로지, 격리 수준을 세밀하게 표현하기 어렵다.
- DRA는 GPU 모델, 메모리, 드라이버, 공유 방식, 토폴로지 요구사항을 resource claim으로 선언하게 해준다.
- MPS는 다중 프로세스 공유, MIG는 하드웨어 격리, time slicing은 개발/검증, exclusive는 대규모 학습에 적합하다고 구분했다.
- EKS/Kubernetes 최신 버전의 DRA 지원 흐름과 GPU 공급 정책/서비스 요구사항의 분리 운영이 핵심 설계 포인트다.

### AWS/기술 키워드

Amazon EKS, Kubernetes DRA, GPU Scheduling, ResourceClaim, NVIDIA GPU, MPS, MIG, Time Slicing, LLM Serving, Agent Workloads, Topology-aware Scheduling

### 현장 메모로 남길 점

GPU 최적화는 "더 많이"가 아니라 "필요한 속성의 GPU를 필요한 워크로드에 정확히 매칭"하는 문제로 바뀌고 있다.

### 블로그용 한줄

LLM/에이전트 시대의 GPU 운영은 카드 수가 아니라 워크로드 요구 조건을 코드로 선언하는 능력에서 갈린다.
