#!/usr/bin/env python3
"""
GitHub Tech Stack Analyzer

GitHub CLI를 사용하여 개인 저장소의 기술 스택을 분석하고
TECH_STACK.md를 자동으로 생성합니다.

사용법:
    python gh_tech_analyzer.py --update              # TECH_STACK.md 업데이트
    python gh_tech_analyzer.py --format markdown     # Markdown 형식 출력
    python gh_tech_analyzer.py --format json         # JSON 형식 출력
    python gh_tech_analyzer.py --verbose             # 상세 출력
"""

import json
import subprocess
import sys
from datetime import datetime, timedelta
from collections import Counter, defaultdict
from pathlib import Path
import argparse


class TechAnalyzer:
    """GitHub 저장소에서 기술 스택 분석"""

    # 기술 분류
    TECH_CATEGORIES = {
        'languages': {
            'Python': ['python', 'py'],
            'JavaScript': ['javascript', 'js', 'javascript/typescript'],
            'TypeScript': ['typescript', 'ts'],
            'Go': ['go'],
            'Rust': ['rust'],
            'Java': ['java'],
            'C++': ['c++', 'cpp'],
            'C#': ['c#', 'csharp'],
            'SQL': ['sql'],
            'Bash': ['bash', 'shell'],
        },
        'frameworks': {
            'FastAPI': ['fastapi'],
            'Django': ['django'],
            'Flask': ['flask'],
            'React': ['react'],
            'Vue': ['vue'],
            'Angular': ['angular'],
            'Express.js': ['express', 'node'],
            'NestJS': ['nestjs'],
        },
        'databases': {
            'PostgreSQL': ['postgresql', 'postgres', 'psql'],
            'MySQL': ['mysql'],
            'MongoDB': ['mongodb', 'mongo'],
            'Redis': ['redis'],
            'SQLite': ['sqlite'],
            'MariaDB': ['mariadb'],
        },
        'cloud': {
            'AWS': ['aws', 'amazon'],
            'GCP': ['gcp', 'google cloud'],
            'Azure': ['azure', 'microsoft'],
            'Docker': ['docker'],
            'Kubernetes': ['kubernetes', 'k8s'],
            'GitHub Actions': ['github actions', 'actions'],
        },
        'tools': {
            'Git': ['git'],
            'VS Code': ['vscode', 'vs code'],
            'Docker': ['docker'],
            'Postman': ['postman'],
            'Jupyter': ['jupyter'],
        },
        'libraries': {
            'SQLAlchemy': ['sqlalchemy'],
            'Pydantic': ['pydantic'],
            'NumPy': ['numpy'],
            'Pandas': ['pandas'],
            'Matplotlib': ['matplotlib'],
            'Scikit-learn': ['scikit-learn', 'sklearn'],
            'TensorFlow': ['tensorflow'],
            'PyTorch': ['pytorch'],
        },
    }

    def __init__(self, username='nobrain711', verbose=False):
        """
        Args:
            username: GitHub 사용자명
            verbose: 상세 출력 여부
        """
        self.username = username
        self.verbose = verbose
        self.repos = []
        self.tech_stack = defaultdict(lambda: {'repos': [], 'count': 0, 'proficiency': 'Beginner'})

    def fetch_repos(self, limit=100):
        """GitHub에서 저장소 목록 조회"""
        try:
            cmd = [
                'gh', 'repo', 'list', self.username,
                '--limit', str(limit),
                '--json', 'name,primaryLanguage,updatedAt,description'
            ]

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

            if result.returncode != 0:
                print(f"❌ GitHub CLI 오류: {result.stderr}")
                return False

            self.repos = json.loads(result.stdout)
            print(f"✓ {len(self.repos)}개 저장소 조회 완료")
            return True

        except subprocess.TimeoutExpired:
            print("❌ GitHub CLI 타임아웃")
            return False
        except json.JSONDecodeError:
            print("❌ JSON 파싱 오류")
            return False
        except Exception as e:
            print(f"❌ 오류: {e}")
            return False

    def analyze_repos(self):
        """저장소들에서 기술 추출"""
        if not self.repos:
            print("❌ 분석할 저장소가 없습니다.")
            return False

        for repo in self.repos:
            name = repo.get('name', '')
            language = repo.get('primaryLanguage', '')
            updated_at = repo.get('updatedAt', '')
            description = repo.get('description', '')

            # 언어별 기술 추출
            if language:
                tech_key = self._normalize_tech(language)
                if tech_key:
                    if tech_key not in self.tech_stack:
                        self.tech_stack[tech_key] = {'repos': [], 'count': 0, 'proficiency': 'Beginner'}

                    self.tech_stack[tech_key]['repos'].append(name)
                    self.tech_stack[tech_key]['count'] += 1

            # 설명에서 기술 추출
            if description:
                techs = self._extract_techs_from_text(description)
                for tech in techs:
                    if tech not in self.tech_stack:
                        self.tech_stack[tech] = {'repos': [], 'count': 0, 'proficiency': 'Beginner'}
                    self.tech_stack[tech]['repos'].append(name)

        # 숙련도 판정
        self._judge_proficiency()

        if self.verbose:
            print(f"✓ {len(self.tech_stack)}개 기술 추출 완료")

        return True

    def _normalize_tech(self, language):
        """언어명을 정규화된 기술명으로 변환"""
        language_lower = language.lower()

        for category, techs in self.TECH_CATEGORIES.items():
            for tech_name, aliases in techs.items():
                for alias in aliases:
                    if alias in language_lower:
                        return tech_name

        return language if language else None

    def _extract_techs_from_text(self, text):
        """텍스트에서 기술 키워드 추출"""
        techs = []
        text_lower = text.lower()

        for category, tech_dict in self.TECH_CATEGORIES.items():
            for tech_name, aliases in tech_dict.items():
                for alias in aliases:
                    if alias in text_lower:
                        techs.append(tech_name)
                        break

        return list(set(techs))  # 중복 제거

    def _judge_proficiency(self):
        """저장소 수 기반 숙련도 판정"""
        for tech, data in self.tech_stack.items():
            count = data['count']

            if count >= 3:
                data['proficiency'] = 'Advanced'
            elif count >= 2:
                data['proficiency'] = 'Intermediate'
            else:
                data['proficiency'] = 'Beginner'

    def generate_markdown(self):
        """TECH_STACK.md 형식으로 생성"""
        now = datetime.now()
        date_str = now.strftime("%Y년 %m월 %d일")

        # 숙련도별 분류
        advanced = {k: v for k, v in self.tech_stack.items() if v['proficiency'] == 'Advanced'}
        intermediate = {k: v for k, v in self.tech_stack.items() if v['proficiency'] == 'Intermediate'}
        beginner = {k: v for k, v in self.tech_stack.items() if v['proficiency'] == 'Beginner'}

        md = f"""# 기술 스택 (Tech Stack)

마지막 업데이트: {date_str}

## Tier 1 — 주요 기술 (Advanced)

"""

        # Advanced 기술들
        for tech in sorted(advanced.keys()):
            data = advanced[tech]
            count = data['count']
            md += f"- **{tech}** — Advanced ({count} repos)\n"

        md += f"""
## Tier 2 — 도구 & 플랫폼 (Intermediate)

"""

        # Intermediate 기술들
        for tech in sorted(intermediate.keys()):
            data = intermediate[tech]
            count = data['count']
            md += f"- **{tech}** — Intermediate ({count} repos)\n"

        md += f"""
## Tier 3 — 라이브러리 & 유틸 (Beginner)

"""

        # Beginner 기술들
        for tech in sorted(beginner.keys()):
            data = beginner[tech]
            count = data['count']
            md += f"- **{tech}** — {count} repo{'s' if count > 1 else ''}\n"

        return md

    def save_to_file(self, output_file):
        """TECH_STACK.md 파일로 저장"""
        try:
            md_content = self.generate_markdown()

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(md_content)

            file_size = Path(output_file).stat().st_size
            print(f"✓ {output_file} 저장 완료 ({file_size/1024:.1f}KB)")
            return True

        except Exception as e:
            print(f"❌ 파일 저장 오류: {e}")
            return False

    def output_json(self):
        """JSON 형식으로 출력"""
        output = {
            'timestamp': datetime.now().isoformat(),
            'username': self.username,
            'total_repos': len(self.repos),
            'total_techs': len(self.tech_stack),
            'tech_stack': dict(self.tech_stack)
        }
        return json.dumps(output, indent=2, ensure_ascii=False)


