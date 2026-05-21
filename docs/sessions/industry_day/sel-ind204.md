# sel-ind204 - [놀유니버스] AWS Transform을 통한 놀유니버스의 .NET 현대화

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

**Title/Time/Track/Speakers**  
- 제목: [놀유니버스] AWS Transform을 통한 놀유니버스의 .NET 현대화
- 시간: 2026-05-20 12:50-13:30 KST
- 트랙: Industry Day / Software & Internet, Travel & Hospitality / Artificial Intelligence, Migration & Modernization
- 발표자: 최준영 테크니컬 어카운트 매니저, AWS; 지윤성 실장, 놀유니버스

**핵심 요약**  
놀유니버스는 28년간 누적된 .NET 레거시 시스템을 AWS Transform for .NET과 Kiro를 활용해 현대화한 사례를 공유했다. 발표에서는 150만 라인, 1,575개 파일을 10시간 만에 분석·전환했고, Kiro로 223개 테스트를 20초 만에 자동 생성했다는 수치가 등장했다. AWS Transform은 프로젝트 전체 의존성 그래프를 분석하고 코드 그룹 단위로 병렬 변환을 오케스트레이션했으며, Kiro는 후속 테스트와 안정화에 쓰인 구조로 설명됐다. 결과적으로 4주 만에 레거시 현대화를 완료하고 컨테이너 기반 AWS 환경, CloudWatch 모니터링, 생산성 3배 향상, 비용 절감 효과를 얻었다고 정리했다.

**주요 포인트**
- 현대화 지연의 이유로 시스템 중단 우려, 비용·리소스 부담, 기술 부채, 복잡한 의존성이 제시됨.
- AWS Transform은 단일 파일 변환이 아니라 전체 프로젝트의 의존성, 변환 순서, 병렬 작업 단위를 잡아주는 에이전틱 AI 시스템으로 소개.
- Kiro는 변환 이후 테스트 자동 생성과 후속 안정화에 투입되어 검증 속도를 높임.
- 컨테이너 기반 배포와 CloudWatch 모니터링으로 운영 체질이 바뀌었다고 설명.
- 발표의 결론은 AI 도구 자체보다 기술 부채 청산을 시작할 실행 체계를 갖추는 것이 중요하다는 메시지.

**AWS/기술 키워드**  
AWS Transform for .NET, Kiro, .NET Framework Modernization, Containers, Amazon CloudWatch, 에이전틱 AI, 의존성 그래프, 테스트 자동화, 기술 부채

**현장 메모로 남길 점**  
현대화는 "코드 변환"보다 "의존성 이해, 검증, 배포, 운영 전환"이 더 큰 과제다. AWS Transform과 Kiro를 역할 분리해 쓴 점이 실제 레거시 전환 사례로 설득력 있다.

**블로그용 한줄**  
놀유니버스는 AWS Transform for .NET과 Kiro로 28년 레거시를 분석·전환·검증하며 .NET 현대화의 실행 속도를 끌어올렸다.


담당 세션: `sel-wps103`, `sel-prt214-s`, `sel-prt303-s`, `sel-prt205-s`, `sel-prt219-s`, `sel-prt208-s`, `sel-prt304-s`, `sel-prt218-s`, `sel-prt107-s`

모든 세션은 helper script로 생성한 VOD 전사본을 기반으로 요약했습니다. 전사 품질상 일부 고유명사/제품명은 공식 세션 메타데이터와 대조해 보정했습니다.
