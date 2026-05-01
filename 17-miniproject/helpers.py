def apply_price(products, percent):
    for product in products:
        product["price"] = round(product["price"] * (1 + percent / 100), 2)
    return products
