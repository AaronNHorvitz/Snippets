#Define standard plots

#Standard Lineplot
def lineplot(x,y,xlabel,ylabel,title):
    rcParams['figure.figsize'] = 10, 5
    plt.plot(x,y,c = 'r')
    plt.xticks(rotation=45)
    plt.ylabel(ylabel,fontsize=14)
    plt.xlabel(xlabel,fontsize=14)
    plt.title(title,fontsize=14)
    plt.show()
    return

#Standard Scatterplot
def scatterplot(x,y,xlabel,ylabel,title):
    rcParams['figure.figsize'] = 10, 5
    plt.scatter(x,y,c = 'r')
    plt.xticks(rotation=45)
    plt.ylabel(ylabel,fontsize=14)
    plt.xlabel(xlabel,fontsize=14)
    plt.title(title,fontsize=14)
    plt.show()
    return

#Standard Horizontal Bar Plot
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

#Lineplot with various features added to it
def lineplot(x,y,
             title="",
             overlay = 'n',            #Overlay plot with subsequent plot
             text_box = 'n',
             title_fontsize  = 14,
             
             xlabel="",
             xlabel_fontsize = 14,
             xticks_fontsize = 11,
             xticks_degrees_rotation = 45,
             
             ylabel="",
             ylabel_fontsize = 14,
             yticks_fontsize = 11,
             yticks_degrees_rotation = 0,

             line_color = 'red',
             line_width = 1,
             figure_height = 5,
             figure_width = 14,
             font = 'Verdana'):
    from pylab import rcParams
    if xlabel == "":
        xlabel = pd.DataFrame(x).columns[0]
    if ylabel == "":
        ylabel = pd.DataFrame(y).columns[0]
    if title == "":
        title = pd.DataFrame(y).columns[0]
    if overlay == 'y':
        title = ""
        ylabel = ""
    rcParams['font.family'] = font
    rcParams['figure.figsize'] = figure_width, figure_height
    title = '{} Line Plot  '.format(title)

    plt.plot(x,y,c = line_color,linewidth = line_width)
    plt.xticks(rotation = xticks_degrees_rotation, fontsize = xticks_fontsize)
    plt.yticks(rotation = yticks_degrees_rotation, fontsize = yticks_fontsize)
    plt.ylabel(ylabel,fontsize = ylabel_fontsize)
    plt.xlabel(xlabel,fontsize = xlabel_fontsize)
    plt.title(title,fontsize=title_fontsize)
    
    if text_box =='y':
        xbox_position = x.tolist()[4]
        ybox_position = y.tolist()[4]
        plt.text(x=xbox_position,y=ybox_position, s=ylabel, fontsize = 10,style='italic',
            bbox={'facecolor':line_color, 'alpha':1, 'pad':7.5})

    plt.tight_layout()
    if overlay == 'n':
        plt.show()

    return
