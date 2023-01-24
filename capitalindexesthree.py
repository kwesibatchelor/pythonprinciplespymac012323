from string import uppercase 
x = "HeLlO"
def capital_indexes(x):
    return[i for i in range(len(x)) if x[i] in uppercase]

print(capital_indexes(x))