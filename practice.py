def denominations_coin(denominations, amount):

    denominations.sort(reverse= True)

    coin_used = []
    coin_count = 0

    for coin in denominations:
     
     if coin <= amount:

        coin_used.append(coin)
        coin_count += 1
        amount-= coin

    return coin_count, coin_used    


denominations = [25, 16,10, 5, 1]

amount = 41

total_denominations, used_coin = denominations_coin(denominations, amount)

print(total_denominations)

print(used_coin)
