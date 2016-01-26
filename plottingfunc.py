import matplotlib.pyplot as plt
def makeplots(counts):
    """
    Plot the counts for the positive and negative words for each timestep.
    Use plt.show() so that the plot will popup.
    """
    # YOUR CODE HERE
    positivelist=[]
    negativelist=[]
    xaxis=[]
    count=0
    for lists in counts:
        count=count+1
        xaxis.append([count])
        positivelist.append(lists[0][1])
    for lists in counts:
        negativelist.append(lists[1][1])
    plt.plot(xaxis,positivelist,label='positive',marker='o')
    plt.plot(xaxis,negativelist,label='negative',marker='o')
    plt.xlabel('Time step')
    plt.ylabel('Word count')
    plt.legend()
    plt.show()

