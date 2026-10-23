import pandas as pd


data = {
    "order_id": [1,2,3,4,5],
    "customer_id": [101,102,101,103,104],
    "amount":[500,None,700,300,900]
}
df= pd.DataFrame(data)
df.to_csv("orders.csv",index=False)

#load the csv file
df=pd.read_csv("orders.csv")

# find missing values and duplicates
print("missing:",df["amount"].isna().sum(),
      "duplicates:",df.duplicated().sum())

#remove duplicate rows
df=df.drop_duplicates()

# fill missing amount with the median
median_value=df["amount"].median()
df["amount"]=df["amount"].fillna(median_value)

print("median used:",median_value)

#convert data types
df["amount"]=df["amount"].astype(float)
df["order_id"]=df["order_id"].astype(str)

#group by customer and aggregate
result=df.groupby("customer_id").agg(
      total=("amount","sum"),
      orders=("order_id","count")
)
print(result)
