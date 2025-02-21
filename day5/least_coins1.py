coins = {10: 0, 5: 0, 2: 0, 1: 0}
price = int(input('Enter the price: '))
for i in coins.keys():
    coins[i] = price // i
    price %= i
for k, v in coins.items():
    print(f'{k} : {v} coins')       


