#write a program which take user input and then add each numbers

# 1st method

#while Lopp
# num = input("Enter a number(e.g 1234):")
# total = 0
# i = 0
# while(i < len(num)):
#     total += int(num[i])
#     i += 1
# print(f"sum is: {total}")

# for Loop
# num = input("Enter a number(e.g 1234):")
# total = 0
# for i in range(0, len(num)):
#     total += int(num[i])
# print(f"Sum is: {total}")




#2nd simple method

num = input("Enter a number(e.g 1234):")
total = 0
for i in num:
    total += int(i)
print(f"Sum is: {total}")