def mincoindenominations(denominations,amount):

    count_coin = 0
    coin_used = []

    for coin in denominations:
        while coin <= amount:
            coin_used.append(coin)
            count_coin +=1
            amount -= coin
    return coin_used,count_coin


denominations = [25,12,10, 5, 1]
amount = 41  # Target amount in cents

used, count = mincoindenominations(denominations,amount)

print(used)
print(count)