import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee['salary'].drop_duplicates().sort_values(ascending=False)
    if N <= 0 or N > len(employee):
        return pd.DataFrame({f"getNthHighestSalary({N})":[None]})
    else:
        result = employee.iloc[N - 1]
        return pd.DataFrame({f"getNthHighestSalary({N})":[result]})