def main():
    """메인 함수"""
    parser = argparse.ArgumentParser(
        description='GitHub 기술 스택 분석 도구',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예시:
  python gh_tech_analyzer.py --update              # TECH_STACK.md 생성
  python gh_tech_analyzer.py --format json         # JSON 출력
  python gh_tech_analyzer.py --verbose             # 상세 출력
        """
    )

    parser.add_argument('--update', action='store_true', help='TECH_STACK.md 업데이트')
    parser.add_argument('--format', choices=['markdown', 'json'], default='markdown', help='출력 형식')
    parser.add_argument('--verbose', action='store_true', help='상세 출력')
    parser.add_argument('--user', default='nobrain711', help='GitHub 사용자명')
    parser.add_argument('--limit', type=int, default=100, help='조회 저장소 개수')
    parser.add_argument('--output', default='TECH_STACK.md', help='출력 파일')

    args = parser.parse_args()

    # 분석기 생성
    analyzer = TechAnalyzer(username=args.user, verbose=args.verbose)

    # 저장소 조회
    if not analyzer.fetch_repos(limit=args.limit):
        sys.exit(1)

    # 분석
    if not analyzer.analyze_repos():
        sys.exit(1)

    # 출력
    if args.format == 'json':
        print(analyzer.output_json())
    else:
        # Markdown 형식
        if args.update:
            # 파일로 저장
            if not analyzer.save_to_file(args.output):
                sys.exit(1)
        else:
            # 표준 출력
            print(analyzer.generate_markdown())


if __name__ == '__main__':
    main()
