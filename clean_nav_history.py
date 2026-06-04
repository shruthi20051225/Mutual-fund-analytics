# clean_nav_history.py

import pandas as pd

df = pd.read_excel("data/raw/nav history.csv.xlsx")

print("Original Shape:", df.shape)

# Date parsing
df["date"] = pd.to_datetime(df["date"])

# Sort
df = df.sort_values(
    ["amfi_code", "date"]
)

# Remove duplicates
df = df.drop_duplicates()

# Forward fill NAV per scheme
df["nav"] = (
    df.groupby("amfi_code")["nav"]
    .ffill()
)

# Validation
invalid_nav = df[df["nav"] <= 0]

print("Invalid NAV rows:", len(invalid_nav))

# Save
df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("Saved Successfully")