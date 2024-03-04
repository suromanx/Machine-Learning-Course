def find_substr(substring,string):
    for i in range(len(string) - len(substring) + 1):
        candidate = string[i:i + len(substring)]
        if candidate == substring:
            return ((i, i + len(substring)))
