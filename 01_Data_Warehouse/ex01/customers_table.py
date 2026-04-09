import os, subprocess

DB_HOST = "localhost"
DB_NAME = "piscineds"
DB_USER = "lmunoz-q"
PG_PASS = "42"

env = {**os.environ, "PGPASSWORD": PG_PASS}

result = subprocess.run(
    ["psql", "-h", DB_HOST, "-U", DB_USER, "-d", DB_NAME, "-t", "-c",
     "SELECT tablename FROM pg_tables WHERE tablename LIKE 'data_%';"],
    check=True, env=env, capture_output=True, text=True
)
tables = [line.strip() for line in result.stdout.splitlines() if line.strip()]

union = "\nUNION ALL\n".join(f"SELECT * FROM {t}" for t in tables)
sql = f"DROP TABLE IF EXISTS customers; CREATE TABLE customers AS {union};"

subprocess.run(
    ["psql", "-h", DB_HOST, "-U", DB_USER, "-d", DB_NAME, "-c", sql],
    check=True, env=env
)
print(f"✅ customers créée depuis : {tables}")
