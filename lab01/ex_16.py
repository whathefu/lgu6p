x= float(input("x :"))
mu =float(input("mu :"))
a =float(input("a :"))

e = 2.718
p = 2.506
y1 = (1 / (a * p)) * e ** ((-(x-mu)**2)/(2*a*a))
print(f'{y1:.3f}')