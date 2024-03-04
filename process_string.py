def process_string(string):
    result = []
    lower_string = string.lower()
    if 'intern' in lower_string:
        lower_string = lower_string.replace('intern','junior')
        result.append(lower_string)
    return result


def process_string(string):
    result = string[1:].lower()
    result = result.replace('intern', 'junior')
    return result

output = process_string('Intern reads a lot of books')
print(output)
