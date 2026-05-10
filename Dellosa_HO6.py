import openpyxl
from datetime import datetime

def favorite_people():

    year_now = datetime.now().year
    people_list = []

    print("--- Favorite People ---")
    print("Enter information for 3 people.\n")

    for number in range(1, 4):

        print(f"Person {number}")

        fname = input("First Name: ")
        lname = input("Last Name: ")

        while True:
            try:
                year_input = int(input("Birth Year: "))

                if year_input > year_now or year_input < 1900:
                    print("Enter a valid year.")
                else:
                    break

            except ValueError:
                print("Numbers only.")

        person_age = year_now - year_input

        data = {
            "ID": number,
            "First": fname,
            "Last": lname,
            "Year": year_input,
            "Age": person_age
        }

        people_list.append(data)
        print()

    # Create Excel file
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    sheet.title = "People"

    # Column titles
    sheet.append(["ID", "First Name", "Last Name", "Birth Year", "Age"])

    # Add data to Excel
    for person in people_list:

        sheet.append([
            person["ID"],
            person["First"],
            person["Last"],
            person["Year"],
            person["Age"]
        ])

    file_name = "people.xlsx"
    workbook.save(file_name)

    print("Data saved successfully.\n")

    # Show saved records
    print("---- SAVED RECORDS ----")

    for person in people_list:

        print(
            person["ID"],
            person["First"],
            person["Last"],
            person["Year"],
            person["Age"]
        )

favorite_people()
