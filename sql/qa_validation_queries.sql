-- 1. Duplicate Email Detection
SELECT email, COUNT(*) AS occurrences
FROM customers
GROUP BY email
HAVING COUNT(*) > 1;

-- 2. Orphan Orders (orders referencing non-existent customers)
SELECT o.order_id, o.customer_id
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

-- 3. Orphan Order Items (items referencing non-existent orders)
SELECT oi.item_id, oi.order_id
FROM order_items oi
LEFT JOIN orders o ON oi.order_id = o.order_id
WHERE o.order_id IS NULL;

-- 4. Order Total Discrepancies (order_total != SUM(line_price))
SELECT o.order_id, o.order_total, COALESCE(SUM(oi.line_price), 0) AS calculated_total
FROM orders o
LEFT JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY o.order_id, o.order_total
HAVING ROUND(o.order_total, 2) <> ROUND(COALESCE(SUM(oi.line_price), 0), 2);

-- 5. Negative / Invalid Product Prices
SELECT product_id, name, unit_price
FROM products
WHERE unit_price <= 0;
