## Age Comparator: Ask for names and ages of two users, and determine who is older and by how many years.

# import libraris for the gradio interface
import gradio as gr

## First person input
print("First Person ")
name1 = input("Enter your name:")
age1 = input("Enter your age:")

## Second person input
print("\nSecond Person ")
name2 = input("Enter your name:")
age2 = input("Enter your age:")
print("-"*30)

## Conditions and output
person1 = [name1, float(age1)]
person2 = [name2, float(age2)]
if person1[1] > person2[1]:
    print(f"{person1[0]} is older than {person2[0]} by {person1[1] - person2[1]} years.")
elif person1[1] == person2[1]:
    print(f"{person1[0]} is of the same age as {person2[0]}.")
else:
    print(f"{person2[0]} is older than {person1[0]} by {person2[1] - person1[1]} years.")




#####
## Gradio interface

# The function
def AgeComparator(name1, age1, name2, age2):
    person1 = [name1, age1]
    person2 = [name2, age2]
    if person1[1] > person2[1]:
        return f"{person1[0]} is older than {person2[0]} by {person1[1] - person2[1]} years."
    elif person1[1] == person2[1]:
        return f"{person1[0]} is of the same age as {person2[0]}."
    else:
        return f"{person2[0]} is older than {person1[0]} by {person2[1] - person1[1]} years."



# The gradio interface    
iAgeComparator = gr.Interface(
    fn = AgeComparator,
    inputs = [
         gr.Textbox(label = "First person name"),
         gr.Number(label = "First person age"),
         gr.Textbox(label = "Second person name"),
         gr.Number(label = "Second person age")
    ],
    outputs = gr.Textbox(label="Response"),
    title = "Age Comparator",
    description = "A simple app that asks for names and ages of two users, and determine who is older and by how many years."
)

iAgeComparator.launch()  # To create a public link, set `share=True` in `launch()`.