import pandas as pd

df = pd.read_csv("dashboard_data.csv")

print("Dashboard Data")
print(df)

total_sales = df["Sales"].sum()
total_customers = df["Customers"].sum()
total_profit = df["Profit"].sum()

print("\nKey Metrics")
print("Total Sales:", total_sales)
print("Total Customers:", total_customers)
print("Total Profit:", total_profit)

with open("dashboard_report.txt", "w") as f:
    f.write("INTERACTIVE DASHBOARD REPORT\n\n")
    f.write(f"Total Sales: {total_sales}\n")
    f.write(f"Total Customers: {total_customers}\n")
    f.write(f"Total Profit: {total_profit}\n")

print("\nDashboard Report Generated")