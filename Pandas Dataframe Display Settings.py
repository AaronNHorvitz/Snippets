# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:33:46 2019

@author: ahorvitz
"""
"""
When writing df.head() to display pandas data, it's annoying to see the data bunched up.
This code, written in a jupyter notebook, will hopefully alleviate some of that concern. 
"""

import pandas as pd
pd.options.display.max_rows = 100        #Increases the number of rows displayed without a break in the middle.
pd.options.display.max_columns = 100     #Increases the number of columns displayed without a break in the middle.
pd.set_option('max_colwidth',100)        #Increases the width of the columns to display 100 characters at the same time.
