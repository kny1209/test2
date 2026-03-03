# from tkinter import Tk, Button

# def order():
#     print("order!")

# otk = Tk()
# otk.geometry('400x300+550+250')
# obtn = Button(otk, text="order", command=order)
# obtn.pack()
# otk.mainloop()

# from tkinter import Tk, Button
# # second way of event bind : using bind func
# # def fname(event):
# #     codeblock

# def order(event):   # event : event info obj (auto transmission)
#     print("order!")

# otk = Tk()
# otk.geometry('400x300+550+250')
# obtn = Button(otk, text="order")

# # obj.bind("<str event>", func obj)
# obtn.bind('<Button-1>',order)

# obtn.pack()
# otk.mainloop()

print('-------------------')
from tkinter import Tk, Button, Label

def msg():
    print("start tkinter")

otk = Tk()
otk.geometry('400x300+550+250')
olabel = Label(otk, text='start label')
olabel.pack(side='top')

obtn = Button(otk, text="start button", command=msg)
obtn.pack(side='bottom')
otk.mainloop()