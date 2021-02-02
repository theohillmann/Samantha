import cv2
import face_recognition
import os
import pyautogui as pag
from time import sleep



def speak(text):
    import os
    import playsound
    from gtts import gTTS

    tts = gTTS(text=text, lang='pt')
    filename = 'voce.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove('voce.mp3')

def recognition():
    def speak(text):
        import os
        import playsound
        from gtts import gTTS
        tts = gTTS(text=text, lang='pt')
        filename = 'voce.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove('voce.mp3')
    import speech_recognition as sr
    recognizer = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio, language='pt-Br')

            break
        except:
            speak('desculpe não entendi. poderia repetir por favor?')

    return text

def showHours():
    from _datetime import datetime
    horas = datetime.now()
    return f'{horas.hour} horas {horas.minute} minutos e {horas.second} segundos'

def showDay():
    from _datetime import datetime
    horas = datetime.now()
    return f'dia {horas.day} do {horas.month}'

def temp():
    '''''
        retorna a temperatura, a probabilidade de chuva e a umidade
    '''''
    from selenium.webdriver import Firefox
    from selenium.webdriver.firefox.options import Options

    try:
        option = Options()
        option.headless = True
        browser = Firefox(options=option)
        browser.get('https://www.google.com/search?client=firefox-b-d&q=cilma+em+curitiba')
        temp = browser.find_element_by_id('wob_tm').text
        prob_chuv = browser.find_element_by_id('wob_pp').text
        umi = browser.find_element_by_id('wob_hm').text

        browser.close()
        return temp, prob_chuv, umi
    except:
        print('talvez sua internet não esteja ligada')



while True:
    texto = str(recognition()).lower()
    print(texto)

    if 'horas são' in texto:
        speak(showHours())

    if 'dia é hoje' in texto:
        speak(showDay())


    #clima
    if 'graus' in texto:
        speak('estou pesquisando, um momento')
        speak(f'{temp()[0]} graus')
    if 'temperatura' in texto:
        speak('estou pesquisando, um momento')
        speak(f'{temp()[0]} graus')
    if 'chover' in texto:
        if 'chance' in texto:
            speak('deixa eu dar uma olhada para o céu, um minuto')
            speak(f'a chance de chover é de {temp()[1]}')
        if 'probabilidade'in texto:
            speak('vou verificar, um minuto')
            speak(f'a chance de chover é de {temp()[1]}')
        if 'vai' in texto:
            speak('deixa eu ver, um minuto')
            speak(f'a chance de chover é de {temp()[1]}')
        if 'Vai' in texto:
            speak('deixa eu ver, um minuto')
            speak(f'a chance de chover é de {temp()[1]}')
    if 'umidade' in texto:
        speak('deixa eu dar uma olhada, só um pouco')
        speak(f'a umidade lá fora é de {temp()[2]}')



    #abrir apliativos
    if 'netflix' in texto:
        speak('pode deixar')
        os.startfile('https://www.netflix.com/browse')
        continue
    if 'prime vídeo' in texto:
        speak('pode deixar')
        os.startfile('https://www.primevideo.com/region/na/ref=av_auth_return_redir')
        continue
    if 'telecine' in texto:
        speak('pode deixar')
        os.startfile('https://www.telecineplay.com.br/')
        continue
    if 'youtube' in texto:
        speak('pode deixar')
        os.startfile('https://www.youtube.com/')
        continue


    if "google" in texto:
        speak('pode deixar')
        os.startfile('https://www.google.com/')
    if "documentos" in texto:
        speak('pode deixar')
        pag.hotkey('ctrl', 'alt', 'p')
    if "documento" in texto:
        speak('pode deixar')
        pag.hotkey('ctrl', 'alt', 'p')

    #encerrar
    if 'encerrar' in texto:
        speak('tem certeza que quer encerrar?')
        encerrar = recognition()

        if 'sim' in encerrar:
            print(encerrar)
            speak('ok, até logo')
            break
        if 'tenho' in encerrar:
            print(encerrar)
            speak('ok, até logo')
            break

        else:
            print(encerrar)
            speak('desculpe, achei que queria encerrar')
