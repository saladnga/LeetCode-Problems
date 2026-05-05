import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee['salary'].drop_duplicates().sort_values(ascending=False)
    if len(df) < 2:
        return pd.DataFrame({f"SecondHighestSalary": [None]})
    else:
        result = df.iloc[1]
        return pd.DataFrame({f"SecondHighestSalary": [result]})