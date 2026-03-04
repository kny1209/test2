print("---list_ swap---")

ca = [10, 11]
print("ca[0] :",ca[0], "ca[1] :",ca[1])

temp = ca[0]
ca[0] = ca[1]
ca[1] = temp
print("ca[0] :",ca[0], "ca[1] :",ca[1])

print("---list_ swap_func---")

def funca(na,nb):
    temp = na
    na = nb
    nb = temp

ca = [10,11]
na = ca[0]
nb = ca[1]
print("ca[0] :",ca[0], ", ca[1] :",ca[1])

funca(ca[0],ca[1])
print("ca[0] :",ca[0], ", ca[1] :",ca[1])     # return X -> swap X

print("---list_ swap_new---")

ca = [10,11]
cb = ca
print("ca :",ca)
print("cb :",cb)

temp = cb[0]
cb[0] = cb[1]
cb[1] = temp

print("ca[0] :",ca[0], ", ca[1] :",ca[1]) 
print("cb[0] :",cb[0], ", cb[1] :",cb[1]) 

print("---list_ swap_new_func---")

def funca(cb):
    temp = cb[0]
    cb[0] = cb[1]
    cb[1]= temp

ca = [10,11]        # cb = ca
print("ca[0] :",ca[0], ", ca[1] :",ca[1])

funca(ca)
print("ca[0] :",ca[0], ", ca[1] :",ca[1])     # return X -> swap X

print("---list_mem---")

a = [10,11,12,13]
print("list a :",a)

a[1] = 21
print("list a :",a)

b=a
print("list b :",b)

b = [30,31,32,33]
print("list b :",b)