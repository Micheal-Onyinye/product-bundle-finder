# product_pair.py

# The goal is to find two product prices that add up to a given budget
# Real-World application: E-commerce app finding bundle suggestions



def find_pair_with_budget(prices, budget):
    # given a sorted listof product prices and a budget,it returns the pairs of prices that add up to the budget.

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



