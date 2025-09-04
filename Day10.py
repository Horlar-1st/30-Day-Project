# Palindrome Checker: Check if a word or phrase is a palindrome (ignore spaces and casing).

# function to exhibit the checker
def isPalindrome(text):
    text = text.strip()             # strip the white spaces
    text = text.lower()             # change to lower cases
    return text == text[::-1]



# import gradio for web presentation
import gradio as gr

ichecker = gr.Interface(
    fn = isPalindrome,
    inputs= gr.Textbox(label="Input", placeholder="Enter your word"),
    outputs = gr.Textbox(label="Result"),
    title = "Palindrome Checker",
    description= "Check if a word or phrase is a palindrome (ignore spaces and casing) and reply `True` if it is palindrome and `False` otherwise."
)

#  Launch the interface

ichecker.launch()                   # To create a public link, set `share=True` in `launch()`. 


# End of program
