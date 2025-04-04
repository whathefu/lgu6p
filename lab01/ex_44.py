operations = {
    '+' : lambda x, y: x + y,
    '-' : lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "오류: 0으로 나눌 수 없습니다"
}

x = int(input("첫번째 숫자를 입력하세요 :"))
y = int(input("두번째 숫자르 입력하세요: "))
op = input("연산자를 입력하세요(+,-,*,/): ")


# for i in operations :
#     i = input("연산자를 입력하세요(+,-,*,/): ")
#     print(operations[i],(x,y))

if op in ['+','-','*','/']:
    result = operations[op](x,y)
    print(result)
else : 
    print("올바른 연산이 아닙니다. ")