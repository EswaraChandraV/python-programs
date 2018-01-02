import numpy as ap
n = int(input())
A = ap.array([input().split() for _ in range(n)], float)
print(ap.linalg.det(A))