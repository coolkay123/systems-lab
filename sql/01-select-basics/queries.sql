-- Predict each result before running the lab.

-- 1. Available products, cheapest first.
SELECT name, price_cents
FROM products
WHERE in_stock = 1
ORDER BY price_cents ASC;

-- 2. Number of products and average price in each category.
SELECT
    category,
    COUNT(*) AS product_count,
    ROUND(AVG(price_cents) / 100.0, 2) AS average_price
FROM products
GROUP BY category
ORDER BY average_price DESC;

