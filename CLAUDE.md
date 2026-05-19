# 이력서 작성 로컬 룰 (Local Rules)

## 1. 문서 구조 및 포맷

### LaTeX 파일 관리
- **주 파일**: `resume_korean.tex` (Malgun Gothic 폰트, XeLaTeX 컴파일)
- **컴파일 명령**: `xelatex resume_korean.tex && xelatex resume_korean.tex`
- **출력**: `resume_korean.pdf` (A4, 1페이지)

### Markdown 문서
- `TECH_STACK.md` — 기술 스택 관리 (3계층 구조)
- `CLAUDE.md` — 이 파일 (로컬 룰)

---

## 2. 이력서 콘텐츠 작성 가이드

### 인적사항 (Personal Information)
- **형식**: 성명, 생년월일(연나이), 성별, 주소, 연락처, 이메일
- **사진**: 3×4cm 크기의 정장 사진 (선택사항, 현재는 placeholder)
- **연락처**: 하이픈 포함 (010-XXXX-XXXX)

### 학력사항 (Education)
- **역순 정렬**: 최신 학력부터 작성
- **기간**: `YYYY.MM -- YYYY.MM` 형식 (졸업 시 `YYYY.MM`)
- **학점**: `3.8/4.5` 형식 (또는 `4.0/4.0`)
- **비고**: "졸업", "예정", "중퇴" 등

### 경력사항 (Work Experience)
- **역순 정렬**: 최신 경력부터 작성
- **기간**: `YYYY.MM -- YYYY.MM` 형식 (현재 직장은 `YYYY.MM -- 현재`)
- **담당업무**: 간결한 문장으로 주요 성과 중심 작성 (1-2줄)
- **최대 3-4개 직장** (면적 유지)

### 자격증 (Certifications)
- **자격증명**: 정확한 정식 명칭 사용
- **발행기관**: 정부 기관 또는 공식 인증 기관
- **취득일**: `YYYY.MM.DD` 형식

### 어학 (Language Proficiency)
- **주요 자격**: TOEIC, TOEFL, OPIc, IELTS 등
- **점수/등급**: 점수 또는 등급 명시
- **취득일**: 최근 순으로 정렬

### 수상/활동 (Awards & Activities)
- **구분**: "수상", "대외활동", "봉사", "프로젝트" 등
- **역순 정렬**: 최근 2-3년 중심
- **간결함**: 각 항목 한 줄 이내

---

## 3. 한국형 이력서 스타일 규칙

### 타이포그래피 (Typography)
- **폰트**: Malgun Gothic (모든 텍스트)
- **색상**:
  - 섹션 헤더: 어두운 파란색 (RGB 31, 73, 125)
  - 레이블 셀: 연한 회색-파란색 (RGB 220, 230, 242)
- **텍스트 크기**:
  - 본문: 10pt
  - 섹션 헤더: 12pt (`\large`)
  - 제목: 12pt (`\Huge`)

### 테이블 레이아웃
- **칸 간격**: 4pt (수평), 1.4배행 (수직)
- **테두리**: 모든 셀에 `\hline` 적용 (한국식 격자)
- **여백**: 상단 15mm, 하단 15mm, 좌우 20mm

### 문자 간격 (Letter Spacing)
- **섹션 제목**: `학\quad력\quad사\quad항` (단어 사이 공간)
- **레이블**: `성\hfill명` (좌우 정렬)
- 목표: 전문성 있고 읽기 쉬운 레이아웃

---

## 4. 컨텐츠 작성 팁

### DO (권장)
✅ 정량적 성과 중심으로 작성
```
좋은 예: "백엔드 API 개발 및 클라우드 인프라 관리 (AWS EC2 3대 운영)"
```

✅ 동사 시작으로 명확하게
```
좋은 예: "데이터 분석 파이프라인 구축, Python 스크립트 작성"
```

✅ 최근 경험 우선
```
좋은 예: 현재 직장부터 시작, 역연대순 배치
```

### DON'T (피할 것)
❌ 너무 길거나 복잡한 문장
```
나쁜 예: "여러 복잡한 기술을 사용하여 복잡한 시스템을 구축하였음"
```

