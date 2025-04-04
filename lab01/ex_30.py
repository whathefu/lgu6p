
n=5

for i in range(n) :
    star = ''
    space = ''

    for j in range(n-i-1):
        space += ' '

    for k in range(i*2+1):
        star += '*'

    row = space + star 
    print(row)