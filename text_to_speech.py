# TTS (Text to Speech)
# STT (Speech To Text)

# -- 가상환경 --
# python -m venv myenv
# .\myenv\Scripts\activate

# pip install gTTS (구글에서 제공하는 TTS)
# pip install playsound==1.2.2 (최신버전은 문제가 있어 버전 지정)

from gtts import gTTS
from playsound import playsound

# 영어 문장
# text = 'Can I help you?'
# text = 'Imagine that you have just arrived at a hotel after a tiring 7-hour overnight flight.'
file_name = 'sample2.mp3'
# tts_en = gTTS(text=text, lang='en')
# tts_en.save(file_name)


# 한글 문장
# text = '법률사무소 거제 정은희 변호사 짱'
# tts_ko = gTTS(text=text, lang='ko')
# tts_ko.save(file_name)
# playsound(file_name) #.mp3 파일 재생

# 긴 문장 (파일에서 불러와서 처리)
with open('sample.txt', 'r', encoding='utf8') as f:
    text = f.read()

tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(file_name)
playsound(file_name) #.mp3 파일 재생

