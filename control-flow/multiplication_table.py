# prompt the user for a number
num = int(input("Enter a number to see its multiplication table: "))
# print the multiplication table using a for loop
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")
