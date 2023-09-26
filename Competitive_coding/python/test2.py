import pandas as pd
df = pd.DataFrame([[2,5],
                  [56,20]],
                  index = list('pq'),
                  columns=list('ab'))


def loc(a,b):
    try:
        out=df.loc[a,b]
    except:
        return 0
    return out


def iloc(a,b):
    try:
        out=df.iloc[a,b]
    except:
        return 0
    return out

print(iloc(0, 'b'))
print(loc(0, 'b'))
print(loc('q', 'a'))
print(iloc('q', 'b'))

