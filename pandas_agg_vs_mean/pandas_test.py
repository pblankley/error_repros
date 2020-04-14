import pandas as pd
import numpy as np

data = pd.DataFrame({
    'cat': ['cat_1', 'cat_1', 'cat_2', 'cat_1', 'cat_2', 'cat_1', 'cat_2', 'cat_1'],
    'num': [5,20,22,3,4,30,10,50],
    'date': ['2019-2-1', '2018-02-03','2020-3-11','2019-2-2', '2019-2-2', '2018-12-4','2020-3-11', '2020-12-12']
})
data['date'] = pd.to_datetime(data['date'])
using_agg = data.groupby('cat').resample('Y', on='date').agg({'num': 'mean'})
using_mean = data.groupby('cat').resample('Y', on='date').mean()

assert(np.allclose(using_agg['num'], using_mean['num']))

print(pd.show_versions())
