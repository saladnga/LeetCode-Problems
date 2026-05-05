import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.sort_values(by='score', ascending=False)
    scores["rank"] = 0
    curr_rank = 0
    prev_score = None
    for i in scores.index:
        curr_score = scores.loc[i, 'score']
        if prev_score != curr_score:
            curr_rank += 1
        scores.loc[i, 'rank'] = curr_rank
        prev_score = curr_score
    return scores[['score', 'rank']]
        
