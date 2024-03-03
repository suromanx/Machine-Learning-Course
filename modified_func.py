def reversed_(array):
    rv=[]
    while array:
        rv.append(array.pop())
    return rv




arr = [1, 2, 3]
print(reversed_(reversed_(arr)))  # [1, 2, 3]
print(arr)  # []