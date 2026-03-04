import tkinter as tk
from tkinter import messagebox

# 피자 가격 (조각당)
pizza_prices = {
    "페퍼로니": 3000,
    "치즈": 2500,
    "불고기": 3500
}

def order_pizza():
    pizza = pizza_var.get()
    slices = slice_var.get()

    if slices <= 0:
        messagebox.showwarning("경고", "조각 수를 1개 이상 선택하세요.")
        return

    total_price = pizza_prices[pizza] * slices

    result_label.config(
        text=f"🍕 주문 내역\n"
             f"피자 종류: {pizza}\n"
             f"조각 수: {slices}조각\n"
             f"총 가격: {total_price:,}원"
    )

# 메인 윈도우 생성
root = tk.Tk()
root.title("조각 피자 주문 프로그램")
root.geometry("350x350")

# 제목
title_label = tk.Label(root, text="🍕 조각 피자 주문", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# 피자 종류 선택
pizza_var = tk.StringVar(value="페퍼로니")

pizza_frame = tk.LabelFrame(root, text="피자 종류")
pizza_frame.pack(pady=10)

for pizza in pizza_prices:
    tk.Radiobutton(
        pizza_frame,
        text=f"{pizza} ({pizza_prices[pizza]}원)",
        variable=pizza_var,
        value=pizza
    ).pack(anchor="w")

# 조각 수 선택
slice_frame = tk.Frame(root)
slice_frame.pack(pady=10)

tk.Label(slice_frame, text="조각 수:").pack(side="left")

slice_var = tk.IntVar(value=1)
slice_spinbox = tk.Spinbox(
    slice_frame,
    from_=1,
    to=10,
    width=5,
    textvariable=slice_var
)
slice_spinbox.pack(side="left")

# 주문 버튼
order_button = tk.Button(
    root,
    text="주문하기",
    command=order_pizza,
    bg="orange",
    fg="white",
    width=15
)
order_button.pack(pady=15)

# 결과 출력
result_label = tk.Label(root, text="", font=("Arial", 11), justify="left")
result_label.pack(pady=10)

# 이벤트 루프
root.mainloop()
