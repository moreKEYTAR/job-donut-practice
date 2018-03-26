

#  Interiew cake, exercise 1 ##############################################
def get_max_profit(prices_lst):
    """Takes in list of prices where index is minutes after 9:30.
    Returns greatest profit possible for one share, without 'shorting'.

    >>> stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
    >>> get_max_profit(stock_prices_yesterday)
    6

    >>> stock_prices_yesterday = [12, 7, 5, 8, 11, 4]
    >>> get_max_profit(stock_prices_yesterday)
    6

    """

    max = prices_lst[-1]
    min = prices_lst[0]
    # It doesn't work if the last item in the list is the lowest, and doesn't
    # work if the first item is the highest.
    for i, price in enumerate(prices_lst):

        if i > 0 and price > max:
            max = price
        if i < len(prices_lst) - 1 and price < min:
            min = price

    return max - min


if __name__ == "__main__":
    import doctest

    result = doctest.testmod(verbose=True)
    if not result.failed:
        print "\nTESTS PASSED."
