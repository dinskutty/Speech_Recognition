import speech_recognition as sr
import time

r = sr.Recognizer()
mic = sr.Microphone()
harvard = sr.AudioFile('./Welcome.wav') #audio file input
with harvard as source:
    time.sleep(1)
    print('Say Something!!')
    audio = r.listen(source)
    try:
        voice = r.recognize_google(audio)
        print(voice)
        f = open('./output.txt','w')

        f.write('This is your Words:\n {}'.format(voice))
        f.close()
    except sr.UnknownValueError:
        print("Sorry! I dont get it! Please repeat")
    except sr.RequestError:
        print('Sorry my speech service is down!')

