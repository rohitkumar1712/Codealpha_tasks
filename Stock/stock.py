# ===============================
# Stock Portfolio Tracker
# ===============================

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145,
    "NFLX": 420
}

portfolio = {}
total_investment = 0

print("=" * 45)
print("        STOCK PORTFOLIO TRACKER")
print("=" * 45)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

# Number of stocks
while True:
    try:
        n = int(input("\nHow many different stocks do you own? "))
        if n > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Invalid input! Enter a valid number.")

# User input
for i in range(n):
    print(f"\nStock {i + 1}")

    while True:
        stock_name = input("Enter Stock Symbol: ").upper()

        if stock_name in stock_prices:
            break
        else:
            print("Stock not available. Choose from the list above.")

    while True:
        try:
            quantity = int(input("Enter Quantity: "))
            if quantity > 0:
                break
            else:
                print("Quantity must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

# Calculate investment
print("\n" + "=" * 45)
print("PORTFOLIO SUMMARY")
print("=" * 45)

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(
        f"{stock:8} | Qty: {quantity:3} | "
        f"Price: ${price:5} | Value: ${investment}"
    )

print("-" * 45)
print(f"Total Investment Value = ${total_investment}")
print("=" * 45)

# Save result
choice = input("\nDo you want to save the result? (yes/no): ").lower()

if choice == "yes":

    file_type = input("Save as TXT or CSV? ").lower()

    if file_type == "txt":
        with open("portfolio.txt", "w") as file:
            file.write("STOCK PORTFOLIO SUMMARY\n")
            file.write("=" * 40 + "\n")

            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                investment = price * quantity
                file.write(
                    f"{stock} | Qty: {quantity} | "
                    f"Price: ${price} | Value: ${investment}\n"
                )

            file.write("\n")
            file.write(f"Total Investment = ${total_investment}")

        print("Data saved successfully in portfolio.txt")

    elif file_type == "csv":
        with open("portfolio.csv", "w") as file:
            file.write("Stock,Quantity,Price,Investment\n")

            for stock, quantity in portfolio.items():
                price = stock_prices[stock]
                investment = price * quantity
                file.write(f"{stock},{quantity},{price},{investment}\n")

            file.write(f"\nTotal Investment,,,{total_investment}")

        print("Data saved successfully in portfolio.csv")

    else:
        print("Invalid file type. Data not saved.")

else:
    print("Result not saved.")

print("\nThank you for using Stock Portfolio Tracker!")