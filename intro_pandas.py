"""A set of pandas exercises"""


def filter_rep(df):
    """
    Write a function that takes a DataFrame with a colum `A` of integers and
    filters out the rows which contain the same value as a row above.
    Check that the index is right, use reset_index if necessary.

    Example:
        A   ...            A   ...
    ___________        ___________
    0 | 1 | ...        0 | 1 | ...
    1 | 1 | ...        1 | 0 | ...
    2 | 0 | ...  -->   2 | 5 | ...
    3 | 5 | ...        3 | 2 | ...
    4 | 5 | ...
    5 | 5 | ...
    6 | 2 | ...
    7 | 1 | ...

    :param df: input data frame with a column `A`
    :type df: pandas.DataFrame
    :return: a dataframe where rows have been filtered out
    :rtype: pandas.DataFrame
    """
    import pandas as pd
    df1: pd.Dataframe = df.drop_duplicates(subset='A', keep='first').reset_index(drop=True)
    return df1


def subtract_row_mean(df):
    """
    Given a DataFrame of numeric values, write a function to subtract the row
    mean from each element in the row.

    Example:
        A   B   C                A     B     C
    _____________         _____________________
    0 | 1 | 5 | 0    -->  0 | -1.0 | 3.0 | -2.0
    1 | 2 | 6 | 1         1 | -1.0 | 3.0 | -2.0

    :param df: input data frame
    :type df:  pandas.DataFrame
    :return:  a dataframe where each row is centred
    :rtype:   pandas.DataFrame
    """
    import numpy as np
    df1 = df.apply(lambda x: x-np.mean(df, axis=1), axis=0)
    return df1

