import pandas as pd
import os

input_file = os.path.join("data", "Persediaan Desember 2023.xlsx")
output_file = os.path.join("data", "persediaan_desember_2023.json")

df = pd.read_excel(input_file)
df.to_json(output_file, orient="records", indent=4)

print(f"✅ File JSON dibuat: {output_file}")
