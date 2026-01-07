import glob, os, subprocess, shlex

CSV_DIR = "customer"
DB_HOST = "db"
DB_NAME = "piscineds"
DB_USER = "lmunoz-q"

DDL = """CREATE TABLE IF NOT EXISTS {table} (
  event_time TIMESTAMPTZ NOT NULL,
  event_type VARCHAR(40) NOT NULL,
  product_id INTEGER NOT NULL,
  price NUMERIC(1000,2) NOT NULL,
  user_id BIGINT NOT NULL,
  user_session UUID NOT NULL
);"""

for path in glob.glob(os.path.join(CSV_DIR, "*.csv")):
    table = os.path.splitext(os.path.basename(path))[0]

    cmd1 = f'psql -h {DB_HOST} -U {DB_USER} -d {DB_NAME} -c "{DDL.format(table=table)}"'
    subprocess.run(shlex.split(cmd1), check=True)
