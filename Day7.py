# Pattern Printer: Ask user for n. Print a right-angle triangle and a diamond if n is odd and ≥ 5.

import sys
n = int(input("Enter an integer n (n ≥ 5): "))
if n < 5:
    print("n must be at least 5.")
    sys.exit(1)
if n % 2 == 0:
    print("n must be odd.")
    sys.exit(1)
# Print right-angle triangle
for i in range(1, n + 1):
    
    print('*' * i)
print()  # Blank line between patterns
# Print diamond pattern
mid = n // 2    
for i in range(mid + 1):
    print(' ' * (mid - i) + '*' * (2 * i + 1))

for i in range(mid - 1, -1, -1):
    print(' ' * (mid - i) + '*' * (2 * i + 1))  

# End of program     