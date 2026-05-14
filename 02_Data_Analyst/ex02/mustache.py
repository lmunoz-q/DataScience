import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://lmunoz-q:42@localhost:5432/piscineds"
)

query = """
SELECT price
FROM customers
WHERE event_type = 'purchase';
"""

df = pd.read_sql(query, engine)
print(df["price"].describe())
