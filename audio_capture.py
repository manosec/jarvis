import pyaudio
import wave
import os
from dotenv import load_dotenv

load_dotenv()

output_directory = os.environ('ARTIFACT_DIRECTORY')

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "./output/voice.wav"

audio_capture = pyaudio.PyAudio()

stream = audio_capture.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            input=True,
                            input_device_index=0,
                            frames_per_buffer=CHUNK)

frames = []


for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

stream.close()

#Audio audio data to local
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio_capture.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

