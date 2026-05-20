# Orchestration Harness for Resume Workflow
# 모든 도구 (Agent + Skill + Hook) 통합 관리

param(
    [string]$Command = "",
    [string]$Option = ""
)

# ============================================================================
# CONFIGURATION
# ============================================================================

$ProjectRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$SkillsDir = Join-Path $ProjectRoot ".claude\skills"
$AgentsDir = Join-Path $ProjectRoot ".claude\agents"
$ScriptsDir = Join-Path $ProjectRoot ".claude\scripts"
$LogDir = Join-Path $ProjectRoot ".claude\logs"
$LogFile = Join-Path $LogDir "orchestrate_$(Get-Date -Format 'yyyyMMdd').log"

# Create log directory if not exists
if (-not (Test-Path $LogDir)) {
    New-Item -ItemType Directory -Path $LogDir | Out-Null
}

# ============================================================================
# LOGGING
# ============================================================================

function Write-Log {
    param([string]$Message, [string]$Level = "INFO")

    $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $LogMessage = "[$Timestamp] [$Level] $Message"

    Write-Host $LogMessage
    Add-Content -Path $LogFile -Value $LogMessage
}

# ============================================================================
# CORE FUNCTIONS
# ============================================================================

function Invoke-Skill {
    param(
        [string]$SkillName,
        [hashtable]$Params = @{}
    )

    Write-Log "Skill 실행: $SkillName" "INFO"

    $SkillFile = Join-Path $SkillsDir "$SkillName.md"
    if (-not (Test-Path $SkillFile)) {
        Write-Log "Skill 파일 없음: $SkillFile" "ERROR"
        return $false
    }

    try {
        switch ($SkillName) {
            "resume-compile" {
                Write-Log "이력서 컴파일 중..." "INFO"
                & xelatex -interaction=nonstopmode (Join-Path $ProjectRoot "resume_korean.tex") | Out-Null
                & xelatex -interaction=nonstopmode (Join-Path $ProjectRoot "resume_korean.tex") | Out-Null
                Write-Log "✓ 이력서 컴파일 완료" "INFO"
            }
            "tech-analyze" {
                Write-Log "기술 스택 분석 중..." "INFO"
                & python (Join-Path $ScriptsDir "gh_tech_analyzer.py") --update
                Write-Log "✓ 기술 스택 분석 완료" "INFO"
            }
            default {
                Write-Log "알 수 없는 Skill: $SkillName" "WARN"
                return $false
            }
        }
        return $true
    } catch {
        Write-Log "Skill 실행 오류: $_" "ERROR"
        return $false
    }
}

function Invoke-Agent {
    param([string]$AgentName)

    Write-Log "Agent 호출: $AgentName" "INFO"

    $AgentFile = Join-Path $AgentsDir "$AgentName.md"
    if (-not (Test-Path $AgentFile)) {
        Write-Log "Agent 파일 없음: $AgentFile" "ERROR"
        return $false
    }

    Write-Log "Agent 설명:" "INFO"
    Get-Content $AgentFile | Select-Object -First 10 | ForEach-Object { Write-Log $_ }

    return $true
}

function Get-WorkflowStatus {
    Write-Log "워크플로우 상태 확인 중..." "INFO"

    $Status = @{
        "resume_pdf" = (Test-Path (Join-Path $ProjectRoot "resume_korean.pdf"))
        "tech_stack_md" = (Test-Path (Join-Path $ProjectRoot "TECH_STACK.md"))
        "scripts" = (Test-Path (Join-Path $ScriptsDir "gh_tech_analyzer.py"))
        "agents" = (Get-ChildItem $AgentsDir -Filter "*.md" -ErrorAction SilentlyContinue | Measure-Object).Count
        "skills" = (Get-ChildItem $SkillsDir -Filter "*.md" -ErrorAction SilentlyContinue | Measure-Object).Count
    }

    Write-Host ""
    Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Cyan
    Write-Host "  📊 워크플로우 상태" -ForegroundColor Cyan
    Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "  이력서 PDF:        $(if ($Status.resume_pdf) { '✓' } else { '✗' }) resume_korean.pdf"
    Write-Host "  기술 스택:         $(if ($Status.tech_stack_md) { '✓' } else { '✗' }) TECH_STACK.md"
    Write-Host "  분석 스크립트:     $(if ($Status.scripts) { '✓' } else { '✗' }) gh_tech_analyzer.py"
    Write-Host "  등록된 Agent:      $($Status.agents)개"
    Write-Host "  등록된 Skill:      $($Status.skills)개"
    Write-Host ""
    Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Cyan
    Write-Host ""
}

