# clean_investor_transactions.py

import pandas as pd

df = pd.read_excel(
    "data/raw/investor transcations.csv.xlsx"
)

print("Original Shape:", df.shape)

# Standardize transaction types

df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

mapping = {
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
}

df["transaction_type"] = (
    df["transaction_type"]
    .replace(mapping)
)

# Date format
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Amount validation
df = df[df["amount_inr"] > 0]

# KYC Validation
valid_kyc = [
    "Verified",
    "Pending"
]

invalid = df[
    ~df["kyc_status"].isin(valid_kyc)
]

print("Invalid KYC:", len(invalid))

df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Saved Successfully")