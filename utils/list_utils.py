# Function to normalize the dictionary structure
def normalize_items(items, price_key):
    return sorted([
        {
            'product_name': item['product_name'],
            'quantity': item['quantity'],
            'product_price': Decimal(item[price_key].replace('$', ''))  # Convert price to Decimal
        }
        for item in items
    ], key=lambda x: (x['product_name'], x['quantity'], x['product_price']))