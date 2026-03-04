# def func(para1,para2,...):
#     codeblock
#     func(arg1,arg2,...)
#     return something

# 재귀함수 사용
'''
def count(n):
    if n == 0:
        print("done!")
        return
    print(n)
    count(n-1)

count(5)

# 반복문 사용
for i in range(5):
    print(5-i)
print("done")
'''

x = 10
def add(n):
    b = x + n
    print("x =",x)  # 읽기 가능
    print("b =",b)
add(10)

# print("--------------------")
# x = 10
# def add(n):
#     x += n      # x = 지역변수, 쓰기 불가능
#     print("x =",x)
# add(10)

print("--------------------")
x = 10
def add(n):
    global x
    x += n
    print("x =",x)
add(10)
