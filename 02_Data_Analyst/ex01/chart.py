import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://lmunoz-q:42@localhost:5432/piscineds")

query_customers_per_day= """
SELECT
    DATE(event_time) AS day,
    COUNT(DISTINCT user_id) AS number_of_customers
FROM customers
WHERE event_type = 'purchase'
GROUP BY day
ORDER BY day;
"""

query_sales_per_month = """
SELECT
    DATE_TRUNC('month', event_time) AS month,
    SUM(price)::float / 1000000 AS total
FROM customers
GROUP BY month
ORDER BY month;
"""

df1 = pd.read_sql(query_customers_per_day, engine)
df2 = pd.read_sql(query_sales_per_month, engine)

plt.figure(figsize=(8, 8))
plt.plot(
    df1["day"],
    df1["number_of_customers"]
)
plt.ylabel("number of customers")
plt.title("Number of customers per day")
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b"))


plt.bar(
    df2["month"].dt.strftime("%b"),
    df2["total"]
)
plt.grid(True, axis='y', linestyle='--', alpha=0.2)
plt.ylabel("total sales in million of A$")
plt.xlabel("month")
plt.title("Total sales per month")

plt.show()

