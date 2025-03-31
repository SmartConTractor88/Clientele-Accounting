import pandas as pd

filepath = "client_data.csv"

df = pd.read_csv(filepath, sep=",") 

data = [['02/03/2025','Kendrick Lamar','01743339999','200','Card','Afro taper fade', 'Started writing a new album.']]

new_data = pd.DataFrame(data)

new_data.to_csv(filepath, index=False, mode="a", header=False)

df = pd.read_csv(filepath, sep=",") 
print(df)


