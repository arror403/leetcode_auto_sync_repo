import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    res=[]
    p=re.compile('^[a-zA-Z]+[\w\.\-]*(@leetcode\.com){1}$')

    for _,r in users.iterrows():
        m=p.match(r['mail'])
        if m:
            res.append([r['user_id'], r['name'], r['mail']])


    return pd.DataFrame({
        'user_id': [x[0] for x in res],
        'name': [x[1] for x in res],
        'mail': [x[2] for x in res]
    })