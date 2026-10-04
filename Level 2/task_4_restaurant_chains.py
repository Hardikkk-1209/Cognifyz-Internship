import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--data", default="../../data/Dataset.csv")
args = parser.parse_args()
df = pd.read_csv(args.data)

name_counts = df["Restaurant Name"].value_counts()
chains = name_counts[name_counts > 1]
chain_stats = df[df["Restaurant Name"].isin(chains.index)].groupby("Restaurant Name").agg(Locations=("Restaurant ID", "count"), Average_Rating=("Aggregate rating", "mean"), Total_Votes=("Votes", "sum")).sort_values(["Locations", "Total_Votes"], ascending=False)
print(chain_stats.head(20).round(2).to_string())
chain_stats.to_csv("level2_task4_restaurant_chains.csv")
