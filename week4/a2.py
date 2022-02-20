import pandas as pd

df1 = pd.DataFrame([["cherry", "Fruit", 100],
                    ["mango", "Fruit", 100],
                    ["potato", "Vegetable", 60],
                    ["onion", "Vegetable", 80]],
                    columns=["Name", "Type", "Price"]
                    )
df2 = pd.DataFrame([["pepper", "Vegetable", 50],
                    ["carrot", "Vegetable", 70],
                    ["banana", "Fruit", 120],
                    ["kiwi", "Fruit", 120]],
                    columns=["Name", "Type", "Price"]
                    )

df3 = pd.concat([df1, df2])

df_fruit = df3.loc[df3["Type"] == "Fruit"].sort_values(by = "Price", ascending = False)
df_veg = df3.loc[df3["Type"] == "Vegetable"].sort_values(by = "Price", ascending = False) 

sum_fruit = sum(df_fruit[:2]["Price"])
sum_veg = sum(df_veg[:2]["Price"])

print(f"Sum of top 2 fruit price : {sum_fruit}")
print(f"Sum of top 2 vegetable price : {sum_veg}")