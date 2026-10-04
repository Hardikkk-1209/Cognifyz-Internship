import argparse
import pandas as pd
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--data", default="../../data/Dataset.csv")
args = parser.parse_args()
df = pd.read_csv(args.data)

services = df.groupby("Price range").apply(lambda x: pd.Series({"Online Delivery %": x["Has Online delivery"].eq("Yes").mean() * 100, "Table Booking %": x["Has Table booking"].eq("Yes").mean() * 100})).reset_index()
print(services.round(2).to_string(index=False))
services.to_csv("level3_task3_price_vs_services.csv", index=False)
ax = services.set_index("Price range")[["Online Delivery %", "Table Booking %"]].plot(kind="bar")
ax.set_xlabel("Price Range")
ax.set_ylabel("Percentage of Restaurants")
ax.set_title("Price Range vs Service Availability")
plt.tight_layout()
plt.savefig("level3_task3_price_vs_services.png", dpi=180)
plt.close()
