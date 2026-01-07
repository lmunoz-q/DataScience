import glob, os, subprocess, shlex

CSV_DIR = "../../subject/customer/"
DB_HOST = "localhost"
DB_NAME = "piscineds"
DB_USER = "lmunoz-q"
PG_PASS = "mysecretpassword"

DDL = """CREATE TABLE IF NOT EXISTS {table} (
  event_time TIMESTAMPTZ NOT NULL,
  event_type VARCHAR(40) NOT NULL,
  product_id INTEGER NOT NULL,
  price NUMERIC(1000,2) NOT NULL,
  user_id BIGINT NOT NULL,
  user_session UUID NOT NULL
);"""

env_with_pass = {**os.environ, "PGPASSWORD": PG_PASS}

csvs = glob.glob(os.path.join(CSV_DIR, "*.csv"))

for path in csvs:
    table = os.path.splitext(os.path.basename(path))[0]

    cmd1 = f'psql -h {DB_HOST} -U {DB_USER} -d {DB_NAME} -c "{DDL.format(table=table)}"'
    subprocess.run(shlex.split(cmd1), check=True, env=env_with_pass)
