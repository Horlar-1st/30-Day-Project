# File Reader: Read and print a text file line by line.

# importing regex library
import re


# Creating a small .txt file

# list of short text 
detail = ["We receive several requests a day for feedback on CVs. We have seen good and bad CV formats. This format is an amalgamation of templates available on Overleaf especially Rover Resume - Fancy Template (https://www.overleaf.com/latex/templates/rover-resume/bpzqtssvfgsn).",
          "We used several resources and made it specialised for the Maths Volunteers Foundation audience by providing more details. Everyone is welcome to use this template.",
          "We suggest to Start all bullet item items with action verbs. You may base form or ing form or verbs where suited. See action verbs here, https://ecs.ihu.edu.gr/co/employment-cvcletter/action-verbs.html",
          "Provide the most relevant information", 
          "Provide evidence for your skills.  For example, if you include MS Office and Python in your skills list,",
          "then provide bullet points detailing what YOU can do in MS Office and Python.",
          "- In each section--start entries with the most recent one", "- Pay attention to grammar, avoid typos", "- Avoid using abbreviations",
          "- If you're applying for jobs, put your experience and skills before education", "- Some examples of presentations are provided"]

# writing in the details 
with open("detailFile.txt", "w") as file:
    file.write("\n".join(detail))


# function to read the .txt file
def file_reader(path):
    try:
        with open(path, "r") as file:
            for i, line in enumerate(file):
                print(f"{i}:\t {line.strip()}")
            #return output
    except FileNotFoundError:
        print("File not found! Check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
# example
file_reader("detailFile.txt")


# end of code
