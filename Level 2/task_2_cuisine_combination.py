import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--data", default="../../data/Dataset.csv")
args = parser.parse_args()
df = pd.read_csv(args.data)

valid = df[df["Cuisines"].notna()].copy()
combo_counts = valid["Cuisines"].str.strip().value_counts().head(15)
combo_ratings = valid.groupby("Cuisines")["Aggregate rating"].agg(["count", "mean"]).loc[combo_counts.index].sort_values("mean", ascending=False)
print("Most common cuisine combinations:")
print(combo_counts.to_string())
print("\nRatings for the most common combinations:")
print(combo_ratings.round(2).to_string())
combo_counts.to_csv("level2_task2_common_cuisine_combinations.csv")
combo_ratings.to_csv("level2_task2_cuisine_combination_ratings.csv")
