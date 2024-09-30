# Stock Portfolio Tracker

class Stock:
    def __init__(self, ticker, shares, buy_price):
        self.ticker = ticker
        self.shares = shares
        self.buy_price = buy_price
        self.current_price = buy_price

    def update_price(self, current_price):
        self.current_price = current_price

    def calculate_value(self):
        return self.shares * self.current_price

    def calculate_profit_loss(self):
        return (self.current_price - self.buy_price) * self.shares


class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def update_stock_price(self, ticker, current_price):
        for stock in self.stocks:
            if stock.ticker == ticker:
                stock.update_price(current_price)
                break

    def display_portfolio(self):
        print("\nStock Portfolio:")
        for stock in self.stocks:
            value = stock.calculate_value()
            profit_loss = stock.calculate_profit_loss()
            print(f"Ticker: {stock.ticker}, Shares: {stock.shares}, "
                  f"Buy Price: {stock.buy_price}, Current Price: {stock.current_price}, "
                  f"Value: {value:.2f}, Profit/Loss: {profit_loss:.2f}")
        print("\nTotal Portfolio Value: ", self.total_value())
        print("Total Profit/Loss: ", self.total_profit_loss())

    def total_value(self):
        return sum(stock.calculate_value() for stock in self.stocks)

    def total_profit_loss(self):
        return sum(stock.calculate_profit_loss() for stock in self.stocks)


def main():
    # Create a portfolio
    portfolio = Portfolio()

    while True:
        print("\n1. Add Stock")
        print("2. Update Stock Price")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            ticker = input("Enter stock ticker: ").upper()
            shares = int(input(f"Enter number of shares for {ticker}: "))
            buy_price = float(input(f"Enter buy price for {ticker}: "))
            stock = Stock(ticker, shares, buy_price)
            portfolio.add_stock(stock)

        elif choice == '2':
            ticker = input("Enter stock ticker to update price: ").upper()
            current_price = float(input(f"Enter current price for {ticker}: "))
            portfolio.update_stock_price(ticker, current_price)

        elif choice == '3':
            portfolio.display_portfolio()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose again.")


if __name__ == '__main__':
    main()
