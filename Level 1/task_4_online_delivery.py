import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--data", default="../../data/Dataset.csv")
args = parser.parse_args()
df = pd.read_csv(args.data)

delivery_counts = df["Has Online delivery"].value_counts()
delivery_percentages = delivery_counts / len(df) * 100
average_ratings = df.groupby("Has Online delivery")["Aggregate rating"].mean().round(2)
result = pd.DataFrame({"Online Delivery": average_ratings.index, "Average Rating": average_ratings.values, "Percentage of Restaurants": [round(delivery_percentages.get(k, 0), 2) for k in average_ratings.index]})
print(result.to_string(index=False))
result.to_csv("level1_task4_online_delivery.csv", index=False)
