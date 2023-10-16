#Convert text to speech
#import packages
from gtts import gTTS, lang
import os
from tkinter import *
from tkinter import messagebox
import speech_recognition as sr

#define functions
#text to speech conversion
def text_to_speech():
        
        text = text_entry.get("1.0","end-1c")
        language = accent_entry.get()
        
        if (len(text)<=1) | (len(language)<=0):
                messagebox.showerror(message="Enter required details")
                return      
        
        speech = gTTS(text = text, lang = language, slow = False)
        
        speech.save("text.mp3")
        
        os.system("mpg123 "+"text.mp3")
        total_length = len(text)
        print(f"Total length of recognized text: {total_length} characters")
        

def list_languages():
        
        messagebox.showinfo(message=list(lang.tts_langs().items()))




window = Tk()

window.geometry("500x300")
window.title("Convert text to Speech ")
title_label = Label(window, text=" text to Speech ").pack()

#text_to_speech input
text_label = Label(window, text="Text:").place(x=10,y=20)
text_entry = Text(window, width=30,height=5)
text_entry.place(x=80,y=20)
#Accent input
accent_label = Label(window, text="Accent:").place(x=10,y=110)
accent_entry = Entry(window,  width=26)
accent_entry.place(x=80,y=110)
#Duration input
duration_label = Label(window, text="Duration:").place(x=10,y=140)
duration_entry = Entry(window,  width=26)
duration_entry.place(x=80,y=140)

#Perform the functions
button1 = Button(window,text='List languages', bg = 'Turquoise',fg='Red',command=list_languages).place(x=10,y=190)
button2 = Button(window,text='Convert Text to Speech', bg = 'Turquoise',fg='Red',command=text_to_speech).place(x=130,y=190)


#close the app
window.mainloop()
