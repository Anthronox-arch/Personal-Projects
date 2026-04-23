import pandas as pd

# https://www.football-data.co.uk/mmz4281/2122/E0.csv

root = "https://www.football-data.co.uk/mmz4281/"

leagues = ['E0', 'E1', 'E2']

dict_countries = {
                   "England Premier" : "E0",
                   "Scotland Division" : "SC0",
                   "Germany Bundesliga" : "D1"
                 }

dict_all_data = {}

for league in dict_countries:
    csv_data_list = []
    
    for season in range(15, 21):
        df_football = pd.read_csv(root + str(season) + str(season + 1) + '/' + dict_countries[league] + '.csv', encoding = 'unicode_escape')
        df_football.insert(1, 'Season', str(season))
        csv_data_list.append(df_football)
        
    df_concatenated = pd.concat(csv_data_list)
    dict_all_data[league] = df_concatenated

# print(dict_all_data)

# Loop through the dictionary and export each DataFrame
for league_name, df in dict_all_data.items():
    # Clean up the name for a filename (remove spaces)
    filename = f"{league_name.replace(' ', '_')}_data.csv"
    
    # Export to CSV
    df.to_csv(filename, index=False)
    print(f"Exported: {filename}")