from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os


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
def speak(text):
    import os
    import playsound
    from gtts import gTTS

    tts = gTTS(text=text, lang='pt')
    filename = 'voce.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove('voce.mp3')
def comandos(text):
    import os
    import pyautogui as pag

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


    #dia e hora
    if 'horas são' in text:
        speak(showHours())

    elif 'dia é hoje' in text:
        speak(showDay())


    #clima
    elif 'graus' in text:
        speak('estou pesquisando, um momento')
        speak(f'{temp()[0]} graus')

    elif 'temperatura' in text:
        speak('estou pesquisando, um momento')
        speak(f'{temp()[0]} graus')

    elif 'chover' in text:
        if 'chance' in text:
            speak('deixa eu dar uma olhada para o céu, um minuto')
            speak(f'a chance de chover é de {temp()[1]}')

        if 'probabilidade'in text:
            speak('vou verificar, um minuto')
            speak(f'a chance de chover é de {temp()[1]}')

        if 'vai' in text:
            speak('deixa eu ver, um minuto')
            speak(f'a chance de chover é de {temp()[1]}')

        if 'Vai' in text:
            speak('deixa eu ver, um minuto')
            speak(f'a chance de chover é de {temp()[1]}')

    elif 'umidade' in text:
        speak('deixa eu dar uma olhada, só um pouco')
        speak(f'a umidade lá fora é de {temp()[2]}')


    #abrir apliativos
    elif 'netflix' in text:
        speak('pode deixar')
        os.startfile('https://www.netflix.com/browse')
    elif 'prime vídeo' in text:
        speak('pode deixar')
        os.startfile('https://www.primevideo.com/region/na/ref=av_auth_return_redir')

    elif 'telecine' in text:
        speak('pode deixar')
        os.startfile('https://www.telecineplay.com.br/')

    elif 'youtube' in text:
        speak('pode deixar')
        os.startfile('https://www.youtube.com/')



    elif "google" in text:
        speak('pode deixar')
        os.startfile('https://www.google.com/')
    elif "documentos" in text:
        speak('pode deixar')
        pag.hotkey('ctrl', 'alt', 'p')
    elif "documento" in text:
        speak('pode deixar')
        pag.hotkey('ctrl', 'alt', 'p')


    #encerrar
    elif 'encerrar' in text:
        speak('tem certeza que quer encerrar?')
        encerrar = recognition()

        if 'sim' in encerrar:
            print(encerrar)
            speak('ok, até logo')
            return True

        elif 'tenho' in encerrar:
            print(encerrar)
            speak('ok, até logo')
            return True

        else:
            print(encerrar)
            speak('desculpe, achei que queria encerrar')


    #falar com samantha
    elif 'conversar' in text:
        speak('claro')
        while True:
            pergunta = recognition()
            if 'encerrar' in pergunta:
                speak('tem certeza que quer para de conversar?')
                encerrar2 = recognition()

                if 'sim' in encerrar2:
                    print(encerrar2)
                    speak('ok, até logo')
                    return True

                elif 'tenho' in encerrar2:
                    print(encerrar2)
                    speak('ok, até logo')
                    return True

                else:
                    print(encerrar2)
                    speak('desculpe, achei que queria encerrar')

            response = bot.get_response(pergunta)
            speak(str(response))
            print(f'Samantha:{response}')
def chamada():
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
                print('nao entendi')
        return text
    def speak(text):
        import os
        import playsound
        from gtts import gTTS

        tts = gTTS(text=text, lang='pt')
        filename = 'voce.mp3'
        tts.save(filename)
        playsound.playsound(filename)
        os.remove('voce.mp3')

    while True:
        text = recognition()
        print(f'o que eu ouvi do ambiente: {text}')
        if 'samantha' in str(text).lower():
            speak('em que posso ajudar?')
            print('abrindo os ouvidos')
            break
        if 'a manta' in str(text).lower():
            speak('em que posso ajudar?')
            print('abrindo os ouvidos')
            break
        if 'samantha' in str(text).lower():
            speak('em que posso ajudar?')
            print('abrindo os ouvidos')
            break
        if 'amanda' in str(text).lower():
            speak('em que posso ajudar?')
            print('abrindo os ouvidos')
            break

        else:
            pass





bot = ChatBot('Samantha' , database_uri='sqlite:///db.sqlite3')


###################################################################################################

#treinando o robo
triner = ListTrainer(bot)

lista = []
for file in os.listdir('chats'):
    text = open(f'chats\{file}',encoding='utf-8', mode= 'r').readlines()
    for i in text:
        lista.append(i.rstrip('\n'))
    triner.train(lista)



while True:
    chamada()


    ja_falou = False

    request = recognition()
    print(f'Você:{request}')
    encerrar = comandos(str(request).lower())

