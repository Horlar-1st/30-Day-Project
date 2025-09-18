# Contact Book: Use a dictionary to save names and phone numbers. Include add, delete, search

# class ContactBook, for managing contacts, with methods to add, delete, and search contacts.
class ContactBook:
    # Initialize the contact book with an empty dictionary
    def __init__(self):
        self.phone_book = {}

    # Helper method to clean and standardize names
    def clean_name(self, inpt):
        return inpt.strip().capitalize()

    # Method to add a contact
    def add_contact(self, name, phone):
        name = self.clean_name(name)
        phone = str(phone).strip()

        if name and phone:
            self.phone_book[name] = phone
            return "✅ Contact added successfully!"
        else:
            return "⚠️ Either the name or phone number is missing. Please check and try again."

    # Method to search for a contact by name or phone number
    def search_contact(self, name="", phone=""):
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
