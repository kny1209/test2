from tkinter import Tk, Label, Checkbutton, BooleanVar, Button

obj = Tk()
obj.geometry("400x300")
obj.title("조각 피자 주문 프로그램")

pizza = {0:('(치즈 피자 (3200원)',3200), 1:('콤비네이션 피자 (3500원)',3500), 2:('불고기 피자(3600원)',3600)}

check_value = {}

for i in range(len(pizza)):
    check_value[i] = BooleanVar()
    ocheckbutton = Checkbutton(obj, text=pizza[i], variable=check_value[i])
    ocheckbutton.pack()

check_value[0].set(True)

olabel = Label(obj, text="피자")
olabel.pack(side='top')
olabel2 = Label(obj, text="")
olabel2.pack(side='bottom')

def buy():
    total = 0
    for i in check_value:
        if check_value[i].get() ==True:
            total+= pizza[i][1]
            print(pizza[i][0])
    print('총가격 :', total,"원")
   

obtn = Button(obj, text="주문", command=buy)
obtn.pack()

obj.mainloop()