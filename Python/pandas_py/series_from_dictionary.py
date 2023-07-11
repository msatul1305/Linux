import pandas as pd
dict_info = {'key1': 2.0, 'key2': 3.1, 'key3': 2.2}
series_obj = pd.Series(dict_info)
print(series_obj)
# Output:
# x     2.0
# y     3.1
# z     2.2
# dtype: float64
