# write a program that take input a list and filter even and odd and return botyh in one list


def filter_list(l):
    even_list = []
    odd_list = []

    for i in l:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    output = [even_list , odd_list]
    return output


# lst = [1,2,3,4,5,6,7,8,9]

lst = list(range(1,10)) # define list 1 to 9

print(filter_list(lst))