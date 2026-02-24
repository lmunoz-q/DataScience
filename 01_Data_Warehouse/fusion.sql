CREATE TABLE IF NOT EXISTS items (
  product_id   BIGINT PRIMARY KEY,
  category_id  BIGINT,
  category_code TEXT,
  brand        TEXT
);

\copy items(product_id, category_id, category_code, brand)
FROM '/chemin/vers/items.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',', NULL '');

ALTER TABLE customers
  ADD COLUMN IF NOT EXISTS category_id BIGINT,
  ADD COLUMN IF NOT EXISTS category_code TEXT,
  ADD COLUMN IF NOT EXISTS brand TEXT;

UPDATE customers c
SET category_id   = i.category_id,
    category_code = i.category_code,
    brand         = i.brand
FROM items i
WHERE c.product_id = i.product_id;
