from datetime import date

# 프로젝트를 완성하기 위해 별도 라이브러리 함수를 사용
# is_leap_year(year) 형식으로 호출하면 year가 윤년이면 True, 아니면 False를 반환
# get_month_days(year, month) 형식으로 호출하면 해당 month의 날 수를 반환
# Mission 1에서 완성되어야 함.
from days_utils import MONTH_DAYS, is_leap_year, get_month_days
def is_leap_year(year):
    if year %  4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
    
def get_month_days(year, month):
    # 달의 날짜 수에 +1해야되는 경우를 여기서 처리하시오.
    # if 문에서 year이 윤년인지는 이미 체크되고 있고 
    # month가 2월인지 추가로 체크하는 논리식을 and로 연결하시오.
    if is_leap_year(year) and (MONTH_DAYS[2]):
        # 이 함수가 전달받은 month 변수를 이용하여 
        # 모든 달의 날짜가 적혀있는 MONTH_DAYS에서 해당 달의 날짜를 
        # 조회 하시오.
        return MONTH_DAYS[2] + 1
    else:
        return MONTH_DAYS[month]



#####################################################################      
# Mission 2 : 두 특정 날짜의 차이를 계산하는 함수 
def my_days(birth_year, birth_month, birth_day, cur_year, cur_month, cur_day):
    # birth_year: 태어난 해
    # birth_month: 태어난 달
    # birth_day: 태어난 날
    # cur_year: 현재 해 또는 차이를 계산하고 싶은 특정 해
    # cur_month: 현재 달 또는 차이를 계산하고 싶은 특정 달
    # cur_day: 현재 날 또는 차이를 계산하고 싶은 특정 날

    #####################################################################      
    # step 1 : 태어난 해에 산 날 수를 구해서 days_part_1에 저장

    # birth_year에 산 날 수를 계산하여 이 변수에 저장
    days_part_1 = 0

    # 태어난 해의 태어난 달에 산 날 수를 계산해서 days_part_1에 저장
    # 태어난 당일은 포함하지 않는다.
    days_part_1 += MONTH_DAYS[birth_month] - birth_day 
    
    # birth_year가 윤년인지를 판단하고 윤년이면 +1
    # is_leap_year()를 사용하여 윤년인지 판단하시오.
    if birth_month == 2 and is_leap_year % 4 ==0 :
        days_part_1 += 1
    
    # 태어난 해의 태어난 달 다음달 부터 12월 31일까지 날을 계산해서
    # days_part_1에 더함
    # range에 적당한 범위를 설정하시오.
    for m in range(birth_month+1, 13):
        days_part_1 += get_month_days(birth_year, m)
    

    #####################################################################      
    # step 2: 태어난 해 다음 해 부터 현재 해 이전 해까지 산 날 수를 계산해서 
    #         days_part_2에 저장
    #         [!주의!] 반드시 윤년을 체크하여 반영하시오.
    days_part_2 = 0

    # 바깥 for 루프에서 년도를 y로 순회하고
    for y in range(birth_year+1, cur_year):
        # 안쪽 for 루프에서 y 년도의 달을 m으로 순회하면서 
        for m in range(1,13):
            # days_part_2에 y년 m월의 날 수를 합산
            days_part_2 += get_month_days(y, m)


    #####################################################################      
    # step 3: 현재 해 산 날 수를 계산해서 days_part_3에 저장
    #
    days_part_3 = 0

    # 1월 부터 현재 달 이전 달까지 산 날수를 모두 계산해서
    # days_part_3에 저장
    for m in range(cur_year, cur_month):
        days_part_3 += get_month_days(cur_year, m)
        
    # step 3: 현재 달의 산 날 수를 days_part_3에 더함
    days_part_3 += cur_day
    
    # 세 개 파트로 나눠서 계산한 날 수를 합산해서 반환하시오.
    return days_part_1 + days_part_2 + days_part_3
    #####################################################################      


#################################################################
# [!주의!] 이 함수의 코드를 수정하시 마시오.
# 검증 함수
# python의 datetime.date를 사용해서 정확한 날 수를 계산
# my_days()를 검증할 목적으로 사용
def true_days(birth_year, birth_month, birth_day, cur_year, cur_month, cur_day):
    d1 = date(birth_year, birth_month, birth_day)
    d2 = date(cur_year, cur_month, cur_day)
    delta = d2 - d1
    
    return delta.days 