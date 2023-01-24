x = "HeLlO"

def capital_indexes(x):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i, l in enumerate(x):
        if l in upper:
            result.append(i)
    return result
print(capital_indexes(x)) 