from collections import OrderedDict
item = OrderedDict()
for _ in range(int(input())):
    j = input().rpartition(" ")
    item[j[0]] = int(j[-1]) + item[j[0]] if j[0] in item else int(j[-1])
for k in item:
    print(k, item[k])