import pandas as pd

idx = ["HDD", "SSD", "USB", "CLOUD"]
data = [19, 11, 5, 97]

series = pd.Series(data, index=idx)

series = series[(series >=10) & (series <=20)]

print(series)
