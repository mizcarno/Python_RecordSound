from numpy.core.records import record
import sounddevice
from scipy.io.wavfile import write
import os
from datetime import datetime

dateTimeObj = datetime.now()
fs = 44100


folder = input('please input your folder : ')
print(f'your folder is {folder}')
second = int(input('please input your time to record : '))
print(f'your time to record is {second}')
name = input('please input your name to record : ')
print(f'your name to record is {name}')
number = int(input('please input your number to record : '))
print(f'your number to record is {number}')

while True :
    print('recording')
    record_voice = sounddevice.rec(int(second * fs), samplerate = fs, channels = 2)
    sounddevice.wait()
    time = dateTimeObj.strftime('_%d-%m-%Y_%H-%M-%S')
    path = str(folder)+'\\'+str(name)+str(number)+str(time)+'.mp3'    
    write(path,fs,record_voice)
    number += 1
    print(path)
    print('Save')