❌ 주관적 표현
```
나쁜 예: "매우 성실하게 일했습니다", "열심히 노력했습니다"
```

❌ 1페이지를 초과하는 콘텐츠
```
유의: A4 1페이지 내에 모든 섹션 배치 필요
```

---

## 5. 파일 수정 프로세스

### 단계별 수정
1. **텍스트 콘텐츠 변경**
   - `resume_korean.tex`의 각 `\hline` 사이 항목 수정
   - 테이블 구조는 유지

2. **섹션 추가/삭제**
   - 새로운 섹션 추가 시 `\resumesection{섹션명}` 앞에 `\vspace{4pt}` 추가
   - 삭제 시 해당 테이블 블록 전체 제거

3. **컴파일 및 검증**
   ```powershell
   cd d:\workspace\00_doc\00_resume
   xelatex resume_korean.tex
   xelatex resume_korean.tex
   ```

4. **PDF 확인**
   - 한글 렌더링 정상 여부 확인
   - 페이지 초과 여부 확인 (반드시 1페이지)
   - 표 정렬 및 색상 확인

### 커밋 메시지 규칙
```
feat: add work experience at ABC Corp (2023-2025)
docs: update TECH_STACK.md with new technologies
fix: correct typo in education section
```

---

## 6. 기술 스택 연동

### TECH_STACK.md와 이력서 동기화
- **Tier 1 기술**: 이력서의 경력사항에서 주요 기술 언급
- **Tier 2 도구**: 자격증/활동 섹션에 반영 (예: Docker, AWS)
- **Tier 3 라이브러리**: 필요시 담당업무 상세 설명에 포함

### 예시
```
경력사항:
근무처: (주)예시기업
담당업무: Python, FastAPI를 이용한 백엔드 API 개발 및 
         AWS EC2 클라우드 인프라 관리

↓ TECH_STACK.md 대응

Tier 1: Python, FastAPI
Tier 2: AWS (EC2), Docker
Tier 3: SQLAlchemy, Pydantic
```

---

## 7. 자주 하는 실수 및 해결책

| 문제 | 원인 | 해결책 |
|------|------|--------|
| PDF 생성 안됨 | 폰트 문제 | Malgun Gothic 설치 확인, xelatex 재시도 |
| 한글이 깨짐 | 인코딩 오류 | UTF-8 인코딩 확인, kotex 패키지 확인 |
| 1페이지 초과 | 콘텐츠 과다 | 텍스트 축약, 섹션 통합 |
| 테이블 정렬 오류 | 열 너비 오류 | `tabularx`의 `X` 타입 재조정 |

---

## 8. 좋은 이력서 체크리스트

- [ ] 1페이지 A4 내에 모든 섹션 배치
- [ ] 한글 렌더링이 정상적으로 표시됨
- [ ] 표 테두리와 색상이 명확함
- [ ] 모든 날짜 형식이 통일됨 (YYYY.MM)
- [ ] 오타, 띄어쓰기 확인 완료
- [ ] 이메일, 연락처 최신 정보 확인
- [ ] 최신 경력/학력이 상단에 배치됨
- [ ] 정량적 성과 중심 작성
- [ ] 1-2줄 이내 간결한 설명
- [ ] TECH_STACK.md와 일관성 유지

---

## 9. 빠른 참조 (Quick Reference)

### 날짜 형식
```
학력: 2014.03 -- 2020.02
경력: 2022.03 -- 현재
자격증: 2021.11.26
```

### 테이블 셀 구조
```latex
\resumesection{섹션명}
\begin{tabularx}{\textwidth}{|p{3cm}|X|...|}
\hline
\labelcell{열제목} & ... & ... \\
\hline
내용 & ... & ... \\
\hline
\end{tabularx}
```

### 컴파일 커맨드
```powershell
xelatex resume_korean.tex && xelatex resume_korean.tex
```

---

## 10. 향후 확장 가능성

- [ ] 영문 이력서 템플릿 추가 (resume_english.tex)
- [ ] 커버레터 템플릿 작성
- [ ] 포트폴리오 링크 QR코드 추가
- [ ] 자기소개서(자소서) 테이블 추가
- [ ] 언어별 버전 자동 생성 스크립트

---

*마지막 업데이트: 2026년 05월 19일*
