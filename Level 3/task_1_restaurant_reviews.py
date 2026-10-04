import argparse
import re
from collections import Counter
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--data", default="../../data/Dataset.csv")
args = parser.parse_args()
df = pd.read_csv(args.data)

texts = df["Rating text"].fillna("").astype(str)
word_pattern = re.compile(r"[A-Za-z]+")
stopwords = {"the", "and", "for", "with", "this", "that", "was", "were", "are", "but", "not", "very", "good", "bad", "has", "have", "had", "too", "from", "they", "you", "restaurant", "rating", "no", "its", "one", "all"}

def keywords(rows):
    words = []
    for value in rows:
        words.extend(w.lower() for w in word_pattern.findall(value))
    return Counter(w for w in words if len(w) > 2 and w not in stopwords)

positive = keywords(texts[df["Rating text"].isin({"Excellent", "Very Good", "Good"})])
negative = keywords(texts[df["Rating text"].isin({"Poor"})])
df["Review Length"] = texts.str.len()
correlation = df[["Review Length", "Aggregate rating"]].corr().iloc[0, 1]
print("Positive keywords:", positive.most_common(15))
print("Negative keywords:", negative.most_common(15))
print(f"Average review length: {df['Review Length'].mean():.2f} characters")
print(f"Review length vs rating correlation: {correlation:.4f}")
pd.DataFrame(positive.most_common(15), columns=["Keyword", "Count"]).to_csv("level3_task1_positive_keywords.csv", index=False)
pd.DataFrame(negative.most_common(15), columns=["Keyword", "Count"]).to_csv("level3_task1_negative_keywords.csv", index=False)
