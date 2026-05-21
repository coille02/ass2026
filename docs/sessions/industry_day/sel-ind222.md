# [하나투어 I AK아이에스] AI가 바꾸는 여행 산업의 무대 뒤: 하나투어, 제주항공의 업무혁신

[Industry Day 세션 목록으로 돌아가기](../../industry_day_sessions.md)

## 세션 정보

- 시간: 2026-05-20 14:30-15:10 KST
- 트랙: Track 8
- 분류: 레벨: 200 - Intermediate, 산업: Aerospace & Satellite, 산업: Travel & Hospitality, 주제: Artificial Intelligence, 주제: Industry Solutions, 주제: Migration & Modernization
- 발표자: 주혜령 솔루션즈 아키텍트(AWS), 이길주 온라인개발 랩장(하나투어), 박수호 항공IT기획팀 팀장(AK아이에스)

## 발표 주제

이 세션은 여행 산업의 백오피스 혁신을 하나투어의 여행 상품 기획 에이전트와 AK아이에스/제주항공의 항공 정비 데이터 AI 전환 사례로 나눠 보여줬다.

하나투어는 초기 LLM loop 방식이 느리고 비싸며 MD가 선택하지 않는 결과를 만든 실패를 겪은 뒤, 여행 데이터를 knowledge graph로 재구성하고 AgentCore와 Neptune 기반 구조로 전환했다. 그 결과 10분 이상 걸리던 상품 초안 생성이 1분 이내로 줄고, 비용도 80% 이상 절감될 것으로 소개됐다.

## 주요 내용

- AWS 파트는 여행 상품 기획 텍스트를 knowledge graph로, 항공 정비 종이 문서를 구조화된 디지털 데이터로 바꾸는 것이 AI 활용의 전제라고 설명했다.
- 하나투어의 1차 LLM 반복 구조는 10-20분 이상 걸리고 토큰/EC2 비용이 컸으며, 결과도 MD의 상품 기획 품질에는 미치지 못했다.
- 외부 지도/검색 기반 LLM을 활용한 2차 시도는 20-30초까지 빨라졌지만, 하나투어 고유 자산과 MD 노하우가 빠져 선택받지 못했다.
- 최종 구조는 Amazon Neptune에 여행 graph를 저장하고, AgentCore Runtime에 배포된 Claude 기반 agent가 AgentCore Gateway를 통해 graph 저장/검색 tool을 호출하는 방식이다.
- “그래프에 없는 데이터는 사용하지 말라”는 원칙으로 hallucination을 줄였고, MD 피드백을 자연어로 받아 Cypher query로 변환해 준실시간으로 graph를 업데이트하는 loop를 만들었다.
- AK아이에스는 MEL 문서와 MRO 정비 이력 데이터를 S3에 적재하고, OpenSearch index와 Bedrock Claude 기반 chatbot agent가 MEL search와 정비 이력 search tool을 호출하는 구조를 소개했다.
- 항공 정비 AI는 hallucination이 안전 리스크가 되므로 신뢰도 scoring, golden dataset 기반 정기 검증, 직급별 사용 권한과 human final decision 원칙을 세웠다.
- AI OCR은 정비사가 모바일로 종이 문서를 촬영하면 S3에 저장하고 Amazon Textract가 표와 손글씨를 읽어 정비 업무 시스템에 입력하는 흐름으로 설명됐다.

## 세부 내용

### 배경과 문제 인식

제주항공과 하나투어가 AWS 생성형 AI로 일궈낸 현장 혁신 사례를 공개합니다. 하나투어의 여행상품 기획 에이전트 고도화와 제주항공의 항공 정비 의사결정 효율화 과정을 다룹니다. 규제가 엄격한 항공 산업과 복잡한 여행 기획 업무에 AI를 안전하게 접목한 실전 노하우와 아키텍처 재설계 전략, 비즈니스 가치 창출에 대한 생생한 인사이트를 만나보세요.

발표는 이 배경에서 출발해 실제 서비스나 운영 환경에서 어떤 제약이 있었고, 이를 해결하기 위해 어떤 기술 선택과 구현 방식을 택했는지를 설명했다. 단순한 기능 소개보다 현장에서 마주한 병목, 데이터 흐름, 운영 책임을 어떻게 정리했는지가 핵심 맥락이다.

### 구현 접근

- AWS 파트는 여행 상품 기획 텍스트를 knowledge graph로, 항공 정비 종이 문서를 구조화된 디지털 데이터로 바꾸는 것이 AI 활용의 전제라고 설명했다.
- 하나투어의 1차 LLM 반복 구조는 10-20분 이상 걸리고 토큰/EC2 비용이 컸으며, 결과도 MD의 상품 기획 품질에는 미치지 못했다.
- 외부 지도/검색 기반 LLM을 활용한 2차 시도는 20-30초까지 빨라졌지만, 하나투어 고유 자산과 MD 노하우가 빠져 선택받지 못했다.
- 최종 구조는 Amazon Neptune에 여행 graph를 저장하고, AgentCore Runtime에 배포된 Claude 기반 agent가 AgentCore Gateway를 통해 graph 저장/검색 tool을 호출하는 방식이다.

### 운영과 확장 관점

- “그래프에 없는 데이터는 사용하지 말라”는 원칙으로 hallucination을 줄였고, MD 피드백을 자연어로 받아 Cypher query로 변환해 준실시간으로 graph를 업데이트하는 loop를 만들었다.
- AK아이에스는 MEL 문서와 MRO 정비 이력 데이터를 S3에 적재하고, OpenSearch index와 Bedrock Claude 기반 chatbot agent가 MEL search와 정비 이력 search tool을 호출하는 구조를 소개했다.
- 항공 정비 AI는 hallucination이 안전 리스크가 되므로 신뢰도 scoring, golden dataset 기반 정기 검증, 직급별 사용 권한과 human final decision 원칙을 세웠다.
- AI OCR은 정비사가 모바일로 종이 문서를 촬영하면 S3에 저장하고 Amazon Textract가 표와 손글씨를 읽어 정비 업무 시스템에 입력하는 흐름으로 설명됐다.

## 정리

이 세션은 [하나투어 I AK아이에스] AI가 바꾸는 여행 산업의 무대 뒤: 하나투어, 제주항공의 업무혁신 이라는 주제를 통해, 실제 산업 현장에서 AWS와 AI/클라우드 기술을 어떻게 서비스 개선과 운영 효율로 연결했는지를 보여줬다. 핵심은 새로운 도구의 나열이 아니라 문제를 정의하고, 데이터와 아키텍처를 정리하며, 운영자가 신뢰할 수 있는 방식으로 결과를 만드는 과정에 있었다.
