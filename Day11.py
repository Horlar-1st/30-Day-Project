# Multiplication Table: Print the 1–10 multiplication table for a given number

# Discription
print("This program prints the 1 - 10 multiplication table for a given number.")

# input
num = input("Enter the number: ")

# try and except block to handle non-integer inputs
try:
    num = int(num)
    print(f"{num} multiplication table is:")
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")
        
# handling ValueError for non-integer inputs
except ValueError:
    print("Wrong input!")

# End of program