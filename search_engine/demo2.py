l = [1, 2, 3, 4, 5]


def f(x):
    l = []
    if x < 4:
        return x * x
    else:
        l.append(x)
        l.append(x)
        return l[:]

res = map(f, l)
# print("l1==>", list(res))
# [1, 4, 9, [4, 4], [5, 5]]

# print(res)
l2 = []
for i in res:
    print(i)
    if isinstance(i, list):
        for j in i:
            l2.append(j)
    else:
        l2.append(i)
print("l2==>", l2)