function Show-Menu {
    Write-Host ""
    Write-Host "╔════════════════════════════════════════════════════╗" -ForegroundColor Green
    Write-Host "║        📋 Resume Workflow Orchestration            ║" -ForegroundColor Green
    Write-Host "╚════════════════════════════════════════════════════╝" -ForegroundColor Green
    Write-Host ""
    Write-Host "  [1] 📊 워크플로우 상태 확인"
    Write-Host "  [2] 📝 이력서 컴파일"
    Write-Host "  [3] 🔍 기술 스택 분석"
    Write-Host "  [4] 🤖 Agent 목록 보기"
    Write-Host "  [5] ⚙️  설정 확인"
    Write-Host "  [6] 📋 로그 보기"
    Write-Host "  [0] 🚪 종료"
    Write-Host ""
}

function Show-Logs {
    if (-not (Test-Path $LogFile)) {
        Write-Host "로그 파일이 없습니다."
        return
    }

    Write-Host ""
    Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Yellow
    Write-Host "  📋 최근 로그 (마지막 20줄)" -ForegroundColor Yellow
    Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Yellow
    Write-Host ""

    Get-Content $LogFile -Tail 20 | ForEach-Object { Write-Host $_ }

    Write-Host ""
}

function Show-Settings {
    Write-Host ""
    Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Magenta
    Write-Host "  ⚙️  시스템 설정" -ForegroundColor Magenta
    Write-Host "═══════════════════════════════════════════════════" -ForegroundColor Magenta
    Write-Host ""
    Write-Host "  프로젝트 경로:     $ProjectRoot"
    Write-Host "  Skills 디렉토리:   $SkillsDir"
    Write-Host "  Agents 디렉토리:   $AgentsDir"
    Write-Host "  Scripts 디렉토리:  $ScriptsDir"
    Write-Host "  로그 디렉토리:     $LogDir"
    Write-Host ""

    # Check dependencies
    Write-Host "  의존성 확인:" -ForegroundColor Cyan

    $xelatex = (Get-Command xelatex -ErrorAction SilentlyContinue) -ne $null
    $gh = (Get-Command gh -ErrorAction SilentlyContinue) -ne $null
    $python = (Get-Command python -ErrorAction SilentlyContinue) -ne $null

    Write-Host "    XeLaTeX:         $(if ($xelatex) { '✓ 설치됨' } else { '✗ 미설치' })"
    Write-Host "    GitHub CLI:      $(if ($gh) { '✓ 설치됨' } else { '✗ 미설치' })"
    Write-Host "    Python:          $(if ($python) { '✓ 설치됨' } else { '✗ 미설치' })"
    Write-Host ""
}

# ============================================================================
# MAIN LOOP
# ============================================================================

function Start-Interactive {
    Write-Log "Orchestration Harness 시작" "INFO"

    while ($true) {
        Show-Menu
        $Selection = Read-Host "선택"

        switch ($Selection) {
            "1" {
                Get-WorkflowStatus
            }
            "2" {
                Write-Host ""
                Invoke-Skill "resume-compile"
                Write-Host ""
            }
            "3" {
                Write-Host ""
                Invoke-Skill "tech-analyze"
                Write-Host ""
            }
            "4" {
                Write-Host ""
                Write-Host "등록된 Agents:" -ForegroundColor Cyan
                Get-ChildItem $AgentsDir -Filter "*.md" -ErrorAction SilentlyContinue | ForEach-Object {
                    Write-Host "  - $($_.BaseName)"
                }
                Write-Host ""
            }
            "5" {
                Show-Settings
            }
            "6" {
                Show-Logs
            }
            "0" {
                Write-Log "Orchestration Harness 종료" "INFO"
                Write-Host "👋 종료합니다." -ForegroundColor Green
                exit 0
            }
            default {
                Write-Host "❌ 잘못된 선택입니다." -ForegroundColor Red
            }
        }
    }
}

# ============================================================================
# COMMAND LINE INTERFACE
# ============================================================================

if ($Command -eq "") {
    Start-Interactive
} else {
    Write-Log "Command 실행: $Command $Option" "INFO"

    switch ($Command) {
        "status" {
            Get-WorkflowStatus
        }
        "compile" {
            Invoke-Skill "resume-compile"
        }
        "analyze" {
            Invoke-Skill "tech-analyze"
        }
        default {
            Write-Host "사용법: .\orchestrate.ps1 [command]"
            Write-Host ""
            Write-Host "Commands:"
            Write-Host "  status              - 워크플로우 상태 확인"
            Write-Host "  compile             - 이력서 컴파일"
            Write-Host "  analyze             - 기술 스택 분석"
            Write-Host ""
        }
    }
}
