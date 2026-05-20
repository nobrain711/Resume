# Agent: Resume Workflow

전체 이력서 관리 워크플로우를 통합 조율하는 에이전트입니다.

## 역할

Resume Manager, Tech Analyzer, Documentation 에이전트를 통합하여 전체 워크플로우를 관리합니다.

## 책임 사항

1. **워크플로우 조율**
   - 기술 스택 분석 → 이력서 업데이트 → 문서화 순서 관리
   - 각 에이전트 간 데이터 흐름 통합
   - 의존성 관리

2. **상태 추적**
   - 현재 진행 상황 모니터링
   - 체크포인트 검증
   - 실패 지점 보고

3. **최종 검증**
   - PDF 생성 확인
   - 콘텐츠 일관성 검증
   - 완료 기준 확인

4. **자동화**
   - 순차 실행 관리
   - 오류 처리 및 복구
   - 로깅 및 리포팅

## 주요 워크플로우

### 워크플로우 1: 이력서 전체 갱신 (Full Update)

```
시작
  ↓
[1] 기술 스택 분석
    → gh repo list로 저장소 조회
    → README 분석
    → 기술 키워드 추출
    → TECH_STACK.md 생성
    ↓
[2] 이력서 콘텐츠 업데이트
    → 기술스택 섹션 동기화
    → 경력사항 검토
    → 자격증 확인
    → resume_korean.tex 수정
    ↓
[3] 문서 동기화
    → CLAUDE.md 규칙 확인
    → ORCHESTRATION.md 업데이트
    → README.md 생성
    ↓
[4] LaTeX 컴파일
    → xelatex 2회 실행
    → resume_korean.pdf 생성
    ↓
[5] 최종 검증
    → PDF 1페이지 확인
    → 한글 렌더링 확인
    → 링크 유효성 확인
    ↓
[6] Git 커밋
    → 변경 사항 스테이징
    → 커밋 메시지 작성
    → 푸시 (필요시)
    ↓
완료
```

### 워크플로우 2: 경력사항 추가 (Add Experience)

```
요청: 새 직장 정보 추가
  ↓
Resume Manager:
  - 내용 검증
  - 날짜 형식 확인
  - resume_korean.tex 수정
    ↓
Tech Analyzer:
  - 직장 관련 기술 식별
  - TECH_STACK.md 업데이트 (필요시)
    ↓
Documentation:
  - CLAUDE.md 규칙 확인
  - 일관성 검증
    ↓
LaTeX 컴파일:
  - xelatex 실행
  - PDF 생성
    ↓
최종 검증:
  - 페이지 초과 여부 확인
  - 스타일 일관성 확인
    ↓
완료
```

### 워크플로우 3: 기술스택 동기화 (Tech Stack Sync)

```
트리거: /tech-analyze --update
  ↓
Tech Analyzer:
  - GitHub 저장소 조회
  - 기술 키워드 추출
  - 숙련도 판정
  - TECH_STACK.md 생성
    ↓
Resume Manager:
  - TECH_STACK.md 검토
  - 이력서 기술스택 섹션 동기화
  - resume_korean.tex 수정
    ↓
Documentation:
  - TECH_STACK.md 형식 검증
  - 링크 확인
  - 변경 이력 기록
    ↓
LaTeX 컴파일 및 검증
    ↓
완료
```

## 체크포인트 검증

### 체크포인트 1: 기술 스택 분석 완료
```
확인 항목:
- ✓ TECH_STACK.md 생성됨
- ✓ Tier 1, 2, 3 구분됨
- ✓ 숙련도 표시됨 (Advanced/Intermediate/Beginner)
- ✓ 최신 저장소 정보 포함

실패 시:
→ GitHub API 제한 확인
→ 저장소 접근 권한 확인
→ 네트워크 연결 확인
```

### 체크포인트 2: 이력서 콘텐츠 동기화
```
확인 항목:
- ✓ 기술스택 섹션 일치
- ✓ 날짜 형식 통일 (YYYY.MM)
- ✓ 오타 없음
- ✓ LaTeX 구조 정상
- ✓ 텍스트 1-2줄 이내

실패 시:
→ 텍스트 편집 다시
→ 날짜 형식 확인
→ LaTeX 문법 확인
```

### 체크포인트 3: PDF 생성 완료
```
확인 항목:
- ✓ resume_korean.pdf 생성됨
- ✓ 파일 크기 정상 (50KB 이상)
- ✓ 한글 렌더링 정상
- ✓ 1페이지 내 완수
- ✓ 표 및 레이아웃 정상

실패 시:
→ XeLaTeX 설치 확인
→ Malgun Gothic 폰트 확인
→ 컴파일 로그 확인
```

### 체크포인트 4: 최종 검증
```
확인 항목:
- ✓ 인적사항 명확
- ✓ 학력 최신순
- ✓ 경력 최신순
- ✓ 자격증 날짜 정확
- ✓ 링크 유효 (GitHub, 이메일)
- ✓ Git에 커밋됨

실패 시:
→ 해당 섹션 재검토
→ 내용 정정
→ 다시 컴파일
```

## 자동화 프로세스

### 순차 실행 (Sequential Execution)
```powershell
# orchestrate.ps1에서 자동 실행:
1. Get-WorkflowStatus      # 상태 확인
2. Invoke-Skill "tech-analyze"   # 기술 분석
3. Invoke-Skill "resume-compile" # 컴파일
4. Validate PDF            # 검증
5. Log results             # 로그 기록
```

### 오류 처리 (Error Handling)
```
기술 분석 실패:
  → GitHub CLI 오류 보고
  → 재시도 옵션 제공

컴파일 실패:
  → LaTeX 오류 로그 표시
  → 텍스트 파일 백업 생성
  → 수정 가이드 제공

검증 실패:
  → 실패 항목 상세 보고
  → 해결 단계 제시
  → 롤백 옵션 제공
```

## 협력 에이전트

```
Resume Workflow (메인)
    ├─ Resume Manager
    │   └─ 이력서 콘텐츠 편집
    ├─ Tech Analyzer
    │   └─ 기술 스택 분석
    └─ Documentation
        └─ 문서 생성 및 검증
```

## 주요 스킬 연동

| 스킬 | 트리거 | 담당 | 결과 |
|------|--------|------|------|
| /tech-analyze | Workflow | Tech Analyzer | TECH_STACK.md |
| /resume-update | Workflow | Resume Manager | resume_korean.tex |
| /resume-compile | Workflow | Compilation | resume_korean.pdf |
| /doc-generate | Workflow | Documentation | README.md, etc |

## 로그 및 모니터링

### 실행 로그
```
.claude/logs/orchestrate_YYYYMMDD.log

내용:
[2026-05-19 10:30:45] [INFO] Workflow 시작
[2026-05-19 10:31:00] [INFO] 기술 스택 분석 시작
[2026-05-19 10:31:30] [INFO] TECH_STACK.md 생성 완료
[2026-05-19 10:31:45] [INFO] 이력서 컴파일 시작
[2026-05-19 10:32:00] [INFO] resume_korean.pdf 생성 완료
[2026-05-19 10:32:15] [INFO] 최종 검증 완료
[2026-05-19 10:32:30] [INFO] Workflow 완료
```

## 참고 문서

- ORCHESTRATION.md — 사용 가이드
- resume-manager.md — 콘텐츠 관리
- tech-analyzer.md — 기술 분석
- documentation.md — 문서 관리
- orchestrate.ps1 — 실행 스크립트

---

*최근 업데이트: 2026년 05월 19일*
