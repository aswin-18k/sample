import requests

API_KEY = "8c8af8a070adab1897ccd47d" 
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

def convert_currency(amount, from_currency, to_currency):
    url = BASE_URL + from_currency.upper()
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error fetching exchange rates. Status Code: {response.status_code}")
        try:
            error_data = response.json()
            print(f"API Error Details: {error_data}")
        except requests.exceptions.JSONDecodeError:
            print(f"API Response Content (not JSON): {response.text}")
        return

    data = response.json()

    # Continue with your existing logic
    if to_currency.upper() not in data['conversion_rates']:
        print("Invalid target currency code.")
        return

    rate = data['conversion_rates'][to_currency.upper()]
    converted_amount = amount * rate

    print(f"\n💱 {amount} {from_currency.upper()} = {converted_amount:.2f} {to_currency.upper()}")
    print(f"📈 Exchange Rate: 1 {from_currency.upper()} = {rate} {to_currency.upper()}")

# --- MAIN ---
try:
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the source currency code (e.g., USD): ")
    to_currency = input("Enter the target currency code (e.g., INR): ")

    convert_currency(amount, from_currency, to_currency)
except ValueError:
    print("Please enter a valid numeric amount.")
