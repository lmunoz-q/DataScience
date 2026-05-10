import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://lmunoz-q:42@localhost:5432/piscineds")

query = """
SELECT
    event_type,
    COUNT(*) AS count
FROM customers
GROUP BY event_type
ORDER BY count DESC;
"""

df = pd.read_sql(query, engine)

plt.figure(figsize=(8, 8))
plt.pie(
    df["count"],
    labels=df["event_type"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Event type from Customers")
plt.axis("equal")
plt.show()
