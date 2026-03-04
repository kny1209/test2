week = ['월', '화', '수', '목', '금', '토', '일']
print(week)
print(week[2:5])
# step
print(week[::2])
print(week[::-2])

print(week[5::])
print(week[0:4])
print(week[-5:5])
#좌 -> 우
print(week[-1:4])  # 겹치는 부분이 없음
print(week[7:5])  # 순서 역순 x
print(week[:])
print(week[6:0:-1])