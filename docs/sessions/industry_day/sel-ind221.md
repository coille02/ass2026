# sel-ind221 - [SK인텔릭스] SK인텔릭스가 구현하는 에이전틱 AI Robotics의 미래

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

**title/time/track/speakers**  
- 제목: [SK인텔릭스] SK인텔릭스가 구현하는 에이전틱 AI Robotics의 미래
- 시간: 2026-05-20 16:10-16:50 KST
- 트랙: AWS Summit Seoul - Track 5
- 발표자: 류기철(AX Tech실장, SK인텔릭스), 조한익(매니저, SK 인텔릭스)

**핵심 요약**  
SK인텔릭스는 가정용 웰니스 로봇 NAMUHX를 중심으로 수동적 기기에서 공감형 파트너로 진화하는 에이전틱 AI 로보틱스 비전을 제시했다. 발표는 실제 가정 환경의 복잡성을 예로 들며 주행, 바이탈 체크, 사용자 동의 기반 데이터 수집, 온디바이스와 클라우드 에이전트의 역할 분담을 설명했다. AWS IoT Core, S3, Aurora, ElastiCache, DynamoDB 등을 활용해 로봇 데이터와 지식 그래프를 구성하고, Bedrock AgentCore와 Converse API로 에이전트 개발과 관찰성을 확보했다고 설명했다. 마지막에는 NAMUHX 오픈 API와 개발자 생태계를 통해 외부 에이전트를 로봇 서비스로 확장하겠다는 방향을 밝혔다.

**주요 포인트**
- 가정용 로봇은 공장 로봇과 달리 장난감, 반려동물, 이동하는 의자처럼 예측 어려운 환경에서 안정적으로 움직여야 한다.
- NAMUHX는 단순 데모가 아니라 전시 기간 동안 지속 주행과 바이탈 사인 체크를 수행한 상용화 제품으로 소개됐다.
- 개인정보와 빠른 반응이 필요한 작업은 온디바이스 에이전트가 처리하고, 복합 추론과 지식 연결은 클라우드가 보완한다.
- IoT 메시지와 사용자/생체/환경 데이터를 S3, Aurora, ElastiCache, DynamoDB 등에 저장하고 그래프 DB 및 온톨로지로 연결한다.
- Bedrock AgentCore Observability와 Converse API를 활용해 에이전트 호출, 모델 비교, 운영 관찰성을 강화했다.

**AWS/기술 키워드**  
Amazon Bedrock AgentCore, Bedrock Converse API, AWS IoT Core, Amazon S3, Amazon Aurora, Amazon ElastiCache, Amazon DynamoDB, Graph DB, 온디바이스 AI, MCP, 로봇 API/SDK

**현장 메모로 남길 점**  
로봇 사례는 “AI가 화면 안에서 답하는 것”을 넘어 물리 세계에서 행동하는 에이전트의 통제와 반응 속도 문제를 보여준다. 개인정보/응답속도는 온디바이스, 장기 기억/추론은 클라우드라는 구분이 블로그에서 좋은 구조가 된다.

**블로그용 한줄**  
SK인텔릭스의 NAMUHX는 로봇이 도구를 넘어 생활 파트너가 되려면 온디바이스 AI와 클라우드 에이전트가 함께 설계돼야 함을 보여줬다.
