import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee = employee[employee['salary'] == employee.groupby('departmentId')['salary'].transform('max')]
    employee = employee.rename(columns={'name': 'Employee', 'salary': 'Salary'})
    employee = employee.merge(department, left_on='departmentId', right_on='id')
    employee = employee.rename(columns={'name': 'Department'})
    return employee[['Department', 'Employee', 'Salary']]