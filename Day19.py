# 19 To-Do List: Build a mini app to add/remove/show tasks using a list.

# import all neccessary library
import re
import gradio as gr

# A class that represent all conditions
class To_do_list:
    def __init__(self):
        self.activities = []
        self.options = ["Show task", "Add task", "Remove task"]

    def handle_dropdown(self):
        return self.options

    def clean_data(self, task):
        task = task.strip()
        task = task.capitalize()
        return task
    
    def add_to_list(self, task):
        task = self.clean_data(task)
        if task in self.activities:
            return f"\"{task}\" is in your To-do list"
        else:
            self.activities.append(task)
            return f"Task \"{task}\" added successfully"

    def remove_to_list(self, task):
        task = self.clean_data(task)
        if task in self.activities:
            self.activities.remove(task)
            return f"Task \"{task}\" removed successfully"
        else:
            return f"\"{task}\" is not in your To-do list, you can added it to your list"

    def show_to_list(self):
        return ", ".join(self.activities)

    def handle_dropdown_change(self, task, select):
        if select == self.options[1]:
            return self.add_to_list(task)
        elif select == self.options[2]:
            return self.remove_to_list(task)
        else:
            return self.show_to_list()
        

# Gradio for interface presentation

Todo = To_do_list()
iTodo = gr.Interface(
    fn = Todo.handle_dropdown_change,
    inputs= [gr.Textbox(label="Input", placeholder="Enter your sentence"),
             gr.Dropdown(label="Select option:", choices=Todo.options)],
    outputs = gr.Textbox(label="Result"),
    title = "Word Counter",
    description= "Count the number of words in a full sentence."
)

#  Launch the interface
iTodo.launch()                          # To create a public link, set `share=True` in `launch()` 