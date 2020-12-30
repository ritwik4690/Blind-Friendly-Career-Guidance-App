from tkinter import *
import speech_recognition as sr
root = Tk()
root.geometry("2000x2000")
root.title("BLIND-FRIENDLY CAREER GUIDANCE")
import pyttsx3
engine=pyttsx3.init()
com1=StringVar()
com2=StringVar()
frame=Frame(root,height=1900,width=2000)
frame0=Frame(root,height=2000,width=2000)
frame1=Frame(root,height=1900,width=2000)
frame2=Frame(root,height=1000,width=2000)
frameA=Frame(root,height=1900,width=2000)
frameB = Frame(root,height=10000,width=2000)
frame3 = Frame(root,height=10000,width=2000)
frame4 = Frame(root,height=10000,width=2000)

#Declaring for tts
l2=Label(frame0, text="Which field are you more interested in? Engineering or Pure Sciences. Confused? Take a quiz?",fg="#0BB0F6", font=("times new roman",20,"bold"))
l7 = Label(frame1, text = "The curriculum for Information Technology Engineering is primarily designed to provide\n students with both the theoretical knowledge and technical skills. The curriculum also\n intends to improve a technological depth of knowledge and skills in analysis, design,\n implementation, and use of both information technology core skills and specialization skills. ",fg="black", font=("Arial",20), anchor='w')
l9 = Label(frame1, text="They design, develop, research and test software and digital\n hardware, digital devices and interfaces. So, various organizations are becoming more oriented\n to recruit IT engineers with a view to operate computer systems, software, servers,\n computer networking or network security.",fg="black", font=("Arial",20), anchor='w')
lE=Label(frameA,text="As a computer engineer, you're responsible for researching, designing, developing and\n testing computer hardware and equipment, including chips, analog sensors, circuit boards,\n keyboards, modems, routers and printers. You may work on the manufacturing\n of these components, as well as the installation.",fg="black",font=("Helvetica",20,))
lC=Label(frameA,text="Computer engineering is a branch of engineering that integrates several fields of computer\n science and electronics engineering required to develop computer hardware and software.\n Computer engineers usually have training in electronic engineering (or electrical engineering),\n software design, and hardware–software integration instead of only software engineering or\n electronic engineering.",fg="black",font=("Helvetica",20,))
l14 = Label(frame2, text = "With the background acquired in the junior year, students are equipped\n to take design classes and to engage in the professional practice/capstone design sequence.\n Required classes also include foundation design and transportation. For the \nrest of the senior year, technical elective courses are available.",fg="black", font=("Arial",20), anchor='w')
l16 = Label(frame2, text="Civil engineers design, construct, supervise, operate, and maintain large \nconstruction projects and systems, including roads, buildings, airports, tunnels, dams,\n bridges, and systems for water supply and sewage treatment. Many\n civil engineers work in design, construction, research, and education.",fg="black", font=("Arial",20), anchor='w')
lJ=Label(frameB, text="Telecommunications engineering, or telecom engineering, is an engineering discipline that\n integrates electrical engineering with computer science to develop telecommunication systems.\n A Telecom equipment engineer is an electronics engineer that designs equipment such\n as routers, switches, multiplexers and other splecialized computer / electronics\n equipment designed to be used in the telecommunication network infrastructure",fg="black", font=("Arial",20), anchor='w')
lL=Label(frameB, text="As an electronics engineer you'll design, develop and test components, devices,\n systems or equipment that use electricity as part of their source of power.\n These components include capacitors, diodes, resistors and transistors",fg="black", font=("Arial",20), anchor='w')
l21 = Label(frame3, text = "Chemical engineering is all about changing raw materials into useful products such as\n clothes, food and drink, and energy. Chemical engineers focus on processes and\n products – they develop and design processes to create\n products; either focussing on improving existing processes or creating new ones.",fg="black", font=("Arial",20), anchor='w')
l23 = Label(frame3, text="Chemical engineers develop and design chemical manufacturing processes. Chemical\n engineers apply the principles of chemistry, biology, physics, and math\n to solve problems that involve the production or use of chemicals, fuel, drugs,\n food, and many other products.",fg="black", font=("Arial",20), anchor='w')
l28 = Label(frame4, text = "Biomedical Engineering, also referred to as Bioengineering, BioMed\n or BME, is a multidisciplinary STEM field that combines biology and engineering,\n applying engineering principles and materials to medicine and healthcare.",fg="black", font=("Arial",20), anchor='w')
l30 = Label(frame4, text="Design biomedical equipment and devices, such as artificial internal\n organs, replacements for body parts, and machines for diagnosing medical problems.\n Install, adjust, maintain, repair, or provide technical support for biomedical equipment.",fg="black", font=("Arial",20), anchor='w')

