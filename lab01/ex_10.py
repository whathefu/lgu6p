name = input("너의이름 : ")
a=input("국어 점수 :")
b=input("영어 점수 :")
c=input("수학 점수 :")
d=input("과학 점수 :")

a = int(a)
b = int(b)
c = int(c)
d = int(d)

total = a+b+c+d
mean = total/4

print(f"{name}의 총점은 {total}이고 평균은{mean}입니다.") 