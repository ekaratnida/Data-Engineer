import pandas as pd
#import sqlite3
from prefect import task, flow
from prefect.logging import get_run_logger

# Task 1: Mock data extraction
@task(retries=3, retry_delay_seconds=10)
def extract_data():
    print("Extracting data...")
    # Simulating raw API data
    raw_data = {
        "user_id": [1, 2, 3, 4],
        "name": ["Alice", "Bob", "Charlie", "David"],
        "signup_age": [28, -5, 34, None]  # Contains bad/missing data
    }
    return pd.DataFrame(raw_data)

# Task 2: Data Transformation using Pandas
@task(log_prints=True)
def transform_data(df: pd.DataFrame):
    print("Cleaning data with Pandas...")
    # Fix the missing/invalid age rows
    df["signup_age"] = df["signup_age"].fillna(0)
    df = df[df["signup_age"] >= 0]
    return df

# Task 3: Load and query using SQL
@task(log_prints=True)
def load_and_query_sql(df: pd.DataFrame):
    logger = get_run_logger()
    logger.info(df.iloc[0])
    #print("Loading data into SQL database...")
    # Connect to a local SQLite Database
    #conn = sqlite3.connect("my_data.db")
    
    # Write Pandas Dataframe to a SQL table
    #df.to_sql("users", conn, if_exists="replace", index=False)
    
    # Run an automated SQL query
    #result = pd.read_sql("SELECT * FROM users WHERE signup_age > 20", conn)
    #print("SQL Query Result (Users older than 20):")
    #print(result)
    
    #conn.close()

# The Orchestrator Flow
@flow(name="test1", log_prints=True)
def main_flow():
    raw_df = extract_data()
    clean_df = transform_data(raw_df)
    load_and_query_sql(clean_df)

if __name__ == "__main__":
    # Execute the flow locally
    main_flow()
    #main_flow.serve(name="abc", cron="*/1 * * * *")
