def max_number(number):
    max_ = (number[0])
    for i in number:
        if i > max_:
            max_ = i
    return max_
print(max_number([3,5,4,6,8,9,2,10,35,3]))