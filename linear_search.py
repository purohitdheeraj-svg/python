
def search_item(list_1, n):
    for value in list_1:
        if n == list_1[value]:
            return list_1.index(value)
        else:
            return -1
        



list_1 = [1,2,3,4,5]
print(search_item(list_1 , 2))