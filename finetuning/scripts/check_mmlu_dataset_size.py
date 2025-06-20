 import pandas as pd

# Read and print sizes
train_df = pd.read_csv('mmlu_dataset/train.csv')
valid_df = pd.read_csv('mmlu_dataset/valid.csv')
test_df = pd.read_csv('mmlu_dataset/test.csv')

print(f"Train set size: {len(train_df)} examples")
print(f"Validation set size: {len(valid_df)} examples")
print(f"Test set size: {len(test_df)} examples")

# Print column names and first row for reference
print("\nColumn names:", train_df.columns.tolist())
print("\nFirst row example:")
print(train_df.iloc[0]) 