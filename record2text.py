#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyaudio
import wave

import requests
def record2text():
    CHUNK = 1024 * 4 # 4倍
    FORMAT = pyaudio.paInt16
    CHANNELS = 1 # モノラル入力
    RATE = 16000
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    
    print("* recording")
    
    frames = []
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK,exception_on_overflow = False)
        frames.append(data)
    
    print("* done recording")
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    path = '/your path to/output.wav'
    APIKEY = 'your API key'
    url = "https://api.apigw.smt.docomo.ne.jp/amiVoice/v1/recognize?APIKEY={}".format(APIKEY)
    files = {"a": open(path, 'rb'), "v":"on"}
    
    r = requests.post(url, files=files)
    json_data = r.json()
    #print(json_data)
    print(json_data['text'])
    return json_data['text']
