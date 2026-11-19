INSERT INTO customers (customer_id, full_name, email, created_at) VALUES
(1, 'Mateo Pimienta', 'mateo@acteris.com', '2026-10-01'),
(2, 'Laura Gomez', 'laura@example.com', '2026-10-02'),
(3, 'Laura Gomez Duplicate', 'laura@example.com', '2026-10-03');

INSERT INTO products (product_id, name, unit_price) VALUES
(10, 'AI QA Suite License', 100.00),
(11, 'API Monitoring Addon', 50.00),
(12, 'Corrupted Negative SKU', -15.00);

INSERT INTO orders (order_id, customer_id, order_total, status) VALUES
(100, 1, 150.00, 'PAID'),
(101, 2, 200.00, 'PAID'),
(102, 999, 50.00, 'PENDING');

INSERT INTO order_items (item_id, order_id, product_id, quantity, line_price) VALUES
(1, 100, 10, 1, 100.00),
(2, 100, 11, 1, 50.00),
(3, 101, 10, 1, 100.00),
(4, 888, 11, 1, 50.00);
