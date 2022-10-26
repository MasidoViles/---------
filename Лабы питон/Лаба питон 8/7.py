def allD(d1, d2):
    for k, v in d2.items():
        if d1.get(k):
            d1[k] = [d1[k], v]
        else:
            d1[k] = v        
    return d1
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = allD(d1, d2)
print(d3)
