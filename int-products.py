"""Returning products of non-index values at that index.
Function name and parameter/argument have been given.

    >>> int_list = [1, 7, 3, 4]
    >>> print get_products_of_all_ints_except_at_index(int_list)
    [84, 12, 28, 21]

    >>> int_list = [1, 2, 6, 5, 9]
    >>> print get_products_of_all_ints_except_at_index(int_list)
    [540, 270, 90, 108, 60]

"""
# VERSION 1 #############################################

# def get_products_of_all_ints_except_at_index(int_list):

#     # Make a list of the products
#     products = []
#     for i in xrange(len(int_list)):
#         product = 1
#         for j, num in enumerate(int_list):
#             if j != i:
#                 product *= num
#         products.append(product)

#     return products


# VERSION 2 #############################################

## Started an idea here. Cannot figure out how to not hard code the index
# integers without another loop

# def get_products_of_all_ints_except_at_index(int_list):

#     # Make a list of the products
#     products = []

#     for i in xrange(len(int_list)):
#         # 0, 1, 2, 3
#         product = int_list[i - 1] * int_list[i - 2] * int_list[i - 3]
#         products.append(product)

#     return products


# VERSION 3 #############################################

def get_products_of_all_ints_except_at_index(int_list):

    # Make a list of the products

    # making a list of the left-side products:
        # Our "pointer" starts at value at index 0. Nothing is to the left,
        # so the first value is 1 (multiplication identity).
        # Our pointer ends when we "look" at the last to-the-left values;
        # the last value in the list has not been used yet.
    left_products = [1]
    for i in xrange(len(int_list) - 1):
        # 0, 1, 2
        left_products.append(left_products[-1] * int_list[i])

    # making a list of right-side products:
        # Our "pointer" starts on the far right/end of the list. There is
        # nothing to the right, so we start with 1 as our placeholder.
        # Our pointer moves backwards, to look at the second to last value;
        # this has one value to its right, which we add to our list.
    right_products = [1]
    for j in xrange((len(int_list) - 1), 0, -1):
        # 3, 2, 1
        right_products.append(right_products[-1] * int_list[j])
    # The right side was stepped through backwards and used appending and the
    # same indexing for lookup. Appending is more efficient, and therefore these
    # were "reversed" as they were appended. Using reverse to undo that "reversing"
    right_products.reverse()

    final_products = []
    for k in xrange(len(int_list)):
        final_products.append(left_products[k] * right_products[k])

    return final_products

if __name__ == "__main__":

    import doctest

    # result = doctest.testmod(verbose=True)
    # # results prints as TestResults(failed=0, attempted=4)
    # # print result, "is result"
    # # print type(result)
    # if not result.failed:
    #     print "\nTESTS PASSED."

    if doctest.testmod().failed == 0:
        print "*** TESTS PASSED ***"
