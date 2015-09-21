# -*- coding: utf-8 -*-

"""
histobin.main
~~~~~~~~~~~~
This module implements the Histobin object.
"""
import pandas as pd
import numpy as np

class Histobin(object):
    """
    Computes varies optimal bin widths for a given Pandas Series

    :param column: Pandas Series object that will be plotted
    """
    def __init__(self, column):
        self.column = column

    @property
    def sqrt(self):
        """
        Returns optimal bin width using the square root choice
        """
        return np.sqrt(len(self.column))
