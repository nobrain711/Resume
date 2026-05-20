# Skill: /resume-compile

LaTeX 이력서를 XeLaTeX로 컴파일하여 PDF를 생성합니다.

## Description

`resume_korean.tex`를 XeLaTeX 엔진으로 컴파일하여 `resume_korean.pdf`를 생성합니다.
2회 연속 실행하여 교차 참조(cross-reference)를 정확히 처리합니다.

## Usage

### 기본 사용
```
/resume-compile
```

### 옵션
```
/resume-compile --verbose     # 상세 출력
/resume-compile --watch       # 파일 변경 감시 (선택사항)
/resume-compile --force       # 강제 컴파일
```

## Implementation

### 1단계: 사전 조건 확인
```powershell
# XeLaTeX 설치 확인
$xelatex = Get-Command xelatex -ErrorAction SilentlyContinue
if (-not $xelatex) {
    Write-Error "XeLaTeX가 설치되지 않았습니다. MiKTeX 또는 TeX Live를 설치해주세요."
    exit 1
}

# resume_korean.tex 존재 확인
$texFile = Join-Path $ProjectRoot "resume_korean.tex"
if (-not (Test-Path $texFile)) {
    Write-Error "resume_korean.tex 파일이 없습니다."
    exit 1
}
```

### 2단계: 컴파일 실행
```powershell
cd $ProjectRoot

# 1차 컴파일 (기본 처리)
Write-Host "이력서 컴파일 중... (1/2)"
& xelatex -interaction=nonstopmode resume_korean.tex | Out-Null

if ($LASTEXITCODE -ne 0) {
    Write-Error "컴파일 실패 (1차)"
    exit 1
}

# 2차 컴파일 (참조 정규화)
Write-Host "이력서 컴파일 중... (2/2)"
& xelatex -interaction=nonstopmode resume_korean.tex | Out-Null

if ($LASTEXITCODE -ne 0) {
    Write-Error "컴파일 실패 (2차)"
    exit 1
}
```

### 3단계: 검증
```powershell
$pdfFile = Join-Path $ProjectRoot "resume_korean.pdf"

if (-not (Test-Path $pdfFile)) {
    Write-Error "PDF 파일이 생성되지 않았습니다."
    exit 1
}

$fileSize = (Get-Item $pdfFile).Length
if ($fileSize -lt 20KB) {
    Write-Warning "PDF 파일 크기가 작습니다: $($fileSize/1KB)KB"
}

Write-Host "✓ 컴파일 완료: resume_korean.pdf ($($fileSize/1KB)KB)" -ForegroundColor Green
```

### 4단계: 정리
```powershell
# 임시 파일 제거 (선택사항)
$tempExtensions = @("aux", "log", "out", "fls", "fdb_latexmk")
foreach ($ext in $tempExtensions) {
    Get-ChildItem $ProjectRoot -Filter "*.$ext" | Remove-Item -Force -ErrorAction SilentlyContinue
}
```

## 오류 처리

| 오류 | 원인 | 해결책 |
|------|------|--------|
| "XeLaTeX not found" | XeLaTeX 미설치 | MiKTeX 또는 TeX Live 설치 |
| "resume_korean.tex not found" | 파일 없음 | 파일 경로 확인 |
| "Compilation failed" | LaTeX 문법 오류 | .log 파일 확인, 텍스트 편집 |
| "PDF not generated" | 출력 실패 | 디스크 공간 확인, 권한 확인 |
| "PDF file too small" | 불완전 생성 | 컴파일 재시도 |

## 의존성

- **XeLaTeX** — LaTeX 컴파일러
- **kotex** — 한글 지원 패키지
- **fontspec** — 폰트 설정
- **Malgun Gothic** — 한글 폰트

## 예상 출력

```
이력서 컴파일 중... (1/2)
이력서 컴파일 중... (2/2)
✓ 컴파일 완료: resume_korean.pdf (67KB)
```

## 생성되는 파일

| 파일명 | 크기 | 설명 |
|--------|------|------|
| resume_korean.pdf | ~67KB | 최종 이력서 PDF |
| resume_korean.aux | ~2KB | 임시 보조 파일 (삭제 가능) |
| resume_korean.log | ~10KB | 컴파일 로그 (오류 확인용) |

## 다음 단계

1. `resume_korean.pdf` 생성 확인
2. PDF 뷰어에서 한글 렌더링 확인
3. A4 1페이지 내 완수 확인
4. 페이지 레이아웃 및 스타일 확인

## 관련 스킬

- `/resume-update` — 이력서 콘텐츠 편집
- `/tech-analyze` — 기술 스택 분석

## 참고 문서

- CLAUDE.md — 로컬 작성 규칙
- resume_korean.tex — 이력서 소스
- ORCHESTRATION.md — 워크플로우 가이드

---

*최근 업데이트: 2026년 05월 19일*
