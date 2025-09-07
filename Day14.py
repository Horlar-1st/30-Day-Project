# Capitalizer: Capitalize the first letter of each word in a sentence (like a title).

# function for capitalizing 
def capitalizer(text):
    '''
    Capitalizes the first letter of each word in the input text.

    This function is useful for creating title-like strings,
    where all the first word starts with a capital letter and strip of all white spacings.

    Parameters
    ----------
    text : str
        A string containing words.

    Returns
    -------
    str
        A new string where each word is capitalized.

    Examples
    --------
    >>> capitalizer("british airways review")
    'British Airways Review'

    >>> capitalizer(" economy class flight ")
    'Economy Class Flight'
    '''
    return text.strip().title()


# gradio interface for the word counter function 
# import gradio library
import gradio as gr

# create a gradio interface
icapitalizer = gr.Interface(
    fn = capitalizer,
    inputs= gr.Textbox(label="Input", placeholder="Enter your sentence."),
    outputs = gr.Textbox(label="Output"),
    title = "Capitalizer",
    description= "Capitalizes the first letter of each word in the input text."
)

#  Launch the interface
icapitalizer.launch()                   # set share=True if you want to share the app publicly
