# JSON Save: Save a Python dictionary to a '.json' file and read it back

# importing necessary libraries
import json

def save_dict_to_json(data, filename):
    """Save a Python dictionary to a JSON file."""
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)        # Pretty print with indentation
    print(f"Data saved to {filename}")

def load_dict_from_json(filename):
    """Load a Python dictionary from a JSON file."""
    with open(filename, "r") as json_file:
        data = json.load(json_file)
    print(f"Data loaded from {filename}")
    return data


# implementation example
if __name__ == "__main__":
    sample_data = {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        "is_student": False,
        "courses": ["Math", "Science", "Art"]
    }

    filename = "sample_data.json"

    # Save the dictionary to a JSON file
    save_dict_to_json(sample_data, filename)

    # Load the dictionary back from the JSON file
    loaded_data = load_dict_from_json(filename)
    print(loaded_data)

# End of code