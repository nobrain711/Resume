# kaggle-utils-dataset

**Lightweight ML Utilities for Kaggle Datasets**

## Overview
머신러닝 및 딥러닝 워크플로우에서 Kaggle 데이터셋을 효율적으로 관리하기 위한 경량 유틸리티 라이브러리. 데이터 다운로드, 전처리, 관리를 단순화합니다.

**Repository**: [nobrain711/kaggle-utils-dataset](https://github.com/nobrain711/kaggle-utils-dataset)

## Key Features
- 📥 **Easy Download**: Kaggle 데이터셋 자동 다운로드
- 📦 **Dataset Management**: 데이터셋 버전 관리
- 🧹 **Data Preprocessing**: 기본 전처리 유틸리티
- 🔄 **Pipeline Integration**: ML 파이프라인 통합
- ⚡ **Lightweight**: 의존성 최소화
- 🎯 **ML-Focused**: 데이터 과학 중심 설계

## Technology Stack
- **Primary Language**: Python
- **Core Libraries**: Pandas, NumPy
- **Kaggle API**: Official Kaggle API
- **Focus**: Data management, ML utilities, automation

## Core Utilities

### 1. Dataset Downloader
```python
# Kaggle 데이터셋 자동 다운로드
from kaggle_utils import download_dataset
download_dataset('dataset-name', 'output-dir')
```

### 2. Data Loader
- CSV, JSON 자동 로딩
- 데이터 타입 추론
- 에러 처리

### 3. Preprocessing Tools
- Missing value 처리
- 범주형 데이터 인코딩
- 수치형 데이터 정규화
- 아웃라이어 탐지

### 4. Dataset Information
- 데이터셋 메타데이터 출력
- 통계 정보 조회
- 데이터 품질 보고서

### 5. Version Management
- 데이터셋 버전 추적
- 재현 가능한 작업 환경
- 백업 및 복구

## Usage Examples

### Basic Dataset Download
```python
from kaggle_utils import KaggleDataset

dataset = KaggleDataset('titanic')
data = dataset.load()
info = dataset.get_info()
```

### Data Preprocessing
```python
from kaggle_utils import preprocess

# 자동 전처리
cleaned_data = preprocess.auto_clean(data)

# 커스텀 전처리
cleaned_data = preprocess.handle_missing(data)
cleaned_data = preprocess.encode_categorical(cleaned_data)
```

## Benefits for Data Scientists
- ⏱️ **Time Saving**: 반복적인 작업 자동화
- 🔄 **Reproducibility**: 일관된 데이터 처리
- 📊 **Quality**: 데이터 품질 향상
- 🚀 **Productivity**: 빠른 프로토타이핑
- 📚 **Best Practices**: ML 표준 작업 흐름

## Use Cases
- **Kaggle Competitions**: 경진대회 데이터 관리
- **Quick ML Projects**: 빠른 머신러닝 프로젝트 시작
- **Data Exploration**: 탐색적 데이터 분석
- **Model Training**: 학습 파이프라인 준비
- **Team Projects**: 팀 협업 시 일관된 환경

## Design Philosophy
- 🎯 **Simple API**: 사용하기 쉬운 인터페이스
- 📦 **Lightweight**: 최소 의존성
- 🔧 **Extensible**: 커스터마이즈 가능
- 📚 **Well-documented**: 상세한 문서
- ⚡ **Efficient**: 성능 최적화

## Library Features
- ✅ One-line dataset download
- ✅ Automatic format detection
- ✅ Common preprocessing tasks
- ✅ Data quality metrics
- ✅ Version control
- ✅ Error handling
- ✅ Logging support

## Skills Demonstrated
- Python library development
- Data science best practices
- API design and user experience
- Documentation and examples
- Version control and maintenance
- Testing and quality assurance
- Kaggle API integration
- Utility function design
