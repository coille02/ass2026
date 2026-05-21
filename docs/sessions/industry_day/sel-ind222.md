# sel-ind222 - [하나투어 I AK아이에스] AI가 바꾸는 여행 산업의 무대 뒤: 하나투어, 제주항공의 업무혁신

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

**제목/시간/트랙/발표자**  
- 제목: [하나투어 I AK아이에스] AI가 바꾸는 여행 산업의 무대 뒤: 하나투어, 제주항공의 업무혁신
- 시간: 2026-05-20 14:30-15:10 KST
- 트랙: Aerospace & Satellite, Travel & Hospitality / Artificial Intelligence, Industry Solutions, Migration & Modernization
- 발표자: 주혜령 솔루션즈 아키텍트(AWS), 이길주 온라인개발 랩장(하나투어), 박수호 항공IT기획팀 팀장(AK아이에스)

**핵심 요약**  
이 세션은 여행 산업의 백오피스 혁신을 하나투어의 여행 상품 기획 에이전트와 AK아이에스/제주항공의 항공 정비 데이터 AI 전환 사례로 나눠 보여줬다. 하나투어는 초기 LLM loop 방식이 느리고 비싸며 MD가 선택하지 않는 결과를 만든 실패를 겪은 뒤, 여행 데이터를 knowledge graph로 재구성하고 AgentCore와 Neptune 기반 구조로 전환했다. 그 결과 10분 이상 걸리던 상품 초안 생성이 1분 이내로 줄고, 비용도 80% 이상 절감될 것으로 소개됐다. AK아이에스는 MEL 문서와 정비 이력 데이터를 검색 가능한 구조로 만들고, Textract 기반 AI OCR로 종이 정비 기록을 시스템 안으로 들여와 항공 안전과 정비 의사결정 속도를 높이는 방향을 제시했다.

**주요 포인트**
- AWS 파트는 여행 상품 기획 텍스트를 knowledge graph로, 항공 정비 종이 문서를 구조화된 디지털 데이터로 바꾸는 것이 AI 활용의 전제라고 설명했다.
- 하나투어의 1차 LLM 반복 구조는 10-20분 이상 걸리고 토큰/EC2 비용이 컸으며, 결과도 MD의 상품 기획 품질에는 미치지 못했다.
- 외부 지도/검색 기반 LLM을 활용한 2차 시도는 20-30초까지 빨라졌지만, 하나투어 고유 자산과 MD 노하우가 빠져 선택받지 못했다.
- 최종 구조는 Amazon Neptune에 여행 graph를 저장하고, AgentCore Runtime에 배포된 Claude 기반 agent가 AgentCore Gateway를 통해 graph 저장/검색 tool을 호출하는 방식이다.
- “그래프에 없는 데이터는 사용하지 말라”는 원칙으로 hallucination을 줄였고, MD 피드백을 자연어로 받아 Cypher query로 변환해 준실시간으로 graph를 업데이트하는 loop를 만들었다.
- AK아이에스는 MEL 문서와 MRO 정비 이력 데이터를 S3에 적재하고, OpenSearch index와 Bedrock Claude 기반 chatbot agent가 MEL search와 정비 이력 search tool을 호출하는 구조를 소개했다.
- 항공 정비 AI는 hallucination이 안전 리스크가 되므로 신뢰도 scoring, golden dataset 기반 정기 검증, 직급별 사용 권한과 human final decision 원칙을 세웠다.
- AI OCR은 정비사가 모바일로 종이 문서를 촬영하면 S3에 저장하고 Amazon Textract가 표와 손글씨를 읽어 정비 업무 시스템에 입력하는 흐름으로 설명됐다.
- 네트워크/서버 장애 시를 대비해 원본 종이 문서를 일정 기간 보관하고, 디지털 저장 완료 후 데이터 원장이 원본을 대체한다는 절차도 함께 설계했다.

**AWS/기술 키워드**
- Amazon Bedrock, Claude, Bedrock AgentCore Runtime, AgentCore Gateway, Amazon Neptune, Amazon DynamoDB, Amazon OpenSearch Service, Amazon Textract, Amazon S3, API Gateway, knowledge graph, Cypher, RAG, AI OCR

**현장 메모로 남길 점**
- 하나투어 사례는 “AI에게 긴 텍스트 대신 지도, 즉 도메인 그래프를 주라”는 메시지가 강했다.
- 제주항공/AK아이에스 사례는 기술보다 변화관리와 안전 거버넌스가 중요했다. 정비 현장에서는 AI가 답을 해도 숙련자가 최종 책임을 지는 구조가 필수다.

**블로그용 한줄**
- “하나투어와 AK아이에스는 AI 혁신의 핵심이 모델 호출이 아니라 도메인 데이터를 AI가 믿고 쓸 수 있는 구조로 바꾸는 데 있음을 보여줬다.”
