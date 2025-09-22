# Password Generator: Create random passwords with a mix of characters. Let user set length.

# importing necessary libraries
import string
import re
import random
import gradio as gr

# function to generate a random password
def PasswordGenerator(length = 15):
    '''
    Create random passwords with a mix of characters.
    
    This function is used to create random passwords with a mix of characters (letters, numbers, special characters) of desired length.

    Parameters
    ----------
    args: int
        length : Length of the password
        
    Returns
    -------
        str: Password of random charater
 
    Examples
    --------
    >>>  PasswordGenerator(10)
    'u]6d<]R?r$'

    >>>  PasswordGenerator(15)
    'sIo73lNfxLb*{88'

    '''
    try:
        if length > 0:
            letters = string.ascii_letters
            special = string.punctuation
            numbers = string.digits
            my_pass = random.choices(letters+special+numbers, k = length)
            return "".join(my_pass)
        else:
            return "Length of password must be greater than 0"
    except Exception as e:
        return f"An error occured: {e}"


# gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## Password Generator")
    with gr.Row():
        length = gr.Number(label="Length of Password", value=12, precision=0)
    password = gr.Textbox(label="Generated Password")
    generate_btn = gr.Button("Generate Password")
    generate_btn.click(PasswordGenerator, inputs=[length], outputs=[password])

# Launch
demo.launch()        # To create a public link, set `share=True` in `launch()`.

