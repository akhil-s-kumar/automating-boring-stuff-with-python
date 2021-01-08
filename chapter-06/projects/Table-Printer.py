def printTable(low): #low - list of words
    #to get max value in a column
    a = []
    for i in range(len(low)):
        b = []
        for j in range(len(low[i])):
            b.append(len(low[i][j]))
        a.append(max(b))

    #main program
    for k in range(len(low[0])):
        for l in range(len(low)):
            print(low[l][k].rjust(a[l]), end=' ')
        print('\n')

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
