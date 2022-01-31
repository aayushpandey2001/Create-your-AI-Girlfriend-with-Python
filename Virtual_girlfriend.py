import pyttsx3
My_Gf=pyttsx3.init()
voices=My_Gf.getProperty('voices')
My_Gf.setProperty('voice',voices[1].id)
My_Gf.say("I Love you Baby")
My_Gf.say("I Miss You")
My_Gf.say("Can I Kiss You!")
My_Gf.runAndWait()