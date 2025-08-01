def apply_discount(price: float, discount_percent: float) -> float:
    if price <= 0:
        return 0.0

    discount_percent = max(0, discount_percent)

    discounted_price = price * (1 - discount_percent / 100)
    return round(discounted_price, 2)
