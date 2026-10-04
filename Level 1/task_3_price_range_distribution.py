import argparse
import pandas as pd
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--data", default="../../data/Dataset.csv")
args = parser.parse_args()
df = pd.read_csv(args.data)

distribution = df["Price range"].value_counts().sort_index()
result = pd.DataFrame({"Price Range": distribution.index, "Restaurant Count": distribution.values, "Percentage": (distribution / len(df) * 100).round(2).values})
print(result.to_string(index=False))
ax = distribution.plot(kind="bar", title="Restaurant Price Range Distribution")
ax.set_xlabel("Price Range")
ax.set_ylabel("Number of Restaurants")
plt.tight_layout()
plt.savefig("level1_task3_price_range_distribution.png", dpi=180)
plt.close()
result.to_csv("level1_task3_price_range_distribution.csv", index=False)
