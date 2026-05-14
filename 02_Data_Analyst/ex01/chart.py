import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sqlalchemy import create_engine


engine = create_engine(
    "postgresql+psycopg2://lmunoz-q:42@localhost:5432/piscineds"
)

query = """
SELECT
    DATE(event_time) AS day,
    COUNT(DISTINCT user_id) AS number_of_customers
FROM customers
WHERE event_type = 'purchase'
GROUP BY day
ORDER BY day;
"""

df = pd.read_sql(query, engine)

print(df.head())
print(df.tail())
