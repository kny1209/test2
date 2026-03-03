# import tkinter

# # 1. 위젯 생성
# otk = tkinter.Tk()      # 부모 윈도우 (위젯)
# obtn = tkinter.Button(otk, text = "click") # 자식 버튼 위젯

# # 2. 위젯 배치
# obtn.pack()

# # 3. 이벤트 바인딩
# # tkinter.Button(command=)

# # 4. 프로그램 동작 유지
# otk.mainloop()

# print("----------------------")
# # from tkinter import *
# from tkinter import Tk, Button

# otk = Tk()
# otk.geometry('100x150+550+250')
# obtn = Button(otk, text="click")
# obtn.pack()
# otk.mainloop()

print("----------------------")
from tkinter import Tk, Button

def hi():
    print("hi, there")

otk = Tk()
otk.geometry('400x300+550+250')
obtn = Button(otk, text="click", command=hi)
obtn.pack()
otk.mainloop()