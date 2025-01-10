from typing import List


def max_denominations(denominations,amount):

    denominations.sort(reverse=True)

    coin_used = []
    number_coin = 0

    for coin in denominations:
        if coin <= amount:
            coin_used.append(coin)
            number_coin += 1
            amount -= coin
    return coin_used, number_coin
denominations = [25, 10, 5, 16,1]
# Example usage
amount = 41  # Target amount in cents

c, n = max_denominations(denominations, amount)

print(f"here is the coin used: {c}")
print (f"here is the number of coins {n}")


def max_activities(start,end):

    activities = list(zip(start,end))

    activities.sort(key=lambda x:x[1])

    selected_activities = [0]
    last_end_time = activities[0][1]
    count = 1

    for i in range(1, len(activities)):
        if activities[i][0] >= last_end_time:
            selected_activities.append(i)
            count+=1
            last_end_time = activities[i][1]
    return count, selected_activities
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]

s,e = max_activities(start,end)
print(s)
print(e)

class Solution:
    def fractional_knapsack(self, weights: List[int], values: List[int], capacity: int) -> float:
        # Step 1: Zip values and weights together
        zipped_items = zip(values, weights)
        
        # Step 2: Calculate value-to-weight ratios and create a list of tuples
        items_with_ratios = [(v / w, w) for v, w in zipped_items]
        
        # Step 3: Sort the items by value-to-weight ratio in descending order
        items = sorted(items_with_ratios, reverse=True)
        
        total_value = 0.0  # Total value accumulated in the knapsack
        
        # Iterate through sorted items
        for value_per_weight, weight in items:
            # If the current item fits fully in the knapsack, take it
            if capacity >= weight:
                total_value += value_per_weight * weight
                capacity -= weight
            else:
                # If only a fraction of the item fits, take the fraction and stop
                total_value += value_per_weight * capacity
                break
        
        # Return the maximum value that can be taken
        return total_value
    
# Example usage:
solution = Solution()
weights = [10, 20, 30]  # Weights of items
values = [60, 100, 120]  # Values of items
capacity = 50  # Capacity of the knapsack

# Call the fractional_knapsack method
max_value = solution.fractional_knapsack(weights, values, capacity)

# Print the result
print(f"Maximum value in the knapsack: {max_value}")

# pm2 start dist/app.js --name "app-mysosevba" && pm2 start dist/workers.js --name "workers-mysosevba" && pm2 start dist/api.js --name "api-mysosevba" && pm2 start dist/mirror.js --name "mirror-mysosevba"