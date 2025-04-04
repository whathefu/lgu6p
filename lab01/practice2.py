import ex_45
import os
input_files = os.listdir('./data')

for file in input_files:
    for file in input_files:
        if file[-3:]=='txt':
            print(file)
            scores = []
            with open(f"./data/{file}", 'r',encoding='utf-8')as f:
                lines = f.readlines()
                for line in lines:
                    scores.append(int(line))
                print(scores)
                print(ex_45.mean(scores))