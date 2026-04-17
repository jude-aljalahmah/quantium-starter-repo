import pandas as pd
import os

# folder where CSVs are stored
data_folder = "data"

# list to store dataframes
dfs = []

# loop through all CSV files
for file in os.listdir(data_folder):
    if file.endswith(".csv"):
        path = os.path.join(data_folder, file)
        df = pd.read_csv(path)

        # keep only Pink Morsels
        df = df[df["product"] == "pink morsel"]

        # create sales column
        df["sales"] = df["quantity"] * df["price"]

        # keep only required columns
        df = df[["sales", "date", "region"]]

        dfs.append(df)

# combine all dataframes
final_df = pd.concat(dfs)

# save output
final_df.to_csv("output.csv", index=False)

print("Done! Output saved as output.csv")