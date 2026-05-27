# voicechat

**Streamlit Voice Chat Application**

## Overview
Streamlit과 OpenAI API를 활용한 음성 기반 채팅 애플리케이션. 사용자 음성 입력을 텍스트로 변환하고, AI가 응답하는 음성 채팅 시스템입니다.

**Repository**: [nobrain711/voicechat](https://github.com/nobrain711/voicechat)

## Key Features
- 🎙️ **Voice Input**: 사용자 음성 인식
- 🤖 **AI Response**: OpenAI GPT 기반 답변
- 🔊 **Voice Output**: AI 응답을 음성으로 변환
- 💬 **Conversation History**: 대화 히스토리 관리
- ⚡ **Real-time Processing**: 실시간 음성 처리
- 🎨 **Simple UI**: Streamlit의 간단한 인터페이스

## Technology Stack
- **Primary Language**: Python
- **Frontend**: Streamlit
- **Speech Recognition**: OpenAI Whisper API
- **LLM**: OpenAI GPT API
- **Text-to-Speech**: OpenAI TTS API
- **Audio Processing**: Audio libraries
- **Focus**: Voice interface, LLM integration, Streamlit

## Architecture Components

### 1. Audio Input Module
- 마이크 입력 캡처
- 음성 파일 업로드
- 음성 품질 관리

### 2. Speech-to-Text Pipeline
- OpenAI Whisper API 활용
- 음성→텍스트 변환
- 언어 감지 및 처리

### 3. LLM Integration
- OpenAI GPT API 호출
- 프롬프트 엔지니어링
- 토큰 관리

### 4. Text-to-Speech Pipeline
- OpenAI TTS API 활용
- 음성 스타일 선택
- 오디오 재생

### 5. Streamlit Interface
- 간단한 UI 디자인
- 실시간 상태 표시
- 대화 히스토리 표시

## Application Flow
```
1. 사용자 음성 입력
   ↓
2. Whisper API로 음성→텍스트 변환
   ↓
3. GPT API로 응답 생성
   ↓
4. TTS API로 텍스트→음성 변환
   ↓
5. 음성 재생 및 히스토리 저장
```

## Use Cases
- **Voice Assistant**: 음성 기반 AI 어시스턴트
- **Language Learning**: 발음 연습 및 피드백
- **Accessibility**: 음성 인터페이스 필요한 사용자
- **Demonstration**: 멀티모달 AI 데모
- **Research**: 음성 UI 연구

## Key Features Implemented
- ✅ Real-time voice transcription
- ✅ Context-aware responses
- ✅ Multi-turn conversations
- ✅ Voice output with different styles
- ✅ Conversation history management
- ✅ Error handling and validation

## Technical Challenges & Solutions
- 🔊 **Audio Quality**: 배경 소음 처리
- ⏱️ **Latency**: 실시간 처리 최적화
- 💰 **API Costs**: 토큰 사용 최적화
- 🔐 **Privacy**: 음성 데이터 보안

## Skills Demonstrated
- Python advanced programming
- Streamlit framework expertise
- OpenAI API integration
- Audio processing
- Real-time system design
- Voice interface development
- LLM prompt engineering
- Multimodal AI applications
