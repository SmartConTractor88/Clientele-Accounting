import pandas as pd
import datetime

filepath = "client_data.csv"

while True:
    
    user_action = input("Add / View / Exit: ").upper()

    if "ADD" in user_action:

        df = pd.read_csv(filepath, sep=",") 

        try: 
            date: str = input("Date (dd/mm/yyyy): ")
            name: str = input("Client name: ").strip().title()
            contact: str = input("Contact: ")
            revenue: float = float(input("Revenue: "))
            paid_with: str = input("Means of payment: ").strip().title()
            service_type: str = input("Type of haircut: ").strip().title()
            note: str = input("Note: ")

            data = [[date, name, contact, revenue, paid_with, service_type, note]]

            new_data = pd.DataFrame(data)
            new_data.to_csv(filepath, index=False, mode="a", header=False)

            df = pd.read_csv(filepath, sep=",", index_col=False) 
            df.set_index('date', inplace=True)
            print(f"Client {name} added successfully.")
            print("**UPDATED DATA**")
            print(df)

        except ValueError:
            print("Invalid input")

    if "VIEW" in user_action:

        print("**CURRENT DATA**")
        df = pd.read_csv(filepath, sep=",", index_col=False) 
        df.set_index('date', inplace=True)
        print(df)

    if "EXIT" in user_action:

        print("Exit successfull")
        break

