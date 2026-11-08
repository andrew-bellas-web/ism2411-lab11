
# Reflection 1:
# I would use .get() when I am not sure if a key exists in a dictionary.
# Bracket notation is useful when I know the key should be there.
# My rule is to use .get() for optional information and brackets for required information.

# Reflection 2:
# This reminds me of using pivot tables in Excel to summarize sales data.
# Python can do the same thing automatically using loops and dictionaries.
# It can be more useful for large datasets because I can reuse the code without doing everything manually.


# Exercise 1: One Customer

customer = {
    "name": "Alice",
    "email": "alice@gmail.com",
    "tier": "gold",
    "ytd_spend": 1500
}

print("Exercise 1")
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# Exercise 2: Update and Add

print("\nExercise 2")

customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


# Exercise 3: Safe Lookup

print("\nExercise 3")

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")


# Exercise 4: Iterate

print("\nExercise 4")

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only gives the keys.
for key in customer:
    print(key)


# Exercise 5: Lookup Table

print("\nExercise 5")

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)
price = 200
final_price = price * (1 - discount)

print(f"Tier: {tier}")
print(f"Discount: {discount:.0%}")
print(f"Final price: ${final_price:.2f}")


# Exercise 6: List of Dicts

print("\nExercise 6")

customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Charlie", "tier": "silver"}
]

for person in customers:
    tier = person["tier"]
    discount = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount

    print(f"{person['name']}: {tier}, discount: ${discount_amount:.2f}")


# Exercise 7: Nested Catalog

print("\nExercise 7")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - {details['stock']} remaining")


# Exercise 8: Sales by Region

print("\nExercise 8")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
    print(f"{region}: ${sales_summary[region]:.2f}")
