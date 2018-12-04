# multiple transctions, but sell before buy
# 1 imagine a cure of the sotck price
# 2 only sum the increase part of the cure


def max_profit(stock_price):
    n = len(stock_price)
    if n < 2:
        return 0

    profit = 0
    for i in range(n - 1):
        current = stock_price[i]
        nx = stock_price[i + 1]
        if nx > current:
            profit += (nx - current)
    return profit
