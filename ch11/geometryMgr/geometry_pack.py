from tkinter import Tk, Label, Button

# 위젯 정리
otk = Tk()
otk.title("arrangement")        # 윈도우 제목 변경
otk.geometry('400x300+550+250')     # 픽셀

olabel1 = Button(otk, text="push1")      
olabel2 = Button(otk, text="push2")
olabel3 = Button(otk, text="push3")


# 웨젯 배치
olabel1.pack(side='left')
olabel2.pack(side='right')
olabel3.pack(side=  'top')

otk.mainloop()