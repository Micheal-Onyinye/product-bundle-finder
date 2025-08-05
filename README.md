# Product Pair Finder 

This project demonstrates a real-world use of the **two-pointer technique** to solve a common problem in e-commerce: finding all product price pairs that together match a user's budget.

Imagine you're building an online shop. A user wants to buy two products with a total budget of ₦10,500. You have a sorted list of product prices:

```python
prices = [1500, 3000, 4500, 6000, 7500, 9000, 10500]
```

You want to suggest all pairs of items that together exactly match their budget.

---

##  How It Works
We use **two pointers**:
- One starts at the beginning (`left`)
- The other at the end (`right`)

We keep checking the sum of the two prices:
- If it matches the target →  Save the pair
- If the sum is too small → Move `left` pointer right **`left` +=1(increase the index by 1)**
- If the sum is too big → Move `right` pointer left
**`right` -=1(decrease the index by 1)**

This continues until both pointers meet.

### Example:
Target: `10500`
- 1500 + 9000 → ✅
- 3000 + 7500 → ✅
- 4500 + 6000 → ✅

---

##  File Structure
```
two-pointer-projects/
└── product-pair-finder/
    ├── product_pair.py     # Main logic
    └── test_pair.py        # Where the function runs
```

---

## To Run It
```bash
python test_pair.py
```

 Sample Output:
```
 Found the following bundles:
 - 1500 + 9000 = 10500
 - 3000 + 7500 = 10500
 - 4500 + 6000 = 10500
```

---

##  The Code
```python
def find_pair_with_budget(prices, budget):

    left = 0
    right = len(prices) - 1
    results= []

    while left < right:
        the_sum = prices[left] + prices[right]

        if the_sum == budget:
            results.append((prices[left], prices[right]))
            left += 1
            right -= 1
        elif the_sum < budget:
            left += 1
        else:
            right -= 1

    return results
```

---

## Real-World Application
This logic is used in:
- E-commerce combo suggestions
- Price-based filters
- Budget-friendly product bundles
- Travel ticket combo planners

---

##  What I Learnt
- Two-pointers are powerful for **finding pairs** in sorted data
- Helps reduce time complexity compared to nested loops
- Easy to scale and reuse across projects (chat apps, filters, media tools)

---


