import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    mask = employee['salary'] == employee.groupby('departmentId')['salary'].transform('max')
    res = employee[mask].copy()
    res = res.merge(
        department,
        left_on='departmentId',
        right_on='id',
        suffixes=('_emp', '_dept')
    )
    res = res.rename(columns={'name_emp': 'Employee', 'name_dept': 'Department', 'salary': 'Salary'})
    return res[['Department', 'Employee', 'Salary']]