import pandas as pd

# Name of the original Cleveland dataset
file_name = "heart+disease/processed.cleveland.data"

# Column names
columns = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal",
    "target"
]

# Read the dataset
data = pd.read_csv(
    file_name,
    names=columns,
    na_values="?"
)

print("Original data:")
print(data.head())

print("\nDataset shape:")
print(data.shape)

# Remove rows containing missing values
data = data.dropna()

# Convert target:
# 0 = no heart disease
# 1,2,3,4 = heart disease
data["target"] = (data["target"] > 0).astype(int)

# Save clean dataset
data.to_csv("heart.csv", index=False)

print("\nClean dataset created successfully!")

print("\nFinal shape:")
print(data.shape)

print("\nTarget values:")
print(data["target"].value_counts())

print("\nSaved as: heart.csv")