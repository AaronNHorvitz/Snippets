def screen_floats(df):
    floating_point_categories          = ['half','single','double','float_','longfloat','float16','float32','float64']
    
    column_name_list = df.columns.to_list()
    float_column_list = []
    for name in column_name_list:
        if df[name].dtypes in floating_point_categories:
            float_column_list.append(name)
        else: pass
    df = df[float_column_list]
    return df

def nan_zero_count(df,screen=False,nan_percent = .20, zero_percent = .20):      #Returns a data frame with the total number of NaNs in each column of data. 
    value_count = len(df)
    df.loc['Total NaNs']    = df.isnull().sum()                              #Create a 'Total NaNs' row on the bottom of the data frame
    df.loc['Total Zeros']   = (df == 0).sum()
    df.loc['Percent NaNs']  = round((df.isnull().sum())/value_count,2)
    df.loc['Percent Zeros'] = round(((df == 0).sum())/value_count,2)
    df = df.sort_values(by = 'Total NaNs', axis = 1, ascending = False)   #Order the data frame to look at least to greatest
    columns_list = df.columns.tolist()
    df = df.iloc[-4:]
    
    
    #Screen out zeros and Nans
    
    if screen == True:
        nan_variables_column_list      = df.columns[df.iloc[2,]<=nan_percent]
        df                             = df[nan_variables_column_list]
        zero_variables_column_list     = df.columns[df.iloc[3,]<=zero_percent]
        df                             = df[zero_variables_column_list]
        
    else:  pass
                                            
    return(df)                          #View the total number of NaN values by each column.

def PCA_graph_2D(data,                     #Dataframe with the data in it
                 components,               #Name of the two principal components to graph in a list format [pc1,pc2]
                 color_map='Set2_r',       #Optional color map scheme
                 transparency = 1,         #Optional bubble transparency level
                 bubble_size = 60,         #Optional bubble size
                 height = 10,              #Optional figure height setting
                 width  = 10,              #Optional figure width setting
                 target_categories = []):   #Name of the target categorical column list format ['target']

    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt
    from matplotlib import rcParams
    %matplotlib inline

  
    principal_component_0 = components[0]
    principal_component_1 = components[1] 
    
    column_list = target_categories+components
    
    df = data[column_list]    #Create a dataframe for graphing that has only the necessary columns
    
    #Convert the target column to numberical target codes to color code them (required by Matplotlib)...


    if target_categories == []:
        color_list = 'black'
    else:
        df['num_categories'] = df[target_categories]                     #Convert the target column to a categorical data type in pandas
        df['num_categories'] = df['num_categories'].astype('category')
        df['num_categories'] = df['num_categories'].cat.codes             #Assign a new column the numerical categorical codes
        color_list = df['num_categories'].tolist()                        #Assign those numbers to a list for Matplotlib to use 

    rcParams['figure.figsize'] = height,width
    plt.scatter(df[principal_component_0],
                df[principal_component_1],
                c=color_list, 
                edgecolor='none', 
                alpha = transparency,
                cmap=color_map,
                s=bubble_size)
    
    #Label the axes
    plt.xlabel('Component 1')
    plt.ylabel('Component 2')
    plt.title('Principal Component 1 by Principal Component 2')    
    plt.legend()
    plt.show()
    
    return

