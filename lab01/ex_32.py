teams = ['타이거즈', '라이온즈', '트윈스', '베어스', '위즈',
         '랜더스', '자이언츠', '이글스', '다이노스즈', '히어로즈']

i=0
for team in teams:
    print(i+1,team)
    i += 1

for i, team in enumerate(teams) : 
    print(f"{i+1}위 {team}")