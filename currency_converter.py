from tkinter import*

#importing currencies from the text file to a dictionary
with open('currencyRates.txt') as f:
    lines = f.readlines()
currency = {}
currList = []
currName = {}
for line in lines:
    divide = line.split('\t')
    currency[divide[0]] = float(divide[2])
    currList.append(divide[0])
    currName[divide[0]] = divide[1]

#button command
def convert():
    optionSelected = var.get()
    taka = float(userInput.get())
    answer = taka * currency[optionSelected]
    ans.set("%.4f"%answer)
    convertedText['text'] = ":" + optionSelected
    convertedText2['text'] = "in " + currName[optionSelected]


root = Tk()
root.geometry('580x200+500+200')
root.title("Currency Converter")
root.resizable(0,0)
root.iconbitmap('images/icon.ico')

#bg image
bgImage = PhotoImage(file = "images/main bg.png")
mainFrame = Label(root,image=bgImage)
mainFrame.pack()
mainFrame.place(x=0,y=0,relwidth=1,relheight=1)

#option list
var = StringVar(mainFrame)
currencySelected = OptionMenu(mainFrame,var,*currList)
currencySelected.config(width=4,font=('times new roman',12),relief=FLAT)
currencySelected.pack() 
currencySelected.place(x=238,y=45)

#User input taker
userInput = Entry(mainFrame,font=('times new roman',16),width = 12)
userInput.pack()
userInput.place(x=60,y=50)

#output
ans = StringVar()
output = Entry(mainFrame,font=('times new roman',16),width = 13,textvariable = ans,justify=RIGHT)
output.pack()
output.place(x=360,y=50)

#convert button
cnvBtn = Button(mainFrame,text='Convert',font=('times new roman',16,'bold'),command=convert,bg="#1B1B1B",fg='white',relief=GROOVE)
cnvBtn.pack()
cnvBtn.place(x=230,y=130)

#bdtText
bdtText = Label(mainFrame,text='BDT:',font=('times new roman',16),bg='black',fg='white')
bdtText.pack()
bdtText.place(x=2,y=50)

#converted text
convertedText = Label(mainFrame,font=('times new roman',16),bg='black',fg='white',width=4,anchor='w')
convertedText.pack()
convertedText.place(x=508,y=50)

#converted text 2
convertedText2 = Label(mainFrame,font=('times new roman',11),bg='black',fg='white',width=20,anchor='e')
convertedText2.pack()
convertedText2.place(x=342,y=80)

root.mainloop()
