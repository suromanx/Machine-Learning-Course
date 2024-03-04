def fifth_element(some_list: list) -> list:
    reversed_list = reversed(some_list)
    answer = []
    count = 0
    for i in reversed_list:
        count += 1
        if count % 5 == 0:
            answer.append(i)
    return answer