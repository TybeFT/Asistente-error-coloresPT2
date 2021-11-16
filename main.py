from pywhatkit.misc import search
import speech_recognition as sr
import subprocess as sub
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard, colors
from pygame import mixer


name = "Sandra"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 145)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("[+] Escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language="es")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')

    except:
        pass
    return rec

def running():
    while True:
        rec = listen()
        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            print("[+] Reproduciendo..." + music)
            talk("Reproduciendo " + music)
            pywhatkit.playonyt(music)
        elif 'busca' in rec:
            search = rec.replace('busca', '')
            wikipedia.set_lang("es")
            wiki = wikipedia.summary(search, 1)
            print(search + ": " + wiki)
            talk(wiki)
        elif 'alarma' in rec:
            alv = rec.replace('alarma', '')
            alv = alv.strip()
            talk("Tu alarma ha sido activada a las " + alv + "horas")
            while True:
                if datetime.datetime.now().strftime('%H:%M') == alv:
                    print("¡Es Hora De Despertar!")
                    print("Presiona 'L' para posponer la alarma :)")
                    mixer.init()
                    mixer.music.load("sanLucasAlarm.mp3")
                    mixer.music.play()
                    if keyboard.read_key() == "l":
                        mixer.music.stop()
                        break
        elif 'colores' in rec:
            talk("Enseguida")
            colors.capture()


if __name__ == '__main__':
    running()

