import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[a-zA-Z][\w\.-]*@leetcode\.com$'
    return users.loc[users["mail"].str.contains(pattern, regex=True)]