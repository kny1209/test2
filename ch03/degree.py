score = int(input("토익 점수를 입력하시오:"))

if score >= 900:
    print("상위권")

elif score >= 600:
    print("중상위권")

elif score >= 300:
    print("중위권")

else:
    print("하위권")

print("if문 종료")

