import wikipedia
import geeta
import win32com.client
speaker=win32com.client.Dispatch("SAPI.SpVoice")
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
    elif choice == 2:
        speaker.Speak(result)
        print(result)
    else:
        print("Bye")
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def Health():
    news=input("Medicine li?")
    c=news.find("Yes")
    h=news.find("Ha")
    if c>=0 or h>0:

        time=input("Good kb li medicine, i mean kitne time pehle, hours btana?")

        if time>4:
            staus=input("Ab tk to tumhe thoda/bahut relief mil hi gaya hoga- Ha ya Na?")
            if staus=="Ha":
                print("Very good")
            else:
                print("Medicine fir se le lo, ya fir jaakr doctor se mil lo :)")
        else:
            print("Wait kro 4 hours complete hone ka, medicine hai thoda time to legi hi")

        choice=input("Timepass ke liye jokes sunoge kya? \n \t Yes \t No")
        n=choice.find("Yes")
        nn=choice.find("Ha")
        m=choice.find("No")
        hh=choice.find("Nhi")
        if n>=0 or nn>=0:

            jokes=open("Jokes.txt","r")
            print(jokes.readlines(6))
            more=input("Aur v jokes sun ne ka mann h kya? -- type More or cancel -- ")
        elif h>=0 or hh>=0:
            print("Okay nhi sunata hu rhne do")

        else:
            print("Error Occured!!")

    else:
        ask=int(input("Kyu nhi li medicine? --\n\t 1. Pta nhi h kon si medicine loo yaar\t 2.Nhi yaar aise hi thik ho jayega"))
        if ask==1:
            medList=open("mediList.txt","r")
            print(medList.read())
        elif ask==2:
            print("Chalo yaar thik h dekh lo aap apna, ha agar thik n ho to medicine le lena!")
        else:
            while ask==1 or ask==2:
                print("Yaar achhe se fillup kro n")
                ask = int(input("Kyu nhi li medicine? --\n\t 1. Pta nhi h kon si medicine loo yaar\t 2.Nhi yaar aise hi thik ho jayega"))
                if ask == 1:
                    medList = open("mediList.txt", "r")
                    print(medList.read())
                elif ask == 2:
                    print("Chalo yaar thik h dekh lo aap apna, ha agar thik n ho to medicine le lena!")
                else:
                    print("Yaar achhe se fillup kro n")

#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
def hurt():
    cause=input("Kaise hurt hua yaar?- Character enter kro \n\tS. Sports me \tT.Table ya another chiz se \t K.Kisi ne chata/mukka mara")
    c2=cause.find("Sports")
    c3=cause.find("sports")
    c4=cause.find("furniture")
    c41 = cause.find("Furniture")
    c5=cause.find("maara")
    c6=cause.find("Mara")
    c7=cause.find("peeta")
    if c2>=0 or c3>=0:
        print("Dhyan se khela kro n yaar! Loi nhi yaara hota h games me, balm and med-cream use kr lo temporarily rahat milegi")
        print("Dekho mere pas ek list hai basic medicines ki check kr lo... ")
        medList=open("MediList.txt","r")
        print(medList.read())
    elif c4>=0 or c41>=0:

        print("Yaar dhyan se dekh kr chalna chahiye n tumhe")
        news=input("Dard km hua ya nhi?\n \t Ha/ Yes \tNo/Nhi")
        if news=="Ha" or news=="Yes":
            print("Chalo achha hua!")
            choice=input("Joke sunoge?")
            d=choice.find("Yes")
            d1=choice.find("yes")
            d11=choice.find("ha")
            d12=choice.find("Ha")
            d2=choice.find("No")
            d21=choice.find("nhi")
            d22=choice.find("Nhi")

            if d>=0 or d1>=0 or d11>=0 or d12>=0:
                print("Okay okay nhi suna rha")
                newChoice=input("To fir kya krna h? Dekho mere pas list h jo tum kr skte ho dekho or btao-\n \t1.Wikipedia se padhai\n\t2.Geeta ka gyan")
                nc=newChoice.find("wiki")
                nc1=newChoice.find("padhai")
                nc2=newChoice.find("geeta")
                nc21=newChoice.find("gyan")
                if nc>=0 or nc1>=0:
                    openWikipedia()
                elif nc2>=0 or nc21>=0:
                    openGeeta()
                else:
                    print("Nothing chosen plz choose one of the option, Cancelling the program!")

 #-------------------------------------------------------------------------------------------------------------------------------------------
 #-------------------------------------------------------------------------------------------------------------------------------------------
 #-------------------------------------------------------------------------------------------------------------------------------------------



