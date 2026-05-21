# sel-ind209 - [빗썸] 빗썸은 생성형 AI를 어떻게 안전하게 운영하는가: Claude Code on Amazon Bedrock

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

**title/time/track/speakers**  
- 제목: [빗썸] 빗썸은 생성형 AI를 어떻게 안전하게 운영하는가: Claude Code on Amazon Bedrock
- 시간: 2026-05-20 16:10-16:50 KST
- 트랙: AWS Summit Seoul - Track 3
- 발표자: 마상범(솔루션즈 아키텍트, AWS), 고주호(팀장, 빗썸), 백길선(팀장, 빗썸)

**핵심 요약**  
빗썸은 Claude Code를 금융권 환경에서 통제 가능하게 운영하기 위해 Amazon Bedrock 기반의 보안 아키텍처를 구축한 경험을 공유했다. 핵심 요구사항은 SSO 인증, 프라이빗 네트워크, 감사 로그, 팀/개인별 비용 관리, 프롬프트 필터링이었다. 발표는 IAM, SCP, CloudTrail, CloudWatch, Direct Connect, LLM Gateway 등을 조합해 개발자 경험을 유지하면서도 규제와 내부통제를 만족시키는 구조를 설명했다. 향후에는 멀티 모델 라우팅, 팀별 시스템 프롬프트/스킬 공유, 개발-배포-운영 전주기 AI 자동화를 확대할 계획이라고 밝혔다.

**주요 포인트**
- 기업 및 금융권에서 Claude Code 같은 강력한 도구는 보안, 규제, 비용 통제 없이 개인 구독형으로 방치할 수 없다.
- API 키 방식 대신 사내 계정 체계와 연동되는 SSO 기반 인증과 권한 회수가 필요하다.
- 개발자 PC의 요청은 Direct Connect와 LLM Gateway를 거쳐 Bedrock Runtime으로 이동하며 인터넷 구간을 제거했다.
- IAM, SCP, CloudTrail, CloudWatch로 접근 제어, 감사 추적, 사용량 관리를 통합했다.
- Claude 스킬과 프롬프트를 조직 카탈로그로 축적해 개인의 AI 활용 노하우를 조직 자산으로 전환하려 했다.

**AWS/기술 키워드**  
Amazon Bedrock, Claude Code, IAM, SCP, AWS Direct Connect, AWS PrivateLink, CloudTrail, CloudWatch, LLM Gateway, Guardrails, SSO, 멀티 모델 라우팅

**현장 메모로 남길 점**  
세션의 핵심 문장은 “보안은 제품이 아니라 설계”로 정리된다. 금융권 생성형 AI 도입 글에서는 개발 생산성보다 먼저 인증, 네트워크 경로, 감사, 비용, 프롬프트 통제를 아키텍처 요구사항으로 잡은 점을 강조하면 좋다.

**블로그용 한줄**  
빗썸의 Claude Code 도입기는 금융권 생성형 AI가 빠르게 쓰이려면 먼저 안전하게 설계돼야 한다는 것을 보여줬다.

### 직접 들은 뒤 메모

빗썸 세션은 핀테크 회사 입장에서 가장 직접적으로 참고할 만했다. Claude Code를 막는 것이 아니라 Bedrock, SSO, 프라이빗 네트워크, 감사 로그, 비용 관리, 프롬프트 필터링을 붙여 안전하게 쓰게 만드는 방향이 핵심이었다. 카카오페이도 개발자들이 이미 AI 도구를 쓰고 있다면, 사용을 금지하거나 개인 역량에 맡기는 것보다 금융권 수준의 통제와 개발자 경험을 함께 만족시키는 내부 AI 개발 플랫폼을 고민해야 한다. 특히 팀별 스킬 공유, 감사 가능한 로그, 모델 라우팅, 비용 가시화는 AX TF에서 우선순위 높게 볼 만하다.
