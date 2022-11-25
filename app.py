from tinydb import TinyDB
from tinydb import Query
import functions
Web = Query()
db = TinyDB("urls.json")

# Welcome Message
print("------------------------------")
print("Welcome to WedSTUB")
print("------------------------------\n")

# Display user options
print(functions.user_options())

# User selects option via input
user_action = input("Please select an action 1-3: ")

# Generate and save a new QR
if user_action == "1":
    functions.generate_qr(),

# Shorten and save a website url
elif user_action == "2":
    functions.url_stub(),

# View a url
elif user_action == "3":
    functions.search_url(),

# Catch all
else:
    print("Please select action 1-3")



