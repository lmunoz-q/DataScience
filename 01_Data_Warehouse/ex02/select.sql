SELECT a.ctid, a.*
FROM events a
JOIN events b
  ON a.user_session = b.user_session
 AND a.user_id = b.user_id
 AND a.event_type = b.event_type
 AND a.product_id = b.product_id
 AND a.price = b.price
 AND a.event_time >= b.event_time
 AND a.event_time <= b.event_time + INTERVAL '1 second'
 AND (a.event_time > b.event_time OR a.ctid > b.ctid)
ORDER BY a.user_session, a.event_time;
