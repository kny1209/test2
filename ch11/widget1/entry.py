from tkinter import Tk, Label, Entry, StringVar     # StringVar : 문자열 변수 저장

# 위젯 정리
otk = Tk()
otk.geometry('400x300+550+250')

# (문자열) 변수 값 위젯과 연결 가능
ostring = StringVar()

# textvariable : 값 변화 자동 변환
oentry = Entry(otk, textvariable=ostring)      
olabel = Label(otk, textvariable=ostring)     

# 웨젯 배치
oentry.pack()
olabel.pack()

otk.mainloop()