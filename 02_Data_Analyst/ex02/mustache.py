import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://lmunoz-q:42@localhost:5432/piscineds"
)

query = """
SELECT price::float AS price
FROM customers
WHERE event_type = 'purchase';
"""

df = pd.read_sql(query, engine)

ret = df["price"].describe()
print(ret.to_string(float_format="{:.2f}".format))

fig1, ax1 = plt.subplots(figsize=(8, 5))

ax1.boxplot(
    df["price"],
    vert=False
)

ax1.set_title("Price distribution of purchased items")
ax1.set_xlabel("price in A$")

plt.tight_layout()
plt.show()
