def sum(array:list):
    assert type(array) is list
    total = 0
    for val in array:
        total += val
    return total

if __name__ == '__main__':
    sum(3)
    sum([3,3])
    sum('3333')
    sum(['3','3'])




