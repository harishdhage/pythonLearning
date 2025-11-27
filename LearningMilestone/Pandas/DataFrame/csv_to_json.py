import pandas as pd
import json

# Read CSV file
csv_file = 'csvData.csv'
df = pd.read_csv(csv_file)

# Convert to JSON
json_file = 'pokemonData.json'
df.to_json(json_file, orient='records', indent=2)

print(f"✓ Successfully converted {csv_file} to {json_file}")
print(f"✓ Total records: {len(df)}")
print(f"\nFirst 3 records:")
print(json.dumps(df.head(3).to_dict(orient='records'), indent=2))
