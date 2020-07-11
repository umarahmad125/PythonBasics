# f = open('myfile.txt','r')
# print(f.read())

# Mode
# a => append
# w => write
# r => read

with open('myfile.txt','r') as file:
    print(file.read())
    # file.write("\nThis is line two")


    #file.seek(0)   # curser moves to 0th position
    file.close()