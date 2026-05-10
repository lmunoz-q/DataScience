import os, subprocess

DB_HOST = "localhost"
DB_NAME = "piscineds"
DB_USER = "lmunoz-q"
PG_PASS = "42"
CONTAINER = "pg-piscineds"

env = {**os.environ, "PGPASSWORD": PG_PASS}

# UBUNTU
result = subprocess.run(
    ["psql", "-h", DB_HOST, "-U", DB_USER, "-d", DB_NAME, "-t", "-c",
     "SELECT tablename FROM pg_tables WHERE tablename LIKE 'data_%';"],
    check=True, env=env, capture_output=True, text=True
)

#Fedora
#result = subprocess.run(
#    [
#        "podman", "exec", "-i", CONTAINER,
#        "psql", "-U", DB_USER, "-d", DB_NAME, "-t", "-c",
#        "SELECT tablename FROM pg_tables WHERE schemaname = 'public' AND tablename LIKE 'data_%';"
#    ],
#    check=True,
#    env=env,
#    capture_output=True,
#    text=True
#)
tables = [line.strip() for line in result.stdout.splitlines() if line.strip()]

if not tables:
    raise Exception("Not detected data_%")

union = "\nUNION ALL\n".join(f"SELECT * FROM {t}" for t in tables)
sql = f"DROP TABLE IF EXISTS customers; CREATE TABLE customers AS {union};"

# UBUNTU
subprocess.run(
    ["psql", "-h", DB_HOST, "-U", DB_USER, "-d", DB_NAME, "-c", sql],
    check=True, env=env
)

#Fedora
#result = subprocess.run(
#    [
#        "podman", "exec", "-i", CONTAINER,
#        "psql", "-U", DB_USER, "-d", DB_NAME, "-c", sql
#    ],
#    check=True,
#    env=env,
#)

print(f"✅ customers created from : {tables}")

