x= int(input("나눠질 수를 입력하세요 :"))
y= int(input("나눌 수를 입력하세요 : "))

def Qr(x, y) :
    # q= x // y
    # r= x % y 
    q=0
    r=0
    while True :
        # x - y = x
        x -= y
        if x > 0:
            q+= 1
        elif x < 0 :
            r =  x + y
            break
        else :
            q += 1
            break

    return (q, r)
