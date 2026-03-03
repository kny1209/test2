from tkinter import Tk, Label, Button

# 위젯 정리
otk = Tk()
# otk.title("arrangement")        # 윈도우 제목 변경
otk.geometry('400x300+550+250')     # 픽셀

obtn1 = Button(otk, text="push1")      
obtn2 = Button(otk, text="push2")
obtn3 = Button(otk, text="push3")

# 웨젯 배치
obtn1.grid(row=0, column=0)
obtn2.grid(row=1, column=1)
obtn3.grid(row=3, column=4, padx=70, pady=20)    # 공백 채움

otk.mainloop()