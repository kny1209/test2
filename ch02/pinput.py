print("첫 번쨰 정수를 입력하시오:")

ra = int(input( ))
rb = int(input("두 번째 정수를 입력하시오:"))
rc = int(ra % rb)
rd = int(ra - rb)

print(ra, "%", rb, "값은", rc, "이다.")
print(ra, "+", rb, "값은", rd, "이다.")
