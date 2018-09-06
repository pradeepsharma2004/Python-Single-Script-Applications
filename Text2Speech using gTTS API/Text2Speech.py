from gtts import gTTS
import os
from tkinter import *

root=Tk()
root.geometry('400x200')
root.title('Text to Speech')
lab1=Label(root,text='Text to speech conversion',bg='powder blue',fg='black',font=('arial 16 bold'))

lab2=Label(root,text='Enter Text',font=('arial 16'),fg='black').pack()
mytext=StringVar()


def fetch():
    language='en'
    myob=gTTS(text=mytext.get(),lang=language,slow=False)
    myob.save('Voice.mp3')

def play():
    from pygame import mixer
    mixer.init()
    mixer.music.load('Voice.mp3')
    mixer.music.play()


ent1=Entry(root,tex=mytext,font=('arial 15')).pack()
but1=Button(root,text='Convert',width=20,bg='brown',fg='white',command=fetch).place(x=125,y=100)
but2=Button(root,text='Play File',width=20,bg='brown',fg='white',command=play).place(x=125,y=160)
root.mainloop()
