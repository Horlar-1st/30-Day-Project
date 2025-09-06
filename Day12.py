# Word Counter: Count the number of words in a full sentence.

# function to count words in a sentence
def word_counter(sentence):
    '''
    Count the number of words in a full sentence.

    This function counts the number of words in a full sentence.

    Parameters
    ----------
    text : str
        A string containing words.

    Returns
    -------
    int
        Number of words in the sentence.

    Examples
    --------
    >>> word_counter("How are you doing today?")
    5

    >>> capitalizer(" economy class flight ")
    3
    '''
    return len(sentence.split())


# gradio interface for the word counter function 
# import gradio library
import gradio as gr

# create a gradio interface
iwordCounter = gr.Interface(
    fn = word_counter,
    inputs= gr.Textbox(label="Input", placeholder="Enter your sentence."),
    outputs = gr.Textbox(label="Number of words"),
    title = "Word Counter",
    description= "Count the number of words in a full sentence."
)

#  Launch the interface

iwordCounter.launch()                   # set share=True if you want to share the app publicly
