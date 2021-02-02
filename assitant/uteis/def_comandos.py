def comandos(text):
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


    if 'horas são' in text:
        speak(showHours())

    if 'dia é hoje' in text:
        speak(showDay())


    #clima
    if 'graus' in text:
        speak('estou pesquisando, um momento')
        speak(f'{temp()[0]} graus')
    if 'temperatura' in text:
        speak('estou pesquisando, um momento')
        speak(f'{temp()[0]} graus')
    if 'chover' in text:
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
    if 'umidade' in text:
        speak('deixa eu dar uma olhada, só um pouco')
        speak(f'a umidade lá fora é de {temp()[2]}')


    #encerrar
    if 'encerrar' in text:
        speak('tem certeza que quer encerrar?')
        encerrar = recognition()

        if 'sim' in encerrar:
            print(encerrar)
            speak('ok, até logo')
        if 'tenho' in encerrar:
            print(encerrar)
            speak('ok, até logo')

        else:
            print(encerrar)
            speak('desculpe, achei que queria encerrar')

    else:
        pass

