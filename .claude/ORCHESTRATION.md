# Orchestration Harness — Usage Guide

Resume Workflow를 관리하는 통합 오케스트레이션 시스템입니다.

## 빠른 시작

### 대화형 모드
```powershell
cd d:\workspace\00_doc\00_resume
.\.claude\orchestrate.ps1
```

메뉴를 선택하여 워크플로우를 진행합니다.

### 명령어 모드
```powershell
.\.claude\orchestrate.ps1 status
.\.claude\orchestrate.ps1 compile
.\.claude\orchestrate.ps1 analyze
```

---

## 주요 기능

### 1. 워크플로우 상태 확인 (status)
```powershell
.\.claude\orchestrate.ps1 status
```

다음 항목을 확인합니다:
- ✓ resume_korean.pdf (PDF 생성 완료)
- ✓ TECH_STACK.md (기술 스택 정보)
- ✓ gh_tech_analyzer.py (GitHub 분석 스크립트)
- Registered Agents (등록된 에이전트 수)
- Registered Skills (등록된 스킬 수)

### 2. 이력서 컴파일 (compile)
```powershell
.\.claude\orchestrate.ps1 compile
```

XeLaTeX로 resume_korean.tex를 컴파일하여 PDF를 생성합니다.
- 컴파일 2회 실행 (교차 참조 정확성)
- 에러 발생 시 자동 보고

### 3. 기술 스택 분석 (analyze)
```powershell
.\.claude\orchestrate.ps1 analyze
```

GitHub 저장소에서 기술 스택을 분석하여 TECH_STACK.md를 업데이트합니다.
- 90개 저장소 조회
- 기술 키워드 자동 추출
- 숙련도 판정 (Advanced/Intermediate/Beginner)

---

## Agents (정의만 포함, 실행은 Claude Code에서)

### 1. Resume Manager
**경로**: `.claude/agents/resume-manager.md`
- 이력서 콘텐츠 관리
- 섹션별 편집 가이드
- 한국형 이력서 작성 규칙

### 2. Tech Analyzer
**경로**: `.claude/agents/tech-analyzer.md`
- GitHub 저장소 분석
- 기술 스택 추출
- TECH_STACK.md 업데이트

### 3. Documentation
**경로**: `.claude/agents/documentation.md`
- 프로젝트 문서화
- 마크다운 관리
- 링크 검증

### 4. Resume Workflow
**경로**: `.claude/agents/resume-workflow.md`
- 전체 워크플로우 통합
- 순차 실행 관리
- 최종 검증

---

## Skills (대화형 상호작용)

### 1. /resume-compile
LaTeX 이력서를 PDF로 컴파일합니다.

```
/resume-compile
```

**동작**:
- xelatex 2회 실행
- resume_korean.pdf 생성
- 컴파일 오류 감지

### 2. /tech-analyze
GitHub 저장소에서 기술 스택을 분석합니다.

```
/tech-analyze --update
```

**동작**:
- gh CLI로 저장소 조회
- 기술 키워드 추출
- TECH_STACK.md 업데이트

### 3. /resume-update
이력서 콘텐츠를 편집합니다.

```
/resume-update --section experience --list
/resume-update --section education --add "학교명 2024.01-현재"
```

**지원 섹션**:
- education (학력사항)
- experience (경력사항)
- skills (기술스택)
- certifications (자격증)

### 4. /doc-generate
마크다운 문서를 자동 생성합니다.

```
/doc-generate --tech-stack
/doc-generate --readme
```

---

## 로그 확인

### 최근 로그 보기
```powershell
.\.claude\orchestrate.ps1
# 메뉴에서 [6] 📋 로그 보기
```

또는 직접 로그 파일 확인:
```powershell
Get-Content .\.claude\logs\orchestrate_20260519.log -Tail 20
```

### 로그 디렉토리
```
.claude/logs/
└── orchestrate_YYYYMMDD.log  (일일 로그 파일)
```

---

