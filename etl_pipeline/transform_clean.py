import pandas as pd

# Load raw data
df = pd.read_csv("etl_pipeline/raw_data.csv")

# Drop rows with missing values
df.dropna(inplace=True)

# Convert date column
df["claim_date"] = pd.to_datetime(df["claim_date"])

# Add flag for high claim amounts
df["high_claim_flag"] = df["claim_amount"].apply(lambda x: 1 if x > 1000 else 0)

# Round adherence scores
df["adherence_score"] = df["adherence_score"].round(2)

# Save cleaned data
df.to_csv("etl_pipeline/clean_data.csv", index=False)

print("✅ Data cleaned and saved to clean_data.csv")