import pandas as pd

name_file = "vacancies_medium.csv"
dataframe = pd.read_csv(name_file, on_bad_lines='skip')
dataframe["years"] = dataframe["published_at"].apply(lambda date: int(date[:4]))
all_years = list(dataframe["years"].unique())
for year in all_years:
    data = dataframe[dataframe["years"] == year]
    data.iloc[:, :6].to_csv(f"csv_files\\year_{year}.csv", index=False)