def org():
    
    frame0=Frame(root,height=2000,width=2000).place(x=0,y=0)
    bg = Label(frame0, bg="grey").pack()
    
    l1=Label(frame0,text="Career Guidance For Science Students",fg="#0BB0F6",font=("Arial",50,"bold")).place(x=30,y=30)
    l2=Label(frame0, text="Which field are you more interested in? Engineering or Pure Sciences? Confused? Take a quiz?",fg="#0BB0F6", font=("times new roman",20,"bold"))
    l2.place(x=150,y=200)
    bV1= Button(frame0, command=lambda:voiceHome1()).place(x=100,y=200)
    bC1= Button(frame0, command=comA).place(x=100,y=250)
    

    b1 = Button(frame0,text='Engineering',fg="white",bg="red",font = "Helvetica 35 bold",relief="raised", command=play).place(x=300,y=300)
    b2 = Button(frame0,text='Pure Sciences',fg="white",bg="purple",font = "Helvetica 35 bold",relief="raised",command=org1).place(x=700,y=300)
    b3 = Button(frame0,text='Take a Quiz',fg="white",bg="#FFCD01",font = "Helvetica 35 bold",relief="raised", command=quiz1).place(x=520,y=500)
    b4 = Button(frame0, text= " Quit ", fg="Black", font = "Helvetica 20", relief="raised",command=quit).place(x=1200,y=600)
    
    
def comA():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak Anything')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            com1 = r.recognize_google(audio)
            print('You said: ', format(com1))
            if(com1=="engineering" or com1=="Engineering"):
                play()
                
            elif(com1=="pure sciences" or com1=="pure Sciences"):
            
                org1()
            elif(com1=="take a quiz"or com1=="take a Quiz"):
                quiz1()
            elif(com1=="quit"):
                root.quit()
            else:
                return voiceRepA()
                print("Option not found.")
                
        except:
            return voiceRepA()
            print("could not recognize your voice")

def voiceRepA():
    engine.say("Try Again")
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
    return comA()
def voiceHome1():
    engine.say(l2['text'])
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.runAndWait()

def org1():
    frameZ=Frame(root,height=2000,width=2000).place(x=0,y=100)
    bg = Label(frameZ, bg="grey").pack()

    bV3= Button(frameZ, command=lambda:voiceHome3()).place(x=100,y=200)
    bC2= Button(frameZ, command=comB).place(x=100,y=250)

    lz=Label(frameZ,text="Select the branch of pure science.",fg="#0BB0F6",font=("Helvetica",30,"bold")).place(x=400,y=120)
        
    b181 = Button(frameZ,text='Physics',fg="white",bg="red",font = "Helvetica 35 bold",relief="raised",command=physics).place(x=300,y=300)
    b182 = Button(frameZ,text='Maths',fg="white",bg="purple",font = "Helvetica 35 bold",relief="raised",command=maths).place(x=1000,y=300)
    b183 = Button(frameZ,text='Chemistry',fg="white",bg="#FFCD01",font = "Helvetica 35 bold",relief="raised",command=chemistry).place(x=300,y=400)
    b184 = Button(frameZ,text='Biology',fg="white",bg="green",font="Helvetica 35 bold",relief="raised",command=biology).place(x=1000,y=400)
    b197 = Button(frameZ, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=org).place(x=1200,y=600)

def comB():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak Anything')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            com1 = r.recognize_google(audio)
            print('You said: ', format(com1))
            if(com1=="physics" or com1=="Physics"):
                physics()
                
            elif(com1=="maths" or com1=="Maths"):
                maths()
            elif(com1=="chemistry" or com1=="Chemistry"):
                chemistry()
            elif(com1=="biology" or com1=="Biology"):
                biology()
            elif(com1=="back"):
                org()
            else:
                return voiceRepB()
                print("Option not found.")
                
        except:
            return voiceRepB()
            print("could not recognize your voice")
def voiceRepB():
    engine.say("Try Again")
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
    return comB()
def voiceHome3():
    engine.say("Select the branch for pure science. Physics. Maths. Chemistry. Biology")
    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)
    engine.runAndWait()

