# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]
quantities_sold = [150, 200, 100, 50]

def calculate_revenue(prices, quantities_sold):
    revenue = []
    for i in range(len(prices)):
        revenue.append(prices[i] * quantities_sold[i])
    return revenue

# Task 3: get revenues
revenue = calculate_revenue(prices, quantities_sold)

# Task 4: define revenue_per_product at module level
revenue_per_product = list(zip(products, revenue))

def formatted_output(revenues):
    for product, rev in sorted(revenues):
        print(f"{product} has total revenue of ${rev}")

# Task 5: display sorted revenues
formatted_output(revenue_per_product)