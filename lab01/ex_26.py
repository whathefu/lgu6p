
while True: 
    a = int(input("[메뉴를 입력하세요]\n 1.게임시작   2.랭킹보기   3.게임종료>>> "))
    if a==1 :
        print("->게임을 시작합니다.")
    elif a==2 :
        print("->실시간 랭킹")
    elif a==3 :
        print("->게임을 종료합니다.")
        break
    else :
        print("다시 입력해주세요")