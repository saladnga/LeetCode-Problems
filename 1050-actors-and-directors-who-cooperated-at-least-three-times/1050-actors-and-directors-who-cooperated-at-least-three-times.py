import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    res = actor_director.groupby(['actor_id', 'director_id'])['timestamp'].nunique().reset_index()
    return res.loc[(res['timestamp'] >= 3), ['actor_id', 'director_id']]