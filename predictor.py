import cricketdata
import gd
import manual
import scorecrd
import random
from tkinter import *
from tkinter import messagebox as mb
root=Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.geometry(f"{w}x{h}")
root.configure(bg="light green")
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

p1 = PhotoImage(file='bg1.png')
root.iconphoto(False, p1)
root.title("RUN PREDICTOR")
##################################################HEADING#######################################################################################
frame=Frame(root)
frame.pack()
head = Label( frame,text="CRICKET RUN PREDICTOR",bg="red",font=('calibre',40,'bold'),borderwidth=3,relief="ridge")
head.pack()


###############################################AUTO&MANUAL#####################################################################################

frame1=Frame(root,borderwidth=2,relief="ridge",bg="red")
frame1.pack(pady=10)
var1=StringVar()
var2=StringVar()
txtover=StringVar()
txtcscore=StringVar()
ball=StringVar()
predict=StringVar()
actscore=StringVar()
aftermatch=StringVar()


r1=Radiobutton(frame1,text="T-20",value="t20",variable=var2,font = ('calibre',20,'bold'))
r1.select()
r1.pack(side=LEFT)
r2=Radiobutton(frame1,text="one-day",value="od",variable=var2,font = ('calibre',20,'bold'))
r2.pack(side=LEFT)
frame2=Frame(root,bg="red",borderwidth=2,relief="ridge")
frame2.pack(pady=10)
r3=Radiobutton(frame2,text="Automatic",value="Automatic",variable=var1,font = ('calibre',20,'bold'))
r3.select()
r3.pack(side=LEFT)
r4=Radiobutton(frame2,text="Manual",value="Manual",variable=var1,font = ('calibre',20,'bold'))
r4.pack(side=LEFT)
def matchwindow(matchlist):
    #matchlist=["ind vs sl","pak vs china","aus vs wb"]
    sroot=Tk()
    sroot.geometry("400x400")
    #sroot.configure(bg="light green")
    #p = PhotoImage(file='bg1.png')
    #sroot.iconphoto(False, p)
    sroot.title("RUN PREDICTOR")
    var=StringVar()
    def get_id():
        print(var.get())
        sroot.destroy()

    if len(matchlist)==0:
        l1=Label(sroot,text="CURRENTLY NO MATCH IS GOING LIVE ",bg="yellow",font=('calibre',10,'bold'),borderwidth=2,relief="ridge")
        l1.pack(pady=50,padx=50)
        b1 = Button(sroot, text="DONE", bg="orange", font=('calibre', 10, 'bold'), bd=10, command=sroot.destroy)
        b1.pack()
    else:
       for (team,link) in matchlist.items():
          Radiobutton(sroot,text=team,value=link,variable=var,font = ('Helvetica',10,'bold'),background="yellow",indicator=0).pack(fill=X,ipady=10)
       b1 = Button(sroot, text="DONE", bg="orange", font=('calibre', 10, 'bold'), bd=10, command=get_id)
       b1.pack()


    sroot.mainloop()
def submit():
    matchlist=""
    if (var1.get()=="Automatic") and (var2.get()=="t20"):
        matchlist=cricketdata.get_matches("t20")
        matchwindow(matchlist)
    elif (var1.get()=="Automatic") and (var2.get()=="od"):
        matchlist=cricketdata.get_matches("odi")
        matchwindow(matchlist)
    elif (var1.get()=="Manual") and (var2.get()=="t20"):
             r1.configure(state=DISABLED)
             r2.configure(state=DISABLED)
             r3.configure(state=DISABLED)
             r4.configure(state=DISABLED)
    elif (var1.get()=="Manual") and (var2.get()=="od"):
             r1.configure(state=DISABLED)
             r2.configure(state=DISABLED)
             r3.configure(state=DISABLED)
             r4.configure(state=DISABLED)



    #print(".....submitbutton working")
def showScard():
    scorecrd.getscore()
frame3=Frame(root)
frame3.pack()
b1=Button(frame3,text="SUBMIT",bg="orange",font=('calibre',10,'bold'),bd=10,command=submit)
b1.pack()



frame4=Frame(root,bg="green",borderwidth=2,relief="ridge")
frame4.pack(pady=(20,0))


lblover=Label(frame4,text="CURRENT OVER",bg="light green",font=('calibre',10,'bold'),borderwidth=2,relief="ridge").grid(column=0,row=0,pady=(10,10),padx=(10,10))
e1 = Entry(frame4,textvariable = txtover,width=10,bd=3,selectbackground='violet')
e1.grid(column=1,row=0,padx=(10,100))

e2= Entry(frame4,textvariable = txtcscore,width=10,bd=3,selectbackground='violet')
e2.grid(column=2,row=0,pady=(10,10),padx=(10,10))



