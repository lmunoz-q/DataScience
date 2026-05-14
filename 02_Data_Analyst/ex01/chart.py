import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sqlalchemy import create_engine


engine = create_engine(
    "postgresql+psycopg2://lmunoz-q:42@localhost:5432/piscineds"
)

query_customers_per_day = """
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
    SUM(price)::float / 1000000 AS total_sales_million
FROM customers
WHERE event_type = 'purchase'
GROUP BY month
ORDER BY month;
"""


query_avg_spend_per_day = """
SELECT
    DATE(event_time) AS day,
    SUM(price)::float / COUNT(DISTINCT user_id) AS avg_spend_per_custommer
FROM customers
WHERE event_type = 'purchase'
GROUP BY day
ORDER BY day;
"""

df1 = pd.read_sql(query_customers_per_day, engine)
df1["day"] = pd.to_datetime(df1["day"])

fig1, ax1 = plt.subplots(figsize=(10, 5))
ax1.plot(
    df1["day"],
    df1["number_of_customers"]
)
ax1.set_title("Number of customers in 2022/2023")
ax1.set_xlabel("date")
ax1.set_ylabel("number of customers")

ax1.xaxis.set_major_locator(mdates.MonthLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
ax1.grid(alpha=0.3)
plt.tight_layout()


df2 = pd.read_sql(query_sales_per_month, engine)
df2["month"] = pd.to_datetime(df2["month"])

fig2, ax2 = plt.subplots(figsize=(6, 4))
bar_containter = ax2.bar(
    df2["month"].dt.strftime("%b"),
    df2["total_sales_million"]
)

ax2.set_title("Total sales per month")
ax2.set_xlabel("month")
ax2.set_ylabel("sales in million of A$")
ax2.grid(axis="y", alpha=0.3)
plt.tight_layout()

df3 = pd.read_sql(query_avg_spend_per_day, engine)
df3["day"] = pd.to_datetime(df3["day"])

fig3, ax3 = plt.subplots(figsize=(10, 5))
ax3.fill_between(
    df3["day"],
    df3["avg_spend_per_custommer"]
)

ax3.set_title("Average spend per customer per day")
ax3.set_xlabel("date")
ax3.set_ylabel("average spend / customer in A$")

ax3.xaxis.set_major_locator(mdates.MonthLocator())
ax3.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
ax3.set_axisbelow(True)
ax3.grid(alpha=0.3)
plt.tight_layout()

plt.show()
