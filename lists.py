a = [10, 1, 10, 2, 3, 4, 3.56, "Hello", [34, 56, [44, 100]]]

print(a.index(2))

print(a[8][2][1])

print(a)

a += 45, "Regina"
a.append(46)

print(a)

if 10 in a:
    print('10 is in list a')
