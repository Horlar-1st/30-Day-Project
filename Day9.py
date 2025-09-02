# Reverse String: Take input and print it reversed. Try both slicing and loops

# By slicing
print("Reverse string by slicing")
inpt = input("Enter your text: ")
print(f"The reverse statement by slicing is {inpt[::-1]}")
print("*-"*40)
# By loop
print("Reverse string by slicing")
# The result to add to
result = ""
# Length of the string
n = len(inpt)
# The loop
for i in range(1, n+1):
    result += inpt[n-i]
print(f"The reverse statement by loop is {result}")