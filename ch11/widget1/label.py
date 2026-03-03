from tkinter import Tk, Label

# 위젯 정리
otk = Tk()
otk.geometry('400x300+550+250')     # 픽셀

olabel1 = Label(otk, text="salmon", bg="salmon", width=70)      # width 단위 : 문자 셀 개수
olabel2 = Label(otk, text="greenyellow", bg="greenyellow",width=70)
olabel3 = Label(otk, text="mediumturquoise", bg="mediumturquoise",width=70)

# 웨젯 배치
olabel1.pack()
olabel2.pack()
olabel3.pack()

otk.mainloop()