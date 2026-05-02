import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    res = activities.groupby('sell_date').agg(
        num_sold=('product', 'nunique'), # Count number sold
        products=('product', lambda x: ",".join(sorted(x.unique()))) # Merge product into products
    ).reset_index()
    return res