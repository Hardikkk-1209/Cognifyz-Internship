import argparse
import pandas as pd
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--data", default="../../data/Dataset.csv")
args = parser.parse_args()
df = pd.read_csv(args.data)

highest = df.loc[df["Votes"].idxmax(), ["Restaurant Name", "City", "Votes", "Aggregate rating"]]
lowest = df.loc[df["Votes"].idxmin(), ["Restaurant Name", "City", "Votes", "Aggregate rating"]]
correlation = df[["Votes", "Aggregate rating"]].corr().iloc[0, 1]
print("Restaurant with highest votes:")
print(highest.to_string())
print("\nRestaurant with lowest votes:")
print(lowest.to_string())
print(f"\nCorrelation between votes and rating: {correlation:.4f}")
plt.figure(figsize=(8, 6))
plt.scatter(df["Votes"], df["Aggregate rating"], s=8, alpha=0.25)
plt.xlabel("Votes")
plt.ylabel("Aggregate Rating")
plt.title("Votes vs Restaurant Rating")
plt.tight_layout()
plt.savefig("level3_task2_votes_vs_rating.png", dpi=180)
plt.close()
pd.DataFrame({"Highest Votes": highest, "Lowest Votes": lowest}).to_csv("level3_task2_extreme_votes.csv")
