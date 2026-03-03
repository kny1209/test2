from tkinter import PhotoImage, Tk, Button, Label

oroot = Tk()
oroot.geometry("600x400")

img1 = PhotoImage(file=r"ch11\widget2\스크린샷 2026-03-02 194059.png")

img_Label = Label(oroot, image=img1)
img_Label.place(x=0, y=0)

obutton1 = Button(oroot, text="push1")
obutton2 = Button(oroot, text="push2")
obutton3 = Button(oroot, text="push3")

obutton1.place(x=10, y=60)
obutton2.place(x=140,y=60)
obutton3.place(x=80, y=10)

oroot.mainloop()