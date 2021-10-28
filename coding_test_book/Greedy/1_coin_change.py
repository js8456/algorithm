# 500, 100, 50, 10원
# 가장 적은 수의 동전으로 거스름을 제공하라


def num_coin(change=1260, coin_type=[500, 100, 50, 10]):
    n = 0
    for coin in coin_type:
        n += change // coin
        change %= coin

    return n


count_coin = num_coin()
count_coin

# 해당 방법은 큰 단위의 동전이 작은 단위의 배수로 이루어졌기 때문에 가능했음
