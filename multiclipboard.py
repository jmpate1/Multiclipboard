#importing relevant modules
import sys
import clipboard
import json

#Creating variable to define filepath
SAVED_DATA = "clipboard.json"

#Creating function to write data to filepath
def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

#Creating function to read data from filepath
def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

#Creating logic to process command line prompts
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved successfully.")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exist.")
    elif command == "list":
        print(data)
    else:
        print("Unknown Command")
else:
    print("Please pass only one command!")

