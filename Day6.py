# import necessary libraries 
import gradio as gr

# Check if the sum of digits of a number is divisible by 3 or 9
class DigitSumChecker:
    def __init__(self):
        pass  
        
    def divisble_by3(self, num):
        """  
        A function that checks if a number is divisible by 3
        """
        try: num = int(num)
        except: return "invalid input"
        sum_ = sum(int(val) for val in str(num))
        if sum_%3 == 0:
            return "divisble by 3"
        return "not divisble by 3"
        
    def divisble_by9(self, num):
        """  
        A function that checks if a number is divisible by 5
        """
        try: num = int(num)
        except: return "invalid input"
        sum_ = sum(int(val) for val in str(num))
        if sum_%9 == 0:
            return "divisble by 9"
        return "not divisble by 9"
    
# Example usage
# Create an instance of the DigitSumChecker class
digitsumChecker = DigitSumChecker()

# Function to get the result for a given number
def digitsumChecker_result(num):
    return f"{num} is {digitsumChecker.divisble_by3(num)} and {digitsumChecker.divisble_by9(num)}."

# Test the function with an example
print(digitsumChecker_result(123456789))  # Output: "123456789 is divisble by 3 and divisble by 9."


if __name__ == "__main__":
    with gr.Blocks() as demo:
        gr.Markdown("# Check if the sum of digits of a number is divisible by 3 or 9")
        with gr.Row():
            num = gr.Number(label="Enter a number")
        with gr.Row():
            btn = gr.Button("Check")
        output = gr.Textbox(label="Result")
        btn.click(digitsumChecker_result, inputs=num, outputs=output)
    
    # Launch the Gradio interface

    demo.launch() # share=True to share the link


## End of code
