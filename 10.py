# Write a Python function that takes a list and returns a new list with unique elements of the first list. 
# Note: don't use collection set.

def unique_elements(list):
    unique_list = []

    for i in list:
        if i not in unique_list:
            unique_list.append(i)

    print(unique_list)


unique_elements([1, 1, 2, 3, 3, 3, 4, 5, 6, 6, 7, 6, 7, 8])
