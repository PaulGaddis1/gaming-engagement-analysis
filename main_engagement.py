# ============================================
# Gaming Engagement Analysis – 2024
# Author: Paul Gaddis
# Role: Information Systems & Technology Student, UTSA
# Description:
#   Python-based data analysis using pandas and matplotlib.
#   Generates KPIs and charts (monthly revenue, revenue by game,
#   sessions by platform) from a synthetic gaming dataset.
#   NOTE: All data is fictional and used for educational purposes.
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("gaming_engagement_2024.csv")

# Ensure month order
months_order = ["January","February","March","April","May","June",
                "July","August","September","October","November","December"]
df["Month"] = pd.Categorical(df["Month"], categories=months_order, ordered=True)

# ---- KPIs ----
total_sessions = df["Sessions"].sum()
total_revenue = df["Revenue"].sum()
avg_session_minutes = (df["AvgSessionMinutes"] * df["Sessions"]).sum() / df["Sessions"].sum()

# Revenue by Game
rev_by_game = df.groupby("Game")["Revenue"].sum().sort_values(ascending=False)

# Monthly revenue trend (all games)
rev_by_month = df.groupby("Month")["Revenue"].sum().sort_index()

print("===== KPIs =====")
print(f"Total Sessions: {int(total_sessions):,}")
print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Weighted Avg Session Length: {avg_session_minutes:.1f} minutes")

print("\nTop 5 Games by Revenue:")
for g, v in rev_by_game.head(5).items():
    print(f" - {g}: ${v:,.0f}")

# ---- Charts ----
# 1) Monthly Revenue Trend
plt.figure()
rev_by_month.plot()
plt.title("Monthly Revenue Trend – 2024")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("chart_monthly_revenue.png", dpi=160)

# 2) Revenue by Game
plt.figure()
rev_by_game.plot(kind="bar")
plt.title("Revenue by Game – 2024")
plt.xlabel("Game")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("chart_revenue_by_game.png", dpi=160)

# 3) Sessions by Platform (total)
sessions_by_platform = df.groupby("Platform")["Sessions"].sum().sort_values(ascending=False)
plt.figure()
sessions_by_platform.plot(kind="bar")
plt.title("Total Sessions by Platform – 2024")
plt.xlabel("Platform")
plt.ylabel("Sessions")
plt.tight_layout()
plt.savefig("chart_sessions_by_platform.png", dpi=160)

print("\nCharts saved:")
print(" - chart_monthly_revenue.png")
print(" - chart_revenue_by_game.png")
print(" - chart_sessions_by_platform.png")
