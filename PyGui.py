from tkinter import messagebox,Button,Label,Entry
from tkinter import *

top = Tk()

button = Button(top,text="Compare",padx=20,pady=10).place(x=400,y=150)

text="DEFAULT"

genome1 = Label(top, text="covid-19").place(x=50,y=150)
genome2 = Label(top, text="othersGen").place(x=600,y=150)

cv19_gen= ["AAATTGC"]
virus_gen =["AACCGTT","GGGAATC","AAGATCC"]

inputCoronaGen = StringVar()
inputVirusGen = StringVar()

e1 = Entry(top, width=30,textvariable = inputCoronaGen)
e1.place(x=120,y=150)
e2 = Entry (top, width =30,textvariable = inputVirusGen)
e2.place(x = 700,y=150)

dropDown = OptionMenu(top,inputCoronaGen,*cv19_gen)
virusGenMenu = OptionMenu(top, inputVirusGen,*virus_gen)

str1 = ""
str2 = ""

def main():
    global top
    global button
    global genome1
    global genome2
    global e1
    global e2
    global cv19_gen
    global virus_gen
    global clicked
    global text
    global str1
    global str2

    top.geometry("1000x400")
    button = Button(top,text="Compare",command=actionListener,padx=20,pady=10).place(x=400,y=150)
    initMenu()
    
    top.mainloop()

def actionListener():
    str1 =e1.get()
    str2 =e2.get()
    similarPercent = genomeAsStr(str1,str2)
    messagebox.showinfo(e2.get(),str(similarPercent)+"%")

def initMenu():
    dropDown.place(x=0,y=0)
    virusGenMenu.place(x=900,y=0)

def genomeAsStr(str1,str2):
    count = 0
    for i in  range(len(str2)):
        if str2[i]!=str1[i]:
            count+=1
    if (len(str2)!=0 and len(str1)!=0):
        count = (len(str2)-count)*100/len(str2)
    else:
        count = 0
    return count

main()