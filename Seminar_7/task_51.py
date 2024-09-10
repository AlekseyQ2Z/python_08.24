def same_by(characteristic, objects):
    result = True
    list_1 = [characteristic(x) for x in objects]
    for i in range(len(list_1) - 1):
        if list_1[i] != list_1[i + 1]:
            result = False
    return result


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('defferent')
