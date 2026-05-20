# Skill: /doc-generate

마크다운 문서를 자동으로 생성하고 관리합니다.

## Description

TECH_STACK.md, README.md, CLAUDE.md 등 프로젝트 문서를 자동으로 생성하고 업데이트합니다.
링크 검증 및 형식 검증을 수행하여 문서 품질을 보장합니다.

## Usage

### 기본 사용
```
/doc-generate --tech-stack     # TECH_STACK.md 생성 (기본)
```

### 옵션
```
/doc-generate --tech-stack                 # TECH_STACK.md 생성/업데이트
/doc-generate --readme                     # README.md 생성
/doc-generate --validate-links             # 링크 유효성 검증
/doc-generate --validate-markdown          # 마크다운 형식 검증
/doc-generate --all                        # 모든 문서 생성/검증
```

## Implementation

### 1단계: 문서 생성 - TECH_STACK.md
```python
def generate_tech_stack_md(tech_data):
    """
    기술 스택 데이터로부터 TECH_STACK.md 생성
    
    Args:
        tech_data: Tech Analyzer로부터의 데이터
    """
    content = """# 기술 스택 (Tech Stack)

마지막 업데이트: {date}

## Tier 1 — 주요 기술 (Advanced)

### 프로그래밍 언어
{tier1_languages}

### 웹 프레임워크
{tier1_frameworks}

### 데이터베이스
{tier1_databases}

## Tier 2 — 도구 & 플랫폼 (Intermediate)

### 클라우드 & DevOps
{tier2_cloud}

### 개발 도구
{tier2_tools}

## Tier 3 — 라이브러리 & 유틸 (Beginner)

### 데이터 처리
{tier3_data}

### 시각화 & 유틸리티
{tier3_utils}
"""
    
    return content.format(
        date=datetime.now().strftime("%Y년 %m월 %d일"),
        tier1_languages=_format_tier1_languages(tech_data),
        tier1_frameworks=_format_tier1_frameworks(tech_data),
        # ... 추가 포맷팅
    )
```

### 2단계: 문서 생성 - README.md
```python
def generate_readme_md():
    """
    프로젝트 README.md 생성
    """
    content = """# 이력서 관리 시스템 (Resume Management System)

## 개요

한국형 이력서를 LaTeX/XeLaTeX로 작성하고, GitHub 저장소 분석을 통해 기술 스택을 자동으로 관리하는 통합 시스템입니다.

## 주요 기능

- 📄 **LaTeX 이력서 관리** — XeLaTeX로 PDF 생성
- 📊 **기술 스택 분석** — GitHub 저장소에서 자동 추출
- 🔄 **자동 동기화** — 이력서와 기술 스택 연동
- 📝 **문서 관리** — TECH_STACK.md, CLAUDE.md 자동 생성
- 🤖 **워크플로우 통합** — Orchestration Harness로 통합 관리

## 파일 구조

```
d:\\workspace\\00_doc\\00_resume\\
├── resume_korean.tex          # LaTeX 이력서 소스
├── resume_korean.pdf          # 생성된 이력서 PDF
├── TECH_STACK.md              # 기술 스택 정보
├── CLAUDE.md                  # 로컬 작성 규칙
├── TECH_STACK.md              # 기술 스택 파일
└── .claude/                   # Claude Code 통합
    ├── orchestrate.ps1        # 오케스트레이션 스크립트
    ├── ORCHESTRATION.md       # 사용 가이드
    ├── agents/                # 에이전트 정의
    ├── skills/                # Claude Code 스킬
    ├── scripts/               # 실행 스크립트
    └── logs/                  # 자동 생성 로그
```

## 시작하기

### 1단계: 의존성 설치
```powershell
# XeLaTeX 설치 (MiKTeX 또는 TeX Live)
# GitHub CLI 설치
# Python 설치 (3.8+)
```

### 2단계: 오케스트레이션 시작
```powershell
cd d:\\workspace\\00_doc\\00_resume
.\\.claude\\orchestrate.ps1
```

### 3단계: 메뉴에서 작업 선택
```
[1] 📊 워크플로우 상태 확인
[2] 📝 이력서 컴파일
[3] 🔍 기술 스택 분석
[4] 🤖 Agent 목록 보기
```

## 사용 예시

### 이력서 컴파일
```powershell
.\\.claude\\orchestrate.ps1 compile
```

### 기술 스택 분석 및 동기화
```powershell
.\\.claude\\orchestrate.ps1 analyze
```

### Claude Code 스킬 사용
```
/resume-compile          # LaTeX 컴파일
/tech-analyze --update   # 기술 스택 분석
/resume-update           # 이력서 콘텐츠 편집
/doc-generate --all      # 모든 문서 생성
```

## 기술 스택

### Tier 1 — 주요 기술
- **XeLaTeX** — LaTeX 컴파일러
- **kotex** — 한글 지원
- **GitHub CLI** — 저장소 조회

### Tier 2 — 도구
- **PowerShell** — 오케스트레이션
- **Python** — 분석 스크립트
- **Git** — 버전 관리

### Tier 3 — 라이브러리
- **Pydantic** — 데이터 검증
- **Click** — CLI 프레임워크

## 로컬 규칙

CLAUDE.md 파일을 참고하여 이력서 작성 규칙을 확인하세요.

### 주요 규칙
- 이력서: 한국형 A4 1페이지
- 폰트: Malgun Gothic
- 날짜 형식: YYYY.MM (예: 2026.01)
- 내용: 정량적 성과 중심
- 문자 제한: 각 항목 1-2줄 이내

## 워크플로우 가이드

### 표준 워크플로우
```
1. 이력서 콘텐츠 편집
2. 기술 스택 분석 및 동기화
3. LaTeX 컴파일 (PDF 생성)
4. 최종 검증
5. Git 커밋
```

### 자동화 워크플로우
```
.\\.claude\\orchestrate.ps1
→ [메뉴] [3] 기술 스택 분석
→ [메뉴] [2] 이력서 컴파일
→ PDF 확인
```

## 문제 해결

### PDF 생성 실패
```powershell
# XeLaTeX 설치 확인
xelatex --version

