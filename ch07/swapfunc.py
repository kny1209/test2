def swap_func(pa, pb):
    temp = pa
    pa = pb
    pb = temp   
    return pa, pb      

na = 10
nb = 11
print("na값 :",na,"nb값 :",nb)

na, nb = swap_func(na, nb)

print("na값 :",na,"nb값 :",nb)