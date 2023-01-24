x = "HeLlO"

def capital_indexes(x):
    up = []
    for i in range(len(x)):
        if x[i].isupper():
            up.append(i)
    return up

print(capital_indexes(x))