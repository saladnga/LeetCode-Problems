import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    filtered = employees.groupby(["emp_id", "event_day"]).sum()
    filtered["total_time"] = filtered["out_time"] - filtered["in_time"]
    filtered = filtered.reset_index()
    filtered = filtered.rename(columns={"event_day": "day"})
    return filtered[["day", "emp_id", "total_time"]]