sandwich_orders = ["panner toast", "mayo toast", "veg toast"]

finished_sandwich = []

while sandwich_orders:
    preparing = sandwich_orders.pop()
    print(f"Currently cooking {preparing.title()}")
    
    finished_sandwich.append(preparing)
  
print(f"\nSandwiches ready to serve:")
  
for sandwich in finished_sandwich:
    print(sandwich)
          