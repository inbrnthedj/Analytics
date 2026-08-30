# Northwind Traders — Employee Incentive Analysis

Analyze the Northwind Traders database to identify the top 5 employees with the highest total order amounts, for the purpose of awarding performance-based incentives.

> **Note:** Northwind Traders is a fictional company used as a sample database. Any resemblance to real entities is purely coincidental.

## Objective

Determine which 5 employees generated the highest total order amounts (by revenue) and should be given incentives for their sales performance.

## Approach

1. **Data Exploration** — Understanding the database schema, table relationships, and available fields
2. **Solution Design** — Drawing out the SQL query logic: joining Orders, OrderDetails, Products, and Employees to compute total order amounts per employee
3. **Implementation & Results** — Writing and executing SQL queries to produce the final ranked output

## Key Files

| File | Description |
|------|-------------|
| [`Documentation.ipynb`](./Documentation.ipynb) | Main analysis notebook with step-by-step walkthrough |
| [`SOURCE.md`](./SOURCE.md) | Data source documentation, schema, and ER diagram |
| `TASK*.sql` | Individual SQL query files for each step of the analysis |
| `*.csv` | Exported database tables (8 tables) |

## Tech Stack

* **Language:** SQL
* **Database:** Northwind sample database (via [w3schools SQL Tryit Editor](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all))
* **Tools:** Jupyter Notebook, VS Code

## Data Source

The dataset is obtained from the w3schools practice database: [SQL Tryit Editor V1.6](https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all). See [`SOURCE.md`](./SOURCE.md) for full schema details.

*Adapted from a guided project on Coursera. The implementation, query design, and analysis are original work.*
