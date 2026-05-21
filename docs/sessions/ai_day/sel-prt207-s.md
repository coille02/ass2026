# sel-prt207-s - LLM 애플리케이션 프로덕션 운영, Observability로 풀다 (sponsored by 와탭, WhaTap)

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

- 시간/트랙/레벨/발표자: 13:50-14:10 KST / Partner Track / 200 Intermediate / 신민철(WhaTap)
- 요약: LLM 애플리케이션은 만들기는 쉬워졌지만 프로덕션 운영에서는 토큰 비용 폭증, 예측 어려운 응답 지연, 품질 저하, 할루시네이션 문제가 발생한다고 설명했다. 기존 APM/RUM만으로는 LLM API 호출, 프롬프트, 응답, 토큰 사용량, 모델 품질을 충분히 관측할 수 없으므로 LLM 전용 옵저버빌리티가 필요하다는 내용이다.
- 주요 포인트:
  - LLM 앱은 단순 API 호출처럼 보여도 실제 프로덕션 파이프라인은 여러 LLM 호출과 도구 호출을 포함한다.
  - 토큰 사용량은 비용과 직결되며 모델별 가격 차이 때문에 비용이 비선형적으로 증가할 수 있다.
  - Provider LLM은 API 영역 중심으로, Local LLM은 인프라 영역까지 포함해 관측 지점을 다르게 봐야 한다.
  - 프롬프트, 응답 품질, 지연, 토큰, 비용, 로그, 트레이스가 함께 연결되어야 운영자가 원인을 찾을 수 있다.
- AWS/기술 키워드: LLM observability, Amazon Bedrock, APM, RUM, token cost, latency, prompt/response trace, monitoring
- AX TF 관점/회사 AX 도입 시사점: 사내 LLM 앱 표준에 토큰 예산, 호출 트레이스, 프롬프트/응답 로깅 정책, 품질 평가 지표를 포함해야 한다. 운영 대시보드 없이 배포된 챗봇은 비용과 품질 리스크를 숨긴다.
- 공유용 한줄: LLM 앱은 배포 후부터 진짜 비용과 품질 문제가 시작된다.
