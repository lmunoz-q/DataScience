BEGIN;

CREATE TABLE customers_clean AS
SELECT
	event_time,
	event_type,
	product_id,
	price,
	user_id,
	user_session
FROM (
	SELECT
		c.*,
		LAG(event_time) OVER (
			PARTITION BY user_session, user_id, event_type, product_id, price
			ORDER BY event_time, ctid
		) AS previous_event_time
	FROM customers c
) AS ordered_customers
WHERE
	previous_event_time IS NULL
	OR event_time > previous_event_time + INTERVAL '1 second';

DROP TABLE customers;

ALTER TABLE customers_clean RENAME TO customers;

COMMIT;
