import pandas as pd
import os

DATA_PATH = "data/raw"

excel_files = [f for f in os.listdir(DATA_PATH) if f.endswith(".xlsx")]

print("=" * 80)
print(f"TOTAL FILES FOUND: {len(excel_files)}")
print("=" * 80)

for file in excel_files:

    print("\n" + "=" * 80)
    print(f"FILE: {file}")
    print("=" * 80)

    file_path = os.path.join(DATA_PATH, file)

    try:
        df = pd.read_excel(file_path)

        print("\nSHAPE:")
        print(df.shape)

        print("\nDATA TYPES:")
        print(df.dtypes)

        print("\nFIRST 5 ROWS:")
        print(df.head())

        print("\nMISSING VALUES:")
        print(df.isnull().sum())

        print("\nDUPLICATE ROWS:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"ERROR READING FILE: {e}")