def physics():
    #physics page
    frameQ = Frame(root,height=10000,width=2000).place(x=0,y=100)

    l80=Label(frameQ, text="Physics",fg="#0BB0F6",font=("Helvetica",30,"bold")).place(x=500,y=120)

    l81=Label(frameQ, text="Your options are:",fg="black",font=("Helvetica",20,"bold")).place(x=350,y=200)
    bV4= Button(frameQ, command=lambda:voicePhy()).place(x=100,y=200)
    l82=Label(frameQ, text="\n1.Geophysicst\n2.Metallurgy\n3.Ratiation Proctection\n4.Research Scientist\n5.Seismic Interpreter" ,fg="black",font=("Arial",20)).place(x=400,y=300)
    b90 = Button(frameQ, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=org1).place(x=1200,y=600)   
def voicePhy():
    engine.say("Your options are: Geophysicst. Metallurgy. Ratiation Proctection. Research Scientist. Seismic Interpreter")
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
def maths():
    #maths page
    
    frameE = Frame(root,height=10000,width=2000).place(x=0,y=100)

    l51=Label(frameE, text="Maths",fg="#0BB0F6",font=("Helvetica",30,"bold")).place(x=450,y=120)

    l52=Label(frameE, text="Your options are:",fg="black",font=("Helvetica",20,"bold")).place(x=350,y=200)
    bV5= Button(frameE, command=lambda:voiceMat()).place(x=100,y=200)
    l53=Label(frameE, text="1.Operational Researcher\n2.Research Scientist\n3.Satistician\n4.Lecturer",fg="black",font=("Arial",20)).place(x=400,y=300)
    b91 = Button(frameE, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=org1).place(x=1200,y=600)
def voiceMat():
    engine.say("Your options are: 1.Operational Researcher. Research Scientist. Satistician. Lecturer")
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
def chemistry():
    #chemistry page
    frameC = Frame(root,height=1000,width=2000).place(x=0,y=100)

    l54=Label(frameC, text="Chemistry",fg="#0BB0F6",font=("Helvetica",30,"bold")).place(x=600,y=200)

    l55=Label(frameC, text="Your options are:",fg="black",font=("Helvetica",25,"bold")).place(x=550,y=300)
    bV6= Button(frameC, command=lambda:voiceChem()).place(x=100,y=200)
    l56=Label(frameC, text="1.Clinical Biochemistry\n2.Foresic Scientist\n3.Pharmacologist\n4.Toxiologist\n5.Chemical Engineer\n6.Analytical Chemist",fg="black",font=("Arial",20)).place(x=550,y=400)
    b92=   Button(frameC, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=org1).place(x=1200,y=600) 
def voiceChem():
    engine.say("Your options are: Clinical Biochemistry. Foresic Scientist. Pharmacologist. Toxiologist. Chemical Engineer. Analytical Chemist")
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
def biology():
    #biology page
    frameB = Frame(root,height=10000,width=2000).place(x=0,y=100)

    l57=Label(frameB, text="Biology",fg="#0BB0F6",font=("Helvetica",30,"bold")).place(x=650,y=200)

    l58=Label(frameB, text="Your options are:",fg="black",font=("Helvetica",25,"bold")).place(x=600,y=300)
    bV7= Button(frameB, command=lambda:voiceBio()).place(x=100,y=200)
    l59=Label(frameB, text="1.Soil Scientist\n2.Research Scientist (Life Sciences)\n3.Nature Conservation Officer\n4.Microbiologist",fg="black",font=("Arial",20)).place(x=530,y=400)
    bV6= Button(frameB, command=lambda:voiceBio()).place(x=100,y=200)
    b93= Button(frameB, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=org1).place(x=1200,y=600)  
def voiceBio():
    engine.say("Your options are: Soil Scientist. Research Scientist (Life Sciences). Nature Conservation Officer. Microbiologist")
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
def play():
    #Engineering page
    frame=Frame(root,height=2000,width=2000).place(x=0,y=100)
    l4=Label(frame, text = "Choose a course to know more about it",fg="#0BB0F6", font=("times new roman",20,"bold")).place(x=450,y=130)

    bV2=  Button(frame, command=lambda:voiceHome2()).place(x=100,y=200)
    bC3= Button(frame, command=comC).place(x=100,y=250)

    b5 = Button(frame, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=org).place(x=1200,y=600)
    b6 = Button(frame,text='Computer Engineering',fg="white",bg="purple",font = "Verdana 20",relief="raised",command=comp).place(x=510,y=170)
    b7 = Button(frame,text='Information Technology',fg="white",bg="#114762",font = "Verdana 20",relief="raised",command=it).place(x=510,y=230)
    b8 = Button(frame,text='Electronics and Telecommunication',fg="white",bg="red",font = "Verdana 20",relief="raised",command=extc).place(x=440,y=290)
    b9 = Button(frame,text='Civil Engineering',fg="white",bg="#FFEF00",font = "Verdana 20",relief="raised",command=civ).place(x=545,y=350)
    b10 = Button(frame,text='Chemical Engineering',fg="white",bg="#00E6FF",font = "Verdana 20",relief="raised",command=chem).place(x=510,y=410)
    b11 = Button(frame,text='Biomedical Engineering',fg="white",bg="#FF0091",font = "Verdana 20",relief="raised",command=biomed).place(x=500,y=470)
    

