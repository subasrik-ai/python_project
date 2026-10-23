import pandas as pd


data = """order_id,customer_id,amount
1,101,500
2,102,
3,101,700
3,101,700
4,103,300
5,104,900
"""


with open("orders.csv", "w") as file:
    file.write(data)



df = pd.read_csv("orders.csv")



print("Missing:", "amount", df["amount"].isna().sum(),
      "| Duplicates:", df.duplicated().sum())


df = df.drop_duplicates()



median_value = df["amount"].median()
print("Median used:", median_value)



df["amount"] = df["amount"].fillna(median_value)


df["amount"] = pd.to_numeric(df["amount"])
df["order_id"] = df["order_id"].astype(str)



result = df.groupby("customer_id").agg(
    total=("amount", "sum"),
    orders=("order_id", "count")
)


print(result)