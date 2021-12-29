rows = int(input("Enter number of rows: "))

print('\n Half Pyramid \n')

for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("")

print('\n Inverted Half Pyramid \n')

for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")

    print("")

print('\n Full Pyramid \n')

k = 0
count = 0
count1 = 0

for i in range(1, rows + 1):
    for space in range(1, (rows - i) + 1):
        print("  ", end="")
        count += 1

    while k != ((2 * i) - 1):
        if count <= rows - 1:
            print(i + k, end=" ")
            count += 1
        else:
            count1 += 1
            print(i + k - (2 * count1), end=" ")
        k += 1

    count1 = count = k = 0
    print("")