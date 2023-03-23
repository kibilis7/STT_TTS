import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# 음성 인식 (듣기, STT)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        print('[나] '+text)
        answer(text)
    except sr.UnknownValueError: # 휘파람 등 인식못하는 경우
        print('인식 실패') # 음성 인식 실패한 경우
    except sr.RequestError as e: # NW 문제 등 요청 자체가 실패한 경우
        print('요청 실패 : {0}'.format(e)) # API key 오류, 네트워크 단절 등


# 대답
def answer(input_text):
    answer_text = ''
    if '안녕' in input_text:
        answer_text = '안녕하세요? 반갑습니다.'
    elif '날씨' in input_text:
        answer_text = '오늘의 서울 기온은 20도입니다. 맑은 하늘이 예상됩니다.'
    elif '환율' in input_text:
        answer_text = '원 달러 환율은 1380원입니다.'
    elif '고마워' in input_text:
        answer_text = '별 말씀을요.'
    elif '종료' in input_text:
        answer_text = '다음에 또 만나요'
        stop_listening(wait_for_stop=False) # 더 이상 듣지 않음
    else:
        answer_text = '잘 알아듣지 못했어요.'
    speak(answer_text)

# 소리내어 읽기(TTS)
def speak(text):
    print('[인공지능] '+text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name): # voice.mp3 파일 삭제
        os.remove(file_name)

speak('무엇을 도와드릴까요?')
r = sr.Recognizer()
m = sr.Microphone() # 마이크 소리

stop_listening = r.listen_in_background(m,listen) # 사람처럼 귀를 계속 열어두는 것
# > 계속 듣고 있다가 음성 들어오면 listen 함수 실행

# stop_listening(wait_for_stop=False) # 더 이상 듣지 않음

while True: #프로그램이 끝나지 않도록 무한 반복
    time.sleep(0.1)

