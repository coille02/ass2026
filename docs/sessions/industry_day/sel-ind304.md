# sel-ind304 - 당근의 CloudHSM/KMS기반 대규모 서명키관리 시스템구축기

[Industry Day 전체 요약으로 돌아가기](../../industry_day_summary.md)

**제목/시간/트랙/발표자**  
- 제목: 당근의 CloudHSM/KMS기반 대규모 서명키관리 시스템구축기
- 시간: 2026-05-20 14:30-15:10 KST
- 트랙: Retail & Consumer Goods / Application Integration, Security & Identity
- 발표자: 박진현 솔루션즈 아키텍트(AWS), 조승환 Identity Service Engineer(당근), 최용환 Site Reliability Engineer(당근)

**핵심 요약**  
당근은 월간 활성 사용자 2,000만 명 이상, 하루 평균 6,500만 건 이상의 인증 요청을 처리하는 환경에서 서명키 유출 위험을 줄이고 대규모 JWT 서명을 안정적으로 처리하기 위해 CloudHSM과 KMS 기반 하이브리드 구조를 구축했다. 기존에는 private key가 Secret Manager에 있어 접근 권한이 있으면 추출 가능성이 남아 있었고, 모바일 앱에서 서명 서비스에 직접 연결되는 구조상 더 촘촘한 접근 제어가 필요했다. CloudHSM은 비용, 지연시간, 선형 확장성 측면에서 메인 서명 백엔드로 선택됐고, KMS는 장애 시 fallback을 위한 standby로 구성됐다. 운영 중 HSM 통신 장애 상황에서도 KMS fallback으로 사용자 영향 없이 서비스를 유지한 사례가 핵심 성과로 소개됐다.

**주요 포인트**
- 서명키는 JWT, 코드 서명, TLS 인증서 등 신뢰 체계의 뿌리이며, 유출 시 공급망 전체와 사용자 인증 체계가 무너질 수 있다는 점을 먼저 짚었다.
- 당근은 private key가 절대 외부로 유출되지 않을 것, 6,000 RPS 수준 서명 트래픽을 감당할 것, SPOF가 없을 것, 접근 제어가 촘촘할 것, 담당자도 임의 서명할 수 없을 것을 요구사항으로 잡았다.
- CloudHSM은 VPC 내부 배치, PKCS#11 표준 인터페이스, 싱글 테넌트, 시간당 과금 구조 덕분에 고트래픽 환경에서 유리하다고 판단했다.
- EKS, Istio Authorization Policy, 보안 그룹, mTLS, Secret Manager, IRSA, CloudTrail, Kyverno 정책을 조합해 HSM 접근 경로를 다층으로 제한했다.
- PKCS#11 세션 고정, scale-in 시 in-flight 요청 오류, max sessions 튜닝, 바이너리 로그 관측성 부족 같은 실전 이슈를 테스트와 로그 수집 컴포넌트로 해결했다.
- JWT `kid` 기반 키 로테이션으로 기존 수천만 토큰을 깨지 않고 HSM/KMS/기존 local key를 공존시키며 무중단 전환했다.

**AWS/기술 키워드**
- AWS CloudHSM, AWS KMS, AWS Secrets Manager, AWS CloudTrail, EKS, Istio, mTLS, IRSA, Kyverno, PKCS#11, JWT, KID, active-standby fallback

**현장 메모로 남길 점**
- 보안 아키텍처의 좋은 사례였다. 키를 “잘 숨기는” 수준이 아니라 추출 불가능성, 접근 주체 분리, fallback, 관측성, 키 로테이션까지 운영 전체를 설계했다.

**블로그용 한줄**
- “당근의 사례는 대규모 인증 시스템에서 CloudHSM과 KMS를 조합하면 보안성과 고가용성을 동시에 잡을 수 있음을 보여줬다.”

### 전사 기반 상세 보강

- 세션 맥락: 당근의 CloudHSM/KMS기반 대규모 서명키관리 시스템구축기
- 공식 설명 보강: 서명키, 아직 환경변수에 저장하고 계신가요? 서명키는 단 하나의 키 유출만으로도 전체 사용자의 인증이 무력화될 수 있는 만큼, 관리에 다양한 고민이 필요합니다. 본 세션에서는 당근이 MAU 2,100만 서비스에 AWS CloudHSM과 KMS기반의 하이브리드 아키텍처를 설계하고 운영하며, 높은 보안성과 비용 최적화를 동시에 달성한 실전 과정을 공유합니다.
- 전사에서 반복적으로 확인된 키워드: KMS, 인증, 전환, 보안, 운영, 테스트, 데이터, 감사, 장애, 고객
- 발표에서 두드러진 주제 축: security, ops, business, governance

#### 발표 흐름
- 초반: KMS, 보안, 인증, 고객, 데이터 중심으로 security, ops, business를 다룬다.
- 중반: KMS, 개발, 인증, 인프라, 추적 중심으로 security, ops, business를 다룬다.
- 후반: KMS, 전환, 운영, 테스트, 장애 중심으로 security, ops, business를 다룬다.

#### 전사에서 확인할 만한 구간
- 00:18 부근: 고객 관련 설명이 나온다. 핵심 문맥은 `많이 사용하고 계시는 고객 중 한 곳입니다.`
- 08:08 부근: KMS, 전략 관련 설명이 나온다. 핵심 문맥은 `내일 4시에 KMS 아키텍처 지나와 서명 키 관리 전략이라는 세션도 준비되어 있으니까 꼭 들어보시길 바라겠습니다.`
- 14:16 부근: IAM, 정책 관련 설명이 나온다. 핵심 문맥은 `AWS API와 그리고 IAM 정책으로 접근곤한을 제거합니다.`
- 17:12 부근: 보안, 인증 관련 설명이 나온다. 핵심 문맥은 `LGSM 사이에 통신이 양방향 인증으로 한층도 보안성을 확보할 수 있었습니다.`
- 33:52 부근: 운영, 전환 관련 설명이 나온다. 핵심 문맥은 `운영 중인 서비스의 사면킬의 신규 시스템으로 무중단 전환하는 작업이 남았는데요.`
