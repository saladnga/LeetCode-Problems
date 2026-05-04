import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    res = employees.merge(employee_uni, left_on='id', right_on='id', how='outer')
    return res.loc[res['name'].notnull(), ['unique_id', 'name']]