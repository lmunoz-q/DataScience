CREATE INDEX CONCURRENTLY customers_dedupe_idx
ON customers (event_time, event_type, product_id, price, user_id, user_session);

