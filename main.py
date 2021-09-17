# sort the array in ascending order 

# small comment to test commit

# input
enter = input("order the list in asc or desc ? ")
#order
def order(how):
    array = [1, 54, 234, 6, 6, 56, 67, 234, 234, 24, 5, 64, 2, 11, 8, 69, 6, 7678]
    if how == "asc":
       array.sort()
    elif how == "desc":
        array.sort(reverse = True)
    return array

print(order(enter))


