import argparse
import pandas as pd
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--data", default="../../data/Dataset.csv")
args = parser.parse_args()
df = pd.read_csv(args.data)

sample = df.sample(min(len(df), 5000), random_state=42)
plt.figure(figsize=(9, 6))
plt.scatter(sample["Longitude"], sample["Latitude"], s=8, alpha=0.35)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Restaurant Geographic Distribution")
plt.tight_layout()
plt.savefig("level2_task3_restaurant_locations.png", dpi=180)
plt.close()
clustered = df.groupby(["City", "Country Code"]).size().sort_values(ascending=False).head(15)
print("Largest restaurant clusters by city:")
print(clustered.to_string())
clustered.to_csv("level2_task3_city_clusters.csv")
