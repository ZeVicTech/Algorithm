import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    stock_prices = list(map(int, input().rstrip().split()))

    profit = 0
    max_price = stock_prices[-1]
    for price in stock_prices[::-1]:
        if max_price < price:
            max_price = price
            continue
        profit += max_price - price

    print(profit)
