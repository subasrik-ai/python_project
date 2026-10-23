import pandas as pd



customers = pd.DataFrame({
    "customer_id": [101, 102, 103, 105],
    "name": ["Arun", "Priya", "Rahul", "Divya"],
    "city": ["Chennai", "Mumbai", "Chennai", "Bangalore"]
})


customers.to_csv("customers.csv", index=False)


orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5],
    "customer_id": [101, 102, 103, 101, 104],
    "amount": [500, 700, 300, 900, 400]
})


customers = pd.read_csv("customers.csv")


inner = pd.merge(orders, customers, on="customer_id", how="inner")
print("Inner join rows:", len(inner))
print(inner)



left = pd.merge(customers, orders, on="customer_id", how="left")
no_orders = left[left["order_id"].isna()]


print("\nNo orders:", ", ".join(no_orders["name"]))


outer = pd.merge(
    orders, customers,
    on="customer_id",
    how="outer",
    indicator=True
)


unmatched_orders = outer[outer["_merge"] == "left_only"]


print("Order without customer: customer_id",
      int(unmatched_orders.iloc[0]["customer_id"]))


january = pd.DataFrame({
    "order_id": [1, 2],
    "customer_id": [101, 102],
    "amount": [500, 700]
})


february = pd.DataFrame({
    "order_id": [3, 4],
    "customer_id": [101, 103],
    "amount": [300, 600]
})


all_orders = pd.concat([january, february], ignore_index=True)


print("\nTotal orders by customer:")
print(all_orders.groupby("customer_id")["amount"].sum())

