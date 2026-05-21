# sel-prt206-s - 속도와 제어를 동시에 - Cloudflare에서 AI 에이전트 구축하기 (sponsored by 클라우드플레어/Cloudflare)

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

- 시간/트랙/레벨/발표자: 13:50-14:10 KST / Partner Track / 100 Foundational / 조성윤(Cloudflare)
- 요약: AI 에이전트가 코드를 작성하고 실행하며 DB 조회와 API 호출까지 수행하는 시대에는 “빠른 배포”와 “권한·감사·격리”가 함께 필요하다고 설명했다. Cloudflare AI Gateway, MCP 서버 포털, 샌드박스 실행 환경을 통해 에이전트의 LLM 호출, 도구 접근, 데이터 유출, 무한 루프, 권한 남용을 통제하는 접근을 제시했다.
- 주요 포인트:
  - 2023년의 AI가 텍스트 생성 도구였다면 2026년의 AI 에이전트는 실행 주체에 가깝다.
  - 에이전트에는 직원처럼 신원, 최소 권한, 정책, 감사 로그, 격리된 실행 환경이 필요하다.
  - MCP 서버 포털은 승인된 도구만 사용하게 하는 관문 역할을 한다.
  - AI Gateway는 LLM 트래픽의 제어 지점으로 DLP, 사용량 제한, 루프 탐지, 소스코드/PII 유출 방지에 활용된다.
- AWS/기술 키워드: Cloudflare AI Gateway, MCP server portal, AI agent sandbox, DLP, policy control, audit log, least privilege
- AX TF 관점/회사 AX 도입 시사점: 사내 에이전트 실험은 “개발자 편의”만 보고 열면 위험하다. 도구 호출을 승인 목록으로 제한하고, 에이전트별 권한과 로그, 샌드박스 실행 정책을 먼저 잡아야 한다.
- 공유용 한줄: AI 에이전트는 도구가 아니라 실행 주체이므로 사람처럼 권한과 감사가 필요하다.


담당 세션: `sel-aim401`, `sel-ant303`, `sel-dvt304`, `sel-mam202`, `sel-dvt204`, `sel-cmp201`, `sel-sec302`, `sel-biz204`, `sel-dev305`, `sel-aim202`, `sel-prt217-s`, `sel-dvt302`, `sel-prt106-s`, `sel-prt103-s`

대부분 helper script로 생성한 VOD 전사본을 기반으로 요약했습니다. 전사 품질상 일부 고유명사와 제품명은 공식 세션 메타데이터와 대조해 보정했습니다. `sel-prt106-s`는 전사 결과에 발화가 없어 메타데이터 기반 요약으로 작성했습니다.
