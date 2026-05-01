import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merge = pd.merge(customers, orders, how='outer', left_on="id", right_on="customerId")
    return merge.loc[(merge["customerId"]).isna(), ["name"]].rename(columns={"name": "Customers"})