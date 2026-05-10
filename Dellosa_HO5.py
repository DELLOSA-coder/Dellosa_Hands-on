import os

file_name = "notes.txt"

# Create file if it does not exist
def create_file():
    if not os.path.exists(file_name):
        file = open(file_name, "w")
        file.write("Never give up.\n")
        file.write("Keep learning every day.\n")
        file.close()

# Read the file
def read_file():
    print("\n--- MESSAGES ---")

    file = open(file_name, "r")
    text = file.read()
    file.close()

    print(text)

# Add new message
def add_message():
    message = input("Enter message: ")

    if message != "":
        file = open(file_name, "a")
        file.write("\n" + message)
        file.close()

        print("Message added.")

# Rewrite file
def rewrite_file():
    confirm = input("Delete everything? yes/no: ")

    if confirm == "yes":

        print("Type new text.")
        print("Type DONE to stop.")

        lines = []

        while True:
            text = input()

            if text == "DONE":
                break

            lines.append(text)

        final_text = "\n".join(lines)

        file = open(file_name, "w")
        file.write(final_text)
        file.close()

        print("File updated.")

# Main program
create_file()

while True:

    print("\n--- MENU ---")
    print("1. Read messages")
    print("2. Add message")
    print("3. Rewrite file")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        read_file()

    elif choice == "2":
        add_message()

    elif choice == "3":
        rewrite_file()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
