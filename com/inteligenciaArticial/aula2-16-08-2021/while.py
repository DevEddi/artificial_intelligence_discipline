print(" WHILE ")
print("--------------------")

s = 0
x = 1
while x < 100:
    s = s + x
    x = x + 1
    print(s)
print("--------------------")
print(" break ")
print("--------------------")

t = 1
while t < 5:
    t = t + 1
    print(t)
    break
print("--------------------")
print(" continue ")
print("--------------------")
t =1
while t < 5:
    t = t + 1
    if t==3:
        continue
    print(t)