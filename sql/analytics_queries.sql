SELECT
    c.region,
    SUM(f.total_amount) AS total_sales
FROM fact_sales f
JOIN dim_customer c ON f.customer_id = c.customer_id        --[Total Sales by Region]
GROUP BY c.region
ORDER BY total_sales DESC;



SELECT
    p.product_name,
    SUM(f.total_amount) AS revenue
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.product_id          --[Top 10 Products by Revenue]
GROUP BY p.product_name
ORDER BY revenue DESC
FETCH FIRST 10 ROWS ONLY;



SELECT
    d.year,
    d.month,
    SUM(f.total_amount) AS monthly_sales
FROM fact_sales f
JOIN dim_date d ON f.date_id = d.date_id                   --[Monthly Sales Trend]
GROUP BY d.year, d.month
ORDER BY d.year, d.month;



SELECT
    c.customer_name,
    AVG(f.total_amount) AS avg_order_value
FROM fact_sales f
JOIN dim_customer c ON f.customer_id = c.customer_id        --[Average Order Value by Customer]
GROUP BY c.customer_name
ORDER BY avg_order_value DESC;