lblball=Label(frame4,text="CURRENT BALL",bg="light green",font=('calibre',10,'bold'),borderwidth=2,relief="ridge").grid(column=3,row=0,pady=(10,10),padx=(10,10))
e3 = Entry(frame4,textvariable = ball,width=10,bd=3,selectbackground='violet')
e3.grid(column=4,row=0,pady=(10,10),padx=(10,10))

prescore=Label(frame4,text="00",bg="light green",font=('calibre',20,'bold'),textvariable=predict,borderwidth=2,relief="ridge",width=3).grid(column=2,row=1,pady=(10,0),padx=(10,100))
predict.set(00)

lblactualscore=Label(frame4,text="Enter Actual Score",bg="light green",font=('calibre',10,'bold'),borderwidth=2,relief="ridge").grid(column=1,row=5,pady=(10,10),padx=(10,10))
actualscore= Entry(frame4,textvariable = actscore,width=10,bd=3,selectbackground='violet')
actualscore.grid(column=1,row=6,pady=(0,100))

lblmscore=Label(frame4,textvariable=aftermatch,bg="light green",font=('calibre',10,'bold'),borderwidth=2,relief="ridge")
lblmscore.grid(column=3,row=5,padx=(10,0))
aftermatch.set("SCORE AFTER MATCH : 00")
scorecardbtn=Button(frame4,text="GET SCORE CARD",bg="orange",command=showScard,font=('calibre',20,'bold'),bd=10).grid(column=3,row=6)


def getscore():
    Score=actscore.get()
    score = txtcscore.get()
    score = int(score)
    e2.delete(0,END)
    e2.insert(0, 0)
    e2.configure(state=DISABLED)
    over=txtover.get()
    bowl = ball.get()
    actualscore.delete(0,END)
    try:
        if (score)or(Score):
            bowl = int(bowl)
            # Score=int(Score)
            if bowl == 6:
                e1.delete(0, END)
                e1.insert(0, int(over) + 1)
                e3.delete(0, END)
                e3.insert(0, 1)

            elif (bowl > 6) or (bowl < 1):
                mb.showwarning("ALERT", "ENTER VALID VALUE")
                e2.configure(state=NORMAL)
            elif (bowl > 0) or (bowl < 7):
                e3.delete(0, END)
                e3.insert(0, bowl + 1)
    except:
        mb.showwarning("ALERT","ENTER VALID INPUT")


    if Score:
        manual.put_data({'ball':int(over)+(bowl/10),'run':Score})
    elif score:
       manual.put_data({'ball':int(over)+(bowl/10),'run':score})
    else :
       mb.showwarning("ENTER SCORE","ENTER ACTUAL SCORE")
    if Score:
        t=0
    else:
        t=random.randint(120,200)
    predict.set(gd.predict_run(int(txtover.get())+int(int(ball.get())/10)))
    aftermatch.set(f"SCORE AFTER MATCH:{t}")


b1=Button(frame4,text="PREDICT SCORE FOR NEXT BALL",bg="orange",font=('calibre',10,'bold'),bd=10,command=getscore).grid(column=2,row=3,padx=(10,100))
note="NOTE :please enter actual score after prediction to get more accurate result"
lblnote=Label(frame4,text=note,bg="yellow",font=('calibre',10,'bold'),borderwidth=2,relief="ridge").grid(column=2,row=4,pady=(0,10),padx=(10,10))






frame5=Frame(root,bg="brown")
frame5.pack()

txtcover=StringVar()
txtcball=StringVar()
Cscore=StringVar()
head = Label( frame5,text="CUSTOM PREDICT",bg="orange",font=('calibre',20,'bold'),borderwidth=3,relief="ridge").grid(column=2,row=0,padx=(10,10),pady=(10,10))

lblcover=Label(frame5,text="Enter OVER",bg="light green",font=('calibre',10,'bold'),borderwidth=2,relief="ridge").grid(column=0,row=1,pady=(10,10),padx=(10,10))
txtcover=Entry(frame5,textvar=txtcover)
txtcover.grid(column=1,row=1,padx=(10,50))

lblball=Label(frame5,text="Enter BALL",bg="light green",font=('calibre',10,'bold'),borderwidth=2,relief="ridge").grid(column=2,row=1,pady=(10,10),padx=(10,10))
txtball=Entry(frame5,textvar=txtcball)
txtball.grid(column=3,row=1,padx=(10,100))

lblmscore=Label(frame5,textvar=Cscore,bg="orange",font=('calibre',10,'bold'),borderwidth=2,relief="ridge").grid(column=6,row=1,padx=(10,100))
Cscore.set("YOUR PREDICTED SCORE:00")
def custom_predict():
    Cover=int(txtcover.get())
    Cball=int(txtcball.get())
    Cscore.set(f"YOUR PREDICTED SCORE:{gd.predict_run(Cover+(Cball/10))}")

b2=Button(frame5,text="PREDICT",bg="orange",font=('calibre',10,'bold'),bd=10,command=custom_predict)
b2.grid(column=4,row=1,padx=(10,100))




root.mainloop()


