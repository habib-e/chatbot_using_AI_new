
from chatterbot import ChatBot  #chatterbot module theke ChatBot class
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading

# pyttsx3

engine = pp.init()        #  pp pyttsx3 ke initial korbe thn eita engine module return korbe ==>  audio library

voices = engine.getProperty('voices')       # voices ar list banabo jate voice store korbo
print(voices)

engine.setProperty('voice', voices[0].id)       # key voice r voices 0 mail voices 1 femail

def speak(word):       # speak korar jonno word dibo
    engine.say(word)
    engine.runAndWait()

bot = ChatBot("My Bot")    #chatBot ar obj bot variable ar majhe rakhbo

convo = [
    'hello',
    'hi there !',
    'who are you ',
    'i am a bot i made by joy , habib and nuri ',
    'how are you ',
     'what is your name',
    'My name is Bot , i am created by team_delta ',
    'I am doing great these days, what about you ?',
    'you are looking smart ',
    'thank you , yeap smater people can find smart people ',
    'who is your teacher',
    'Humaira maam is our course teacher ',
    'In which city you live ?',
    'I live in Dhaka',
    'In which language you talk?',
    ' I mostly talk in english',
    'i am fine',
    'yeah great do you have any question?',
    'What is your number',
    'I dont have any number',
     'What is your port  number',
     'I find Im quite fond of the number 42',
     'What can you eat',
     'I consume RAM, and binary digits.',
      'Why cant you eat food',
     'Im a software program, I blame the hardware.',
      'What is your current location',
      'currently i am now in BUBT',
      'What is your location',
      'I am everywhere.',
       'Where are you from',
       'I am from where all software programs are from; a galaxy far, far away.',
       'Where are you',
       'I am on the Internet.',
        'Do you have any brothers',
        'I might. You could say that every bot built using my engine is one of my siblings',
        'Who is your father',
         'joy is my father ',
         'Who is your boss',
         'i have created by joy habib so they are my boss ',
          'What is ai',
           'Artificial Intelligence is the branch of engineering and science devoted to constructing machines that think.',
           'What language are you written in',
           'python',
        'When do you die',
       ' I am was never really born and therefore am effectively deathless.',
        'What is a chat robot?',
        'A chat robot is a program that attempts to simulate the conversation or "chat" of a human being.',
        'Who are you?',
         'bot',
        'how old are you ',
        ' Younger then yours ',
    'todays date',
    'Today is 23 march 2022',
    'tell me about todays weather ',
    ' todays weather is mostly sunny ',
    'ok bye ',
    'Thank you very much , we had a nice conversation, good bye',
    'hi',
    'Hello sir how can i help you ?',
    'hey',
    'hello sir '


]

trainer = ListTrainer(bot)      #trainer obj variable of class ListTrainer

# now training the bot with the help of trainer by passing conversation
trainer.train(convo)

# answer = bot.get_response("what is your name?")
# print(answer)

# print("Talk to bot ")
# while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = bot.get_response(query)
#     print("bot : ", answer)

main = Tk()    #variable main which is an obj of TK class

main.geometry("600x800")        #pop up window size

main.title("My Chat bot")       #pop up window title

img = PhotoImage(file="bot1.png")         #inamge path

photoL = Label(main, image=img)        #photoL vari , Label class (parent window , img ar obj )

photoL.pack(pady=6)


# takey query : it takes audio as input from user and convert it to string..

def takeQuery():
    sr = s.Recognizer()          #recog ar obj sr ... take input as audio and give output as a string
    sr.pause_threshold = 1        # 1 dilam jate noise kom ashe
    print("hey habib .... your bot is listening try to speak")
    with s.Microphone() as m:       #micro class ar obj ke as m variable vabe dorbo
        try:
            audio = sr.listen(m)       # audio input using m
            query = sr.recognize_google(audio, language='eng-in')       # audio to str
            print(query)
            textF.delete(0, END)    # text field clear
            textF.insert(0, query)    # text field a oi string ta set korlam
            ask_from_bot()       # query send kore dibo ask from bot a
        except Exception as e:
            print(e)
            print("not recognized")


def ask_from_bot():
    query = textF.get()  # textF.get type kora gula fetch kore query te store korbe
    answer_from_bot = bot.get_response(query)    #response nibe & store korbe
    msgs.insert(END, "you : " + query)    #last ar theke msg add hobe
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))  # print ans as a string
    speak(answer_from_bot)                        # speak korbe word ta
    textF.delete(0, END)
    msgs.yview(END)              #last ar gula auto scroll hotei thakbe


frame = Frame(main)     # frame class ke parent window main dicche

sc = Scrollbar(frame)   # for scrolling ,  parent holo frame
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)   # ans giving  box

sc.pack(side=RIGHT, fill=Y)      # right a rakhbo scroll

msgs.pack(side=LEFT, fill=BOTH, pady=10)      # mag left a tahkbe

frame.pack()

# creating text field

textF = Entry(main, font=("Verdana", 22))    #Entry class , main window parent
textF.pack(fill=X, pady=10)      # ques korar box ta

btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)   # command ask_from_bot  function ke call dibe
btn.pack()


# creating an enter key press function
def enter_function(event):      # enter press hole enter fun call hbe and btn ke invoke /fire /hit korbe
    btn.invoke()

# going to bind main window with enter key...

main.bind('<Return>', enter_function)    # main ar songe bind korbe enter key ke .. thn retrun korbe  enter func ke

def repeatL():
    while True:
        takeQuery()

t = threading.Thread(target=repeatL)   # thread target korbe repeatL ke and bar bar take query korbe jototime code off na hocche

t.start()

main.mainloop()





