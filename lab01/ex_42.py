X = [[78, 80, 95, 55, 67, 43], [45, 67, 90, 87, 88, 93]]

def mean(l):
    S = 0
    for k in range(len(l)) :
        x_k = l[k]
        S += x_k

    N = len(l)
    m = S/N
    
    return m 

for i in X : 
    m = mean(i)
    print(m)
    