CREATE TABLE IF NOT EXISTS data_2022_oct (
	event_time		TIMESTAMPTZ,
	event_type		VARCHAR(40),
	product_id		INTEGER,
	price			NUMERIC(1000, 2),
	user_id			BIGINT,
	user_session	UUID
);

CREATE TABLE IF NOT EXISTS data_2022_nov (
	event_time		TIMESTAMPTZ,
	event_type		VARCHAR(40),
	product_id		INTEGER,
	price			NUMERIC(1000, 2),
	user_id			BIGINT,
	user_session	UUID
);

CREATE TABLE IF NOT EXISTS data_2022_dec (
	event_time		TIMESTAMPTZ,
	event_type		VARCHAR(40),
	product_id		INTEGER,
	price			NUMERIC(1000, 2),
	user_id			BIGINT,
	user_session	UUID
);

CREATE TABLE IF NOT EXISTS data_2023_jan (
	event_time		TIMESTAMPTZ,
	event_type		VARCHAR(40),
	product_id		INTEGER,
	price			NUMERIC(1000, 2),
	user_id			BIGINT,
	user_session	UUID
);
