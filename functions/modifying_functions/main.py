def apply_discount(price, discount=0.05):
    return (price*(1-discount))

def apply_tax(price, tax=0.07):
    return (price*(1+tax))

def calculate_total(price, discount=0.05, tax=0.07):
     price_a = apply_tax(price, tax) 
     price_b = apply_discount(price_a, discount)
     return price_b

print(f"Total cost with default discount and tax: ${calculate_total(120)}")
print(f"Total cost with custom discount and tax: ${calculate_total(100, discount=0.10, tax=0.08)}")