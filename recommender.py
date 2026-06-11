import pandas as pd

df = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

risk = input(
    "Risk Appetite (Low/Moderate/High): "
)

filtered = df[
    df["risk_grade"]
    .str.contains(risk, case=False)
]

result = filtered.sort_values(
    "sharpe_ratio",
    ascending=False
).head(3)

print(result[
    [
        "scheme_name",
        "risk_grade",
        "sharpe_ratio"
    ]
])