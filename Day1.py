# Number Analyzer: Determine if a number is even/odd, positive/negative/zero, and prime.

class NumberAnalyzer:
    def iseven(self, num):
        if num%2 == 0:
            return "even"
        return "odd"

    def ispositive(self, num):
        if num > 0:
            return "positive"
        elif num < 0:
            return "negative"
        return "zero"

    def isprime(self, num):
        if num < 2:
            return "not prime"
        if isinstance(num, float):
            return "not prime"
        for i in range(2, int(num)):
            if num%i == 0:
                return "not prime"
        return "prime"

## End of code

## Initializing
myNumberAnalyzer = NumberAnalyzer()

## Examples
num_list = [34, -0.4, 6, 8, -9, -12, 0, 4, 3.5]
for i in num_list:
    result = f"{i} is {myNumberAnalyzer.iseven(i)}, {myNumberAnalyzer.ispositive(i)}, and {myNumberAnalyzer.isprime(i)}"

    print(result)

#End of program 

