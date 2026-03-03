from tkinter import Tk, Label, Button

# 위젯 정리
otk = Tk()
# otk.title("arrangement")        # 윈도우 제목 변경
otk.geometry('400x300+550+250')     # 픽셀

obtn1 = Button(otk, text="push1")      
obtn2 = Button(otk, text="push2")
obtn3 = Button(otk, text="push3")

# 웨젯 배치
obtn1.place(x=10,y=60)
obtn2.place(x=140, y=60)
obtn3.place(x=80, y=10) 

otk.mainloop()
