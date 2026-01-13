import glob, os, subprocess, shlex

CSV_DIR = "../data"
DB_HOST = "localhost"
DB_NAME = "piscineds"
DB_USER = "lmunoz-q"
PG_PASS = "42"

DDL = """CREATE TABLE IF NOT EXISTS {table} (
  event_time   TIMESTAMPTZ,
  event_type   VARCHAR(40),
  product_id   INTEGER,
  price        NUMERIC(1000,2),
  user_id      BIGINT,
  user_session UUID
);"""

env_with_pass = {**os.environ, "PGPASSWORD": PG_PASS}

csvs = glob.glob(os.path.join(CSV_DIR, "*.csv"))

for path in csvs:
  table = os.path.splitext(os.path.basename(path))[0]
  cmd = f'psql -h {DB_HOST} -U {DB_USER} -d {DB_NAME} -c "{DDL.format(table=table)}"'
  subprocess.run(shlex.split(cmd), check=True, env=env_with_pass)
