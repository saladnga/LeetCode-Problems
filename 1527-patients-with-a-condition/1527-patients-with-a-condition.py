import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    type1 = r'(^| )DIAB1' #Exclude signs and words
    return patients.loc[patients["conditions"].str.contains(type1)]