# 18. Letter Counter: Take a word and count how often each letter appears using a dictionary

# Set in your input as word
word = input("Enter your word: ")

# dictionary to collect the letters and occurences
dict1 = {}

# the collection of the data
for i in word:
    dict1.update({i: word.count(i)})
# output template 
print("_"*19)
print(f"|Letters|Occurence|") 
for i in dict1.keys():
    print(f"| {i} \t|  {dict1.get(i)} \t  |")


# End of code
