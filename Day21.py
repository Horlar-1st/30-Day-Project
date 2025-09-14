# Fibonacci Generator: Write a function to generate the Fibonacci sequence up to n terms.

# Import gradio for interface display
import gradio as gr

# The class for the exhibition
class fibonacci_generator:
    def fibonacci_generator(self, n):
        if n >=0 and isinstance(n, int):
            lst = [0,1]
            for i in range(n):
                lst.append(lst[-1]+lst[-2])
            return lst[:n+1]
        else:
            return "n must be a postive whole number"

    def output(self, n):
        if n >=0 and isinstance(n, int):
            lst1 = [str(i) for i in self.fibonacci_generator(n)]
            return ', '.join(lst1)
        else:
            return self.fibonacci_generator(n)



# initialization 
fib_generator = fibonacci_generator()

# gradio for visualisation
ifibonacci = gr.Interface(
    fn = fib_generator.output,
    inputs= gr.Number(label="Input the number of terms"),
    outputs = gr.Textbox(label="Result"),
    title = "Fibonacci Generator",
    description= "An app to generate the Fibonacci sequence up to n terms."
)

#  Launch the interface
ifibonacci.launch()             # To create a public link, set `share=True` in `launch()`.

# End of program
