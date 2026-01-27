DELETE FROM events a
USING events b
WHERE
  -- mêmes infos (donc "doublon") sauf le temps
  a.user_session = b.user_session
  AND a.user_id = b.user_id
  AND a.event_type = b.event_type
  AND a.product_id = b.product_id
  AND a.price = b.price

  -- a est dans la fenêtre [b.event_time ; b.event_time + 1s]
  AND a.event_time >= b.event_time
  AND a.event_time <= b.event_time + INTERVAL '1 second'

  -- pour ne pas se supprimer soi-même :
  -- si même event_time, on tranche au ctid ; sinon on supprime celui qui est plus tard
  AND (a.event_time > b.event_time OR a.ctid > b.ctid);
