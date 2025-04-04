score = [[90, 85, 93],
         [78, 92, 89]]

# print(score[0][1])

hap1 = 0
hap2 = 0

# for i in score[0] :
#     hap1 = hap1 + i
# for j in score[1] :
#     hap2 = hap2 + j
#     h= [hap1, hap2]
# print(f"지수의 총점은 {hap1}, 만수의 총점은 {hap2}") 

# for i in range(len(score)):
#     S=0
#     for j in range(len(score[0])):
#         S += score[i][j]
#     print(S)

# print("-------")


# for i in range(len(score[0])):
#     S=0
#     for j in range(len(score)):
#         S += score[j][i]
#     print(S)

for i in range(len(score)):
    S=0
    for j in range(len(score[0])):
        S += score[i][j]
    print(S)

    