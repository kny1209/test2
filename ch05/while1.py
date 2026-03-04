print("---for---")
for num in range(3):
    print("hi turtle",num)

print("---while---")
num = 0
while num < 3:
    print("hi turtle",num)
    num = num+1 #증감식:while문 빠져나올 수 있도록

# print("---무한반복---")
# while True:
#     print("ctrl+c를 누르세요.")

print("---복합 대입 연산자---")
stra = "python"
strb = " programming"
stra += strb
print(stra)
