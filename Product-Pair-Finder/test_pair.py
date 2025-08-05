from product_pair import find_pair_with_budget

prices = [1500, 3000, 4500, 6000, 7500, 9000, 10500]  # Sorted product prices (₦)
budget = 10500  # Customer's bundle budget

pairs = find_pair_with_budget(prices, budget)

if pairs:
    print(f"Found the following bundles")
    for l,r in pairs:
      print(f"{l} +{r} = {budget}")
        
else:
    print("No bundle found within budget.")