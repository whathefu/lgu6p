operations = {
    '+' : lambda x, y: x + y,
    '-' : lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y }

x = int(input("첫번째 숫자를 입력하세요 :"))
y = int(input("두번째 숫자르 입력하세요: "))
op = input("연산자를 입력하세요(+,-,*,/): ")
result = operations[op](x,y)
print(result)

try : 
    x = int(input("첫번째 숫자를 입력하세요 :"))
    y = int(input("두번째 숫자르 입력하세요: "))
    op = input("연산자를 입력하세요(+,-,*,/): ")
    result = operations[op](x,y)
    print(result)
    

except ZeroDivisionError as e:
    print("오류: 0으로 나눌 수 없습니다.")
    print(e)

except ValueError as e:
    print("입력 값을 확인하세요.")
    print(e)

except KeyError as e :
    print("연산자는 +,-,*,/ 만 사용")
    print(e)

except Exception as e:
    print("알수 없는 오류")
    print(e)
finally:
    print("프로그램 종료")