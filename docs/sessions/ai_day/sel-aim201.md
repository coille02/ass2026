# sel-aim201 - Nova Forge와 Bedrock RFT로 모델 성능 극대화

[AI Day 전체 요약으로 돌아가기](../../ai_day_summary.md)

- 시간/트랙/레벨/발표자: 13:50-14:10 KST / Track 8, AI·Business Applications / 200 Intermediate / 우지환(AWS), 황윤상(AWS)
- 요약: 기업 고유 데이터와 업무 프로세스를 반영한 모델 커스터마이징 방법으로 Nova Forge와 Amazon Bedrock RFT를 소개했다. Nova Forge는 모델 개발 단계별 체크포인트, AWS 큐레이션 데이터, 기업 데이터, 보상 함수를 결합해 기업 맞춤 모델을 만들고, Bedrock RFT는 대규모 라벨 데이터 없이 강화학습 기반으로 정확도와 안전성을 높이는 방법을 제공한다.
- 주요 포인트:
  - 범용 파운데이션 모델은 기업 프로세스와 규제 맥락을 충분히 알지 못하므로 커스텀 모델 수요가 생긴다.
  - Nova Forge는 Nova 모델 개발 단계의 체크포인트를 활용해 기업 데이터와 AWS 데이터셋을 블렌딩한다.
  - 보상 함수는 “좋은 답변”의 기준을 기업별로 반영하는 장치다.
  - Bedrock RFT는 SFT의 데이터 한계를 보완하고, 적은 데이터로도 모델 행동을 강화할 수 있다.
- AWS/기술 키워드: Amazon Nova Forge, Amazon Bedrock, RFT, RLVR, RLAIF, reward function, S3, custom model, fine-tuning
- AX TF 관점/회사 AX 도입 시사점: RAG만으로 해결되지 않는 전문 업무는 커스텀 모델 또는 RFT 후보로 분류해야 한다. 단, “좋은 답변”의 평가 기준과 보상 함수를 업무 부서가 함께 정의할 수 있어야 한다.
- 공유용 한줄: 모델 커스터마이징은 데이터만 넣는 일이 아니라 회사가 원하는 답의 기준을 학습시키는 일이다.
