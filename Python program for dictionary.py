D = {1 : [1, 2, 3], 2: (4, 6, 8)}
D[1].append(4)
print(D[1], end = " ")
L = list(D[2])
L.append(10)
D[2] = tuple(L)
print(D[2])
