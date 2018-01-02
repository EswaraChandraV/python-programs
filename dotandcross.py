import numpy as ap
m = input()
A = ap.array([input().split() for _ in range(int(m))], int)
B = ap.array([input().split() for _ in range(int(m))], int)
print(ap.dot(A,B))
