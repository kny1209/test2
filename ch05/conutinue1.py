print("---continue---")
count = 0
while count < 3:
    count += 1
    if count == 2:
        continue
    print(count)

print("---break---")
count = 0
while count < 3:
    count+=1
    if count == 2:
        break
    print(count)

print("---이중 for문---")
for j in range(5): #[1,2,3,4,5]
    for i in range(10): #[1,2,3,4,5,6,7,8,9,10]
        print("*",end="")
    print()