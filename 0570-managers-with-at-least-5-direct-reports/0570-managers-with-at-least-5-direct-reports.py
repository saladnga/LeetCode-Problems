import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    count = employee.groupby('managerId').size().reset_index(name='reports')
    top_reports = count[count['reports'] >= 5]
    res = employee[['id', 'name']].merge(
        top_reports,
        left_on='id',
        right_on='managerId',
    )
    return res[['name']]