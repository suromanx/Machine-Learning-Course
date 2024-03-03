def reversed_(array):
    rv=[]
    for element in reversed(array):
        rv.append(element)
    return rv




arr = [1, 2, 3]
print(reversed_(reversed_(arr)))  # [1, 2, 3]
print(arr)  # []