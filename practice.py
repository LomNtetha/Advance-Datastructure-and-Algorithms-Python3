def make_denominations(denominations,amount):

    denominations.sort(reverse = True)
    list_coin = []
    num_coins = 0

    for coin in denominations:

        if coin <= amount:
            num_coins +=1
            list_coin.append(coin)
            amount -=coin
           

    return list_coin, num_coins

denominations = [25, 16,10, 5, 1]
amount = 41  # Target amount in cents

list_oin, nums_coin = make_denominations(denominations, amount)
print(list_oin)
print(nums_coin)