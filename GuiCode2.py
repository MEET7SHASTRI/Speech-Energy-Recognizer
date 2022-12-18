from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import pyttsx3

import speech_recognition as s
sr=s.Recognizer()
analyzer=SentimentIntensityAnalyzer()
tell=pyttsx3.init()

from tkinter import *

from PIL import ImageTk,Image

global full_text
window=Tk()
window.title("Speech Emotion Recognition")
window.geometry("400x400")
window.maxsize(400,400)
window.iconbitmap("icon_image.ico")
window.minsize(400,400)
i=ImageTk.PhotoImage(Image.open("Speechbackground.png"))

def speech_emotion_reco(): # Main Part analyzing
                           # Second Tab
    try:
        print("listening....")
        with s.Microphone() as m:
            tell.say("Start Saying.....")
            tell.runAndWait()
            sr.adjust_for_ambient_noise(m)
            audio = sr.listen(m,timeout=5,phrase_time_limit=10)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
        query = str(query)
        total = analyzer.polarity_scores(query)
        print(total)
        positive = total['pos']
        negative = total['neg']
        neutral=total['neu']
        overall = total['compound']

        positive= positive * 100
        negative= negative * 100
        overall= overall * 100
        neutral=neutral*100
        max_all=max(positive,negative,neutral)
        if max_all==positive:
            return ('''The speech seems positive
                      😊😊😊😊😊😊😊😊😊''')
        elif max_all == negative:
            return ('''The speech seems negative
                        😔😔😔😔😔😔😔😔😔😔''')
        elif positive == 0 and negative == 0:
            return ("The speech is totally neutral")
        else:
            from_second=max(positive,negative)
            if from_second == positive:
               return(f'''The speech seems neutral with positive abbreviations 
                          Positive={positive}%
                          Neutral={neutral}%''')
            elif from_second == negative:
                return (f'''The speech seems neutral with negative abbreviations
                            Negative={negative}%
                            Neutral={neutral}%''')
            else:
                return ("The speech seems totally neutral")
    except Exception as e:
        print(e)
        return "Try again"

def command_speech(): # Last Tab to be opened for output
    c=speech_emotion_reco()
    popup = Toplevel(window)
    popup.title("Speech Emotion Recognition")
    popup.minsize(700, 150)
    popup.maxsize(700, 150)
    popup.geometry('700x150')
    labeling=Label(popup,text=c,font=('Arial',15),bg='black',fg='white')
    labeling.pack()



def speech(): # Second Tab
    new=Toplevel(window)
    new.iconbitmap("icon_image.ico")
    new.title("Speech Emotion Recognition")
    new.geometry('300x300')
    new.maxsize(300,300)
    new.minsize(300,300)
    l=Label(new,text="Speech Emotion Recognition",bg='yellow',font=('Arial',15))
    l.pack()

    il=Label(new,image=i)
    il.pack()
    b=Button(new,text='Click here for recording',bg='yellow',font=('Arial',15),background='pink',command=command_speech)
    b.pack()




#image

my_img=ImageTk.PhotoImage(Image.open("icon_image.png"))
# Label
mainlabel=Label(window,text="Sentiment Analysis",font=('Arial',30))
mainlabel.pack()
label1=Label(window,image=my_img)
label1.pack()
#label
setlabel=Label(window,text="Press The Button",font=('Arial',15),bg='yellow',fg='black',width=30,height=2)
setlabel.pack()

#Speech Button
speechbutton=Button(window,text="Speech Emotion Recogntion",font=('Arial',20),bg='blue',fg='white',height=2,command=speech)
speechbutton.pack()



window.mainloop()