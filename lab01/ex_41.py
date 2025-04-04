# f = int(input("수 : "))

# def mean(l) :
#         n = len(l)
#         s = sum(l)
#         # S = 0
#         # count = 0
#         # for i in l:
#         #       S+=i
#         m = s / n
#         return m

# avg = mean([1,2,3])
# print(avg)
# print

def mean(l):
    S = 0
    for k in range(len(l)) :
        x_k = l[k]
        S += x_k

    N = len(l)
    m = S/N
    
    return m 

avg = mean([1,2,3,4,5,6])
print(avg)