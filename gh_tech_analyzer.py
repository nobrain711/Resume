#!/usr/bin/env python3
"""
GitHub Tech Stack Analyzer
GitHub의 진행 중인 프로젝트들을 분석하여 TECH_STACK.md를 자동으로 생성/업데이트
"""

import json
import subprocess
from datetime import datetime, timedelta
from collections import defaultdict
from pathlib import Path
import re

class GitHubTechAnalyzer:
    """GitHub 저장소 분석 및 기술 스택 추출"""

    # 기술 키워드 맵핑
    TECH_KEYWORDS = {
        # 프로그래밍 언어
        'Python': ['python', 'py', 'pydantic', 'fastapi', 'django', 'flask'],
        'JavaScript': ['javascript', 'js', 'node', 'npm', 'webpack'],
        'TypeScript': ['typescript', 'ts', 'tsconfig'],
        'Go': ['go', 'golang', 'main.go'],
        'Rust': ['rust', 'cargo', 'toml'],
        'SQL': ['sql', 'postgres', 'mysql', 'oracle', 'plsql'],
        'Bash': ['bash', 'shell', 'sh'],
        'HCL': ['hcl', 'terraform', 'tf'],
        'HTML': ['html', 'html5'],

        # 웹 프레임워크
        'React': ['react', 'jsx'],
        'Vue': ['vue', 'vuejs'],
        'FastAPI': ['fastapi'],
        'Django': ['django', 'djangorestframework'],
        'Express.js': ['express'],
        'Flask': ['flask'],
        'Streamlit': ['streamlit'],
        'Chainlit': ['chainlit'],

        # 데이터/ML
        'Pandas': ['pandas', 'pd'],
        'NumPy': ['numpy', 'np'],
        'Scikit-Learn': ['scikit', 'sklearn'],
        'PyTorch': ['pytorch', 'torch'],
        'TensorFlow': ['tensorflow', 'tf'],
        'XGBoost': ['xgboost'],
        'LightGBM': ['lightgbm'],
        'OpenCV': ['opencv', 'cv2'],
        'Jupyter': ['jupyter', 'ipynb'],

        # LLM/AI
        'Claude API': ['claude', 'anthropic'],
        'Ollama': ['ollama'],
        'LangChain': ['langchain'],
        'LlamaIndex': ['llama_index'],

        # 인프라
        'Docker': ['docker', 'dockerfile'],
        'Kubernetes': ['kubernetes', 'k8s'],
        'AWS': ['aws', 'ec2', 's3', 'rds'],
        'GitHub Actions': ['github actions', 'workflow', '.github/workflows'],
        'Terraform': ['terraform', 'tf'],

        # 도구
        'Git': ['git', 'gitignore'],
        'Postman': ['postman'],
        'VS Code': ['vscode'],
        'MongoDB': ['mongodb', 'mongo'],
        'PostgreSQL': ['postgresql', 'postgres'],
        'MySQL': ['mysql'],
        'Redis': ['redis'],
    }

    def __init__(self, username: str = "nobrain711"):
        self.username = username
        self.repos = []
        self.tech_stats = defaultdict(lambda: {
            'count': 0,
            'projects': [],
            'last_update': None,
            'level': 'basic'
        })

    def fetch_repos(self) -> list:
        """gh CLI로 모든 저장소 조회"""
        print(f"[*] Fetching repositories for {self.username}...")
        cmd = [
            'gh', 'repo', 'list', self.username,
            '--limit', '100',
            '--json', 'name,description,pushedAt,url'
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', check=True)
            if result.stdout.strip():
                self.repos = json.loads(result.stdout)
            else:
                print("[ERROR] Empty response from gh command")
                return []
            print(f"[OK] Found {len(self.repos)} repositories")
            return self.repos
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Error fetching repos: {e.stderr}")
            return []

    def analyze_repo(self, repo: dict) -> dict:
        """저장소 분석: README, 파일 이름 등에서 기술 추출"""
        name = repo['name']
        description = repo.get('description', '')
        pushed_at = repo.get('pushedAt', '')

        # 상태 판정
        if pushed_at:
            last_push = datetime.fromisoformat(pushed_at.replace('Z', '+00:00'))
            days_ago = (datetime.now(last_push.tzinfo) - last_push).days

            if days_ago < 90:
                status = 'active'
            elif days_ago < 180:
                status = 'recent'
            else:
                status = 'inactive'
        else:
            status = 'unknown'

        # 저장소 이름과 설명에서 기술 추출
        text = f"{name} {description}".lower()
        detected_techs = set()

        for tech, keywords in self.TECH_KEYWORDS.items():
            for keyword in keywords:
                if keyword in text:
                    detected_techs.add(tech)
                    break

        return {
            'name': name,
            'description': description,
            'status': status,
            'last_push': pushed_at,
            'techs': detected_techs
        }

    def analyze_all(self) -> dict:
        """모든 저장소 분석"""
        print("\n[*] Analyzing repositories...")

        for repo in self.repos:
            analysis = self.analyze_repo(repo)

            # 기술별 통계 업데이트
            for tech in analysis['techs']:
                self.tech_stats[tech]['count'] += 1
                self.tech_stats[tech]['projects'].append(analysis['name'])
                self.tech_stats[tech]['last_update'] = analysis['last_push']

                # 숙련도 판정
                if analysis['status'] == 'active':
                    self.tech_stats[tech]['level'] = 'advanced'
                elif analysis['status'] == 'recent':
                    if self.tech_stats[tech]['level'] != 'advanced':
                        self.tech_stats[tech]['level'] = 'intermediate'
                else:
                    if self.tech_stats[tech]['level'] == 'basic':
                        self.tech_stats[tech]['level'] = 'beginner'

        print(f"[OK] Detected {len(self.tech_stats)} technologies")
        return dict(self.tech_stats)

    def generate_markdown(self) -> str:
        """TECH_STACK.md 자동 생성"""
        markdown = f"""# 기술 스택 (Tech Stack)

*마지막 자동 업데이트: {datetime.now().strftime('%Y년 %m월 %d일')}*

## Tier 1: 핵심 기술 (Core Technologies)

### 프로그래밍 언어 (Programming Languages)
"""

        # 기술을 숙련도별로 정렬
        techs_by_level = defaultdict(list)
        for tech, stats in sorted(self.tech_stats.items(), key=lambda x: x[1]['count'], reverse=True):
            techs_by_level[stats['level']].append((tech, stats))

        # 상급 기술
        if techs_by_level['advanced']:
            markdown += "\n**상급 (자주 사용)**\n"
            for tech, stats in techs_by_level['advanced']:
                markdown += f"- **{tech}** — {len(stats['projects'])}개 프로젝트\n"

        # 중급 기술
        if techs_by_level['intermediate']:
            markdown += "\n**중급 (가끔 사용)**\n"
            for tech, stats in techs_by_level['intermediate']:
                markdown += f"- **{tech}** — {len(stats['projects'])}개 프로젝트\n"

        # 초급/기초 기술
        if techs_by_level['beginner'] or techs_by_level['basic']:
            markdown += "\n**학습 중 / 기초**\n"
            for tech, stats in techs_by_level['beginner'] + techs_by_level['basic']:
                markdown += f"- **{tech}** — {', '.join(stats['projects'][:2])}\n"

        # 활성 프로젝트
        markdown += "\n## GitHub 활성 프로젝트\n\n"
        markdown += "| 프로젝트 | 설명 | 상태 | 마지막 업데이트 |\n"
        markdown += "|---------|------|------|---------------|\n"

        for repo in sorted(self.repos, key=lambda x: x.get('pushedAt', ''), reverse=True)[:15]:
            name = repo['name']
            desc = repo.get('description', '')[:40]
            pushed = repo.get('pushedAt', 'N/A')[:10]
            status = '활성' if pushed > datetime.now().isoformat()[:10] else '진행 중'
            markdown += f"| {name} | {desc} | {status} | {pushed} |\n"

        markdown += f"\n---\n*이 섹션은 자동으로 생성됩니다. (`gh_tech_analyzer.py` 실행)*\n"

        return markdown

    def run(self) -> str:
        """전체 분석 실행"""
        print("[START] Starting GitHub Tech Analyzer...\n")

        self.fetch_repos()
        self.analyze_all()

        markdown = self.generate_markdown()

        print("\n[OK] Analysis complete!")
        print("\n[*] Generated Markdown (saving to file...)")

        return markdown


def main():
    """메인 실행"""
    analyzer = GitHubTechAnalyzer()
    markdown = analyzer.run()

    # 선택: 파일로 저장할지 stdout으로만 출력할지
    output_file = Path("TECH_STACK_AUTO.md")
    output_file.write_text(markdown, encoding='utf-8')
    print(f"\n[OK] Saved to {output_file}")


if __name__ == "__main__":
    main()
