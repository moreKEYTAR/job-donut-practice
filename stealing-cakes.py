# coding: utf-8
"""

Write a function max_duffel_bag_value() that takes a list of cake type tuples 
and a weight capacity, and returns the maximum monetary value the duffel 
bag can hold.

Weights and values may be any non-negative integer. Yes, it's weird to think 
about cakes that weigh nothing or duffel bags that can't hold anything. 
But we're not just super mastermind criminals—we're also meticulous about 
keeping our algorithms flexible and comprehensive.
(kg, shillings)

    >>> cake_tuples = [(7, 160), (3, 90), (2, 15)]
    >>> capacity = 20
    >>> max_duffel_bag_value(cake_tuples, capacity)
    555

    >>> cake_tuples = [(7, 160), (0, 90), (2, 15)]
    >>> capacity = 20
    >>> max_duffel_bag_value(cake_tuples, capacity)
    'Infinity'

        Former answer:
        'The 90 shilling cake is 0 kg. Duffel can hold infinity cakes of that value!'

    >>> cake_tuples = [(7, 160), (3, 90), (2, 15)]
    >>> capacity = 0
    >>> max_duffel_bag_value(cake_tuples, capacity)
    0

    >>> cake_tuples = [(7, 160), (3, 0), (2, 15)]
    >>> capacity = 20
    >>> max_duffel_bag_value(cake_tuples, capacity)
    365


    Note:
    For above return string, this may not be what is desired in this case...unspecified.

SIGNATURE:

    function(list, integer)
        - list is full of integer tuples representing kilograms, shillings
        - integer represents container capacity, in kilograms

        return integer representing shillings

STRATEGY:

    Calculate the shillings per kilogram value of each cake, store in a 
    dictionary with the value that is the tuple index number. I need to make
    this a float to stay accurate, and but round shillings for output.

    Before that, it should check whether the duffel capacity is 0 (if so return 0)

    Needs to account for when the cakes have 0 mass/weight (when tuple at 0 is 0),
    so there is no zero division.

"""

###### VERSION 1 ######

def max_duffel_bag_value(cake_tuples, capacity):

    if capacity == 0:
        return capacity

    # Make the shillings value a float for float division in Python 2.7
    cake_tuples = [(item[0], float(item[1])) for item in cake_tuples]

    for i, n in enumerate(cake_tuples):
        try:
            value_per_cake = n[1] / n[0]
            # will result in zero denominator if kg for a cake is 0; see except
        except:
            # NEED TO LEARN HOW TO HANDLE DOCTEST FOR VARIABLE OUTPUT..... HERE
            # print """The {num:.0f} shilling cake is 0 kg. Duffel can hold infinity cakes of that value!""".format(num=n[1])
            # May need to modify to integer value returned, or other spec
            value_per_cake = "Infinity"
            cake_tuples[i] = (n[0], n[1], value_per_cake)
        else:
            cake_tuples[i] = (n[0], n[1], value_per_cake)
            # Tuples in the list are now:
                # (kg per cake, shillings per cake, shillings per kg)

    cake_tuples.sort(key=lambda item: item[2], reverse=True)
    # https://stackoverflow.com/questions/37914387/python-sort-using-key-and-lambda-what-does-lambda-do
    # This orders each tuple by the most profitable cake, to try to add as many of those as possible.
    # If a cake has infinite value because it is weightless, this will sort to the front because it is a string

    total_shillings = 0

    for i in xrange(len(cake_tuples)):

        if isinstance(cake_tuples[i][2], str) and cake_tuples[i][1] != 0:
        # could also check whether the [0] in tuple is == 0, for 0 kg per cake)
            return cake_tuples[i][2]

        elif cake_tuples[i][0] <= capacity and cake_tuples[i][2] > 0:
        # checks to make sure the cake is smaller than the capacity left,
        # and that the cake has any monetary value at all (otherwise why bother)
            cakes, remaining_capacity = divmod(capacity, cake_tuples[i][0])
            # In one line, generates a tuple (num cakes can fit, remaining capacity)
            # and unpacks it.
            total_shillings += cakes * cake_tuples[i][1]
            capacity = remaining_capacity

    return int(round(total_shillings, 0))


if __name__ == "__main__":
    import doctest
    # result = doctest.testmod(verbose=True)
    # if not result.failed:

    if doctest.testmod(verbose=True).failed == 0:
        print "\n *** TESTS PASSED ***"
