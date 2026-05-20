# Skill: /tech-analyze

GitHub 저장소에서 기술 스택을 자동으로 분석하여 TECH_STACK.md를 생성/업데이트합니다.

## Description

GitHub CLI (gh)를 사용하여 개인 저장소를 조회하고, 사용된 기술을 자동으로 추출합니다.
기술을 Tier 1-3으로 분류하고 숙련도를 판정하여 TECH_STACK.md를 생성합니다.

## Usage

### 기본 사용
```
/tech-analyze --update
```

### 옵션
```
/tech-analyze --update          # TECH_STACK.md 생성/업데이트 (기본)
/tech-analyze --format json     # JSON 형식으로 출력
/tech-analyze --format markdown # Markdown 형식으로 출력 (기본)
/tech-analyze --verbose         # 상세 출력
```

## Implementation

### 1단계: GitHub CLI 사전 조건 확인
```powershell
# GitHub CLI 설치 확인
$gh = Get-Command gh -ErrorAction SilentlyContinue
if (-not $gh) {
    Write-Error "GitHub CLI (gh)가 설치되지 않았습니다."
    exit 1
}

# 인증 확인
$auth = & gh auth status 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Error "GitHub 인증이 필요합니다. 'gh auth login'을 실행해주세요."
    exit 1
}
```

### 2단계: 저장소 조회
```powershell
# GitHub에서 최대 100개 저장소 조회
$repos = & gh repo list nobrain711 `
    --limit 100 `
    --json name,primaryLanguage,updatedAt,description `
    | ConvertFrom-Json

Write-Host "조회된 저장소: $($repos.Count)개"
```

### 3단계: 기술 키워드 추출
```python
# gh_tech_analyzer.py 스크립트 실행

import json
import subprocess
from datetime import datetime, timedelta
from collections import Counter

def extract_tech_stack(repos):
    """
    저장소 목록에서 기술 키워드 추출
    """
    tech_count = Counter()
    tech_details = {}
    
    for repo in repos:
        name = repo['name']
        language = repo['primaryLanguage']
        updated_at = repo['updatedAt']
        
        # 언어별 기술 분류
        if language:
            tech_count[language] += 1
            if language not in tech_details:
                tech_details[language] = {'count': 0, 'repos': []}
            tech_details[language]['count'] += 1
            tech_details[language]['repos'].append(name)
    
    return tech_count, tech_details

def judge_proficiency(tech, repo_count, last_updated):
    """
    숙련도 판정:
    - Advanced: 3개 이상 또는 최근 1년 내 활동 있는 2개 이상
    - Intermediate: 2개 또는 최근 활동 있는 1개
    - Beginner: 1개 또는 오래된 활동
    """
    days_since_update = (datetime.now() - last_updated).days
    is_recent = days_since_update <= 365
    
    if repo_count >= 3 or (repo_count >= 2 and is_recent):
        return "Advanced"
    elif repo_count >= 2 or (repo_count == 1 and is_recent):
        return "Intermediate"
    else:
        return "Beginner"
```

### 4단계: Tier 분류
```
Tier 1 (Advanced — 주요 기술):
  - 3개 이상의 저장소에서 사용
  - 주로 프로그래밍 언어, 프레임워크, 데이터베이스

Tier 2 (Intermediate — 도구 & 플랫폼):
  - 2개의 저장소에서 사용
  - 클라우드, DevOps, CI/CD 도구

Tier 3 (Beginner — 라이브러리 & 유틸):
  - 1개 저장소에서만 사용
  - ORM, 데이터 처리, 시각화 라이브러리
```

### 5단계: TECH_STACK.md 생성
```markdown
# 기술 스택 (Tech Stack)

마지막 업데이트: 2026년 05월 19일

## Tier 1 — 주요 기술 (Advanced)

### 프로그래밍 언어
- **Python** — Advanced (12 repos)
  - 데이터 분석, 백엔드 개발 중심
  - 최근 활동: 2026년 05월

- **JavaScript/TypeScript** — Advanced (8 repos)
  - 프론트엔드, 백엔드 (Node.js) 개발
  - 최근 활동: 2026년 04월

### 웹 프레임워크
- **FastAPI** — Intermediate (2 repos)
- **Django** — Intermediate (2 repos)
- **React** — Intermediate (3 repos)

### 데이터베이스
- **PostgreSQL** — Advanced (10 repos)
- **MongoDB** — Intermediate (2 repos)

## Tier 2 — 도구 & 플랫폼 (Intermediate)

### 클라우드 & DevOps
- **AWS (EC2, S3, RDS)** — Intermediate (5 repos)
- **Docker** — Intermediate (6 repos)
- **GitHub Actions** — Intermediate (4 repos)
- **Kubernetes** — Beginner (1 repo)

## Tier 3 — 라이브러리 & 유틸 (Beginner)

### ORM & 데이터 처리
- **SQLAlchemy** — 3 repos
- **Pydantic** — 2 repos
- **NumPy** — 1 repo
- **Pandas** — 1 repo

### 시각화
- **Matplotlib** — 1 repo
```

### 6단계: 검증
```powershell
$techStackFile = Join-Path $ProjectRoot "TECH_STACK.md"

if (-not (Test-Path $techStackFile)) {
    Write-Error "TECH_STACK.md 생성 실패"
    exit 1
}

$fileSize = (Get-Item $techStackFile).Length
Write-Host "✓ TECH_STACK.md 생성 완료 ($($fileSize/1KB)KB)" -ForegroundColor Green
```

## 오류 처리

| 오류 | 원인 | 해결책 |
|------|------|--------|
| "GitHub CLI not found" | gh 미설치 | GitHub CLI 설치 (https://cli.github.com) |
| "Not authenticated" | gh 미인증 | `gh auth login` 실행 |
| "Rate limit exceeded" | API 호출 초과 | 1시간 대기 또는 `gh api rate_limit` 확인 |
| "No repos found" | 저장소 없음 | GitHub 사용자명 확인 |
| "Analysis failed" | 분석 오류 | 저장소 README 존재 확인 |

## 의존성

- **GitHub CLI (gh)** — 저장소 조회
- **Python** — 분석 스크립트 (gh_tech_analyzer.py)
- **GitHub 계정** — 저장소 접근 권한

## 생성되는 파일

| 파일명 | 크기 | 설명 |
|--------|------|------|
| TECH_STACK.md | ~5KB | 기술 스택 정보 |

## 예상 출력

```
조회된 저장소: 90개
분석 중...
  - Python: 12개 저장소 (Advanced)
  - JavaScript: 8개 저장소 (Advanced)
  - PostgreSQL: 10개 저장소 (Advanced)
  - AWS: 5개 저장소 (Intermediate)
  - Docker: 6개 저장소 (Intermediate)
  ...
✓ TECH_STACK.md 생성 완료 (5KB)
```

## 다음 단계

1. `TECH_STACK.md` 생성 확인
2. 이력서의 기술스택 섹션과 비교
3. 불일치 사항 수정 및 `/resume-compile` 실행

## 관련 스킬

- `/resume-update` — 이력서 기술스택 동기화
- `/resume-compile` — PDF 컴파일

## 참고 문서

- TECH_STACK.md — 생성되는 기술 스택 파일
- gh_tech_analyzer.py — Python 분석 스크립트
- ORCHESTRATION.md — 워크플로우 가이드

---

*최근 업데이트: 2026년 05월 19일*
