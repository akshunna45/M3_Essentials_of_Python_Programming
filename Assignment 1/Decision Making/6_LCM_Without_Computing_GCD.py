def lcm(x, y):
  large = max(x, y)
  small = min(x, y)
  i = large
  while(True):
    if(i % small == 0):
      return i
    i = i + large

x = int(input("Enter The First Number:"))
y = int(input("Enter The Second Number:"))
print("LCM of", x, "and", y, "is:", lcm(x,y))