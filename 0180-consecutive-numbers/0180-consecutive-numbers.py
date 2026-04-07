import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    res=set()
    for k,g in groupby(list(logs['num'])):
        if len(list(g))>=3:
            res.add(k)

    return pd.DataFrame({'ConsecutiveNums': list(res)})