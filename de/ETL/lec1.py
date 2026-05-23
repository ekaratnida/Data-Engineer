import pandas as pd
import numpy as np

def extract_data():

    raw_data = {
        'Transaction_ID': [101, 102, 103, 104],
        'User_ID': [5001, 5002, 5001, 5003],
        'Product': [' laptop ', 'Smartphone', ' LAPTOP ', 'Headphones'],
        'Price': [1200.00, 800.00, 1200.00, np.nan],
        'Quantity': [1, 2, 1, 1],
        'Purchase_Date': ['2026/05/20', '20-05-2026', '2026-05-21', '2026-05-22']
    }
    df = pd.DataFrame(raw_data)
    print("--- Extracted Raw Data ---")
    print(df, "\n")
    return df

def transform_data(df):

    print("--- Starting Transformation ---")
    
    df = df.dropna(subset=['Price'])
    
    df['Product'] = df['Product'].str.strip().str.upper()
    
    df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'], errors='coerce').dt.strftime('%Y-%m-%d')
    
    df['Total_Spent'] = df['Price'] * df['Quantity']
    
    df = df.drop_duplicates()
    
    print(df, "\n")

    return df

def load_data(df, target_destination):

    df.to_csv(target_destination, index=False)
    
    print(f"--- Load Complete! Data successfully saved to: {target_destination} ---")

if __name__ == "__main__":

    # 1. Extract
    raw_df = extract_data()
    
    # 2. Transform
    transformed_df = transform_data(raw_df)
    
    # 3. Load
    load_data(transformed_df, 'warehouse_sales_fact.csv')
