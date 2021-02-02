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
                speak('nao rolou')

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
        print(text)
        if 'samantha' in str(text).lower():
            speak('em que posso ajudar?')
            print('sim')
            break
        if 'a manta' in str(text).lower():
            speak('em que posso ajudar?')
            print('sim')
            break
        else:
            pass


chamada()