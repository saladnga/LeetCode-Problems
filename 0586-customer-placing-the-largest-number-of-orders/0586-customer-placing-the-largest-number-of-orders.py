import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders['order_count'] = orders.groupby('customer_number')['order_number'].transform('count')
    return orders.loc[(orders['order_count'] == orders['order_count'].max()), ['customer_number']].drop_duplicates()