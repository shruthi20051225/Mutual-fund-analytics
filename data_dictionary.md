# Mutual Fund Analytics Data Dictionary

## Dataset 1: Fund Master

Source: AMFI India

| Column Name        | Data Type | Description                        |
| ------------------ | --------- | ---------------------------------- |
| amfi_code          | Integer   | Unique AMFI scheme code            |
| fund_house         | Text      | Mutual fund company name           |
| scheme_name        | Text      | Mutual fund scheme name            |
| category           | Text      | Equity, Debt, Hybrid category      |
| sub_category       | Text      | Large Cap, Mid Cap, Small Cap etc. |
| plan               | Text      | Direct or Regular plan             |
| launch_date        | Date      | Scheme launch date                 |
| benchmark          | Text      | Benchmark index                    |
| expense_ratio_pct  | Float     | Expense ratio percentage           |
| exit_load_pct      | Float     | Exit load percentage               |
| min_sip_amount     | Integer   | Minimum SIP amount                 |
| min_lumpsum_amount | Integer   | Minimum lumpsum investment         |
| fund_manager       | Text      | Fund manager name                  |
| risk_category      | Text      | Risk level                         |
| sebi_category_code | Text      | SEBI category code                 |

---

## Dataset 2: NAV History

Source: MFAPI / AMFI

| Column Name | Data Type | Description     |
| ----------- | --------- | --------------- |
| amfi_code   | Integer   | Scheme code     |
| date        | Date      | NAV date        |
| nav         | Float     | Net Asset Value |

---

## Dataset 3: AUM by Fund House

Source: AMFI Quarterly Reports

| Column Name    | Data Type | Description       |
| -------------- | --------- | ----------------- |
| date           | Date      | Reporting date    |
| fund_house     | Text      | Fund house name   |
| aum_lakh_crore | Float     | AUM in lakh crore |
| aum_crore      | Integer   | AUM in crore      |
| num_schemes    | Integer   | Number of schemes |

---

## Dataset 4: Monthly SIP Inflows

Source: AMFI Monthly Notes

| Column Name               | Data Type | Description           |
| ------------------------- | --------- | --------------------- |
| month                     | Text      | Reporting month       |
| sip_inflow_crore          | Integer   | SIP inflow amount     |
| active_sip_accounts_crore | Float     | Active SIP accounts   |
| new_sip_accounts_lakh     | Float     | New SIP registrations |
| sip_aum_lakh_crore        | Float     | SIP AUM               |
| yoy_growth_pct            | Float     | Year-over-year growth |

---

## Dataset 5: Category Inflows

Source: AMFI

| Column Name      | Data Type | Description       |
| ---------------- | --------- | ----------------- |
| month            | Text      | Month             |
| category         | Text      | Fund category     |
| net_inflow_crore | Integer   | Net inflow amount |

---

## Dataset 6: Industry Folio Count

Source: AMFI

| Column Name         | Data Type | Description     |
| ------------------- | --------- | --------------- |
| month               | Text      | Reporting month |
| total_folios_crore  | Float     | Total folios    |
| equity_folios_crore | Float     | Equity folios   |
| debt_folios_crore   | Float     | Debt folios     |
| hybrid_folios_crore | Float     | Hybrid folios   |
| others_folios_crore | Float     | Other folios    |

---

## Dataset 7: Scheme Performance

Source: Computed from NAV History

| Column Name        | Data Type | Description           |
| ------------------ | --------- | --------------------- |
| amfi_code          | Integer   | Scheme code           |
| scheme_name        | Text      | Scheme name           |
| fund_house         | Text      | Fund house            |
| category           | Text      | Fund category         |
| plan               | Text      | Direct/Regular        |
| return_1yr_pct     | Float     | 1-year return         |
| return_3yr_pct     | Float     | 3-year return         |
| return_5yr_pct     | Float     | 5-year return         |
| benchmark_3yr_pct  | Float     | Benchmark return      |
| alpha              | Float     | Alpha measure         |
| beta               | Float     | Beta measure          |
| sharpe_ratio       | Float     | Sharpe ratio          |
| sortino_ratio      | Float     | Sortino ratio         |
| std_dev_ann_pct    | Float     | Annualized volatility |
| max_drawdown_pct   | Float     | Maximum drawdown      |
| aum_crore          | Integer   | AUM                   |
| expense_ratio_pct  | Float     | Expense ratio         |
| morningstar_rating | Integer   | Morningstar rating    |
| risk_grade         | Text      | Risk classification   |

---

## Dataset 8: Investor Transactions

Source: Simulated Investor Data

| Column Name        | Data Type | Description              |
| ------------------ | --------- | ------------------------ |
| investor_id        | Text      | Investor identifier      |
| transaction_date   | Date      | Transaction date         |
| amfi_code          | Integer   | Scheme code              |
| transaction_type   | Text      | SIP, Lumpsum, Redemption |
| amount_inr         | Integer   | Transaction amount       |
| state              | Text      | Investor state           |
| city               | Text      | Investor city            |
| city_tier          | Text      | Tier classification      |
| age_group          | Text      | Investor age group       |
| gender             | Text      | Gender                   |
| annual_income_lakh | Float     | Annual income            |
| payment_mode       | Text      | Payment method           |
| kyc_status         | Text      | KYC verification status  |

---

## Dataset 9: Portfolio Holdings

Source: Mutual Fund Portfolio Disclosures

| Column Name       | Data Type | Description              |
| ----------------- | --------- | ------------------------ |
| amfi_code         | Integer   | Scheme code              |
| stock_symbol      | Text      | Stock ticker             |
| stock_name        | Text      | Company name             |
| sector            | Text      | Industry sector          |
| weight_pct        | Float     | Portfolio weight         |
| market_value_cr   | Float     | Market value             |
| current_price_inr | Float     | Stock price              |
| portfolio_date    | Date      | Portfolio reporting date |

---

## Dataset 10: Benchmark Indices

Source: NSE/BSE

| Column Name | Data Type | Description         |
| ----------- | --------- | ------------------- |
| date        | Date      | Index date          |
| index_name  | Text      | Benchmark name      |
| close_value | Float     | Closing index value |
