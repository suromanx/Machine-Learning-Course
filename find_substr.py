def find_substr(letters, str):
    the_result = []
    for i in range(len(str) - len(letters) + 1):
        candidate = str[i:i + len(letters)]
        if candidate == letters:
            the_result.append(candidate)

    return the_result


letters = ['мы']
str = ['Летом мы хотим отдыхать на море']
