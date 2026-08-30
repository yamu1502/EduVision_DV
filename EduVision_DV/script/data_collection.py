import pandas as pd
import os

os.makedirs("data/cleaned", exist_ok=True)

# 1. Rendu files chaduvadam
qs = pd.read_csv("data/raw/qs_rankings.csv")
the = pd.read_csv("data/raw/the_rankings.csv")

print("1. Data load ayindi")
print("QS rows:", qs.shape[0], " THE rows:", the.shape[0])

# 2. Columns ni clean cheyyadam
qs.columns = [c.strip().lower().replace(" ", "_") for c in qs.columns]
the.columns = [c.strip().lower().replace(" ", "_") for c in the.columns]

print("\nQS Columns:", list(qs.columns))
print("THE Columns:", list(the.columns))

# 3. Correct column peru tho rename cheyyadam
qs = qs.rename(columns={'institution_name': 'university_name'})
the = the.rename(columns={'name': 'university_name'})

# 4. Country columns kuda rename
qs = qs.rename(columns={'country': 'country'})
the = the.rename(columns={'location': 'country'})

print("\n2. Columns renamed to 'university_name'")

# 5. Merge cheyyadam
merged = pd.merge(qs, the, on="university_name", how="outer", suffixes=('_qs', '_the'))

print("3. Merged rows:", len(merged))

# 6. Save cheyyadam
merged.to_csv("data/cleaned/merged_rankings.csv", index=False)
print("4. SUCCESS! File saved: data/cleaned/merged_rankings.csv")