def comC():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak Anything')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            com2 = r.recognize_google(audio)
            print('You said: ', format(com1))
            if(com2 =="computer" or com2=="computer science" or com2=="computer science engineering" or com2=="computer engineering"):
                comp()
            elif(com2=="information technology" or com2=="information Technology"):
                it()
            elif(com2=="electronics and telecommunication" or com2=="electronics and telecommunication"):
                extc()
            elif(com2=="civil Engineering" or com2=="civil engineering"):
                civ()
            elif(com2=="chemical engineering" or com2=="chemical Engineering"):
                chem()
            elif(com2=="biomedical Engineering" or com2=="biomedical engineering"):
                biomed()
            elif(com2=="back"):
                org()
            else:
                return voiceRepC()
                print("Option not found.")
                
        except:
            return voiceRepC()
            print("could not recognize your voice")
def voiceRepC():
    engine.say("Try Again")
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
    return comC()
def voiceHome2():
    engine.say("Choose a course. Computer, Information Technology, Electronics and Telecommunication, Civil Engineering, Chemical Engineering, Biomedical Engineering")
    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)
    engine.runAndWait()


def it():
    #IT page
    frame1 = Frame(root,height=1900,width=2000).place(x=0,y=100)

    b13 = Button(frame1, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=play).place(x=1200,y=600)
    bVit=Button(frame1, command=lambda:voiceIT1()).place(x=100,y=150)
    bVit2=Button(frame1, command=lambda:voiceIT2()).place(x=150,y=150)
    bC3= Button(frame1, command=comIT).place(x=100,y=250)
    l5= Label(frame1, text = "Information Technology",fg="#0BB0F6", font=("Helvetica",30,"bold")).place(x=450,y=120)
    l6 =  Label(frame1, text = "Curriculum:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=200)
    l7 = Label(frame1, text = "The curriculum for Information Technology Engineering is primarily designed to provide\n students with both the theoretical knowledge and technical skills. The curriculum also\n intends to improve a technological depth of knowledge and skills in analysis, design,\n implementation, and use of both information technology core skills and specialization skills. ",fg="black", font=("Arial",20), anchor='w').place(x=190,y=200)
    l8 = Label(frame1, text="Job Profile:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=350)
    l9 = Label(frame1, text="They design, develop, research and test software and digital\n hardware, digital devices and interfaces. So, various organizations are becoming more oriented\n to recruit IT engineers with a view to operate computer systems, software, servers,\n computer networking or network security.",fg="black", font=("Arial",20), anchor='w').place(x=190,y=350)
    l10 = Label(frame1, text="Salary:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=525)
    l11 = Label(frame1, text="$52000 to $59000 per annum",fg="black", font=("Arial",20), anchor='w').place(x=190,y=525)

def voiceIT1():
    engine.say(l7["text"])
    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
def voiceIT2():
    engine.say(l9["text"])
    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)
    engine.runAndWait()

def comIT():  
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak Anything')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            com1 = r.recognize_google(audio)
            print('You said: ', format(com1))
            if(com1=="back" or com1=="Back"):
                play()
            else:
                return voiceRepIT()
                print("Option not found.")
                
        except:
            return voiceRepIT()
            print("could not recognize your voice")
def voiceRepIT():
    engine.say("Try Again")
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
    return comIT()
def comp():
    #Comp page
    frameA=Frame(root,height=1900,width=2000).place(x=0,y=100)

    bVcomp=Button(frameA, command=lambda:voiceComp1()).place(x=100,y=150)
    bVcomp2=Button(frameA, command=lambda:voiceComp2()).place(x=150,y=150)

    bC4= Button(frameA, command=comComp).place(x=100,y=250)

    lA=Label(frameA,text="COMPUTER ENGINEERING",fg="#0BB0F6",font=("Helvetica",30,"bold")).place(x=440,y=120)
    lB=Label(frameA,text="Curriculum:",fg="black",font=("Helvetica",20,"bold")).place(x=30,y=250)
    lC=Label(frameA,text="Computer engineering is a branch of engineering that integrates several fields of computer\n science and electronics engineering required to develop computer hardware and software.\n Computer engineers usually have training in electronic engineering (or electrical engineering),\n software design, and hardware–software integration instead of only software engineering or\n electronic engineering.",fg="black",font=("Helvetica",20,)).place(x=190,y=250)
    lD=Label(frameA,text="Job Profile:",fg="black",font=("Helvetica",20,"bold")).place(x=30,y=410)
    lE=Label(frameA,text="As a computer engineer, you're responsible for researching, designing, developing and\n testing computer hardware and equipment, including chips, analog sensors, circuit boards,\n keyboards, modems, routers and printers. You may work on the manufacturing\n of these components, as well as the installation.",fg="black",font=("Helvetica",20,)).place(x=190,y=410)
    lF=Label(frameA,text="Salary:",fg="black",font=("Helvetica",20,"bold")).place(x=30,y=550)
    lG=Label(frameA,text="Approx. $110,650 per annum",fg="black",font=("Helvetica",20,)).place(x=150,y=550)
    
    b13 = Button(frameA, text="Back",fg="Black", font="Helvetica 20", relief="raised", command=play).place(x=1200,y=600)

def voiceComp1():
    engine.say(lC["text"])
    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
def voiceComp2():
    engine.say(lE["text"])
    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
def comComp():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak Anything')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            com1 = r.recognize_google(audio)
            print('You said: ', format(com1))
            if(com1=="back" or com1=="Back"):
                play()
            else:
                return voiceRepComp()
                print("Option not found.")
                
        except:
            return voiceRepComp()
            print("could not recognize your voice")
def voiceRepComp():
    engine.say("Try Again")
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
    return comComp()
def civ():
    #Civil Engg
    frame2 = Frame(root,height=10000,width=2000).place(x=0,y=100)

    b13 = Button(frame2, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=play).place(x=1200,y=600)
    bVciv=Button(frame2, command=lambda:voiceCiv1()).place(x=100,y=150)
    bVciv2=Button(frame2, command=lambda:voiceCiv2()).place(x=150,y=150)
    bC5= Button(frame2, command=ComCiv).place(x=100,y=250)
    l12= Label(frame2, text = "Civil Engineering",fg="#0BB0F6", font=("Helvetica",30,"bold")).place(x=450,y=120)
    l13 =  Label(frame2, text = "Curriculum:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=200)
    l14 = Label(frame2, text = "With the background acquired in the junior year, students are equipped\n to take design classes and to engage in the professional practice/capstone design sequence.\n Required classes also include foundation design and transportation. For the \nrest of the senior year, technical elective courses are available.",fg="black", font=("Arial",20), anchor='w').place(x=190,y=200)
    l15 = Label(frame2, text="Job Profile:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=350)
    l16 = Label(frame2, text="Civil engineers design, construct, supervise, operate, and maintain large \nconstruction projects and systems, including roads, buildings, airports, tunnels, dams,\n bridges, and systems for water supply and sewage treatment. Many\n civil engineers work in design, construction, research, and education.",fg="black", font=("Arial",20), anchor='w').place(x=190,y=350)
    l17 = Label(frame2, text="Salary:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=525)
    l18 = Label(frame2, text="$50000 to $65000 per annum",fg="black", font=("Arial",20), anchor='w').place(x=190,y=525)

def voiceCiv1():
    engine.say(l14["text"])
    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
def voiceCiv2():
    engine.say(l16["text"])
    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
def ComCiv():   
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak Anything')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            com1 = r.recognize_google(audio)
            print('You said: ', format(com1))
            if(com1=="back" or com1=="Back"):
                play()
            else:
                return voiceRepCiv()
                print("Option not found.")
                
        except:
            return voiceRepCiv()
            print("could not recognize your voice")
def voiceRepCiv():
    engine.say("Try Again")
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
    return comCiv()
def extc():
    #EXTC Page
    frameB = Frame(root,height=10000,width=2000).place(x=0,y=100)
    bC6= Button(frameB, command=ComExtc).place(x=100,y=250)
    b13 = Button(frameB, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=play).place(x=1200,y=600)
    bVex=Button(frameB, command=lambda:voiceEx1()).place(x=100,y=150)
    bVex2=Button(frameB, command=lambda:voiceEx2()).place(x=150,y=150)
    lH=Label(frameB, text="ELECTRONICS & TELECOMMUNICATION ENGINEERING",fg="#0BB0F6", font=("Helvetica",30,"bold")).place(x=200,y=120)
    lI=Label(frameB, text="Curriculum:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=200)
    lJ=Label(frameB, text="Telecommunications engineering, or telecom engineering, is an engineering discipline that\n integrates electrical engineering with computer science to develop telecommunication systems.\n A Telecom equipment engineer is an electronics engineer that designs equipment such\n as routers, switches, multiplexers and other splecialized computer / electronics\n equipment designed to be used in the telecommunication network infrastructure",fg="black", font=("Arial",20), anchor='w').place(x=190,y=200)
    lK=Label(frameB, text="Job Profile:", font=("Helvetica",20,"bold")).place(x=10,y=375)
    lL=Label(frameB, text="As an electronics engineer you'll design, develop and test components, devices,\n systems or equipment that use electricity as part of their source of power.\n These components include capacitors, diodes, resistors and transistors",fg="black", font=("Arial",20), anchor='w').place(x=190,y=375)
    lM=Label(frameB, text="Salary:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=525)
    lN=Label(frameB, text="$5620 to $7024 per annum",fg="black", font=("Arial",20), anchor='w').place(x=190,y=525)

def voiceEx1():
    engine.say(lJ["text"])
    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
def voiceEx2():
    engine.say(lL["text"])
    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
def ComExtc():   
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak Anything')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            com1 = r.recognize_google(audio)
            print('You said: ', format(com1))
            if(com1=="back" or com1=="Back"):
                play()
            else:
                return voiceRepExtc()
                print("Option not found.")
                
        except:
            return voiceRepExtc()
            print("could not recognize your voice")
def voiceRepExtc():
    engine.say("Try Again")
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
    return comExtc()
def chem():
    #chemical Engg
    frame3 = Frame(root,height=10000,width=2000).place(x=0,y=100)
    bC7= Button(frame3, command=ComChem).place(x=100,y=250)
    b14 = Button(frame3, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=play).place(x=1200,y=600)
    bVchem=Button(frame3, command=lambda:voiceChem1()).place(x=100,y=150)
    bVchem2=Button(frame3, command=lambda:voiceChem2()).place(x=150,y=150)

    l19= Label(frame3, text = "Chemical Engineering",fg="#0BB0F6", font=("Helvetica",30,"bold")).place(x=450,y=120)
    l20 =  Label(frame3, text = "Curriculum:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=200)
    l21 = Label(frame3, text = "Chemical engineering is all about changing raw materials into useful products such as\n clothes, food and drink, and energy. Chemical engineers focus on processes and\n products – they develop and design processes to create\n products; either focussing on improving existing processes or creating new ones.",fg="black", font=("Arial",20), anchor='w').place(x=190,y=200)
    l22 = Label(frame3, text="Job Profile:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=350)
    l23 = Label(frame3, text="Chemical engineers develop and design chemical manufacturing processes. Chemical\n engineers apply the principles of chemistry, biology, physics, and math\n to solve problems that involve the production or use of chemicals, fuel, drugs,\n food, and many other products.",fg="black", font=("Arial",20), anchor='w').place(x=190,y=350)
    l24 = Label(frame3, text="Salary:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=525)
    l25 = Label(frame3, text="$60,770 per annum",fg="black", font=("Arial",20), anchor='w').place(x=190,y=525)

def voiceChem1():
    engine.say(l21["text"])
    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
def voiceChem2():
    engine.say(l23["text"])
    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
def ComChem():   
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak Anything')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            com1 = r.recognize_google(audio)
            print('You said: ', format(com1))
            if(com1=="back" or com1=="Back"):
                play()
            else:
                return voiceRepChem()
                print("Option not found.")
                
        except:
            return voiceRepChem()
            print("could not recognize your voice")
def voiceRepChem():
    engine.say("Try Again")
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
    return comChem()
def biomed():
    #Biomedical Engg
    frame4 = Frame(root,height=10000,width=2000).place(x=0,y=100)
    bC8= Button(frame4, command=ComBio).place(x=100,y=250)
    b14 = Button(frame4, text= "Back", fg="Black", font = "Helvetica 20", relief="raised",command=play).place(x=1200,y=600)
    bVbio=Button(frame4, command=lambda:voiceBio1()).place(x=100,y=150)
    bVbio2=Button(frame4, command=lambda:voiceBio2()).place(x=150,y=150)

    l26= Label(frame4, text = "Biomedical Engineering",fg="#0BB0F6", font=("Helvetica",30,"bold")).place(x=450,y=120)
    l27 =  Label(frame4, text = "Curriculum:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=200)
    l28 = Label(frame4, text = "Biomedical Engineering, also referred to as Bioengineering, BioMed\n or BME, is a multidisciplinary STEM field that combines biology and engineering,\n applying engineering principles and materials to medicine and healthcare.",fg="black", font=("Arial",20), anchor='w').place(x=190,y=200)
    l29 = Label(frame4, text="Job Profile:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=350)
    l30 = Label(frame4, text="Design biomedical equipment and devices, such as artificial internal\n organs, replacements for body parts, and machines for diagnosing medical problems.\n Install, adjust, maintain, repair, or provide technical support for biomedical equipment.",fg="black", font=("Arial",20), anchor='w').place(x=190,y=350)
    l31 = Label(frame4, text="Salary:",fg="black", font=("Helvetica",20,"bold")).place(x=10,y=525)
    l32 = Label(frame4, text="$80,751 per annum",fg="black", font=("Arial",20), anchor='w').place(x=190,y=525)
def voiceBio1():
    engine.say(l28["text"])
    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
def voiceBio2():
    engine.say(l30["text"])
    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
def ComBio():   
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak Anything')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            com1 = r.recognize_google(audio)
            print('You said: ', format(com1))
            if(com1=="back" or com1=="Back"):
                play()
            else:
                return voiceRepBio()
                print("Option not found.")
                
        except:
            return voiceRepBio()
            print("could not recognize your voice")
def voiceRepBio():
    engine.say("Try Again")
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
    return comBio()

def quiz1():
    #Quiz1
    
    frameE=Frame(root,height=2000,width=2000).place(x=0,y=0)
    bg = Label(frameE, bg="grey").pack()
    
    l65=Label(frameE,text="1. Do you want to study about the \n practical application of Sciences.",fg="#0BB0F6",font=("Arial",50,"bold")).place(x=200,y=30)
            
    b81 = Button(frameE,text='A. YES',fg="white",bg="red",font = "Helvetica 35 bold",relief="raised",command=click1).place(x=300,y=400)
    b82 = Button(frameE,text='B. NO',fg="white",bg="purple",font = "Helvetica 35 bold",relief="raised",command=click2).place(x=1000,y=400)
    bCW= Button(frameE, command=comW).place(x=100,y=250)
    bVW=  Button(frameE, command=lambda:voiceW()).place(x=100,y=200)
    b83 = Button(frameE, text= "Next", fg="Black", font = "Helvetica 20", relief="raised",command=quiz2).place(x=1000,y=550)
def comW():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak Anything')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            com1 = r.recognize_google(audio)
            print('You said: ', format(com1))
            if(com1=="Yes" or com1=="yes"):
                click1()
                
            elif(com1=="no" or com1=="No"):
            
                click2()
            else:
                return voiceRepW()
                print("Option not found.")
                
        except:
            return voiceRepW()
            print("could not recognize your voice")
def voiceRepW():
    engine.say("Try Again")
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
    return comW()
def voiceW():
    engine.say("Do you want to study about the practical application of Sciences")
    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)
    engine.runAndWait()

def quiz2():
#Quiz2
    
    frameF=Frame(root,height=2000,width=2000).place(x=0,y=0)
    bg = Label(frameF, bg="grey").pack()
    
    l66=Label(frameF,text="2. Are you willing to study uptil \n you get you Ph.D degree?",fg="#0BB0F6",font=("Arial",50,"bold")).place(x=200,y=30)
    bCX= Button(frameF, command=comX).place(x=100,y=250)  
    b84 = Button(frameF,text='A. YES',fg="white",bg="red",font = "Helvetica 35 bold",relief="raised",command=click3).place(x=300,y=400)
    b85 = Button(frameF,text='B. NO',fg="white",bg="purple",font = "Helvetica 35 bold",relief="raised",command=click4).place(x=1000,y=400)
    bVX=  Button(frameF, command=lambda:voiceX()).place(x=100,y=200)
    b86 = Button(frameF, text= "Next", fg="Black", font = "Helvetica 20", relief="raised",command=quiz3).place(x=1000,y=550)
def comX():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak Anything')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            com1 = r.recognize_google(audio)
            print('You said: ', format(com1))
            if(com1=="Yes" or com1=="yes"):
                click3()
                
            elif(com1=="no" or com1=="No"):
            
                click4()
            else:
                return voiceRepX()
                print("Option not found.")
                
        except:
            return voiceRepX()
            print("could not recognize your voice")
def voiceRepX():
    engine.say("Try Again")
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
    return comX()
def voiceX():
    engine.say(" Are you willing to study uptil you get you Ph.D degree?")
    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
def quiz3():
    #Quiz3

    frameG=Frame(root,height=2000,width=2000).place(x=0,y=0)
    bg = Label(frameG, bg="grey").pack()
    
    l67=Label(frameG,text="3. Are you interested in \n developing new theories?",fg="#0BB0F6",font=("Arial",50,"bold")).place(x=150,y=30)
    bCY= Button(frameG, command=comY).place(x=100,y=250)    
    b87 = Button(frameG,text='A. YES',fg="white",bg="red",font = "Helvetica 35 bold",relief="raised",command=click5).place(x=300,y=400)
    b88 = Button(frameG,text='B. NO',fg="white",bg="purple",font = "Helvetica 35 bold",relief="raised",command=click6).place(x=1000,y=400)
    bVY=  Button(frameG, command=lambda:voiceY()).place(x=100,y=200)
    b89 = Button(frameG, text= "Next", fg="Black", font = "Helvetica 20", relief="raised",command=quiz4).place(x=1000,y=550)

def comY():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak Anything')
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
        try:
            com1 = r.recognize_google(audio)
            print('You said: ', format(com1))
            if(com1=="Yes" or com1=="yes"):
                click5()
                
            elif(com1=="no" or com1=="No"):
            
                click6()
            else:
                return voiceRepY()
                print("Option not found.")
                
        except:
            return voiceRepY()
            print("could not recognize your voice")
def voiceRepY():
    engine.say("Try Again")
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
    return comY()
def voiceY():
    engine.say(" Are you interested in developing new theories?")
    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)
    engine.runAndWait()

def quiz4():
    
    frameH=Frame(root,height=2000,width=2000).place(x=0,y=0)
    bg = Label(frameH, bg="grey").pack()
    
    l68=Label(frameH,text="4. Are you interested in learning skills \n based upon problem solving.",fg="#0BB0F6",font=("Arial",50,"bold")).place(x=150,y=30)
    bCZ= Button(frameH, command=comZ).place(x=100,y=250)
    b99 = Button(frameH,text='A. YES',fg="white",bg="red",font = "Helvetica 35 bold",relief="raised",command=click8).place(x=300,y=400)
    b98 = Button(frameH,text='B. NO',fg="white",bg="purple",font = "Helvetica 35 bold",relief="raised",command=click7).place(x=1000,y=400)
    bVZ=  Button(frameH, command=lambda:voiceZ()).place(x=100,y=200)
    b96 = Button(frameH, text= "Next", fg="Black", font = "Helvetica 20", relief="raised",command=result).place(x=1000,y=550)

def comZ():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak Anything')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            com1 = r.recognize_google(audio)
            print('You said: ', format(com1))
            if(com1=="Yes" or com1=="yes"):
                click7()
                
            elif(com1=="no" or com1=="No"):
            
                click7()
            else:
                return voiceRepZ()
                print("Option not found.")
                
        except:
            return voiceRepZ()
            print("could not recognize your voice")
def voiceRepZ():
    engine.say("Try Again")
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
    return comZ()
def voiceZ():
    engine.say("Are you interested in learning skills based upon problem solving.")
    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)
    engine.runAndWait()
engg=IntVar()
applied=IntVar()


def click1():
    eng=engg.get()
    eng=eng+1
    print(eng)

    
    return quiz2()
    
def click2():
    app=applied.get()
    app=app+1
    return quiz2()


def click4():
    eng=engg.get()
    eng=eng+1
    return quiz3()
    
def click3():
    app=applied.get()
    app=app+1
    return quiz3()


def click6():
    eng=engg.get()
    eng=eng+1
    return quiz4()
    
def click5():
    app=applied.get()
    app=app+1
    return quiz4()


def click7():
    eng=engg.get()
    eng=eng+1
    return result()
    
def click8():
    
    app=app+1
    return result()








def result():
    
    frameI=Frame(root,height=2000,width=2000).place(x=0,y=0)
    bg = Label(frameI, bg="grey").pack()
    
    l45=Label(frameI,text="The Course You Should Choose is:",fg="#0BB0F6",font=("Arial",50,"bold")).place(x=200,y=30)
    eng=engg.get()
    app=applied.get()    
    if eng==app:
        l121=Label(frameI,text="Engineering",fg="#0BB0F6",font=("Arial",50,"bold")).place(x=400,y=200)
    else:
        l122=Label(frameI,text="Pure Sciences",fg="#0BB0F6",font=("Arial",50,"bold")).place(x=600,y=200)
    
    b45 = Button(frameI, text= "Home", fg="Black", font = "Helvetica 20", relief="raised",command=org).place(x=1200,y=600)
    
org()
root.mainloop()
