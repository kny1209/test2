b = 0
print("b = ",b)
b = 1
print("b = ",b)

def scope_test():
    a = 1
    print("a in scope_test() func :",a)

a = 0
print("a out of scope_test() func :",a)
scope_test()
print("a after scope_test() func :",a)
