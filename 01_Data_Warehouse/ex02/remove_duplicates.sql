DELETE FROM customers a
USING customers b
WHERE
  a.user_session	IS NOT DISTINCT FROM b.user_session
  AND a.user_id		IS NOT DISTINCT FROM b.user_id
  AND a.event_type	IS NOT DISTINCT FROM b.event_type
  AND a.product_id	IS NOT DISTINCT FROM b.product_id
  AND a.price		IS NOT DISTINCT FROM b.price
  AND a.event_time >= b.event_time
  AND a.event_time < b.event_time + INTERVAL '1 second'
  AND (a.event_time > b.event_time OR a.ctid > b.ctid);
