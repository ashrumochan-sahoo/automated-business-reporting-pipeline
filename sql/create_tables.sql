CREATE TABLE dim_customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    region VARCHAR(50),
    country VARCHAR(50),
    created_date DATE
);


CREATE TABLE dim_product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    unit_price DECIMAL(10,2)
)


CREATE TABLE dim_date (
    date_id INT PRIMARY KEY,      -- Format: YYYYMMDD
    full_date DATE,
    year INT,
    month INT,
    day INT,
    weekday VARCHAR(10)
);


CREATE TABLE fact_sales (
    sales_id INT PRIMARY KEY,
    date_id INT,
    customer_id INT,
    product_id INT,
    quantity INT,
    total_amount DECIMAL(12,2)
);

