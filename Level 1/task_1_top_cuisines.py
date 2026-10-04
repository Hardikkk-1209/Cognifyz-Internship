import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--data", default="../../data/Dataset.csv")
args = parser.parse_args()
df = pd.read_csv(args.data)

cuisines = df["Cuisines"].dropna().str.split(", ").explode()
counts = cuisines.value_counts()
result = pd.DataFrame({"Cuisine": counts.head(3).index, "Restaurant Count": counts.head(3).values, "Percentage of Restaurants": (counts.head(3).values / len(df) * 100).round(2)})
print(result.to_string(index=False))
result.to_csv("level1_task1_top_cuisines.csv", index=False)
