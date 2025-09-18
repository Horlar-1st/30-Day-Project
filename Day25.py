# Contact Book: Use a dictionary to save names and phone numbers. Include add, delete, search

# class ContactBook, for managing contacts, with methods to add, delete, and search contacts.
class ContactBook:
    # Initialize the contact book with an empty dictionary
    def __init__(self):
        self.phone_book = {}

    # Helper method to clean and standardize names
    def clean_name(self, inpt):
        '''To clean and standardise names'''
        return inpt.strip().capitalize()

    # Method to add a contact
    def add_contact(self, name, phone):
        '''To add name and contact number to contact list'''
        name = self.clean_name(name)
        phone = str(phone).strip()

        if name and phone:
            self.phone_book[name] = phone
            return "✅ Contact added successfully!"
        else:
            return "⚠️ Either the name or phone number is missing. Please check and try again."

    # Method to search for a contact by name or phone number
    def search_contact(self, name="", phone=""):
        '''To search name or contact number to contact list'''
        name = self.clean_name(name)
        phone = str(phone).strip()

        if name in self.phone_book:
            return f"📞 {name}'s phone number is {self.phone_book[name]}."
        elif phone:
            for key, value in self.phone_book.items():
                if value == phone:
                    return f"📇 The contact for number {phone} is {key}."
        return "❌ Contact not found."

    # Method to delete a contact by name or phone number
    def delete_contact(self, name="", phone=""):
        '''To delete name and contact number to contact list'''
        name = self.clean_name(name)
        phone = str(phone).strip()

        if name in self.phone_book:
            del self.phone_book[name]
            return f"🗑️ {name} has been deleted successfully."
        elif phone:
            for key, value in list(self.phone_book.items()):
                if value == phone:
                    del self.phone_book[key]
                    return f"🗑️ Contact with number {phone} ({key}) has been deleted successfully."
        return "❌ Contact not found."



# import gradio for creating a web interface
import gradio as gr

# Create an instance of MyContactBook

MyContactBook = ContactBook()

# Define the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("##  Phone Book")
    gr.Markdown("Add, delete, or search for contacts by name or phone number.")
    
    with gr.Row():
        name = gr.Textbox(label="Enter name", max_lines=1)
        phone = gr.Textbox(label="Enter phone number")
    
    with gr.Row():
        add = gr.Button("+ Add")
        delete = gr.Button("- Delete")
        search = gr.Button("🔄 Search")

    with gr.Row():
        result_output = gr.Textbox(label="Result", interactive=False)
        
    add.click(fn=MyContactBook.add_contact, inputs=[name, phone], outputs = result_output)
    delete.click(fn=MyContactBook.delete_contact, inputs=[name, phone], outputs = result_output)
    search.click(fn=MyContactBook.search_contact, inputs=[name, phone], outputs = result_output)

# gradio launch
demo.launch()           # To create a public link, set `share=True` in `launch()`.