## 시스템 설정

### 의존성 확인
```powershell
.\.claude\orchestrate.ps1
# 메뉴에서 [5] ⚙️  설정 확인
```

필수 도구:
- **XeLaTeX** — LaTeX 컴파일러 (이력서 PDF 생성)
- **GitHub CLI (gh)** — GitHub 저장소 조회
- **Python** — 기술 스택 분석 스크립트

### 설정 파일
- `.claude/settings.json` — Claude Code 설정
- `.claude/orchestrate.ps1` — 오케스트레이션 스크립트

---

## 워크플로우 예시

### 시나리오 1: 이력서 업데이트 및 컴파일
```powershell
# 1. 이력서 콘텐츠 편집
/resume-update --section experience --add "새로운 직장 2026.01-현재"

# 2. LaTeX 컴파일
.\.claude\orchestrate.ps1 compile

# 3. PDF 확인
# resume_korean.pdf 생성 완료
```

### 시나리오 2: 기술 스택 동기화
```powershell
# 1. GitHub에서 분석
.\.claude\orchestrate.ps1 analyze

# 2. TECH_STACK.md 자동 업데이트
# 기술 스택이 최신화됨

# 3. 이력서에 반영 (필요시)
/resume-update --section skills --sync
```

### 시나리오 3: 전체 워크플로우 실행
```powershell
# 1. 상태 확인
.\.claude\orchestrate.ps1 status

# 2. 기술 스택 분석
.\.claude\orchestrate.ps1 analyze

# 3. 이력서 컴파일
.\.claude\orchestrate.ps1 compile

# 4. 최종 PDF 확인
```

---

## 문제 해결

### PDF 생성 실패
```powershell
# 1. XeLaTeX 설치 확인
xelatex --version

# 2. Malgun Gothic 폰트 확인
fc-list | grep "Malgun"

# 3. 직접 컴파일 시도
cd d:\workspace\00_doc\00_resume
xelatex -interaction=nonstopmode resume_korean.tex
```

### GitHub CLI 오류
```powershell
# 1. gh 설치 확인
gh --version

# 2. 로그인 상태 확인
gh auth status

# 3. 재로그인
gh auth login
```

### Python 스크립트 오류
```powershell
# 1. Python 설치 확인
python --version

# 2. 필수 모듈 설치
pip install requests  # GitHub API 호출용

# 3. 스크립트 직접 실행
python .\.claude\scripts\gh_tech_analyzer.py --update
```

---

## 디렉토리 구조

```
.claude/
├── orchestrate.ps1                 # 메인 오케스트레이션 스크립트
├── settings.json                   # Claude Code 설정
├── ORCHESTRATION.md                # 이 파일 (사용 가이드)
│
├── agents/                         # 에이전트 정의
│   ├── resume-manager.md           # 이력서 관리 에이전트
│   ├── tech-analyzer.md            # 기술 분석 에이전트
│   ├── documentation.md            # 문서화 에이전트
│   └── resume-workflow.md          # 전체 워크플로우 에이전트
│
├── skills/                         # 스킬 정의 (Claude Code에서 사용)
│   ├── resume-compile.md           # LaTeX 컴파일 스킬
│   ├── tech-analyze.md             # 기술 분석 스킬
│   ├── resume-update.md            # 이력서 편집 스킬
│   └── doc-generate.md             # 문서 생성 스킬
│
├── scripts/                        # 실행 스크립트
│   └── gh_tech_analyzer.py         # GitHub 기술 분석 Python 스크립트
│
└── logs/                           # 자동 생성되는 로그
    └── orchestrate_YYYYMMDD.log
```

---

## 추가 정보

- **XeLaTeX 문서**: https://tug.org/xetex/
- **Korean LaTeX (kotex)**: http://faq.ktug.org/
- **GitHub CLI 가이드**: https://cli.github.com/
- **로컬 규칙**: `CLAUDE.md` 참고

---

*최근 업데이트: 2026년 05월 19일*
