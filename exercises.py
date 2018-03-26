#  Interiew Cake, Exercise 1 ##############################################

#### VERSION 1 ####

# def get_max_profit(prices_lst):
#     """Takes in list of prices where index is minutes after 9:30.
#     Returns greatest profit possible for one share, without 'shorting'.

#     >>> stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
#     >>> get_max_profit(stock_prices_yesterday)
#     6

#     >>> stock_prices_yesterday = [12, 7, 5, 8, 11, 4]
#     >>> get_max_profit(stock_prices_yesterday)
#     6

#     """

#     max = prices_lst[-1]
#     min = prices_lst[0]
#     # It doesn't work if the last item in the list is the lowest, and doesn't
#     # work if the first item is the highest.
#     for i, price in enumerate(prices_lst):

#         if i > 0 and price > max:
#             max = price
#         if i < len(prices_lst) - 1 and price < min:
#             min = price

#     return max - min


#### VERSION 2 ####
def get_max_profit(stock_prices):
    """Assuming a list of at least two values.

        >>> stock_prices = [10, 7, 5, 11, 9]
        >>> get_max_profit(stock_prices)
        6

        >>> stock_prices_yesterday = [12, 7, 5, 8, 11, 4]
        >>> get_max_profit(stock_prices_yesterday)
        6

        >>> stock_prices_yesterday = [12, 11, 10, 8, 5, 1]
        >>> get_max_profit(stock_prices_yesterday)
        -1

    """
    # Calculate the max profit
    profit = stock_prices[-1] - stock_prices[0]
    trend = None
    profits = [profit]

    for i in xrange(len(stock_prices) - 1):
        # i is 0, 1, 2, 3, if length is 5 (example)

        delta = stock_prices[i + 1] - stock_prices[i]

        if delta < 0:
            profits.append(profit)
            if delta > profit:
                profit = delta
            trend = "down"

        elif 0 < delta:
            if trend == "up":
                profit += delta
            #   if i + 1 == len(stock_prices) - 1:
            #       profits.append(profit)
            else:
                trend = "up"
                profit = delta
                # if i + 1 == len(stock_prices) - 1:
                #   profits.append(profit)
            if i + 1 == len(stock_prices) - 1:
                profits.append(profit)

        else:
            trend = "flat"
            if delta > profit:
                profit = delta

    return max(profits)


if __name__ == "__main__":
    import doctest

    result = doctest.testmod(verbose=True)
    if not result.failed:
        print "\nTESTS PASSED."
