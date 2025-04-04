import ex_45

s = input("평균을 구할 숫자 입력하세요.")

print(s)
# s = s.replace(',',' ')
# L=s.split
# print(L)
print(
    ex_45.mean(
        [int(i) for i in s.replace(',',' ').split()]
    )
)



