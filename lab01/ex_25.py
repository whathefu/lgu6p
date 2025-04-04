passwd = "abcd"

P = input("패스워드를 입력하시오 : ")

for i in range(1, 5) : 
    if P != passwd :
        print("패스워드가 틀립니다.")
        P = input("패스워드를 입력하시오 : ")
    else :
        print("로그인이 완료되었습니다.")
        break
    
if  P != passwd :
    print("다섯번 모두 틀리셨습니다.")
    
else :
    print("로그인 완료")