# 자격증 & 교육 & 수상 기록 (Certificates, Education & Awards Records)

이 폴더는 모든 자격증, 교육 수료증, 수상 및 활동 기록을 체계적으로 관리합니다.

---

## 📂 폴더 구성

| 파일 | 설명 |
|------|------|
| **CERTIFICATIONS.md** | 자격증 & 어학 자격 (JLPT, MOS, 빅데이터 1급 등) |
| **EDUCATION_TRAINING.md** | 교육 프로그램 & 수료증 (스마트시티, VR 교육 등) |
| **AWARDS_ACTIVITIES.md** | 수상 & 활동 (메이커톤, 프로젝트, 동아리 등) |
| **CLAUDE.md** | 📖 **관리 가이드 (필독!)** |
| **README.md** | 이 파일 (폴더 개요) |

---

## 📋 이력서 샘플 (Resume Sample)

이력서 작성 시 참고할 수 있는 샘플:

[📄 Resume Sample](sample.pdf)

---

## 🚀 빠른 시작

### 1. 새로운 항목 추가
1. 해당 파일(CERTIFICATIONS/EDUCATION_TRAINING/AWARDS_ACTIVITIES) 오픈
2. [CLAUDE.md](CLAUDE.md)의 포맷 따라서 작성
3. 이미지/PDF 파일은 `images/certificates/` 폴더에 저장

### 2. 항목 수정
1. 해당 파일에서 메타데이터 업데이트
2. 경로 및 포맷 일관성 확인 (CLAUDE.md 참조)

### 3. Commit 진행
```bash
git add certificates_records/
git commit -m "feat: add [자격증명] (YYYY.MM.DD)"
```

---

## 📸 이미지 저장소

- **위치**: 상위 폴더 → `images/certificates/`
- **형식**: JPG, PNG, PDF
- **이름 규칙**: 한글/영문 모두 가능

---

## 📖 관리 규칙

**반드시 읽어야 할 파일**: [CLAUDE.md](CLAUDE.md)

- ✅ 작성 포맷 (메타데이터, 이미지/PDF 표시)
- ✅ DO/DON'T 체크리스트
- ✅ 경로 관리 규칙
- ✅ 커밋 메시지 규칙

---

## 💡 핵심 포맷 (요약)

```markdown
### [항목명]
- **기관**: [기관명] | **등급/점수**: [정보]

![Certificate](../../images/certificates/filename.jpg)
```

자세한 내용은 [CLAUDE.md](CLAUDE.md) 참조.

---

## 🔄 Git 관리

### 권장 커밋 메시지
```
feat: add [자격증명] certification (YYYY.MM.DD)
docs: update CERTIFICATIONS.md with [새 항목]
fix: correct metadata in EDUCATION_TRAINING.md
```

### 예시
```bash
git commit -m "feat: add JLPT N3 certification (2023.05.14)"
git commit -m "docs: update CERTIFICATIONS.md with MOS"
git commit -m "fix: correct image path for 빅데이터전문가 1급"
```

---

## ✨ 특징

- 📌 **하이브리드 포맷**: 이미지는 인라인, PDF는 링크로 표시
- 🎯 **일관된 구조**: 3개 파일 모두 동일한 포맷
- 📱 **프리뷰 친화적**: GitHub, IDE에서 즉시 확인 가능
- 🔗 **경로 관리**: 상대경로로 이동성 높음

---

**마지막 업데이트**: 2026년 05월 25일
