def collatz(number):
    if number%2==0:
        r = number//2
        print(r)
        if r !=1:
            collatz(r)
        return r
    else:
        r = 3*number+1
        print(r)
        if r !=1:
            collatz(r)
        return r

n = int(input("Enter Number: "))
collatz(n)

