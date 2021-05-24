import pyttsx3
from gtts import gTTS
from tqdm import tqdm
from time import sleep

engine = pyttsx3.init()

file_path = 'text.txt'
# file_path = input('Enter File Path: ')

file = open(file_path, 'r')
theText = file.read()

engine.say(theText)
engine.runAndWait()

file.close()

for i in tqdm(range(100)):
    sleep(0.01)

tts = gTTS(text=theText, lang='en')
tts.save('filename.mp3')

print('File saved')
