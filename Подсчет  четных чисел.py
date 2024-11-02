def counter (list_):
    count = 0
    for i in list_:
        if i == 0:
            continue
        if i % 2 == 0:
            count+=1
    return count
print(counter([2,3,2,4,5,6,8,5,10]))