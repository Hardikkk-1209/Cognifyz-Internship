import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--data", default="../../data/Dataset.csv")
args = parser.parse_args()
df = pd.read_csv(args.data)

bins = [0, 1, 2, 3, 4, 5]
labels = ["0-1", "1-2", "2-3", "3-4", "4-5"]
rating_ranges = pd.cut(df["Aggregate rating"], bins=bins, labels=labels, right=True, include_lowest=True)
distribution = rating_ranges.value_counts().sort_index()
result = pd.DataFrame({"Rating Range": distribution.index.astype(str), "Restaurant Count": distribution.values})
print(result.to_string(index=False))
print(f"Most common rating range: {distribution.idxmax()}")
print(f"Average number of votes: {df['Votes'].mean():.2f}")
result.to_csv("level2_task1_rating_distribution.csv", index=False)
