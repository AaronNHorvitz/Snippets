def dataframe_statistics(df,plot_data = 'yes'):
    
    #Import dependencies
    import pandas as pd
    import numpy as np
    import datetime as dt
    import time
    import matplotlib
    from matplotlib import pyplot as plt
    from matplotlib import rcParams
    
    #Set matplotlib to plot inline
    %matplotlib inline
    

    
    def data_quality_plot(statistics,title='Total Count In Each Column'):
    

        rcParams['figure.figsize'] = 14, round(len(statistics)/2,0)
        statistics        = statistics.sort_values('Count', ascending = True)
        value_counts      = statistics['Count']
        nans              = statistics['NaNs']
        total             = statistics['NaNs']+statistics['Count']
        zeros             = statistics['Zeros']

        column_statistics = statistics['Column'].str.wrap(27)  #to set max line width of 27

        ten_percent       = total.max()*.10

        ylabel = 'Column Statistics'
        xlabel = 'Count'
        title = title
        horizontalalignment = 'left'

        plt.barh(column_statistics, value_counts, color = 'lavender',align = 'center',edgecolor='darkgrey')
        plt.barh(column_statistics, nans, color = 'lightgreen',align = 'center',edgecolor='black',alpha=0.45)
        plt.barh(column_statistics, zeros, color = 'sandybrown',align = 'center',edgecolor='darkgrey')
        plt.axvline(x=ten_percent,color='brown',linewidth = 1.4, linestyle  = 'dashdot')
        
        plt.xticks(rotation=45,fontsize = 12,fontweight='light',color = 'darkblue')
        plt.yticks(fontsize = 12, fontweight='light',color = 'darkblue',horizontalalignment = 'right',wrap=True)
        plt.xlabel(xlabel,fontsize=12)
        plt.title(title,fontsize=15,fontweight='light')

        
        #Label text on each horizontal bar plot
        for i, v in enumerate(value_counts):
            plt.text(v + 3, i-.2, str(v), color='navy', fontsize = 12, fontweight='light')

        #Label text on each horizontal bar plot
        for i, v in enumerate(zeros):
            plt.text(v + 3, i-.2, str(v), color='sienna', fontsize = 12, fontweight='light')

        #Label text on each horizontal bar plot
        for i, v in enumerate(nans):
            plt.text(v + 3, i-.2, str(v), color='darkgreen', fontsize = 12, fontweight='light')

            
        category = ['10% Marker','Count of Values','NaNs Count','Zeros  Count']
        plt.legend(category, loc = 1)
        plt.show()

        return 

    #Declare a list column types
    boolean_categories                 = ['bool_','bool8']
    integer_categories                 = ['byte','short','intc','int_','longlong','intp','int8','int32','int64']
    unsigned_integer_categories        = ['ubyte','ushort','uintc','uint','ulonglong','uintp','uint8','uint16','uint32','uint64']
    floating_point_categories          = ['half','single','double','float_','longfloat','float16','float32','float64']
    complex_floating_point_categories  = ['csingle','complex','clongfloat','complex64','complex128']
    object_categories                  = ['object_']
    void_categories                    = ['void']
    datetime_categories                = ['datetime64[ns]','datetime64','datetime32[ns]','datetime[32]']
    timedelta_categories               = ['timedelta[ns]','timedelta32[ns]','timedelta64','timedelta32']

    #Name and Data Type
    name_list  = []
    dtype_list = []

    #Value Counts
    count_list = []
    unique_count_list = []
    
    #Missing Values Lists- Initialize multple lists
    null_list = []
    zero_list = []
    percent_nulls_list = []
    percent_zeros_list = []

    #Summary Statistics Lists - Initialize multiple lists
    sum_list   = []
    mean_list  = []
    mad_list   = []
    median_list = [] 
    mode_list = []
    min_list = []
    max_list = []
    upper_quartile_list = []
    lower_quartile_list = []
    std_list = []
    var_list = []
    sem_list = []
    skew_list = [] 
    kurtosis_list = []

    #_____________Actions on each list____________________

    #Send the columns to a list
    name_list = df.columns.tolist()

    #Put all the datatypes into a list
    for column_name in name_list:

        #Create the data type
        if   df[column_name].dtypes in boolean_categories: dtype = 'Boolean'
        elif df[column_name].dtypes in integer_categories: dtype = 'Integer'
        elif df[column_name].dtypes in floating_point_categories: dtype = 'Float'
        elif df[column_name].dtypes in complex_floating_point_categories: dtype = 'Complex Float'
        elif df[column_name].dtypes in object_categories: dtype = 'Object'
        elif df[column_name].dtypes in datetime_categories: dtype = 'DateTime'    
        elif df[column_name].dtypes in timedelta_categories: dtype = 'TimeDelta' 
        else: dtype = 'Unknown' 

        #Create value counts
        num_rows      = len(df[column_name])
        count         = df[column_name].count()
        unique_count  = df[column_name].nunique()
        null_count    = df[column_name].isnull().sum()
        zero_count    = (df[column_name]==0).sum()
        percent_nulls = round((null_count/num_rows)*100,2) 
        percent_zeros = round((zero_count/num_rows)*100,2)
    
        #Append the statistics to a list
        dtype_list.append(dtype)
        count_list.append(count) 
        unique_count_list.append(unique_count)
        null_list.append(null_count)
        zero_list.append(zero_count)
        percent_nulls_list.append(percent_nulls)
        percent_zeros_list.append(percent_zeros)

    for column_name in name_list:

        if ((df[column_name].dtypes in integer_categories) | (df[column_name].dtypes in floating_point_categories)):

        #Create summary statistics
            summation     = round(df[column_name].sum(),3)          #Sum of the column
            mean          = round(df[column_name].mean(),3)         #Mean 
            mad           = round(df[column_name].mad(),3)          #Mean Absolute Deviation
            median        = round(df[column_name].median(),3)       #Median
            mode          = round(df[column_name].mode(),3)         #Mode
            minimum       = round(df[column_name].min(),3)          #Minimum
            maximum       = round(df[column_name].max(),3)          #Maximum
            upper_quartile = round(df[column_name].quantile(.75),3) #Upper Quartile
            lower_quartile = round(df[column_name].quantile(.25),3) #Lower Quartile
            std           = round(df[column_name].std(),3)          #Standard Deviation
            variance      = round(df[column_name].var(),3)          #Variance
            sem           = round(df[column_name].std(),3)          #Standard Error of the Mean 
            skew          = round(df[column_name].skew(),3)         #Skewness
            kurtosis      = round(df[column_name].kurt(),3)         #Kurtosis
        
        else:
            summation     = None
            mean          = None
            mad           = None
            median        = None
            mode          = None
            minimum       = None
            maximum       = None
            upper_quartile = None
            lower_quartile = None
            std           = None
            variance      = None
            sem           = None 
            skew          = None
            kurtosis      = None
        
        sum_list.append(summation)
        mean_list.append(mean)
        mad_list.append(mad)
        median_list.append(median)
        mode_list.append(mode)
        min_list.append(minimum)
        max_list.append(maximum)
        upper_quartile_list.append(upper_quartile)
        lower_quartile_list.append(lower_quartile)
        std_list.append(std)
        var_list.append(variance)
        sem_list.append(sem)
        skew_list.append(skew)
        kurtosis_list.append(kurtosis)
        
        
    statistics_dictionary = {'Column': name_list,
                             'Data Type': dtype_list,
                             'Count': count_list,
                             'Count of Unique Values': unique_count_list,
                             'NaNs':  null_list,
                             'Zeros': zero_list,
                             'NaN Percentage': percent_nulls_list,
                             'Zero Percentage': percent_zeros_list,
                             'Sum':sum_list,
                             'Mean':mean_list,
                             'Median':median_list,
                             'Maximum':max_list,
                             'Minimum':min_list,
                             'Upper Quartile':upper_quartile_list,
                             'Lower Quartile':lower_quartile_list,
                             'Standard Deviation':std_list,
                             'Variance':var_list,
                             'Mean Absolute Deviation':mad_list,
                             'Standard Error':sem_list,
                             'Skew':skew_list,
                             'Kurtosis':kurtosis_list
                            }
    statistics = pd.DataFrame(statistics_dictionary)
    statistics = statistics.sort_values('Count', ascending = False)
    
    if plot_data == 'yes':
        
        object_statistics = statistics.loc[statistics['Data Type']=='Object']
        float_statistics = statistics.loc[statistics['Data Type']=='Float']
        integer_statistics = statistics.loc[statistics['Data Type']=='Integer']


        if len(object_statistics) > 0:
            data_quality_plot(object_statistics,'Quality of the Object Data')
        else: pass
        
        if len(float_statistics) > 0:
            data_quality_plot(float_statistics,'Quality of the Float Data')
        else: pass
    
        if len(integer_statistics) > 0:
            data_quality_plot(integer_statistics,'Quality of the Integer Data')
        else: pass    
    
        
        statistics.head()
        return statistics
    
    else: 
    
        return statistics
