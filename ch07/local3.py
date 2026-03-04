# b = 0
# print("b = ",b)
# b = 1
# print("b = ",b)

# p18
def scope_test():
    global a        
    a += 3
    print("a in scope_test() func :",a)
    
a = 0
print("a out of scope_test() func :",a)
scope_test()
print("a after scope_test() func :",a)

print("--------------------")

# p19
def scope_test():
    a = 0
    a += 3
    print("a in scope_test() func :",a)
    return a
    
a = 0
print("a out of scope_test() func :",a)
a1 = scope_test()
print("a after scope_test() func :",a)
print("local a after scope_test() func :",a1)

# global keyword
# 1. local -> global
# 2. block making local 