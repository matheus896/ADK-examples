import yfinance as yf
from datetime import datetime

# This is the function you want to test, copied here for isolation.
def get_stock_price(ticker: str) -> dict:
    """Retrieves current stock price and saves to session state."""
    print(f"--- Tool: get_stock_price called for {ticker} ---")

    try:
        # Fetch stock data
        stock = yf.Ticker(ticker)
        current_price = stock.info.get("currentPrice")

        if current_price is None:
            # Try 'regularMarketPrice' as a fallback
            current_price = stock.info.get("regularMarketPrice")

        if current_price is None:
            return {
                "status": "error",
                "error_message": f"Could not fetch price for {ticker}. Check the ticker symbol.",
            }

        # Get current timestamp
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return {
            "status": "success",
            "ticker": ticker,
            "price": current_price,
            "timestamp": current_time,
        }

    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error fetching stock data: {str(e)}",
        }

if __name__ == "__main__":
    # Test with a valid ticker
    print("Testing with a valid ticker (GOOGL):")
    googl_data = get_stock_price("GOOGL")
    print(googl_data)
    print("-" * 20)

    # Test with an invalid ticker
    print("Testing with an invalid ticker (INVALIDTICKER):")
    invalid_data = get_stock_price("NVDA")
    print(invalid_data)
    print("-" * 20)

    # Test with another valid ticker
    print("Testing with another valid ticker (MSFT):")
    msft_data = get_stock_price("MSFT")
    print(msft_data)
    print("-" * 20) 