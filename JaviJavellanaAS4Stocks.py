def calculate_change(open_price, close_price):
    return close_price - open_price

def calculate_percentage_change(open_price, close_price):
    change = close_price - open_price
    return (change / open_price) * 100

def get_market_status(change):
    if change > 0:
        return "GAIN"
    elif change < 0:
        return "LOSS"
    else:
        return "NO CHANGE"

def display_summary(stock_name, open_price, close_price, change, percentage_change, market_status):
    print()
    print("Daily Stock Summary")
    print("Opening Price:", open_price)
    print("Closing Price:", close_price)
    print("Price Change:", change)
    print("Percentage Change:", percentage_change, "%")
    print("Market Status:", market_status)

stock_name = input("Enter the stock name: ")
open_price = float(input("Enter the opening price: "))
close_price = float(input("Enter the closing price: "))

change = calculate_change(open_price, close_price)
percentage_change = calculate_percentage_change(open_price, close_price)
market_status = get_market_status(change)

display_summary(stock_name, open_price, close_price, change, percentage_change, market_status)
