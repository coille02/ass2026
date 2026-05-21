# 인퍼런스와 모델 퍼포먼스 최적화를 위한 EKS 아키텍처

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

## 세션 정보

- 시간: 2026-05-21 12:50-13:30 KST
- 트랙: Track 6
- 레벨: 200 - Intermediate
- 발표자: 정영준(AWS)
- 주제: Architecture, Artificial Intelligence, Cloud Operations, Software & Internet

## 발표 주제

Amazon EKS 에서 NVIDIA GPU 기반의 인퍼런스 및 GPU 워크로드 최적화 기법을 다룹니다. Opex가 매우 높은 클라우드 AI 플렛폼을 최적화하고, 처리량은 높이고 지연을 최소화하여 Agentic AI 워크로드를 통한 변화를 가속화 하는 EKS 기반의 아키텍처에 대하여 설명합니다.

LLM 추론 비용과 지연을 줄이기 위한 Amazon EKS 기반 GPU 운영 전략을 다뤘다. EKS Auto Mode, Karpenter, GPU Operator, Cluster Autoscaler, DRA 등을 워크로드 성숙도에 따라 선택하고, vLLM, KV cache-aware routing, GPU autoscaling, tiered gateway 구성으로 처리량과 GPU utilization을 높이는 방향을 설명했다.

## 주요 내용

- LLM 추론 최적화는 비용 절감과 UX 개선이 동시에 걸린 문제이며, first-token latency와 throughput을 함께 봐야 한다.
- 시작점은 EKS Auto Mode가 적합하고, 더 세밀한 GPU 분할과 최적화가 필요하면 managed node, Cluster Autoscaler, DRA 조합으로 확장한다.
- 대규모·MoE 모델은 양자화, 모델 가중치 로딩 최적화, Nitro 기반 네트워크 최적화가 중요하다.
- 에이전틱 AI 플랫폼은 모델 개발, 평가, 배포, 추론까지 단일 워크플로우로 이어져야 운영 가능하다.

## 세부 내용

### 문제의식과 배경

LLM 추론 최적화는 비용 절감과 UX 개선이 동시에 걸린 문제이며, first-token latency와 throughput을 함께 봐야 한다. 시작점은 EKS Auto Mode가 적합하고, 더 세밀한 GPU 분할과 최적화가 필요하면 managed node, Cluster Autoscaler, DRA 조합으로 확장한다.

### 접근 방식과 아키텍처

대규모·MoE 모델은 양자화, 모델 가중치 로딩 최적화, Nitro 기반 네트워크 최적화가 중요하다. 에이전틱 AI 플랫폼은 모델 개발, 평가, 배포, 추론까지 단일 워크플로우로 이어져야 운영 가능하다.

### 운영 포인트와 확장 방향

관련 기술 키워드는 Amazon EKS, EKS Auto Mode, GPU, NVIDIA, Karpenter, DRA, vLLM, KV cache, autoscaling, tiered gateway, Nitro이다.

## 정리

이 세션의 핵심은 인퍼런스와 모델 퍼포먼스 최적화를 위한 EKS 아키텍처를 단순한 기능 소개가 아니라 실제 업무와 운영 환경에 적용하기 위한 조건으로 풀어냈다는 점이다. LLM 추론 최적화는 비용 절감과 UX 개선이 동시에 걸린 문제이며, first-token latency와 throughput을 함께 봐야 한다.

발표는 AI 활용이 성과로 이어지려면 모델이나 도구 선택뿐 아니라 데이터, 권한, 운영 절차, 관측 가능성을 함께 설계해야 한다는 메시지로 정리된다.
