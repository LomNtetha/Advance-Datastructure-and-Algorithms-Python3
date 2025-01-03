def coin_denominations(denominations,amount):

    denominations.sort(reverse=True)

    count = 0
    coin_used = []

    for coin in denominations:
        while coin <= amount:
            coin_used.append(coin)
            count+=1
            amount-=coin
    return count, coin_used

denominations = [16,10, 5, 25,1]
amount = 41 

number_of_cois, coin_used = coin_denominations(denominations,amount)

print(f"Here is coin used: {coin_used}")

print(f"Here is coin used:{number_of_cois}")