import requests

class StockAnalyzer:
    def __init__(self, api_key):
        self.api_key = api_key

    def analyze_stock(self, symbol):
        url = f"https://api.stockdata.com/v1/stock/{symbol}/analysis"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(url, headers=headers)
        data = response.json()

        if response.status_code == 200:
            if "analysis" in data:
                print(f"Stock Analysis for {symbol}:")
                for analysis in data["analysis"]:
                    date = analysis["date"]
                    recommendation = analysis["recommendation"]
                    target_price = analysis["target_price"]
                    print(f"- Date: {date}, Recommendation: {recommendation}, Target Price: {target_price}")
            else:
                print(f"No stock analysis found for {symbol}.")
        else:
            print("Unable to retrieve stock analysis.")

def main():
    api_key = "YOUR_API_KEY"
    symbol = "AAPL"

    analyzer = StockAnalyzer(api_key)
    analyzer.analyze_stock(symbol)

if __name__ == "__main__":
    main()
