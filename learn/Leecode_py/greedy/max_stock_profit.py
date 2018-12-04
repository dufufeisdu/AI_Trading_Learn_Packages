# mine:O(n^2)
# init max=0
# For each day:
# at this day i buy stock
# check the max profit
# if max_profit>max
# update max
# return max


def max_profit(stock_price):
    max_price = 0
    days = len(stock_price)
    for day in range(days - 1):
        max_p = max([stock_price[day] - stock_price[i]
                     for i in stock_price[day:]])
        if max_price < max_p:
            max_price = max_p
    return max_price
# Updated:
# 1 find the max price
# 2 from


def max_prifot_U(stock_price):
    if len(stock_price) < 2:
        return 0
    profit = 0
    min_stock_price = stock_price[0]
    for i in range(len(stock_price)):
        profit = max(profit, stock_price[i] - min_stock_price)
        min_stock_price = min(min_stock_price, stock_price[i])
    return profit


if __name__ == "__main__":
    tests = [[1, 3, 5, 7, 10, 11], [1, -3, 7, 2], [4, 3, 2, 1]]
    for test in tests:
        print(max_prifot_U(test))
