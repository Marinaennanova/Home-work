def unique(list_):
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)
    return new_list
print(unique([1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]))