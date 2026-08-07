import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    mask = users['mail'].str.match(r'^[a-zA-Z]+[\w.\-]*@leetcode\.com$', na=False)
    return users.loc[mask, users.columns].reset_index(drop=True)