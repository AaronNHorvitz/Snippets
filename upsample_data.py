def upsample_data(X_train, y_train):
    
    from sklearn.utils            import resample
    #Obtain target column name 
    target_column_name = y.name
    
    # concatenate our training data back together
    X = pd.concat([X_train, y_train], axis=1)

    print('=======================================================================================')
    print('Here is a count of the unique target values in the TRAINING data set BEFORE upsampling.')
    print('=======================================================================================')

    values_dict    = {}                      #Create a dictionary for the target values and the value counts
    highest_value  = 0                       #Set the value for the higher count
    lowest_value   = np.inf                  #Set the value for the lower count
    values = X[target_column_name].value_counts()      #Put the value counts in a series.

    print('Index      Target | Count')
    for i in range(0,len(values)):
        print(i,'        ',values.index[i],'     |', values[values.index[i]])
    
    #Find the highest and lowest values
    highest_value   = values.max()
    lowest_value    = values.min()

    highest_target  = values.loc[values == highest_value].index[0]
    lowest_target   = values.loc[values == lowest_value].index[0]

    print('===================================================================================')
    print('Here is the highest and lowest value in the count.')
    print('===================================================================================')
    print('           Target | Count')

    print('Highest:  ',highest_target,'     |' ,highest_value)
    print('Lowest:   ',lowest_target, '     |' ,lowest_value)

    # upsample the training data ONLY......
    # separate minority and majority classes

    majority = X.loc[X[target_column_name] == highest_target]
    minority = X.loc[X[target_column_name] == lowest_target]

    # upsample minority
    minority_upsampled = resample(minority,
                                  replace = True,            # sample with replacement
                                  n_samples = len(majority), # match number in majority class
                                  random_state = 42)         # reproducible results

    # combine majority and upsampled minority
    upsampled = pd.concat([majority, minority_upsampled])

    # split the data back into target and feature data
    y_train = upsampled[target_column_name]
    X_train = upsampled.drop(target_column_name, axis=1)

    # calculate the number of each category in the upsampled amount to print
    values_after = upsampled[target_column_name].value_counts()      #Put the value counts in a series.

    #Find the highest and lowest values
    highest_value_after   = values_after.max()
    lowest_value_after    = values_after.min()

    highest_target_after  = values.loc[values == highest_value].index[0]
    lowest_target_after   = values.loc[values == lowest_value].index[0]

    # check new class counts
    print('======================================================================================')
    print('Here is a count of the unique target values in the TRAINING data set AFTER upsampling.')
    print('======================================================================================')
    print('           Target | Count')
    print('Highest:  ',highest_target_after,'     |' ,highest_value_after)
    print('Lowest:   ',lowest_target_after, '     |' ,lowest_value_after)
    
    return X_train, y_train
