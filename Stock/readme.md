# 📈 Stock Portfolio Tracker

A simple Python-based Stock Portfolio Tracker that allows users to calculate the total investment value of their stock portfolio using predefined stock prices.

---

## 📌 Project Description

This project demonstrates the use of Python fundamentals such as dictionaries, user input, loops, arithmetic operations, and file handling.

Users can:
- Enter stock symbols.
- Enter the quantity of each stock owned.
- Calculate the total investment value.
- Save the portfolio summary to a `.txt` or `.csv` file.

---

## 🎯 Objective

The objective of this project is to build a basic stock portfolio tracker that calculates the total investment value based on manually defined stock prices.

---

## ✨ Features

- Hardcoded stock price dictionary
- User-friendly console interface
- Calculates investment value for each stock
- Displays complete portfolio summary
- Calculates total investment value
- Saves results in:
  - Text file (`portfolio.txt`)
  - CSV file (`portfolio.csv`)
- Input validation for stock names and quantities

---

## 🛠 Technologies Used

- Python 3
- Dictionaries
- Loops
- Conditional Statements
- File Handling
- Exception Handling

---

## 📂 Project Structure

```
StockPortfolioTracker/
│
├── stock_portfolio_tracker.py
├── README.md
├── portfolio.txt        (Generated)
└── portfolio.csv        (Generated)
```

---

## 📊 Hardcoded Stock Prices

| Stock Symbol | Price ($) |
|--------------|-----------|
| AAPL | 180 |
| TSLA | 250 |
| GOOGL | 140 |
| MSFT | 330 |
| AMZN | 145 |
| NFLX | 420 |

---

## ▶️ How to Run

1. Install Python 3.
2. Download or clone the project.
3. Open a terminal or command prompt.
4. Navigate to the project folder.
5. Run the program:

```bash
python stock_portfolio_tracker.py
```

---

## 💻 Example Output

```
=============================================
        STOCK PORTFOLIO TRACKER
=============================================

Available Stocks:
AAPL : $180
TSLA : $250
GOOGL : $140
MSFT : $330
AMZN : $145
NFLX : $420

How many different stocks do you own? 2

Stock 1
Enter Stock Symbol: AAPL
Enter Quantity: 5

Stock 2
Enter Stock Symbol: TSLA
Enter Quantity: 3

=============================================
PORTFOLIO SUMMARY
=============================================
AAPL     | Qty: 5 | Price: $180 | Value: $900
TSLA     | Qty: 3 | Price: $250 | Value: $750
---------------------------------------------
Total Investment Value = $1650
=============================================

Do you want to save the result? yes
Save as TXT or CSV? txt

Data saved successfully in portfolio.txt
```

---

## 📁 Output Files

### portfolio.txt

```
STOCK PORTFOLIO SUMMARY
========================================
AAPL | Qty: 5 | Price: $180 | Value: $900
TSLA | Qty: 3 | Price: $250 | Value: $750

Total Investment = $1650
```

### portfolio.csv

```
Stock,Quantity,Price,Investment
AAPL,5,180,900
TSLA,3,250,750

Total Investment,,,1650
```

---

## 📚 Concepts Used

- Python Dictionary
- User Input (`input()`)
- Loops (`for`, `while`)
- Conditional Statements (`if-else`)
- Arithmetic Operations
- Exception Handling (`try-except`)
- File Handling (`.txt` and `.csv`)

---

## 🚀 Future Improvements

- Fetch real-time stock prices using an API.
- Store portfolio information in a database.
- Create a graphical user interface (GUI).
- Display profit/loss calculations.
- Generate charts for portfolio analysis.

---

## 👨‍💻 Author

**Your Name**

Python Programming Project

---

## 📄 License

This project is for educational purposes only.