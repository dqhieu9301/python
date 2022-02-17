test = int(input())
while test>0:
    n =int(input())
    if(n % 2 == 0):
        sum = 0
        for i in range(2 ,n + 2,2):
            sum += float(1/i)
        print("{:.6f}".format(sum))
    else:
        sum = 0
        for i in range(1 ,n + 2,2):
            sum += float(1/i)
        print("{:.6f}".format(sum))
    test -=1