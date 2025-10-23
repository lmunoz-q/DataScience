-- Créer une table avec les colonnes appropriées et les types de données
CREATE TABLE data_2022_oct (
event_time TIMESTAMP,
event_type VARCHAR,
product_id INT,
price FLOAT,
user_id INT,
user_session VARCHAR
);

CREATE TABLE data_2022_nov (
event_time TIMESTAMP,
event_type VARCHAR,
product_id INT,
price FLOAT,
user_id INT,
user_session VARCHAR
);

CREATE TABLE data_2022_dec (
event_timee TIMESTAMP,
event_type VARCHAR,
product_id INT,
price FLOAT,
user_id INT,
user_session VARCHAR
);

CREATE TABLE data_2023_jan (
event_time TIMESTAMP,
event_type VARCHAR,
product_id INT,
price FLOAT,
user_id INT,
user_session VARCHAR
);


-- Copier les données du CSV dans la table
\COPY data_2022_oct FROM '/docker-entrypoint-initdb.d/customer/data_2022_oct.csv' DELIMITER ',' CSV HEADER;
\COPY data_2022_nov FROM '/docker-entrypoint-initdb.d/customer/data_2022_nov.csv' DELIMITER ',' CSV HEADER;
\COPY data_2022_dec FROM '/docker-entrypoint-initdb.d/customer/data_2022_dec.csv' DELIMITER ',' CSV HEADER;
\COPY data_2023_jan FROM '/docker-entrypoint-initdb.d/customer/data_2023_jan.csv' DELIMITER ',' CSV HEADER;
