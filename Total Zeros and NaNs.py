def total_zeros(df):      #Returns a data frame with the total number of zeros in each column of data. 

    df.loc['Total Zeros']   = (df == 0).sum()                              #Create a 'Total Zero' row on the bottom of the data frame
    df = df.sort_values(by = 'Total Zeros', axis = 1, ascending = False)   #Order the data frame to look at least to greatest
    columns_list = df.columns.tolist()
    df = df[-1:]
#    df = df.astype(int)                                                    #Use this line of code to convert values to int
#    df.head()                                                              #Use this line of code to display the totals
    return(df)                                                             #View the total numbers of NaN values by each column.

def total_nans(df):      #Returns a data frame with the total number of NaNs in each column of data. 

    df.loc['Total NaNs']   = df.isnull().sum()                              #Create a 'Total NaNs' row on the bottom of the data frame
    df = df.sort_values(by = 'Total NaNs', axis = 1, ascending = False)   #Order the data frame to look at least to greatest
    columns_list = df.columns.tolist()
    df = df[-1:]
#    df = df.astype(int)                                                    #Use this line of code to convert values to int.
    df.head()                                                               #use this line of code to display the totals
    return(df)                                                             #View the total numbers of NaN values by each column.
    
