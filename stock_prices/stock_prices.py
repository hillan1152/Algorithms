#!/usr/bin/python

# import argparse


def find_max_profit(prices):
    # BUY LOW NUMBER WITHIN AN ARRAY
    # SELL HIGH LATER IN THE ARRAY
    buy_low = []
    sell_high = []
    # CANNOT BUY AT THE VERY LAST DIGIT IN THE ARRAY
    # MUST SELL IF YOU MAKE IT TO THE LAST PART OF THE ARRAY
    for i in range(0, len(prices) - 1):
        if prices[i] < prices[i + 1]:
            buy_low.append(prices[i])
            print(buy_low)
        elif prices[i + 1] > prices[i]:
            sell_high.append(prices[i])
            print(sell_high)
    # LOOP THROUGH THE ARRAY, STARTING WITH THE FIRST NUMBER
    #       (POSSIBLY TRY WHILE LOOP IF BUY != PRICES[-1])
    #   LOOP AGAIN TO GET NEXT NUM IN ARRAY
    #     CALCULATE THE DIFFERENCE BETWEEN THE FIRST AND NEXT LOOPED NUMBER
    #     DO IT FOR THE ENTIRE ARRAY
    #
    #


print(find_max_profit([1050, 270, 1540, 3800, 2]))
# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(
#         description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int,
#                         nargs='+', help='an integer price')
#     args = parser.parse_args()

#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))
