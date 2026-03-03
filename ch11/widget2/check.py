from tkinter import Tk
from tkinter import Button
from tkinter import BooleanVar
from tkinter import Checkbutton

oroot = Tk()    # parent window (widget)
oroot.geometry("400x300")

coffee = {0:'americano',1:'latte',2:'cappucino',3:'espresso'}

check_value = {}
check_value[0] = BooleanVar()   # 불리언 값 저장
check_value[1] = BooleanVar()
check_value[2] = BooleanVar()
check_value[3] = BooleanVar()

check_value[0].set(True)
# print(check_value[0].get())

for i in range(len(coffee)):
    check_value[i] = BooleanVar()
    ocheckbutton1 = Checkbutton(oroot, text=coffee[i], variable=check_value[i])
    ocheckbutton1.pack()
# ocheckbutton2 = Checkbutton(oroot, text=coffee[1], variable=check_value[1])
# ocheckbutton3 = Checkbutton(oroot, text=coffee[2], variable=check_value[2])
# ocheckbutton4 = Checkbutton(oroot, text=coffee[3], variable=check_value[3])


# ocheckbutton2.pack()
# ocheckbutton3.pack()
# ocheckbutton4.pack()

def buy():
    for i in check_value:
        if check_value[i].get() ==True:
            print(coffee[i])
   

obtn = Button(oroot, text="order", command=buy)
obtn.pack()

oroot.mainloop()