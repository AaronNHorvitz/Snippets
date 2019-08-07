#Define standard plots

def lineplot(x,y,xlabel,ylabel,title):
    rcParams['figure.figsize'] = 10, 5
    plt.plot(x,y,c = 'r')
    plt.xticks(rotation=45)
    plt.ylabel(ylabel,fontsize=14)
    plt.xlabel(xlabel,fontsize=14)
    plt.title(title,fontsize=14)
    plt.show()
    return

def scatterplot(x,y,xlabel,ylabel,title):
    rcParams['figure.figsize'] = 10, 5
    plt.scatter(x,y,c = 'r')
    plt.xticks(rotation=45)
    plt.ylabel(ylabel,fontsize=14)
    plt.xlabel(xlabel,fontsize=14)
    plt.title(title,fontsize=14)
    plt.show()
    return

def barplot(x,y,xlabel,ylabel,title):
    rcParams['figure.figsize'] = 10, 5
    width = 8
    plt.bar(x,y,color = 'r',width=width)
    plt.xticks(rotation=45)
    plt.ylabel(ylabel,fontsize=14)
    plt.xlabel(xlabel,fontsize=14)
    plt.title(title,fontsize=14)
    plt.show()
    return
