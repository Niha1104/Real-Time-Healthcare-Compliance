import pandas as pd

# Simulated API response (mock data)
data = {
    "patient_id": [101, 102, 103, 104, 105],
    "claim_amount": [500.25, 1300.75, 890.50, 2500.00, 300.00],
    "adherence_score": [0.95, 0.45, 0.85, 0.33, 0.90],
    "claim_date": ["2025-04-01", "2025-04-02", "2025-04-02", "2025-04-03", "2025-04-04"]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("etl_pipeline/raw_data.csv", index=False)

print("✅ Mock API data saved to raw_data.csv")