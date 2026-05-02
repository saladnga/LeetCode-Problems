import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses = courses.groupby("class")["student"].nunique().reset_index()
    return courses.loc[(courses["student"] >= 5), ["class"]]