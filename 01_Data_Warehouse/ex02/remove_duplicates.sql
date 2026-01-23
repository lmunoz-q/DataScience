CREATE TABLE customers_clean AS
SELECT DISTINCT *
FROM customers;

DROP TABLE customers;
ALTER TABLE customers_clean RENAME TO customers;
