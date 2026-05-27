# 4th_data_playground

**Perfume Data Crawling & Analysis**

## Overview
조동휘가 주도한 향수 데이터 크롤링 사전조사 프로젝트. 온라인 향수 정보 수집, 데이터 정제, 분석을 위한 데이터 파이프라인 구축합니다.

**Repository**: [Joraemon-s-Secret-Gadgets/4th_data_playground](https://github.com/Joraemon-s-Secret-Gadgets/4th_data_playground)

## Key Features
- 🕷️ **Web Scraping**: 향수 정보 자동 수집
- 📊 **Data Extraction**: 정보 추출 및 정제
- 🔍 **Source Analysis**: 다양한 소스 데이터 통합
- 💾 **Data Storage**: 구조화된 데이터 저장
- 📈 **Quality Assurance**: 데이터 품질 검증
- 🔄 **Pipeline Automation**: 자동화된 수집 프로세스

## Technology Stack
- **Primary Language**: Python
- **Frameworks**: BeautifulSoup, Scrapy, Selenium
- **Data Processing**: Pandas, NumPy
- **Database**: SQL/NoSQL
- **Focus**: Web scraping, data engineering

## Implementation Details

### Data Collection
- 향수 전문점 데이터 크롤링
- 제품 정보 추출
- 가격 정보 수집
- 고객 리뷰 데이터

### Data Processing
- 텍스트 정제 및 정규화
- 중복 제거
- 데이터 검증
- 메타데이터 추출

### Data Structure
```
Perfume Data:
- 제품명, 브랜드
- 향수 특성 (top/middle/base notes)
- 가격, 용량
- 출시 연도
- 고객 평점, 리뷰
```

## Use Cases
- **olfit 프로젝트**: 향수 추천 시스템의 데이터 소스
- **시장 분석**: 향수 시장 트렌드 파악
- **경쟁 분석**: 경쟁사 제품 모니터링
- **추천 시스템**: 학습 데이터 구축

## Challenges & Solutions
- **Dynamic Content**: JavaScript 렌더링 처리
- **Rate Limiting**: 요청 조절 및 재시도 로직
- **Data Quality**: 이상치 탐지 및 정제
- **Scalability**: 대규모 데이터 수집 최적화

## Key Achievements
- 🏆 **데이터 파이프라인 구축**: 자동화된 수집 시스템
- 📊 **대규모 데이터**: 수천 개의 향수 정보 수집
- 🔄 **지속적 업데이트**: 정기적 데이터 갱신
- 🎯 **높은 품질**: 신뢰할 수 있는 데이터

## Skills Demonstrated
- Python 웹 크롤링 기술
- 데이터 엔지니어링 능력
- 자동화 스크립트 작성
- 데이터 정제 및 전처리
- 파이프라인 설계 및 구현
- SQL/데이터베이스 관리
- 문제 해결 능력
