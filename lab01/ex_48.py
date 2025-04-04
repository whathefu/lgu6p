# with open("file_w.txt","w",encoding="utf-8")as f :
#     f.write("안녕 파이썬")
#     f.write("Hello Python")

# with open("file_w.txt", "r", encoding='utf-8')as f:
#     lines = f.readline()
#     # print(lines, type(lines))
#     for lines in lines :
#         print(lines end='')

import ex_45
import os

input_files = os.listdir('./data')

with open('ex_48.txt', 'w')as fw:
    for file in input_files:
        # print(file,type(file), file[-3:])
        if file[-3:]=='txt':
            
            print(file)
            name = file[:-4]
            
            scores = []
            with open(f"./data/{file}", 'r', encoding='utf-8')as f:
                lines = f.readlines()
                lines = int(lines)

                for line in lines:
                    scores.append(int(line))
                    
                print(scores)
                # print(ex_45.mean(scores),ex_45.std(scores))
            m= ex_45.mean(scores)
            sigma = ex_45.std(scores)

            fw.write(f"{name}: {m}, {sigma}")






# if 1 :
#     with open(f"./data/jisoo.txt",'r' , encoding='utf-8') as f:
#         pass