# Malgun Gothic 폰트 확인
fc-list | grep "Malgun"
```

### GitHub CLI 오류
```powershell
# 인증 상태 확인
gh auth status

# 재로그인
gh auth login
```

### 상세 로그 확인
```powershell
Get-Content .\\.claude\\logs\\orchestrate_*.log -Tail 50
```

## 참고 문서

- [CLAUDE.md](CLAUDE.md) — 로컬 작성 규칙
- [TECH_STACK.md](TECH_STACK.md) — 기술 스택 정보
- [.claude/ORCHESTRATION.md](.claude/ORCHESTRATION.md) — 워크플로우 가이드
- [XeLaTeX 공식 문서](https://tug.org/xetex/)
- [GitHub CLI 가이드](https://cli.github.com/)

## 라이선스

개인 프로젝트

## 최종 업데이트

2026년 05월 19일
"""
    
    return content
```

### 3단계: 링크 검증
```python
def validate_links(markdown_file):
    """
    마크다운 파일의 모든 링크 검증
    """
    errors = []
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 마크다운 링크 정규식: [text](url)
    links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', content)
    
    for text, url in links:
        if url.startswith('http'):
            # 외부 URL: HTTP 상태 코드 확인 (선택사항)
            try:
                response = requests.head(url, timeout=5)
                if response.status_code != 200:
                    errors.append(f"❌ {url}: {response.status_code}")
            except:
                errors.append(f"⚠️  {url}: 접근 불가")
        elif url.startswith('#'):
            # 내부 링크: 헤딩 확인
            heading = url[1:].replace('-', ' ').lower()
            if heading not in content.lower():
                errors.append(f"❌ #{heading}: 헤딩 없음")
        else:
            # 상대 경로: 파일 존재 확인
            file_path = os.path.join(os.path.dirname(markdown_file), url)
            if not os.path.exists(file_path):
                errors.append(f"❌ {url}: 파일 없음")
    
    return errors
```

### 4단계: 마크다운 형식 검증
```python
def validate_markdown(markdown_file):
    """
    마크다운 형식 검증
    """
    errors = []
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines, 1):
        # 제목 형식 (# 또는 ##)
        if line.startswith('#') and not line.startswith('# '):
            errors.append(f"Line {i}: 제목 뒤 공백 필수 (# Title)")
        
        # 리스트 형식 (- 또는 *)
        if line.strip().startswith('-') and not line.startswith('  -'):
            if i > 1 and not lines[i-2].strip().endswith(':'):
                errors.append(f"Line {i}: 리스트 들여쓰기 필요")
        
        # 코드 블록 언어 명시
        if line.strip().startswith('```') and not line.strip()[3:]:
            errors.append(f"Line {i}: 코드 블록 언어 명시 필요 (```python)")
    
    return errors
```

### 5단계: 파일 저장 및 검증 완료
```powershell
function Save-GeneratedDocuments {
    Write-Host "📄 문서 생성 중..."
    
    # TECH_STACK.md 저장
    $techStack | Out-File -Path "$ProjectRoot\TECH_STACK.md" -Encoding UTF8
    Write-Host "✓ TECH_STACK.md 생성"
    
    # README.md 저장
    $readme | Out-File -Path "$ProjectRoot\README.md" -Encoding UTF8
    Write-Host "✓ README.md 생성"
    
    # 링크 검증
    $linkErrors = Validate-Links "$ProjectRoot\TECH_STACK.md"
    if ($linkErrors.Count -gt 0) {
        Write-Warning "링크 검증 결과: $($linkErrors.Count)개 오류"
        $linkErrors | ForEach-Object { Write-Host "  $_" }
    } else {
        Write-Host "✓ 링크 검증 완료"
    }
    
    # 마크다운 검증
    $mdErrors = Validate-Markdown "$ProjectRoot\TECH_STACK.md"
    if ($mdErrors.Count -gt 0) {
        Write-Warning "마크다운 검증 결과: $($mdErrors.Count)개 오류"
    } else {
        Write-Host "✓ 마크다운 검증 완료"
    }
}
```

## 생성되는 파일

| 파일명 | 크기 | 설명 |
|--------|------|------|
| TECH_STACK.md | ~5KB | 기술 스택 정보 |
| README.md | ~4KB | 프로젝트 개요 |

## 검증 항목

- ✅ 마크다운 형식 정상
- ✅ 모든 헤딩 계층 구조 유지
- ✅ 링크 유효성 확인
- ✅ 오타 및 띄어쓰기 확인
- ✅ 최근 업데이트 날짜 포함

## 다음 단계

1. 생성된 문서 확인
2. 링크 및 형식 검증 결과 확인
3. 필요시 수정
4. Git 커밋

## 관련 스킬

- `/tech-analyze` — 기술 스택 분석
- `/resume-compile` — PDF 컴파일

## 참고 문서

- TECH_STACK.md — 생성되는 기술 스택
- README.md — 생성되는 프로젝트 개요
- ORCHESTRATION.md — 워크플로우 가이드

---

*최근 업데이트: 2026년 05월 19일*
