import pandas as pd

idx = ["Sue", "Ryan", "Jay", "Jane", "Anna"]
col = ["round_1", "round_2", "round_3", "round_4", "round_5"]
data = [[55, 65, 68, 66, 57],
        [64, 77, 71, 79, 67],
        [88, 81, 79, 89, 77],
        [45, 35, 30, 46, 47],
        [91, 96, 90, 97, 90]]

df = pd.DataFrame(data, index = idx, columns = col)

df["round_6"] = [11, 15, 13, 17, 19]

print(df.describe().loc[["mean", "max", "min"]])