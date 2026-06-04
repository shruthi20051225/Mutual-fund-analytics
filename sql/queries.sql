-- =====================================================
-- 1. Top 5 Funds by AUM
-- =====================================================

SELECT
    fund_house,
    MAX(aum_crore) AS max_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY max_aum DESC
LIMIT 5;


-- =====================================================
-- 2. Average NAV Per Month
-- =====================================================

SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav), 2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- =====================================================
-- 3. SIP Transactions Count
-- =====================================================

SELECT
    COUNT(*) AS total_sip_transactions
FROM fact_transactions
WHERE transaction_type = 'SIP';


-- =====================================================
-- 4. Transactions by State
-- =====================================================

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- =====================================================
-- 5. Funds with Expense Ratio Less Than 1%
-- =====================================================

SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- =====================================================
-- 6. Top Categories by Number of Funds
-- =====================================================

SELECT
    category,
    COUNT(*) AS total_funds
FROM dim_fund
GROUP BY category
ORDER BY total_funds DESC;


-- =====================================================
-- 7. Top 10 Funds by 5-Year Return
-- =====================================================

SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- =====================================================
-- 8. Average Alpha by Category
-- =====================================================

SELECT
    d.category,
    ROUND(AVG(f.alpha), 2) AS avg_alpha
FROM fact_performance f
JOIN dim_fund d
    ON f.amfi_code = d.amfi_code
GROUP BY d.category
ORDER BY avg_alpha DESC;


-- =====================================================
-- 9. Risk Grade Distribution
-- =====================================================

SELECT
    risk_grade,
    COUNT(*) AS fund_count
FROM fact_performance
GROUP BY risk_grade
ORDER BY fund_count DESC;


-- =====================================================
-- 10. Top 10 Transaction Cities
-- =====================================================

SELECT
    city,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY city
ORDER BY total_transactions DESC
LIMIT 10;