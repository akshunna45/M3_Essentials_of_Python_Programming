def TribRec(n):
    if (n == 0 or n == 1 or n == 2):
        return 0
    elif (n == 3):
        return 1
    else:
        return (TribRec(n - 1) +
                TribRec(n - 2) +
                TribRec(n - 3))
def printTrib(n):
    for i in range(1, n):
        print(TribRec(i), " ", end="")
n = int(input("Enter Number: "))
printTrib(n)