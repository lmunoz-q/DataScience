CREATE TABLE IF NOT EXISTS customers (
  event_time   TIMESTAMPTZ,
  event_type   VARCHAR(40),
  product_id   INTEGER,
  price        NUMERIC(1000,2),
  user_id      BIGINT,
  user_session UUID
);

INSERT INTO customers
SELECT * FROM data_2023_feb
UNION ALL
SELECT * FROM data_2023_feb2;
