import math

def DigitalRoot(num):

    if (num == "0"):
        return 0


    ans = 0
    for i in range(0, len(num)):
        ans = (ans + int(num[i])) % 9
    if (ans == 0):
        return 9
    else:
        return ans % 9


num = "7895"

print(DigitalRoot(num))