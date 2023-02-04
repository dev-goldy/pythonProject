def sort(list):
    size = len(list)
    for i in range(size):
        sizo = len(list)
        for j in range(sizo-1):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp

