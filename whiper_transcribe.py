import whisper
from dotenv import load_dotenv
import os

load_dotenv()


model  = whisper.load_model('large')

result = model.transcribe('./output/voice.wav')

with open('./output/whisper.txt', 'w') as whisper_content:
    print(result)
    whisper_content.write(result['text'])
    whisper_content.close()
    
    