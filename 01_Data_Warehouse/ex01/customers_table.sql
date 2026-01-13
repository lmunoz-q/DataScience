CREATE TABLE IF NOT EXISTS customers (
  event_time   TIMESTAMPTZ,
  event_type   VARCHAR(40),
  product_id   INTEGER,
  price        NUMERIC(1000,2),
  user_id      BIGINT,
  user_session UUID
);

SELECT * FROM
