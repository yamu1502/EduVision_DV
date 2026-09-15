import pandas as pd
import os

os.makedirs("data/cleaned", exist_ok=True)

# 1. Nuvvu unna exact file peru tho chaduvadam
qs = pd.read_csv("data/raw/qs_rankings.csv")
the = pd.read_csv("data/raw/the_rankings.csv")

print("1. Data load ayindi")
print("QS rows:", qs.shape[0], " THE rows:", the.shape[0])

# 2. Columns ni clean cheyyadam
qs.columns = [c.strip().lower().replace(" ", "_") for c in qs.columns]
the.columns = [c.strip().lower().replace(" ", "_") for c in the.columns]

# 3. University column ni rename cheyyadam
qs = qs.rename(columns={'institution_name': 'university_name'})
the = the.rename(columns={'name': 'university_name'})

# 4. Country column ni rename
qs = qs.rename(columns={'country': 'country'})
the = the.rename(columns={'location': 'country'})

# 5. Merge cheyyadam
merged = pd.merge(qs, the, on="university_name", how="outer", suffixes=('_qs', '_the'))

print("2. Merged rows:", len(merged))

# 6. Save cheyyadam
merged.to_csv("data/cleaned/merged_rankings.csv", index=False)
print("3. SUCCESS! File saved: data/cleaned/merged_rankings.csv")
