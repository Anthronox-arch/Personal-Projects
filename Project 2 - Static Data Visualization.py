import pandas as pd
import matplotlib.pyplot as plt

df_population_raw = pd.read_csv(r"D:\Applications\Thonny\Datasets (Nexskill)\population_total.csv")
df_population_raw = df_population_raw.dropna()
df_population_reshaped = df_population_raw.pivot(index = 'year', columns = 'country', values = 'population')
df_countries = df_population_reshaped[['United States', 'Pakistan', 'China', 'India', 'Malaysia']]

# Lineplot

df_countries.plot(kind = 'line', xlabel = 'Year', ylabel = 'Population', title = "Countries and their Populations (1955 - 2020)", figsize = (8, 4))
plt.show()

# Barplot

df_year_2020 = df_countries[df_countries.index.isin([2020])]
# For barplot, index should be alphabets.
df_year_2020 = df_year_2020.T
df_years = df_countries[df_countries.index.isin([1980, 1990, 2000, 2010, 2020])]
df_years.plot(kind = 'bar')
plt.show()

# Piechart

df_year_2020 = df_countries[df_countries.index.isin([2020])]
df_year_2020 = df_year_2020.T
df_year_2020 = df_year_2020.rename(columns = {2020 : '2020'})
# Change from integer to string. Bad practice to have integers in columns.
df_year_2020.plot(kind = 'pie', y = '2020')
plt.show()

# Boxplot

df_countries['Pakistan'].plot(kind = 'box')
df_countries.plot(kind = 'box')
plt.show()

# Histogram
df_countries[['Pakistan', 'China']].plot(kind = 'hist')
plt.show()

# Scatterplot

df_sample = df_population_raw[df_population_raw['country'].isin(['China', 'Pakistan', 'Indonesia', 'Brazil', 'India'])]
df_sample.plot(kind = 'scatter', x = 'year', y = 'population')
plt.show()