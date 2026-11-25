# Sales Data Analyzer

## 1. Project Overview

The **Sales Data Analyzer** is a Python-based data analysis project that processes retail sales records from a CSV file.

It validates raw transaction records, calculates overall revenue and unit metrics, performs multi-dimensional grouping by product and sales region, identifies top-selling products, and generates visual reports using charts.

The project uses Python libraries like Pandas and Matplotlib to automate sales tracking and make commercial performance analysis faster and error-free.

## 2. Features

- **Data Validation:** Identifies and skips invalid records (non-numeric amounts or invalid quantities) and eliminates duplicate transactions before calculations run.
- **Sales Summary:** Computes overall turnover, total transaction count, and cumulative units sold across all valid records.
- **Categorical Grouping:** Uses Pandas `groupby()` to calculate product-wise total earnings and region-wise sales distribution.
- **Top 5 Leaderboard:** Identifies and displays the top 5 best-selling products sorted by total quantity sold.
- **Bar Chart:** Displays region-wise sales distribution graphically using Matplotlib.
- **Line Chart:** Illustrates daily sales revenue momentum chronologically over time.
- **Interactive Menu:** Allows users to select different analytical reports through a simple command-line menu.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| Pandas | Reading, validating, cleaning, and grouping CSV data |
| Matplotlib | Creating bar and line charts |
| CSV | Storing raw sales transaction records |
| VS Code / Terminal | Development environment and execution console |

## 4. Project Structure

```text
SalesDataAnalyzer/
│
├── codebase/
│   ├── sales.csv
│   └── sales_analyzer.py
└── documentation/
    ├── README.md
    └── problem_statement.txt
```

### File Description

- `codebase/sales.csv` – Contains transaction date, product name, region, quantity sold, and amount.
- `codebase/sales_analyzer.py` – Contains the clean Python code for validation, analysis, grouping, and visualization.
- `documentation/README.md` – Provides documentation, specifications, and instructions for running the project.
- `documentation/problem_statement.txt` – The official problem statement, requirements, and test cases.

## 5. Installation and Setup

### Step 1: Install Python

Download and install Python 3 from:

https://python.org

### Step 2: Install Required Libraries

Open the terminal and execute:

```bash
python -m pip install pandas matplotlib
```

### Step 3: Open the Project

Open the project folder in VS Code or your preferred terminal.

Make sure that both `sales.csv` and `sales_analyzer.py` are present inside the `codebase/` folder.

## 6. How to Run the Project

Open the terminal, navigate into the `codebase` directory, and execute the script:

```bash
cd codebase
python sales_analyzer.py
```

The program will validate the CSV records on startup and display the interactive menu.

## 7. Menu Options

The program provides the following options:

| Option | Function |
|---|---|
| 1 | Display overall sales summary (Total Revenue, Transactions, Units Sold) |
| 2 | Display product-wise & region-wise sales and show Region Bar Chart |
| 3 | Display the Top 5 best-selling products leaderboard |
| 4 | Display chronological daily sales trend (Line Chart) |
| 5 | Exit the program |

### Key Metrics Calculation

- **Total Revenue = Sum of all valid Amount entries**
- **Total Transactions = Total number of valid rows processed**
- **Units Sold = Sum of all Quantity values**
- **Top Product = Product with the highest cumulative units sold**

## 8. Data Validation

The program checks every row in `codebase/sales.csv` before performing calculations.

A record is skipped if any of the following conditions occur:

- Amount contains non-numeric text or symbols (e.g. `Amount = 'abc'`).
- Quantity cannot be parsed as a valid integer.
- The row is an exact duplicate of a previously recorded transaction.

Invalid records are reported in the console with their row number and excluded so they do not distort revenue calculations or averages.

## 9. Sample Dataset

The project uses `codebase/sales.csv` with standard transaction fields:

| Date | Product | Region | Quantity | Amount (INR) |
|---|---|---|---:|---:|
| 2026-08-01 | Laptop | North | 2 | 100000 |
| 2026-08-02 | Mouse | South | 10 | 5000 |
| 2026-08-03 | Laptop | South | 1 | 50000 |
| 2026-08-04 | Keyboard | North | 5 | 7500 |
| 2026-08-05 | Monitor | East | 3 | 45000 |

## 10. Expected Output

The project generates:

1. Row-level data sanitization alerts when invalid entries are encountered (e.g. `Row 2 skipped: invalid Amount 'abc'`).
2. An overall financial summary showing total revenue, transactions, and units sold.
3. Pipe-separated product-wise and region-wise revenue summaries.
4. An interactive bar chart for region-wise sales.
5. A ranked leaderboard table showing the top 5 selling items.
6. A chronological line graph plotting daily revenue trends.

## 11. Conclusion

The Sales Data Analyzer demonstrates how Python can automate business sales analysis, clean messy real-world transaction logs, and present actionable insights.

Using Pandas and Matplotlib, it turns raw tabular CSV data into clean summary statistics, categorized performance metrics, and intuitive visual charts suitable for business decision-making.

---

**Project Name:** Sales Data Analyzer  
**Course:** Bachelor of Computer Applications (BCA) - 3rd Semester  
**Language:** Python 3  
**Libraries:** Pandas, Matplotlib  
**Data Format:** CSV  
