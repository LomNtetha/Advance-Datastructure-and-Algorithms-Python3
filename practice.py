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