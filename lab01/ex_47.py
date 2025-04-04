import pandas as pd

df = pd.read_excel("./data/scores.xlsx")

# print( df.to_dict() )

df = df.T.to.dict()
data = [v for k, v in df.items()]
print(data)