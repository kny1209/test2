import tkinter as tk

root = tk.Tk()

options_list = ['black', 'navy', 'green']

selectied_option = tk.StringVar()   # 클래스를통해 생성

selectied_option.set(options_list[0])

options_menu = tk.OptionMenu(root, selectied_option, *options_list)
options_menu.pack()

root.mainloop()


#C:\rokey\py_work\ch11\widget2\스크린샷 2026-03-02 194059.png
#ch11\widget2\스크린샷 2026-03-02 194059.png
# .\ch11\widget2\스크린샷 2026-03-02 194059.png

# ..\ch11\widget2\스크린샷 2026-03-02 194059.png    cd 10

# ..\..\ch11\widget1\button.py     cd test
