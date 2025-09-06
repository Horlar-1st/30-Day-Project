# Dash Replacer: Replace every space in a string with a dash ('-').

# Function for dash replacer
def dash_replacer(text):
    '''
    Replace every space in a string with a dash ('-')

    This function is useful for replacing spaces in a sentence with dash. 
    
    Parameters
    ----------
    text : str
        A string containing words separated by spaces.

    Returns
    -------
    str
        A new string where each word separated BY spaces are replaced with dashes.

    Examples
    --------
    >>> dash_replacer("british airways review")
    'British-Airways-review'

    >>> dash_replacer("economy class flight")
    'economy-class-flight'
    '''
    return text.replace(" ", "-")

# gradio interface for the dash replacer function
# import gradio library
import gradio as gr

# create a gradio interface
idash_replacer = gr.Interface(
    fn = dash_replacer,
    inputs= gr.Textbox(label="Input", placeholder="Enter your sentence."),
    outputs = gr.Textbox(label="Output"),
    title = "Dash Replacer",
    description= "Replace every space in a string with a dash ('-')"
)

#  Launch the interface
idash_replacer.launch()                   # set share=True if you want to share the app publicly
