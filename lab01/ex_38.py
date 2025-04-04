data = [
    {'name':'철수', 'math':85, 'eng':90, 'sci':75},
    {'name':'준호', 'math':73, 'eng':85, 'sci':75},
    {'name':'영희', 'math':92, 'eng':88, 'sci':75}
    ]
result ={}

for i in data:
     hap =i['math']+i['eng']+i['sci']
     nom = hap/3
     result =[hap,nom]

     print(i['name'])
     print(result)

     result[i['name']] = result

print(result)

#      result[i['name'] ] = result


