import sqlite3
from pathlib import Path
import unittest

BASE_DIR = Path(__file__).resolve().parent.parent
SCHEMA_SQL = (BASE_DIR / "sql" / "schema.sql").read_text(encoding="utf-8")
SEED_SQL = (BASE_DIR / "sql" / "seed_data.sql").read_text(encoding="utf-8")


class TestSQLQAValidation(unittest.TestCase):
    def setUp(self) -> None:
        self.conn = sqlite3.connect(":memory:")
        self.conn.executescript(SCHEMA_SQL)
        self.conn.executescript(SEED_SQL)

    def tearDown(self) -> None:
        self.conn.close()

    def test_detects_duplicate_customer_emails(self) -> None:
        rows = self.conn.execute(
            "SELECT email, COUNT(*) FROM customers GROUP BY email HAVING COUNT(*) > 1;"
        ).fetchall()
        self.assertEqual(rows, [("laura@example.com", 2)])

    def test_detects_orphan_orders_without_customer(self) -> None:
        rows = self.conn.execute(
            "SELECT o.order_id FROM orders o LEFT JOIN customers c ON o.customer_id = c.customer_id WHERE c.customer_id IS NULL;"
        ).fetchall()
        self.assertEqual(rows, [(102,)])

    def test_detects_orphan_order_items_without_order(self) -> None:
        rows = self.conn.execute(
            "SELECT oi.item_id FROM order_items oi LEFT JOIN orders o ON oi.order_id = o.order_id WHERE o.order_id IS NULL;"
        ).fetchall()
        self.assertEqual(rows, [(4,)])

    def test_detects_order_total_discrepancies(self) -> None:
        rows = self.conn.execute(
            """
            SELECT o.order_id, o.order_total, COALESCE(SUM(oi.line_price), 0) AS calc
            FROM orders o
            LEFT JOIN order_items oi ON o.order_id = oi.order_id
            GROUP BY o.order_id, o.order_total
            HAVING ROUND(o.order_total, 2) <> ROUND(COALESCE(SUM(oi.line_price), 0), 2)
            ORDER BY o.order_id;
            """
        ).fetchall()
        self.assertEqual(rows, [(101, 200.0, 100.0), (102, 50.0, 0.0)])

    def test_detects_negative_product_prices(self) -> None:
        rows = self.conn.execute(
            "SELECT product_id, unit_price FROM products WHERE unit_price <= 0;"
        ).fetchall()
        self.assertEqual(rows, [(12, -15.0)])


if __name__ == "__main__":
    unittest.main()
