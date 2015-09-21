# -*- coding: utf-8 -*-

"""
Histobin library
~~~~~~~~~~~~~~~~~~~~~
Histobin is a library to make bin width selection for histograms
extremely simple. Basic usage:
   >>> import pandas as pd
   >>> from histobin import Histobin
   >>> hb = Histobin(df.column)
   >>> df.column.plot(kind='hist', bins=hb.sqrt)

Other methods of selecting bin widths are supported.
"""

from .main import Histobin