def PCA_graph_3D(data,                     #Dataframe with the data in it
                 components,               #Name of the first principal component column in quotes 'Principal Component 0'
                 color_3d_axis_lines = 'r',#Optional color settings for 3D axis lines
                 color_map='Set2_r',       #Optional color map scheme
                 transparency = 1,         #Optional bubble transparency level
                 bubble_size = 60,         #Optional bubble size
                 height = 14,              #Optional figure height setting 
                 width = 14,               #Optional figure width setting
                 target_categories = []):   #Name of the target categorical column list format ['target']):              
    
    import pandas as pd
    import numpy as np
    from matplotlib import pyplot as plt
    from matplotlib import rcParams
    from mpl_toolkits.mplot3d import Axes3D

    principal_component_0 = components[0]
    principal_component_1 = components[1] 
    principal_component_2 = components[2] 
    
    column_list = target_categories+components
    
    df = data[column_list]    #Create a dataframe for graphing that has only the necessary columns
    
    #Convert the target column to numberical target codes to color code them (required by Matplotlib)...


    if target_categories == []:
        color_list = 'black'
    else:
        df['num_categories'] = df[target_categories]                     #Convert the target column to a categorical data type in pandas
        df['num_categories'] = df['num_categories'].astype('category')
        df['num_categories'] = df['num_categories'].cat.codes             #Assign a new column the numerical categorical codes
        color_list = df['num_categories'].tolist()                        #Assign those numbers to a list for Matplotlib to use 

    
    # Plot initialisation
    rcParams['figure.figsize'] = height,width
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df[principal_component_0],
               df[principal_component_1],
               df[principal_component_2],
               c = color_list,
               alpha = transparency,
               cmap='Set2_r',
               s = bubble_size)

    # make simple, bare axis lines through space:
    xAxisLine = ((min(df[principal_component_0]), max(df[principal_component_0])), (0, 0), (0,0))
    ax.plot(xAxisLine[0], xAxisLine[1], xAxisLine[2], color_3d_axis_lines)
    yAxisLine = ((0, 0), (min(df[principal_component_1]), max(df[principal_component_1])), (0,0))
    ax.plot(yAxisLine[0], yAxisLine[1], yAxisLine[2], color_3d_axis_lines)
    zAxisLine = ((0, 0), (0,0), (min(df[principal_component_2]), max(df[principal_component_2])))
    ax.plot(zAxisLine[0], zAxisLine[1], zAxisLine[2], color_3d_axis_lines)

    # label the axes
    ax.set_xlabel('Component 1')
    ax.set_ylabel('Component 2')
    ax.set_zlabel('Component 3')
    
    plt.show()
                 
    return

def Normalize(data,                                   #Data frame source df
              variable_list,                          #List of columns to normalize 
              target_column = False,):                #List of target variables if needed.

    
    import scipy.stats as st
    
    df = data[variable_list]
    column_list = df.columns.to_list()
    #Create the residuals column, normalized residuals, the Z Score, and Normalized Residuals by Percent for later analysis. 

    for name in column_list:
        
        norm_name    = 'Normalized_'+str(name)
        z_name       = 'Zscore_'+str(name)
        percent_name = 'Perc_Normal'+str(name) 
        
        df[norm_name] = (df[name]-df[name].mean())/(df[name].max()-df[name].min())
        df[z_name] = (df[norm_name] - df[norm_name].mean())/df[norm_name].std(ddof=0)
        df[percent_name] = df[z_name].apply(lambda x: st.norm.cdf(x))
        
        df = df.drop(columns=[name,norm_name, z_name])     #This leaves only the normalized columns.!!!
                                                           #This can be appended to the original dataframe if needed....

    
    if target_column != False:                             #Reorder the columns so the target column if first in the list.
        df[target_column] = data[target_column]
        column_list = df.columns.to_list()
        column_list = [column_list[-1]] + column_list[:-1]
        df = df[column_list]
        return df
    
    else:
        return df
    
    return df



def PCA(data,                              #Dataframe source usually denoted as df
        target_column):               #The name of the target column with classifiers:  example 'target'

    from sklearn.decomposition import PCA
    from sklearn.preprocessing import scale
    
    df                     = data.copy()
    df                     = df.dropna()          #DROPS ALL ROWS WITH NAN values since PCA can't be conducted with NaN values.
    
    column_list            = df.columns.to_list()

    variable_list = column_list.copy()
    
    for x in target_column:
        if x in variable_list:
            variable_list.remove(x)
    
    target_columns = df[target_column]
    variables      = df[variable_list]
    
    X = variables.values
    X = scale(X)
    pca = PCA(n_components=8)
    pca.fit(X)
    principal_components=pca.fit_transform(X)
    
    var = pca.explained_variance_ratio_
    principal_df = pd.DataFrame(data = principal_components)
    principal_df = principal_df.add_prefix('Principal Component ')
    df = df.drop(columns=variable_list)                  #This leaves only the principal components!!!
    df = pd.concat([df,principal_df],axis=1)
    rcParams['figure.figsize'] = 10, 10
    plt.plot(var)

    plt.show()
    
    return df
