# prompt the user for pattern size
size = int(input("Enter the size of the pattern: "))
# initialize row counter
row = 0
while row < size:
    # initialize column counter
    col = 0
    while col < size:
        # print "*" without newline
        print("*", end="")
        col += 1
    # move to the next line after finishing a row
    print()
    row += 1