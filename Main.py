import wikipedia
import win32com.client
from FriendModule import *
from geeta import *

#Set SAPI.SpVoice=sapi.Getvoices.Item(1)
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak("Hello, it is Krishna, welcome to this program, here i will try to resolve a;; your modern psychological problems")
print("Welcome to the vrtual world of modern solution of modern problems")

def openWikipedia():
    title=input(("Enter your topic to get knowledge dude-"))
    limit=int(input("Enter your limit for the discussion in sentences-"))
    result=wikipedia.summary(title,sentences=limit)
    choice = int(input("Enter your choice for output\n \t 0. For Textual Output \t 1.For Voice output \t2.For voice "
                       "result with then textual result--"))
    if choice == 0:
        print(result)
    elif choice == 1:
        speaker.Speak(result)
        print("Spoken")
    elif choice == 2:
        speaker.Speak(result)
        
        print(result)
    else:
        print("None selected select one")
        while choice>=0  and choice<=2:
            choice=int(input("Select from given options\n0.Print\n1.Listen\n2.Both\nEnter Your Choice-"))

while 1:
    tool=input("Which tool do you want to use? \n 1. For Wikipedia\t 2.Machine Friend")
    if tool=="Wikipedia" or tool=="wikipedia" or tool=="1":
        openWikipedia()
    elif tool=="Machine Friend" or tool=="2" or tool=="friend":
        greet()
    else:
        print("None seleted, select one")
        continue
    

# result=wikipedia.summary(topic,sentences=num)

# for i in range(1,5,1):
#     joke = pyjokes.get_joke(language="en", category="twister")
#     print(joke)
