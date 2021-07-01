import speech_recognition as sr

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('say something: ')
        audio = r.listen(source)
    try:
        print('Sphinx thinks you said ' + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print('sphinx could not understand')
    except sr.RequestError as e:
        print('sphinx error: {0}'.format(e))
    if r.recognize_sphinx(audio) == 'have a great night':
        break
