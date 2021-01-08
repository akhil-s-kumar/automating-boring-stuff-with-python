import random
numberOfStreaks = 0
for experimentNumber in range(100):
    loht = [] #list of head or tail
    for i in range(100):
        loht.append(random.choice(['H','T']))
    print(loht)

    count = 1
    for j in range(0,len(loht)-1):
        if loht[j]==loht[j+1]:
            count+=1
            if count == 6:
                print(count)
                numberOfStreaks+=1
                count = 1
        else:
            count = 1
    
print('Chance of streak: %s%%' % (numberOfStreaks / 100))

