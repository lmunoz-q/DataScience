import glob, os, subprocess, shlex

CSV_DIR = "./data"
DB_HOST = "localhost"
DB_NAME = "piscineds"
DB_USER = "lmunoz-q"
PG_PASS = "42"

CREATE_TABLE = """CREATE TABLE IF NOT EXISTS {table} (
  event_time   TIMESTAMPTZ,
  event_type   VARCHAR(40),
  product_id   INTEGER,
  price        NUMERIC(1000,2),
  user_id      BIGINT,
  user_session UUID
);"""

COPY_CMD = """\\copy {table} FROM '/data/{filename}' DELIMITER ',' CSV HEADER;"""

env_with_pass = {**os.environ, "PGPASSWORD": PG_PASS}

csvs = glob.glob(os.path.join(CSV_DIR, "*.csv"))

for path in csvs:
    table = os.path.splitext(os.path.basename(path))[0]
#UBUNTU
#    cmd = f'psql -h {DB_HOST} -U {DB_USER} -d {DB_NAME} -c "{CREATE_TABLE.format(table=table)}"'
#FEDORA
    cmd = f'podman exec -i pg-piscineds psql -U {DB_USER} -d {DB_NAME} -c "{CREATE_TABLE.format(table=table)}"'
    subprocess.run(shlex.split(cmd), check=True, env=env_with_pass)

    filename = os.path.basename(path)
    copy = COPY_CMD.format(table=table, filename=filename)
#UBUNTU
#    cmd2 = f"psql -h {DB_HOST} -U {DB_USER} -d {DB_NAME} -c \"{copy}\""
#FEDORA
    cmd2 = f'podman exec -i pg-piscineds psql -U {DB_USER} -d {DB_NAME} -c "{copy}"'
    subprocess.run(shlex.split(cmd2), check=True, env=env_with_pass)
    print(f"✅ {table} chargée")
