import pandas as pd
import cufflinks as cf
from IPython.display import display, HTML
import numpy as np


alpha = np.float64(1.0)
color = f'rgba(226, 74, 51, {float(alpha)})'


cf.set_config_file(sharing = 'public', theme = 'ggplot', offline = True)

df_population_raw = pd.read_csv(r"D:\Applications\Thonny\Datasets\population_total.csv")

df_population_raw = df_population_raw.dropna()

df_pivot = df_population_raw.pivot(index = 'year', columns = 'country', values = 'population')

df_pivot = df_pivot[['United States', 'Pakistan', 'India', 'China', 'Germany']]

# Lineplot

print(df_pivot.iplot(kind = 'line'))
