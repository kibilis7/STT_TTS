# pip install SpeechRecognition
# pip install PyAudio (마이크 인식)

import speech_recognition as sr

# (선택1) 마이크로부터 음성 듣기
r = sr.Recognizer()
with sr.Microphone() as source:
    print('듣고 있어요')
    audio = r.listen(source) # 마이크로부터 음성 듣기

# (선택2) 파일로부터 음성 불러오기 (wav, aiff/aiff-c, flac 가능, mp3는 불가)
# r = sr.Recognizer()
# with sr.AudioFile('sample.mp3') as source:
#     audio = r.record(source) 

# 네트워크 연결이 되어있어야 작동함
# 구글서버에서 처리해서 내려준다

try:
    # 구글 API 로 인식 (하루 50회 제한)

    #영어 문장
    text = r.recognize_google(audio, language='en-US')
    print(text)

    #한글 문장
    text = r.recognize_google(audio, language='ko')
    print(text)

except sr.UnknownValueError: # 휘파람 등 인식못하는 경우
    print('인식 실패') # 음성 인식 실패한 경우
except sr.RequestError as e: # NW 문제 등 요청 자체가 실패한 경우
    print('요청 실패 : {0}'.format(e)) # API key 오류, 네트워크 단절 등


