from tkinter import Tk, Button

# 위젯 정리
otk = Tk()
otk.geometry('400x300+550+250')
obtn1 = Button(otk, text="push1")
obtn2 = Button(otk, text="push2")
obtn3 = Button(otk, text="push3")

# 웨젯 배치
obtn1.pack()
obtn2.pack()
obtn3.pack()

otk.mainloop()