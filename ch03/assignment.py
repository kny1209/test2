score = int(input("score:"))

if 80 < score <= 100:
    print("grade is A") 

elif 60 < score <= 80:
    print("grade is B") 

elif 40 < score <= 60:
    print("grade is C") 

elif 20 < score <= 40:
    print("grade is D") 

elif 0 <= score <= 20:
    print("grade is B") 

else:
    print("제대로 입력하시오.")