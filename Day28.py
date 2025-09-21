# 28 Simple Calculator App: Text-based menu calculator (add/subtract/multiply/divide). Use functions.

def SimpleCalculatorApp(inpt1, inpt2, operation):
    '''
    Text-based menu calculator that performs basic operations between two numbers.
    
    This function is used to perform addition, subtraction, multiplication, or division between two numbers.

    Parameters
    ----------
    args
        inpt1 (int/float): The first value/number
        inpt1 (int/float): The second value/number
        operation (str):   Select the operation to perform. It could be either "Add", "Subtract", "Divide", or "Multiply"

    Returns
    -------
        float/int: Result of the operation
 
    Examples
    --------
    >>>  SimpleCalculatorApp(34,56,"Add")
    90

    >>>  SimpleCalculatorApp(34,56,"Subtract")
    -22

    '''
    
    if operation == "Add":
        return inpt1 + inpt2
    elif operation == "Subtract":
        return inpt1 - inpt2
    elif operation == "Multiply":
        return inpt1 * inpt2
    elif operation == "Divide":
        return inpt1 / inpt2
    else:
        return "Please select an operation"


# import gradio for creating a web interface
import gradio as gr

# gradio interface
iSimpleCal = gr.Interface(
    fn=SimpleCalculatorApp,
    inputs=[gr.Number(label ="Enter the first number"),
            gr.Number(label = "Enter the second number"), 
            gr.Dropdown(label ="Select operation", choices=["----","Add", "Subtract", "Divide", "Multiply"])],
    outputs= gr.Textbox(label="Result"),
    title= "Simple Calculator App",
    description="Text-based menu calculator that performs addition, subtraction, multiplication, or division operation between two numbers"
)


# to launch
iSimpleCal.launch()     # To create a public link, set `share=True` in `launch()`.
