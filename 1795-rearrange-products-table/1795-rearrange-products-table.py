import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    df = products.melt(id_vars=['product_id'], value_vars=['store1', 'store2', 'store3']).dropna()
    df = df.rename(columns={'variable': 'store', 'value': 'price'})
    return df