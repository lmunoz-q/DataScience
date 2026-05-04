CREATE TABLE IF NOT EXISTS items (
  product_id BIGINT,
  category_id BIGINT,
  category_code TEXT,
  brand TEXT
);

-- faire la copie sur pgadmin

ALTER TABLE customers
  ADD COLUMN IF NOT EXISTS category_id BIGINT,
  ADD COLUMN IF NOT EXISTS category_code TEXT,
  ADD COLUMN IF NOT EXISTS brand TEXT;

UPDATE customers c
SET
  category_id = i.category_id,
  category_code = i.category_code,
  brand = i.brand
FROM (
  SELECT DISTINCT ON (product_id)
    product_id, category_id, category_code, brand
  FROM items
  ORDER BY product_id
) i
WHERE c.product_id = i.product_id;
