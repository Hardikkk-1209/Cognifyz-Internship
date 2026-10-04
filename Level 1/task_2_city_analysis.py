import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--data", default="../../data/Dataset.csv")
args = parser.parse_args()
df = pd.read_csv(args.data)

city_counts = df["City"].value_counts()
average_ratings = df.groupby("City")["Aggregate rating"].mean().sort_values(ascending=False)
highest_count_city = city_counts.idxmax()
highest_rating_city = average_ratings.idxmax()
result = average_ratings.reset_index()
result.columns = ["City", "Average Rating"]
print(f"City with highest number of restaurants: {highest_count_city}")
print(f"Number of restaurants: {city_counts.loc[highest_count_city]}")
print(f"City with highest average rating: {highest_rating_city}")
print(f"Average rating: {average_ratings.loc[highest_rating_city]:.2f}")
result.to_csv("level1_task2_city_average_ratings.csv", index=False)
