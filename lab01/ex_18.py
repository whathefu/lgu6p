w = float(input("몸무게를 입력하시오 : "))
h = float(input("키를 입력하시오 : "))

bmi = w/h**2
print(f"BMI :{bmi}")
if bmi >= 25 :
    print("비만")
elif bmi >=23 :
    print("과체중")
elif bmi >=18.5 : 
    print("정상")
else :
    print("저체중")
