import speech_recognition as sr
#data_dict =[]
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('say something: ')
        audio = r.listen(source)
    try:
        #print('Sphinx thinks you said ' + r.recognize_sphinx(audio))
        
        #data_dict.append(r.recognize_google(audio, show_all = True))
        #print(data_dict)
        print('google thinks you said ' + r.recognize_google(audio, show_all = True))
    except sr.UnknownValueError:
        print('google could not understand')
    except sr.RequestError as e:
        print('google error: {0}'.format(e))
    if r.recognize_google(audio) == 'have a great night':
        break
