# 자격증 & 교육 & 수상 기록 관리 가이드

## 📋 개요

이 폴더는 모든 자격증, 교육 수료증, 수상 및 활동 기록을 체계적으로 관리합니다.

---

## 📂 파일 구조

```
certificates_records/
├── CERTIFICATIONS.md      # 자격증 & 어학 자격 기록
├── EDUCATION_TRAINING.md  # 교육 & 수료증 기록
├── AWARDS_ACTIVITIES.md   # 수상 & 활동 기록
├── CLAUDE.md              # 이 파일 (관리 가이드)
└── images/certificates/   # 증명 이미지 & PDF (상위 폴더)
```

---

## 🎨 작성 포맷 (하이브리드 방식)

**모든 파일은 다음 포맷을 따릅니다:**

### 항목 구조

```markdown
### [자격증/교육/수상명]
- **기관**: [발행기관명] | **등급/점수**: [등급 또는 점수]
- **취득일**: YYYY.MM.DD (선택사항)

![Certificate Name](../../images/certificates/filename.jpg)
```

### 규칙

1. **메타데이터 라인**
   - 형식: `- **기관**: [기관명] | **기타정보**: [정보]`
   - 필수: 기관명
   - 선택: 취득일, 등급, 점수

2. **이미지/PDF 표시**
   - **이미지 파일** (JPG, PNG): `![alt text](../../images/certificates/filename.jpg)` (인라인 표시)
   - **PDF 파일**: `[View Certificate](../../images/certificates/filename.pdf)` (링크)
   - 경로는 상위 폴더의 `images/certificates/`를 기준으로 함

3. **날짜 형식**
   - 취득일: `YYYY.MM.DD` (예: 2023.05.14)
   - 기간: `YYYY.MM -- YYYY.MM` (예: 2023.03 -- 2024.12)

4. **섹션 구분**
   - 주 섹션: `## 🏅 [섹션명]`
   - 부 섹션: `### [항목명]`
   - 섹션 사이: `---` (구분선)

---

## 📝 작성 예시

### CERTIFICATIONS.md 예시

```markdown
# 자격증 (Certifications)

## 🗣️ 어학 (Language Proficiency)

### JLPT N3
- **기관**: 일본 정부 | **등급**: N3

![JLPT N3](../../images/certificates/N3.jpg)

### MOS
- **기관**: Microsoft

[View Certificate](../../images/certificates/mos.pdf)

---

## 💼 IT 자격증

### 빅데이터전문가 1급
- **기관**: 한국데이터산업진흥원 | **취득일**: 2022.04.15

![Big Data Specialist](../../images/certificates/빅데이터전문가%201급.jpg)
```

---

## ✅ 항목 추가 체크리스트

새로운 자격증/교육/수상을 추가할 때:

- [ ] 해당 파일(CERTIFICATIONS/EDUCATION_TRAINING/AWARDS_ACTIVITIES) 선택
- [ ] 기관명 정확하게 기입 (정식명칭)
- [ ] 취득일/시간 확인 (형식: YYYY.MM.DD 또는 YYYY.MM)
- [ ] 이미지/PDF가 `images/certificates/` 폴더에 있는지 확인
- [ ] 파일명이 한글인 경우 URL 인코딩 확인 (`%20` for space, `%25` for %)
- [ ] 마크다운 링크 경로가 올바른지 확인 (`../../images/certificates/`)
- [ ] 특수문자 처리 (괄호, 슬래시 등)
- [ ] 프리뷰에서 이미지가 제대로 로드되는지 확인

---

## 🔧 파일 수정 규칙

### DO (권장)
✅ 기관명은 공식 정식명칭 사용
```
좋은 예: 한국데이터산업진흥원, 일본 정부
```

✅ 취득일은 증명서에 명시된 날짜 사용
```
좋은 예: 2023.05.14, 2022.04.15
```

✅ 메타데이터는 파이프(|)로 구분
```
좋은 예: - **기관**: A | **등급**: B | **취득일**: 2023.01.01
```

### DON'T (피할 것)
❌ 메타데이터 빠뜨리기
```
나쁜 예: ### JLPT N3 (기관명 없음)
```

❌ 잘못된 경로
```
나쁜 예: ![cert](images/certificates/file.jpg) (상대경로 오류)
```

❌ 이미지 파일이 없는데 링크만 작성
```
나쁜 예: ![cert](../../images/certificates/nonexistent.jpg)
```

❌ 혼재된 포맷
```
나쁜 예: 어떤 항목은 메타데이터 있고, 어떤 항목은 없음
```

---

## 📸 이미지 관리

### 이미지 저장소
- 위치: 상위 폴더 → `images/certificates/`
- 포맷: JPG, PNG
- 이름 규칙: 한글/영문 모두 가능, 파일명에 스페이스는 URL 인코딩(`%20`)

### 파일명 작성 예시
```
❌ 나쁜 예:
- JLPT N3.jpg (스페이스 미인코딩)
- 빅데이터전문가 1급 (확장자 없음)

✅ 좋은 예:
- N3.jpg
- JLPT_N3.jpg
- 빅데이터전문가%201급.jpg (스페이스 인코딩)
```

---

## 🔄 버전 관리

### 커밋 메시지 규칙
```
feat: add [자격증명] certification (YYYY.MM.DD)
docs: update CERTIFICATIONS.md with [새 항목]
fix: correct [항목명] metadata in EDUCATION_TRAINING.md
```

### 예시
```
feat: add JLPT N3 certification (2023.05.14)
docs: update CERTIFICATIONS.md with language proficiency
fix: correct file path for 빅데이터전문가 1급 image
```

---

## 📋 3개 파일 역할

### CERTIFICATIONS.md
- 자격증, 어학시험, IT 자격
- 주기: 1-2년마다 추가
- 강조점: 기관명, 등급/점수, 취득일

### EDUCATION_TRAINING.md
- 교육 프로그램 수료증, 교육 수료, 훈련 과정
- 주기: 정기적 추가
- 강조점: 기관명, 프로그램명, 교육 시간/기간

### AWARDS_ACTIVITIES.md
- 수상, 수상력, 동아리, 프로젝트, 대외활동
- 주기: 즉시 추가
- 강조점: 목표, 역할, 성과

---

## ⚠️ 주의사항

1. **경로 관리**: 이 폴더에서 이미지로 이동할 때는 `../../images/certificates/` 사용
2. **인코딩**: 한글 파일명은 마크다운에서 자동으로 인코딩됨 (수동 수정 금지)
3. **일관성**: 3개 파일 모두 같은 포맷 유지
4. **백업**: 이미지 원본은 반드시 `images/certificates/`에만 보관

---

## 🚀 향후 확장

- [ ] 영문 버전 작성 (CERTIFICATIONS_EN.md)
- [ ] 이력서에서 자동 참조 링크
- [ ] GitHub/포트폴리오 사이트에 연동
- [ ] 발급 기관별 분류 인덱스

---

*마지막 업데이트: 2026년 05월 25일*
