CREATE TABLE data_2022_oct (
	event_time		TIMESTAMPTZ,
	event_type		VARCHAR(40),
	product_id		INTEGER,
	price			NUMERIC(1000, 2),
	user_id			BIGINT,
	user_session	UUID
);

CREATE TABLE data_2022_nov (
	event_time		TIMESTAMPTZ,
	event_type		VARCHAR(40),
	product_id		INTEGER,
	price			NUMERIC(1000, 2),
	user_id			BIGINT,
	user_session	UUID
);

CREATE TABLE data_2022_dec (
	event_time		TIMESTAMPTZ,
	event_type		VARCHAR(40),
	product_id		INTEGER,
	price			NUMERIC(1000, 2),
	user_id			BIGINT,
	user_session	UUID
);

CREATE TABLE data_2023_jan (
	event_time		TIMESTAMPTZ,
	event_type		VARCHAR(40),
	product_id		INTEGER,
	price			NUMERIC(1000, 2),
	user_id			BIGINT,
	user_session	UUID
);


COPY data_2022_oct(event_time,event_type,product_id,price,user_id,user_session)
FROM '<chemin_interne_dans_le_conteneur>'
WITH (FORMAT csv, HEADER true);

COPY data_2022_nov(event_time,event_type,product_id,price,user_id,user_session)
FROM '<chemin_interne_dans_le_conteneur>'
WITH (FORMAT csv, HEADER true);

COPY data_2022_dec(event_time,event_type,product_id,price,user_id,user_session)
FROM '<chemin_interne_dans_le_conteneur>'
WITH (FORMAT csv, HEADER true);

COPY data_2023_jan(event_time,event_type,product_id,price,user_id,user_session)
FROM '<chemin_interne_dans_le_conteneur>'
WITH (FORMAT csv, HEADER true);
