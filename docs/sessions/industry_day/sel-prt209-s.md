# sel-prt209-s - 에버랜드의 VMware에서 Nutanix 클라우드 클러스터로 마이그레이션 여정 (sponsored by Nutanix)

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

**제목/시간/트랙/발표자**  
- 제목: 에버랜드의 VMware에서 Nutanix 클라우드 클러스터로 마이그레이션 여정 (sponsored by Nutanix)
- 시간: 2026-05-20 15:30-15:50 KST
- 트랙: Industry Day / Cloud Operations, Hybrid Cloud & Multicloud, Migration & Modernization
- 발표자: 김상우 상무, Nutanix

**핵심 요약**  
Nutanix는 엔터프라이즈가 클라우드의 유연성을 원하지만 기존 운영 모델과 애플리케이션을 한 번에 바꾸는 데 큰 리스크를 느낀다는 문제에서 출발했다. 발표는 `Nutanix Cloud Clusters(NC2) on AWS`가 온프레미스 Nutanix 운영 환경을 AWS로 확장해 동일한 관리 방식으로 프라이빗 클라우드와 퍼블릭 클라우드를 연결한다고 설명했다. 단순 마이그레이션뿐 아니라 DR, 온디맨드 클린룸, 데이터 보호, 사이버 복구, VM·컨테이너·AI 워크로드까지 단일 운영 모델로 확장할 수 있음을 강조했다. 에버랜드 사례에서는 VMC on AWS에서 NC2 on AWS로 제한된 일정 안에 이전하며 안정성, 비용 리스크 완화, 운영 연속성을 확보한 여정을 공유했다.

**주요 포인트**
- 기업의 클라우드 여정은 프라이빗, 하이브리드, 클라우드 퍼스트 단계로 이어지며, 핵심은 어느 위치에서든 일관된 운영 모델을 유지하는 것이다.
- NC2는 기존 Nutanix Prism 기반 관리 방식, 네트워크·보안 정책, 자동화 운영 프로세스를 AWS 위에서도 유지하게 해준다.
- AWS 서비스와의 연동을 통해 S3, RDS, Load Balancer, Bedrock 같은 서비스를 필요 시 활용하면서 기존 업무 환경은 안정적으로 이전할 수 있다고 설명했다.
- 온디맨드 클린룸은 평상시 NC2 클러스터를 대기 상태로 두고, 변경 불가능한 스냅샷을 S3에 저장했다가 비상 시 자동 복구 환경을 구성하는 방식이다.
- 삼성물산 리조트/에버랜드 사례는 VMC 라이선스 비용 리스크를 줄이고, Multi-AZ 기반 액티브-액티브 운영과 Nutanix Move 자동화 도구로 3개월 내 이전을 완료한 사례로 제시됐다.

**AWS/기술 키워드**  
Nutanix Cloud Clusters(NC2) on AWS, VMware Cloud on AWS, Nutanix Move, Multi-AZ, Active-Active, Amazon S3, Amazon RDS, Elastic Load Balancing, Amazon Bedrock, Hybrid Cloud, Disaster Recovery, Immutable Snapshot, On-demand Clean Room, Cyber Recovery

**현장 메모로 남길 점**  
마이그레이션 세션이지만 "클라우드 네이티브로 전면 재설계"가 아니라 시간·리스크·비용의 현실적 균형을 찾는 증검다리 전략이 핵심이었다. 에버랜드처럼 다운타임이 고객 경험에 직결되는 환경에서는 운영 모델 유지가 큰 가치로 제시됐다.

**블로그용 한줄**  
Nutanix는 NC2 on AWS로 기존 VMware 기반 운영 모델을 유지하면서 에버랜드 워크로드를 안정적으로 이전하고, DR·데이터 보호·하이브리드 확장까지 이어지는 현실적 클라우드 전환 방식을 제시했다.


> Worker 6 담당 세션 9개. 모든 세션은 `process_session.py`로 VOD 오디오를 추출하고 faster-whisper `base` 모델로 생성한 실제 transcript를 참고했다. 일부 고유명사와 음성 인식 오류는 행사 메타데이터와 문맥으로 보정했다.

### 전사 기반 상세 보강

- 세션 맥락: 에버랜드의 VMware에서 Nutanix 클라우드 클러스터로 마이그레이션 여정 (sponsored by Nutanix)
- 공식 설명 보강: 이 세션에서는 에버랜드의 VMware Cloud on AWS에서 Nutanix Cloud Clusters(NC2) on AWS로의 전환 사례를 통해 아키텍처, AWS 마이그레이션 가속화, 재해 복구 등 핵심 이점을 살펴봅니다. 또한 Move 기반 VM 이전, VMware에서 NC2로의 전환 방법과 모니터링, 가시성, 운영 사례를 소개합니다.
- 전사에서 반복적으로 확인된 키워드: 운영, 고객, 데이터, 비용, 리스크, 인프라, 전략, 자동화, S3, 전환
- 발표에서 두드러진 주제 축: ops, business, data, governance

#### 발표 흐름
- 초반: 운영, 인프라, 고객, 데이터, 에이전트 중심으로 ops, business, data를 다룬다.
- 중반: 운영, 리스크, 비용, 데이터, 보안 중심으로 ops, business, data를 다룬다.
- 후반: 운영, 데이터, 고객, 비용, 자동화 중심으로 ops, business, data를 다룬다.

#### 전사에서 확인할 만한 구간
- 01:44 부근: 리스크, 운영 관련 설명이 나온다. 핵심 문맥은 `다운타임이나 그리고 운영 변화 자체가 큰 리스크로 이어질 수 있다는 겁니다.`
- 05:54 부근: 고객, 데이터 관련 설명이 나온다. 핵심 문맥은 `특히 핵심 업무나 민감한 데이터는 여전히 고객이 직접 통제 가능한 환경을 선호하는 경우가 많습니다.`
- 10:07 부근: 리스크, 운영 관련 설명이 나온다. 핵심 문맥은 `운영과 보안 리스크가 커질 수밖에 없다는 거예요.`
- 16:13 부근: 고객, 비용 관련 설명이 나온다. 핵심 문맥은 `어떤 고객은 비용이 월성? 어떤 고객은 빠른 서비스 복구와 연속성을`
- 17:23 부근: 고객, 장애 관련 설명이 나온다. 핵심 문맥은 `장애는 바로 직접적인 고객 경험을`
