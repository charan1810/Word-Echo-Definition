from tkinter import *
import pyttsx3
from nltk.corpus import wordnet
import nltk

# nltk.download('wordnet')

def speak(audio):
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def meaning():
    query=str(text.get())
    synsets=wordnet.synsets(query)
    res=''
    
    if synsets:
        for syn in synsets:
            res+=f'{syn.definition()}\n'
        spokentext.set(res)
        speak('The meaning is :'+res)
    else:
        res=f'Meaning of {query} is not found'
        spokentext.set(res)
        speak(res)


wpage=Tk()
wpage.title("Charan's-Dictionary")
wpage.geometry('500x500')
wpage.config(bg='Black')


text=StringVar(wpage)
spokentext=StringVar(wpage)

Label(wpage, text="Word-Echo Definition Voice Assistant", bg='white',fg='black', font=('Ariel', 15, 'bold')).pack(pady=10)
Label(wpage,text='Please enter the word',bg='white',font=('monsterrat',15),anchor='e',justify='left').pack(pady=10)

Entry(wpage, textvariable=text, width=35, font=('calibre', 13, 'normal')).pack(pady=10)

querylabel=Label(wpage,textvariable=spokentext,bg='white',anchor='e',font=('calibre', 13, 'normal'), justify=LEFT, wraplength=500).pack(pady=10)
spokentext.set("Which word do you want to find the meaning of")
speak("Which word do you want to find the meaning of")

# Button to get the meaning
Button(wpage, text="Speak Meaning", bg='SlateGray4', font=('calibre', 13),
      command=meaning ).pack(pady=10)

wpage.mainloop()
