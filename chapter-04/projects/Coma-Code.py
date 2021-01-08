def lts(low): #lts - list to string, low - list of words
    es = '' #es - empty string
    le = 'and '+low[-1] #le - last element
    for i in range(0,len(low)-1):
        es = es + low[i] + ', '
    es = es + le
    print(es)
    return es

cl = list(eval(input("Enter List: "))) #cl - created list
if len(cl)==0:
    print("List cannot be empty!")
elif len(cl)==1:
    print(cl[0])
else:
    lts(cl)
