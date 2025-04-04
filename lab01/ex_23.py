id = "python"
passwd = "abcd"

ID = input("ID를 입력하시오 : ")

if ID != id :
        print("그런아이디는 존재하지 않습니다.")
        ID = input("ID를 입력하시오 : ")
        if ID == id :
             Password = input("Password를 입력하시오 : ")
             if Password == passwd :
                  print("로그인 되었습니다.")
              
else :
    Password = input("Password를 입력하시오 : ")
    if Password == passwd :
         print("로그인 되었습니다.")

    