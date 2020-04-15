#!/usr/bin/python

import argparse

# UNDERSTAND:
# BOT FOCUSES ON BUYING AND SELLING AMAZON STOCK
# FUNCTION: receives a LIST of stock prices. Returns the max profit that can be made from a single buy/sell

# find difference b/t smallest and largest prices in the list.
# anything purchased before is the BUY, anything after will be sold
# subtract 1st num by 2nd



# PLAN
def find_max_profit(prices):
    #  DECLARE Max_profit to keep track of maximum profit available
    max_profit = 0
    # LOOP through all items in the array besides the last
    for i in range(0, len(prices)):
        #   DECLARE variable to keep track of Current Buy = Curr_Buy
        curr_buy = i
        j = curr_buy + 1
    #   LOOP to get all SELL points:
        while j > curr_buy and j < len(prices):
            curr_sell = j
            curr_profit = prices[curr_sell] - prices[curr_buy]
            if curr_profit > max_profit:
                max_profit = curr_profit
            j += 1
    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()
    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
