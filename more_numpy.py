"""Some exercises that can be done with numpy (but you don't have to)"""
import numpy as np


def all_unique_chars(string):
    """
    Write a function to determine if a string is only made of unique
    characters and returns True if that's the case, False otherwise.
    Upper case and lower case should be considered as the same character.

    Example:
    "qwr#!" --> True, "q Qdf" --> False

    :param string: input string
    :type string:  string
    :return:      true or false if string is made of unique characters
    :rtype:        bool
    """

    x = np.full((0, ), 0)
    string = string.lower()
    for i in string:
        x = np.append(x, i)
    y = np.unique(x, return_counts=True)[1]
    return bool(np.all(y <= 1))


def find_element(sq_mat, val):
    """
    Write a function that takes a square matrix of integers and returns the
    position (i,j) of a value. The position should be returned as a list of two
    integers. You need to return only one position. if the value is present
    multiple times, a single valid position should be returned.

    The matrix is structured in the following way:
    - each row has strictly decreasing values with the column index increasing
    - each column has strictly decreasing values with the row index increasing
    The following matrix is an example:

    Example:
    mat = [ [10, 7, 5],
            [ 9, 4, 2],
            [ 5, 2, 1] ]
    find_element(mat, 4) --> [1, 1]

    The function should raise an exception ValueError if the value isn't found.

    :param sq_mat: the square input matrix with decreasing rows and columns
    :type sq_mat:  numpy.array of int
    :param val:    the value to be found in the matrix
    :type val:     int
    :return:      the position of the value in the matrix
    :rtype:        list of int
    :raise ValueError:
    """

    if val in sq_mat:
        return list(np.argwhere(sq_mat == val)[0])
    else:
        raise ValueError


def filter_matrix(mat):
    """
    Write a function that takes an n x p matrix of integers and sets the rows
    and columns of every zero-entry to zero.

    Example:
    [ [1, 2, 3, 1],        [ [0, 2, 0, 1],
      [5, 2, 0, 2],   -->    [0, 0, 0, 0],
      [0, 1, 3, 3] ]         [0, 0, 0, 0] ]

    The complexity of the function should be linear in n and p.

    :param mat: input matrix
    :type mat:  numpy.array of int
    :return:   a matrix where rows and columns of zero entries in mat are zero
    :rtype:    numpy.array
    """
    mat_c = mat[:]
    temp_r = set()
    temp_c = set()
    for i in np.argwhere(mat == 0):
        temp_r.add(i[0])
        temp_c.add(i[1])
    for i in temp_r:
        mat_c[i] = 0
    for j in temp_c:
        mat_c[:, j] = 0
    return mat_c


def largest_sum(intlist):
    """
    Write a function that takes in a list of integers,
    finds the sublist of contiguous values with at least one
    element that has the largest sum and returns the sum.
    If the list is empty, 0 should be returned.

    Example:
    [-1, 2, 7, -3] --> the sublist with larger sum is [2, 7], the sum is 9.

    Time complexity target: linear in the number of integers in the list.

    :param intlist: input list of integers
    :type intlist:  list of int
    :return:       the largest sum
    :rtype:         int
    """
    r = []
    for w in range(1, len(intlist)+1):
        for i in range(len(intlist)-w+1):
            r.append(intlist[i:i+w])
    x = [sum(i) for i in r]
    if not x:
        return 0
    else:
        return max(x)


def pairprod(intlist, val):
    """
    Write a function that takes in a list of positive integers (elements > 0)
    and returns all unique pairs of elements whose product is equal to a given
    value. The pairs should all be of the form (i, j) with i<=j.
    The ordering of the pairs does not matter.

    Example:
    ([3, 5, 1, 2, 3, 6], 6) --> [(2, 3), (1, 6)]

    Complexity target: subquadratic

    :param intlist: input list of integers
    :type intlist:  list of int
    :param val:     given value products will be compared to
    :type val:      int
    :return:       pairs of elements such that the product of corresponding
                    entries matches the value val
    :rtype:         list of tuple
    """
    l_1 = list(set(intlist))
    r = [(i, j) for i in l_1 for j in l_1 if i * j == val]
    r_f = list(set([tuple(sorted(i)) for i in r]))
    return r_f

    


