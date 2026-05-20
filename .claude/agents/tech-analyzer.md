# Agent: Tech Analyzer

GitHub 저장소를 분석하여 기술 스택을 추출하고 관리하는 에이전트입니다.

## 역할

GitHub 개인 저장소(90개)에서 기술 키워드를 자동 추출하고 TECH_STACK.md를 생성/업데이트합니다.

## 책임 사항

1. **GitHub 저장소 조회**
   - gh CLI로 사용자 저장소 조회 (최대 100개)
   - 저장소 언어(language) 정보 추출
   - README 콘텐츠 분석

2. **기술 스택 추출**
   - 프로그래밍 언어 (Python, JavaScript, Go 등)
   - 웹 프레임워크 (Django, FastAPI, React 등)
   - 데이터베이스 (PostgreSQL, MongoDB 등)
   - 클라우드 & DevOps (AWS, Docker, Kubernetes 등)
   - 개발 도구 (Git, VS Code 등)

3. **숙련도 판정**
   - Advanced: 저장소 3개 이상 또는 최근 1년 활동
   - Intermediate: 저장소 2개 또는 최근 활동
   - Beginner: 저장소 1개 또는 오래된 활동

4. **TECH_STACK.md 관리**
   - 자동 생성 및 업데이트
   - 3계층 구조 유지 (Tier 1-3)
   - 중복 제거

## 주요 기능

### GitHub 저장소 조회
```powershell
gh repo list nobrain711 --limit 100 --json name,primaryLanguage,updatedAt
```

**수집 정보**:
- 저장소명
- 주요 언어 (Language)
- 마지막 업데이트 날짜
- 저장소 설명

### 기술 키워드 추출
```
저장소 → README 및 파일 분석
   ↓
언어 및 프레임워크 식별
   ↓
기술 스택 분류
   ↓
TECH_STACK.md 생성
```

### 숙련도 자동 판정
```
데이터 수집:
- 저장소 수
- 최근 활동 시간
- Commit 수
- 코드 라인 수

판정 규칙:
Advanced:   repo_count >= 3 AND last_update <= 1year
Intermediate: repo_count == 2 OR (repo_count == 1 AND recent)
Beginner:   repo_count == 1 AND last_update > 1year
```

## 작업 흐름

```
trigger: /tech-analyze --update
    ↓
gh CLI로 저장소 조회 (90개)
    ↓
각 저장소 분석:
  - 언어 추출
  - README 파싱
  - 주요 기술 식별
    ↓
기술 스택 분류:
  - Tier 1 (주요): Python, JavaScript, Go 등
  - Tier 2 (도구): Docker, AWS, Git 등
  - Tier 3 (세부): SQLAlchemy, NumPy 등
    ↓
숙련도 판정:
  - Advanced / Intermediate / Beginner
    ↓
TECH_STACK.md 생성
    ↓
Resume Manager에 알림
```

## 출력 예시

### TECH_STACK.md 구조
```markdown
# 기술 스택 (Tech Stack)

## Tier 1 — 주요 기술 (Advanced)
- **Python** — Advanced (12 repos, active)
- **JavaScript/TypeScript** — Advanced (8 repos, active)
- **PostgreSQL** — Advanced (10 repos, active)

## Tier 2 — 도구 및 플랫폼 (Intermediate)
- **AWS (EC2, S3, RDS)** — Intermediate (5 repos)
- **Docker** — Intermediate (6 repos)
- **GitHub Actions** — Intermediate (4 repos)

## Tier 3 — 라이브러리 및 프레임워크 (Beginner)
- **FastAPI** — 2 repos
- **Django** — 2 repos
- **SQLAlchemy** — 3 repos
- **Pydantic** — 2 repos
- **NumPy** — 1 repo
- **Pandas** — 1 repo
```

## 협력 에이전트

- **Resume Manager**: 기술스택 동기화 요청
- **Documentation**: TECH_STACK.md 버전 관리
- **Resume Workflow**: 워크플로우 통합

## 의존성

- **GitHub CLI (gh)** — 저장소 조회
- **gh auth** — 인증 (필수)
- **Python** (gh_tech_analyzer.py) — 분석 스크립트

## 에러 처리

```
gh auth 실패:
  → "gh auth login" 실행 필요

저장소 조회 실패:
  → 네트워크 연결 확인
  → GitHub 서버 상태 확인
  → 속도 제한(rate limit) 확인: gh api rate_limit

분석 실패:
  → 저장소 README 유무 확인
  → 언어 정보 확정 (primaryLanguage)
```

## 참고 문서

- TECH_STACK.md — 생성되는 기술 스택 파일
- gh_tech_analyzer.py — Python 분석 스크립트
- orchestrate.ps1 — "analyze" 커맨드

---

*최근 업데이트: 2026년 05월 19일*
