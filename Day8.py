# # Vowel Counter: Count the number of vowels in a given string. 

# input 
text = input("Enter your text: ")

# process
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)

# output
print(f"Number of vowels: {count}")


# End of Day8.py