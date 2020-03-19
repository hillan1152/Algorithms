#!/usr/bin/python

# import argparse
import math


def find_max_profit(prices):
    # BUY LOW NUMBER WITHIN AN ARRAY
    # SELL HIGH LATER IN THE ARRAY
    profit = []
    # CANNOT BUY AT THE VERY LAST DIGIT IN THE ARRAY
    # MUST SELL IF YOU MAKE IT TO THE LAST PART OF THE ARRAY
    for i in range(0, len(prices) - 1):
        buy = i
        for j in range(i + 1, len(prices)):
            if buy >= j:
                pass
            else:
                current_buy = prices[buy]
                current_sell = prices[j]
                profit.append(current_sell - current_buy)
    return max(profit)
    # LOOP THROUGH THE ARRAY, STARTING WITH THE FIRST NUMBER
    #       (POSSIBLY TRY WHILE LOOP IF BUY != PRICES[-1])
    #   LOOP AGAIN TO GET NEXT NUM IN ARRAY›
    #     CALCULATE THE DIFFERENCE BETWEEN THE FIRST AND NEXT LOOPED NUMBER
    #     DO IT FOR THE ENTIRE ARRAY

# Other Approach
# def find_max_profit(prices):
#     profits = []
#     for i in range(0, len(prices)-1):
#         buy = i
#         for j in range(i+1, len(prices)):
#             current_sell = prices[j]
#             current_buy = prices[buy]
#             profit = current_sell - current_buy
#             profits.append(profit)
#         return max(profits)


# QUICKER AND MOST EFFICIENT
# def find_max_profit(prices):
#     current_min_price = prices[0]
#     max_prof = prices[1] - current_min_price
#     for i in range(1, len(prices)):
#         price = prices[i]
#         max_prof = max(price - current_min_price, max_prof)
#         current_min_price = min(price, current_min_price)
#     return max_prof


# find_max_profit([1050, 270, 1540, 3800, 2])
print(find_max_profit([1050, 270, 1540, 3800, 2]))
# print(find_max_profit([1050, 270, 1540, 3800, 2]))
# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(
#         description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int,
#                         nargs='+', help='an integer price')
#     args = parser.parse_args()

#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))
