import pandas as pd

files = {
    "fund master.csv.xlsx": "fund_master_clean.csv",
    "aum by fund house.csv.xlsx": "aum_by_fund_house_clean.csv",
    "monthly sip inflows.csv.xlsx": "monthly_sip_inflows_clean.csv",
    "category inflows.csv.xlsx": "category_inflows_clean.csv",
    "industry folio count.csv.xlsx": "industry_folio_count_clean.csv",
    "portofolio holdings.csv.xlsx": "portfolio_holdings_clean.csv",
    "bench mark indices.csv.xlsx": "benchmark_indices_clean.csv"
}

for source, output in files.items():
    df = pd.read_excel(f"data/raw/{source}")
    df.to_csv(f"data/processed/{output}", index=False)

print("All cleaned files saved.")