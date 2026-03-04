id_1 = 'kny'
password_1= '1234'

id = input("아이디를 입력하시오:")

if id == id_1:
    print("아이디 일치")
    password = input("암호를 입력하시오:")
    if password == password_1:
        print("로그인 성공")

    else:
        print("암호가 틀립니다")

else:
    print("아이디가 일치하지 않습니다.")