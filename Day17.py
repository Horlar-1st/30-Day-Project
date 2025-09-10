# Prime Checker (Function): Define a function to check if a number is prime.

# Function

def isPrime(num):
    '''
    To check if a number is prime.

    This function is used to check if a number is prime.

    Parameters
    ----------
    args : int
        A postive whole number

    Returns
    -------
    Bool
        `True` if the number is a prime number and `False` otherwise.

    Examples
    --------
    >>> isPrime(101)
    False

    >>> isPrime(1234567)
    False

    '''
    if num <= 1 or isinstance(num, int) == False:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# importing gradio interface
import gradio as gr

isPrime_interface = gr.Interface(
    fn = isPrime,
    inputs= gr.Number(label="Input your number"),
    outputs = gr.Textbox(label="Output"),
    title = "Prime Checker",
    description= "This interface is used to check if a number is prime."
)

#  Launch the interface
isPrime_interface.launch()

