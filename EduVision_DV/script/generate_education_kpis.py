import pandas as pd
import os

os.makedirs("data/cleaned", exist_ok=True)

qs = pd.read_csv("data/raw/qs_rankings.csv")
the = pd.read_csv("data/raw/the_rankings.csv")

qs.columns = [c.strip().lower().replace(" ", "_") for c in qs.columns]
the.columns = [c.strip().lower().replace(" ", "_") for c in the.columns]

qs = qs.rename(columns={'institution_name': 'university_name'})
the = the.rename(columns={'name': 'university_name'})

merged = pd.merge(qs, the, on="university_name", how="outer", suffixes=('_qs', '_the'))
merged.to_csv("data/cleaned/merged_rankings.csv", index=False)

print("SUCCESS! merged_rankings.csv created")