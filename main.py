import pandas as pd

filepath = "client_data.csv"

while True:
    
    user_action = input("Add / View / Exit: ").upper()

    if "ADD" in user_action:

        df = pd.read_csv(filepath, sep=",") 

        date = input("Date (dd/mm/yyyy): ")
        name = input("Client name: ").strip().title()
        contact = input("Contact: ")
        revenue = input("Revenue: ")
        paid_with = input("Means of payment: ").strip().title()
        service_type = input("Type of haircut: ").strip().title()
        note = input("Note: ")

        data = [[date, name, contact, revenue, paid_with, service_type, note]]

        new_data = pd.DataFrame(data)
        new_data.to_csv(filepath, index=True, mode="a", header=False)

        df = pd.read_csv(filepath, sep=",") 
        print(f"Client {name} added successfully.")
        print("**UPDATED DATA**")
        print(df)

    if "VIEW" in user_action:

        print("**CURRENT DATA**")
        df = pd.read_csv(filepath, sep=",") 
        print(df)

    if "EXIT" in user_action:

        print("Exit successfull")
        break

