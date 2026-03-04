#1
for num in [3,1,2]:
    print(num)
print("--------------")
for num in range(2):
    print(num)
print("--------------")

#2
clovers = ['clover1','clover2','clover3']
for clover in clovers:
    print(clover)
print("--------------")

#3
clovers = ['clover1','clover2','clover3']
for clover in range(3):
    print(clovers[clover])
print("--------------")

#4
count = 0
while count <3:
    print(count)
    count+=1
print("--------------")

#5
count = 1
while count <4:
    count+=1
    print(count)
print("--------------")

#6
count = 0
while count <= 5:
    if count % 2 != 0:
        print(count)
    count += 1
print("--------------")

#7
'''
price = 0
while price != -1:
    price = int(input("enter the price(fin:-1):)"))
    if price > 10000:
        print("expensive")
    elif price > 5000:
        print("good")
    elif price > 0:
        print("cheap")
print("--------------")
'''
#8
for i in range(101):
    if i % 3 == 0:
        print(i, end=" ")
    else:
        pass
print("\n--------------")

#9
for i in range(1,11):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print("\n--------------")


#10
i = int(input("enter the num for getting sum:"))
total = 0
for i in range(1,i+1):
    total += i 
print("sum of 1 to",i,"is",total)
print("\n--------------")


# #11
# i = int(input("enter the num for getting sum:"))
# total = 0
# while i < i+1:
#     total += i   
# print("sum of 1 to",i,"is",total)    

#p.33
for j in range(11):
    print("1X",j,"=",j)

#p.34
for j in range(1,3):
    print(j,"단")
    for i in range(11):
        print(j,"*",i,"=",j*i)

#p.35
for j in range(1,6):
    print(j,"단")
    for i in range(11):
        print(j,"*",i,"=",j*i)