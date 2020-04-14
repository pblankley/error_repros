import pandas as pd

data_url = 'https://drive.google.com/open?id=1j66Z6bYrlRN6jbvhko6zqR99uBfS3blO'
data = pd.read_csv(data_url)
print(data)
using_agg = data.groupby('Campaign ID').resample('Y', on='other date').agg({'Click Cost': 'mean'})
using_mean = data.groupby('Campaign ID').resample('Y', on='other date').mean()
diff = using_agg['Click Cost'] == using_mean['Click Cost']

print(diff)

# assert(np.allclose(using_agg['Click Cost'], using_mean['Click Cost']))

print(pd.show_versions())
