# create a function that take two list as input and filter same element and return that as a list

def filter_list(l1, l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output

lst1 = list(range(1,10))
lst2 = [1,5,7]

print(filter_list(lst1,lst2))