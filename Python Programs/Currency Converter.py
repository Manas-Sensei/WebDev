# Define exchange rates relative to USD
rate_EUR = 0.86
rate_JPY = 147
rate_GBP = 0.75
rate_INR = 87.5

while True:
    amount_input = input("Enter amount (or type 'exit' to quit): ")
    if amount_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    try:
        amount = float(amount_input)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        continue
    
    source_currency = input("Enter source currency (USD, EUR, JPY, GBP, INR): ").upper()
    if source_currency not in ("USD", "EUR", "JPY", "GBP", "INR"):
        print("Invalid source currency.")
        continue
    
    target_currency = input("Enter target currency (USD, EUR, JPY, GBP, INR): ").upper()
    if target_currency not in ("USD", "EUR", "JPY", "GBP", "INR"):
        print("Invalid target currency.")
        continue
    
    # Convert source amount to USD
    if source_currency == "USD":
        amount_in_usd = amount
    elif source_currency == "EUR":
        amount_in_usd = amount / rate_EUR
    elif source_currency == "JPY":
        amount_in_usd = amount / rate_JPY
    elif source_currency == "GBP":
        amount_in_usd = amount / rate_GBP
    elif source_currency == "INR":
        amount_in_usd = amount / rate_INR
    
    # Convert USD amount to target currency
    if target_currency == "USD":
        converted_amount = amount_in_usd
    elif target_currency == "EUR":
        converted_amount = amount_in_usd * rate_EUR
    elif target_currency == "JPY":
        converted_amount = amount_in_usd * rate_JPY
    elif target_currency == "GBP":
        converted_amount = amount_in_usd * rate_GBP
    elif target_currency == "INR":
        converted_amount = amount_in_usd * rate_INR
    
    print(f"{amount:.2f} {source_currency} is {converted_amount:.2f} {target_currency}\n")
