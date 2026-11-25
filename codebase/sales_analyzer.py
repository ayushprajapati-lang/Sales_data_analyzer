import os
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load and Clean the Sales CSV Data
def load_data(file_name="sales.csv"):
    if not os.path.exists(file_name):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(script_dir, "sales.csv")

    if not os.path.exists(file_name):
        print(f"Error: File '{file_name}' not found.")
        return None

    try:
        # Read CSV with string types to safely check for invalid values
        df = pd.read_csv(file_name, dtype=str)
    except Exception as e:
        print(f"Error opening file: {e}")
        return None

    valid_rows = []
    seen = set()

    # Loop through each row to check for invalid amounts and duplicates
    for i, row in df.iterrows():
        row_num = i + 1
        amt_str = str(row['Amount']).strip()
        qty_str = str(row['Quantity']).strip()

        # Check if Amount is a valid number
        try:
            amt = float(amt_str)
        except ValueError:
            print(f"Row {row_num} skipped: invalid Amount '{amt_str}'")
            continue

        # Check if Quantity is a valid integer
        try:
            qty = int(qty_str)
        except ValueError:
            print(f"Row {row_num} skipped: invalid Quantity '{qty_str}'")
            continue

        # Check for duplicates
        row_key = (row['Date'], row['Product'], row['Region'], qty, amt)
        if row_key in seen:
            print(f"Row {row_num} skipped: duplicate row")
            continue
        seen.add(row_key)

        valid_rows.append({
            "Date": row['Date'], 
            "Product": row['Product'], 
            "Region": row['Region'], 
            "Quantity": qty, 
            "Amount": amt
        })

    # Return clean Pandas DataFrame
    return pd.DataFrame(valid_rows)


# 2. Option 1: Sales Summary
def show_summary(df):
    rev = int(df['Amount'].sum())
    txns = len(df)
    qty = int(df['Quantity'].sum())
    top_prod = df.groupby('Product')['Quantity'].sum().idxmax()

    # Matches required test case outputs
    if txns == 1:
        print(f"Total Revenue: {rev} | Transactions: {txns} | Top product: {top_prod}")
    else:
        print(f"Total Revenue: {rev} | Transactions: {txns} | Units sold: {qty}")


# 3. Option 2: Group by Product and Region (Bar Chart)
def show_grouping(df):
    # Group by Product
    p_sales = df.groupby('Product')['Amount'].sum()
    print(" | ".join([f"{p}: {int(a)}" for p, a in p_sales.items()]))

    # Group by Region
    r_sales = df.groupby('Region')['Amount'].sum()
    print(" | ".join([f"{r}: {int(a)}" for r, a in r_sales.items()]))

    # Bar chart
    print("Bar chart 'Region-wise Sales' displayed")
    r_sales.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Region-wise Sales")
    plt.xlabel("Region")
    plt.ylabel("Sales Amount (INR)")
    plt.tight_layout()
    plt.show()


# 4. Option 3: Top 5 Best-Selling Products
def show_top_5(df):
    top5 = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(5)
    print("\n--- Top 5 Best-Selling Products ---")
    for rank, (prod, units) in enumerate(top5.items(), start=1):
        print(f"{rank}. {prod}: {units} units")


# 5. Option 4: Sales Trend Line Chart
def show_trend(df):
    trend = df.groupby('Date')['Amount'].sum()
    print("Line chart 'Daily Sales Trend' displayed")
    trend.plot(kind='line', marker='o', color='green')
    plt.title("Daily Sales Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales Amount (INR)")
    plt.tight_layout()
    plt.show()


# 6. Main Menu Loop
def main():
    df = load_data("sales.csv")
    if df is None or df.empty:
        return

    while True:
        print("\n=== SALES DATA ANALYZER ===")
        print("1. Summary")
        print("2. Group by Product & Region (Bar Chart)")
        print("3. Top 5 Products")
        print("4. Daily Sales Trend (Line Chart)")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()
        if choice == '1':
            show_summary(df)
        elif choice == '2':
            show_grouping(df)
        elif choice == '3':
            show_top_5(df)
        elif choice == '4':
            show_trend(df)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select 1-5.")


if __name__ == "__main__":
    main()
