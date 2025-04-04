# A=[1,2,3,4]
# B=[4,5,6,7]

# c=0
# for i in range(len(A)):
#     c += A[i]*B[i]
# print(c)

A=[[1,0,1,2],
   [0,2,0,3],
   [1,2,1,7]]
B=[[2,3],
   [0,1],
   [1,1],
   [3,2]]

row = len(A)
col = len(B[0])

C=[]

for i in range(row) :
    temp = []
    for j in range(col) :
        temp.append(0)
    C.append(temp)

for i in range(len(A)) :
    for j in (len(B[0])) : 
        for k in range(len(A[0])) :
            C[i][j] += A[i][k]*B[k][j]
print(C)

                   