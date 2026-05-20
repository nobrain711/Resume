# Skill: /resume-update

이력서 콘텐츠를 대화형으로 편집하고 검증합니다.

## Description

`resume_korean.tex`의 특정 섹션 (학력, 경력, 기술스택 등)을 안전하게 수정합니다.
편집 후 자동으로 컴파일하여 변경 사항을 검증합니다.

## Usage

### 기본 사용
```
/resume-update
```

### 섹션 목록
```
/resume-update --section education --list       # 학력사항 목록
/resume-update --section experience --list      # 경력사항 목록
/resume-update --section skills --list          # 기술스택 목록
/resume-update --section certifications --list  # 자격증 목록
```

### 항목 추가
```
/resume-update --section education --add "영남이공대학교 2021.03-2024.02"
/resume-update --section experience --add "회사명 2026.01-현재 소프트웨어 엔지니어"
/resume-update --section skills --add "Go"
```

### 항목 수정
```
/resume-update --section experience --edit 1 "새로운 설명"
```

### 항목 삭제
```
/resume-update --section experience --delete 1
```

### 컴파일
```
/resume-update --compile        # 변경 후 자동 컴파일
/resume-update --compile --view # 컴파일 후 PDF 보기
```

## Implementation

### 1단계: 섹션 선택
```powershell
$sections = @{
    "education" = "학력사항"
    "experience" = "경력사항"
    "skills" = "기술스택"
    "certifications" = "자격증"
    "language" = "어학"
    "awards" = "수상 & 활동"
}

Write-Host "편집할 섹션을 선택해주세요:"
foreach ($section in $sections.Keys) {
    Write-Host "  - $section : $($sections[$section])"
}
```

### 2단계: 현재 내용 표시
```powershell
function Show-Section {
    param([string]$SectionName)
    
    $texFile = Get-Content (Join-Path $ProjectRoot "resume_korean.tex") -Raw
    
    # 섹션별 정규식으로 내용 추출
    switch ($SectionName) {
        "education" {
            $pattern = '\\section\{학력사항\}(.*?)(?=\\section|\\\end\{document\})'
        }
        "experience" {
            $pattern = '\\section\{경력사항\}(.*?)(?=\\section|\\\end\{document\})'
        }
        "skills" {
            $pattern = '\\section\{기술스택\}(.*?)(?=\\section|\\\end\{document\})'
        }
    }
    
    if ($texFile -match $pattern) {
        Write-Host "현재 내용:"
        Write-Host $matches[1]
    }
}
```

### 3단계: 콘텐츠 검증
```powershell
function Validate-Content {
    param([string]$Content, [string]$SectionName)
    
    $errors = @()
    
    # 공통 검증
    if ([string]::IsNullOrWhiteSpace($Content)) {
        $errors += "빈 콘텐츠입니다."
    }
    
    switch ($SectionName) {
        "education" {
            # 날짜 형식 (YYYY.MM -- YYYY.MM)
            if ($Content -notmatch '\d{4}\.\d{2}.*\d{4}\.\d{2}') {
                $errors += "날짜 형식이 잘못되었습니다. 형식: YYYY.MM -- YYYY.MM"
            }
        }
        "experience" {
            # 기간 및 직책 확인
            if ($Content -notmatch '\d{4}\.\d{2}') {
                $errors += "기간 정보가 없습니다."
            }
        }
        "skills" {
            # 기술명 확인
            if ($Content -match '[\{\}]') {
                $errors += "특수 문자가 포함되어 있습니다: \{\}"
            }
        }
    }
    
    return $errors
}
```

### 4단계: 파일 수정
```powershell
function Update-ResumeSection {
    param(
        [string]$SectionName,
        [string]$NewContent
    )
    
    $texFile = Join-Path $ProjectRoot "resume_korean.tex"
    $content = Get-Content $texFile -Raw
    
    $pattern = "\\section\{$sectionPattern\}(.*?)(?=\\section|\\end\{document\})"
    
    # LaTeX 구조 유지하며 교체
    $newContent = $content -replace $pattern, "`$0$newContent"
    
    Set-Content -Path $texFile -Value $newContent
    
    Write-Host "✓ $SectionName 업데이트 완료"
}
```

### 5단계: 컴파일 및 검증
```powershell
function Compile-AndValidate {
    Write-Host "이력서 컴파일 중..."
    
    & xelatex -interaction=nonstopmode resume_korean.tex | Out-Null
    & xelatex -interaction=nonstopmode resume_korean.tex | Out-Null
    
    if (Test-Path "resume_korean.pdf") {
        $fileSize = (Get-Item "resume_korean.pdf").Length
        Write-Host "✓ 컴파일 완료: $($fileSize/1KB)KB"
        
        # 페이지 초과 경고
        if ($fileSize -gt 500KB) {
            Write-Warning "PDF 파일이 큽니다. 페이지 초과 여부를 확인해주세요."
        }
    } else {
        Write-Error "컴파일 실패"
        exit 1
    }
}
```

## 섹션별 예시

### 학력사항 추가
```
입력:
  섹션: education
  학교: 영남이공대학교
  기간: 2021.03 -- 2024.02
  학과: 컴퓨터공학과
  학점: 3.75/4.5

결과:
  \resumeSubheading
    {영남이공대학교}
    {2021.03 -- 2024.02}
    {컴퓨터공학과 (학점: 3.75/4.5)}
    {대구광역시}
```

### 경력사항 추가
```
입력:
  회사: (주)OO기업
  기간: 2025.01 -- 현재
  직책: 소프트웨어 엔지니어
  지역: 서울시 강남구
  담당업무:
    - 백엔드 API 개발 (FastAPI, Python)
    - AWS 인프라 관리 (EC2, RDS)

결과:
  \resumeSubheading
    {(주)OO기업}
    {2025.01 -- 현재}
    {소프트웨어 엔지니어}
    {서울시 강남구}
  
  \begin{itemize}
    \resumeItem{백엔드 API 개발 (FastAPI, Python)}
    \resumeItem{AWS 인프라 관리 (EC2, RDS)}
  \end{itemize}
```

## 오류 처리

| 오류 | 원인 | 해결책 |
|------|------|--------|
| "Invalid date format" | 날짜 형식 오류 | YYYY.MM 형식 사용 |
| "Validation failed" | 콘텐츠 검증 실패 | 오류 메시지 확인, 수정 |
| "Compilation failed" | LaTeX 문법 오류 | .log 파일 확인 |
| "LaTeX structure broken" | 구조 손상 | Git으로 롤백, 다시 시도 |

## 의존성

- **XeLaTeX** — PDF 컴파일
- **Git** — 버전 관리 (옵션)

## 백업 및 복구

### 자동 백업
```powershell
# 수정 전 백업 생성
Copy-Item resume_korean.tex "resume_korean.$(Get-Date -Format 'yyyyMMdd_HHmmss').tex.bak"
```

### 복구
```powershell
# Git으로 복구
git checkout resume_korean.tex

# 또는 백업 파일로 복구
Copy-Item resume_korean.*.tex.bak resume_korean.tex
```

## 다음 단계

1. 이력서 수정 완료
2. PDF에서 변경 사항 확인
3. `/resume-compile`로 최종 컴파일
4. `git add` 및 `git commit`으로 저장

## 관련 스킬

- `/resume-compile` — PDF 컴파일
- `/tech-analyze` — 기술스택 동기화

## 참고 문서

- CLAUDE.md — 작성 규칙
- resume_korean.tex — 이력서 소스
- ORCHESTRATION.md — 워크플로우 가이드

---

*최근 업데이트: 2026년 05월 19일*
