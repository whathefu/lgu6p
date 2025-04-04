user_id = "python-master"
user_pw = "p1234"

AUTH = False

def login():
    global AUTH

    if AUTH:
        AUTH = False
        print("로그아웃 되었습니다.")
        return
    
    while user_id != input("ID: "):
        print("아이디가 없습니다.")

    while user_pw != input("PW: "):
        print("패스워드가 틀립니다.")

    print("로그인 성공")
    AUTH = True
    

def auth_required(func):
    def wrapper(*args, **kwargs):
        if AUTH == True:
            print("접근 승인")
            func(*args, **kwargs)
        else:
            print("접근 권한 없음")
    
    return wrapper



def order_list():
    print("********************")
    print("구매 리스트 출력")
    print("만두, 아이스크림, 콜라")
    print("********************")

def return_list():
    print("********************")
    print("반품 리스트 출력")
    print("커피, 책")
    print("********************")

def recommend_list():
    print("********************")
    print("추천 목록 출력")
    print("참치, 라면, 피자")
    print("********************")

while True:
    print("====================")
    print("[0] : 로그인 ")
    print("[1] : 구매 리스트")
    print("[2] : 교환 반품 리스트")
    print("[3] : 오늘의 추천 상품")
    c = input("메뉴 선택: ")
    if c == "0":
            login()
    elif c == "1":
            order_list()
    elif c == "2":
            return_list()
    elif c == "3":
            recommend_list()
    else:
        break


