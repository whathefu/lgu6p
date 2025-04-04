
import random

class Linear :
    def __init__(self, in_feature, out_feature):
        # self.weight =[
        #     [random.random(), random.random()],
        #     [random.random(), random.random()],
        #     [random.random(), random.random()]
        # ]
        self.in_feature = in_feature
        self.out_feature = out_feature
        
        self.weight = [
            [random.random() for _ in range(out_feature)]
            for _ in range(in_feature)
        ]
        self.bias = [random.random(), random.random()] # out_feature개

    def matmul(self, A, B):
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

     
        #행렬곱 A,B를 해서 
        #결과행렬 C를 반환

    def foward(self, x):
        #x * self.weight + self.bias
        Z = self.matmul(x, self.weight)
        y = Z + self.bias
        # print(Z)
        for i in range(len(Z)):
            for j in range(len(self.bias)):
                Z[i][j] = Z[i][j] + self.bias[j]


        return Z

linear = Linear(4,2)
x= [[1,2,3],
    [4,5,6]]

print(linear.forward(x)) 
#결과는 2행 2열

import numpy as np

x_np = np.array(x)
W_np = np.array(linear.weight)
b_np = np.array(linear.bias)

y_np = np.dot(x_np, W_np)+ b_np
print(y_np)
