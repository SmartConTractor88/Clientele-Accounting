import pandas as pd

filepath = "clientele.xlsx"

df = pd.read_excel(filepath, sheet_name="2025", index_col="date")

print(df)


