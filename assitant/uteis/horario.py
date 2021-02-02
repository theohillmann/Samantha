
def recognition():
    import speech_recognition as sr

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio, language='pt-Br')

    return text

def showHours():
    from _datetime import datetime
    horas = datetime.now()
    return f'{horas.hour}:{horas.minute}:{horas.second}'

def showDay():
    from _datetime import datetime
    horas = datetime.now()
    return f'dia {horas.day} do {horas.month}'


texto = recognition()
print(texto)

if 'horas são' in texto:
    print(showHours())

if 'dia é hoje' in texto:
    print(showDay())
