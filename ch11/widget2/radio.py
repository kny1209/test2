from tkinter import Tk
from tkinter import Button
from tkinter import Radiobutton
from tkinter import IntVar


oroot = Tk()    # parent window (widget)
oroot.geometry("400x300")

radio_value = IntVar()  # 정수 변수 생성
radio_value.set(-1)      # 정수값 설정  # -1 : 아무것도 선택 안 되도록 설정 = 초기화


lunch = {0:'A lunch',1:'B lunch',2:'C lunch'}

# variable : 클릭된 버튼의 정보를 저장한 변수명 설정    
# value : radio_value에 저장된 데이터를 지정하는 변수
orb1 = Radiobutton(oroot, text=lunch[0], variable=radio_value, value=0)
orb2 = Radiobutton(oroot, text=lunch[1], variable=radio_value, value=1)
orb3 = Radiobutton(oroot, text=lunch[2], variable=radio_value, value=2)

orb1.pack()
orb2.pack()
orb3.pack()

def buy():
    value = radio_value.get()
    print(lunch[value])

obtn = Button(oroot, text="order", command=buy)
obtn.pack()

oroot.mainloop()
