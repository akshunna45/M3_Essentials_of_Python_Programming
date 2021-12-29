def SumTriangular(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * (i + 1) / 2
    return sum

n = int(input("enter number: "))
print(SumTriangular(n))