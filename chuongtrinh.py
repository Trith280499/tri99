#Tạ Hoàng Trí - 43.01.104.189

from tkinter import *
def calculate(event):
 tx1=float(tx_1.get());
 tx2=float(tx_2.get());

 value1 = tx1 + tx2
 value2 = tx1 - tx2
 value3 = tx1 * tx2
 value4 = tx1 / tx2
 print(value1)
 print(value2)
 print(value3)
 print(value4)
 updateDisplay1(value1);
 updateDisplay2(value2);
 updateDisplay3(value3);
 updateDisplay4(value4);	
def updateDisplay1(myString):
	displayVariable1.set(myString)

def updateDisplay2(myString):
	displayVariable2.set(myString)
def updateDisplay3(myString):
    	displayVariable3.set(myString)

def updateDisplay4(myString):
	displayVariable4.set(myString)

root=Tk()
root.geometry("400x400")
root.title("Tính toán ")
root.grid()

lbl1=Label(root, text="Nhập số thứ nhất", font=("TimeNewRoman",14))
lbl1.pack()
tx_1= Entry(root, width=30, font=("TimeNewRoman",14))
tx_1.pack()

lbl2=Label(root, text="Nhập số thứ hai", font=("TimeNewRoman",14))
lbl2.pack()
tx_2= Entry(root, width=30, font=("TimeNewRoman",14))
tx_2.pack()

button_1 = Button(root, text="Tính toán", font=("TimeNewRoman",20,"bold"), bg="cyan", fg="red") 
button_1.bind("<Button-1>", calculate)
button_1.pack()

lbl2=Label(root, text="Tổng", font=("TimeNewRoman",14))
lbl2.pack()

displayVariable1 = StringVar()
displayLabel1 = Label(root, textvariable=displayVariable1, font=("TimeNewRoman",14))
displayLabel1.pack()

lbl2=Label(root, text="Hiệu", font=("TimeNewRoman",14))
lbl2.pack()

displayVariable2 = StringVar()
displayLabel2 = Label(root, textvariable=displayVariable2, font=("TimeNewRoman",14))
displayLabel2.pack()

lbl2=Label(root, text="Nhân", font=("TimeNewRoman",14))
lbl2.pack()

displayVariable3 = StringVar()
displayLabel3 = Label(root, textvariable=displayVariable3, font=("TimeNewRoman",14))
displayLabel3.pack()

lbl2=Label(root, text="Chia", font=("TimeNewRoman",14))
lbl2.pack()

displayVariable4 = StringVar()
displayLabel4 = Label(root, textvariable=displayVariable4, font=("TimeNewRoman",14))
displayLabel4.pack()

root.mainloop()