


















# fruits = ['바나나', '파인애플', '복숭아', '사과', '포도']
# for i in range(5):
#     print(fruits[i])

#     if fruits[i] == "사과":
#         print("사과를 찾았습니다!")
    


# def solution(a, b):
# 		sum = a+b
# 		sub = a-b
# 		multi = a*b
# 		return sum, sub, multi
# a = int(input("정수를 입력하시오:"))
# b = int(input("정수를 입력하시오:"))
# sum, sub, multi = solution(a,b)
# print("덧셈:",sum)
# print("뺼셈:",sub)
# print("곱셈:",multi)


def sum_1(a):
    total = 0
    for i in range(1,a+1):
        total += i 
    return total

a = int(input("정수를 입력하시오:"))
result = sum_1(a)
print(result)
