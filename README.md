# SQL QA Data Validation Suite (MySQL + Docker + Python)

[![SQL QA Validation Suite](https://github.com/MrMoon1725/sql-qa-data-validation/actions/workflows/sql-qa.yml/badge.svg)](https://github.com/MrMoon1725/sql-qa-data-validation/actions/workflows/sql-qa.yml)

SQL Quality Assurance project demonstrating **data integrity validation**, **anomaly detection**, and **post-API database verification** using **MySQL 8.0 (Docker Compose)** and automated **Python `unittest` (`sqlite3`)** checks in CI.

---

## QA Checks Covered (`sql/qa_validation_queries.sql`)

1. **Duplicate Detection:** Flags duplicate customer emails (`GROUP BY ... HAVING COUNT(*) > 1`).
2. **Referential Integrity (Orphan Orders):** Identifies orders linked to missing customers (`LEFT JOIN ... WHERE NULL`).
3. **Orphan Line Items:** Identifies `order_items` referencing non-existent orders.
4. **Financial Total Discrepancies:** Compares `orders.order_total` against `SUM(order_items.line_price)`.
5. **Domain / Constraint Anomalies:** Flags negative or zero product prices (`unit_price <= 0`).

---

## Running Locally

```bash
python -m unittest discover -s tests -v
```
