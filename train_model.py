import pandas as pd

# Load our cleaned dataset
data = pd.read_csv("heart.csv")

print("Dataset loaded successfully!")

X = data.drop("target", axis=1)
y = data["target"]

print("\nInput data (X):")
print(X.head())

print("\nTarget data (y):")
print(y.head())

print("\nNumber of input columns:")
print(X.shape[1])

print("\nNumber of patients:")
print(X.shape[0])
from sklearn.model_selection import train_test_split

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining patients:")
print(X_train.shape[0])

print("\nTesting patients:")
print(X_test.shape[0])
# --------------------------------
# Train the machine learning model
# --------------------------------

from sklearn.linear_model import LogisticRegression

# Create the model
model = LogisticRegression(max_iter=1000)

# Teach the model using training data
model.fit(X_train, y_train)

print("\nModel training completed!")
# --------------------------------
# Make predictions
# --------------------------------

y_pred = model.predict(X_test)

print("\nPredictions:")
print(y_pred)
# --------------------------------
# Check accuracy
# --------------------------------

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)

print("\nModel accuracy:")
print(accuracy)

print("\nModel accuracy percentage:")
print(accuracy * 100, "%")
# --------------------------------
# Classification Report
# --------------------------------

from sklearn.metrics import classification_report

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
# --------------------------------
# Confusion Matrix
# --------------------------------

from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["No Disease", "Disease"],
    yticklabels=["No Disease", "Disease"]
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Heart Disease Prediction - Confusion Matrix")

plt.show()
# --------------------------------
# Compare different ML models
# --------------------------------

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    ),
    "K-Nearest Neighbors": KNeighborsClassifier()
}

print("\n==============================")
print("MODEL COMPARISON")
print("==============================")

for name, model in models.items():

    # Train model
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Calculate accuracy
    model_accuracy = accuracy_score(y_test, predictions)

    print("\n" + name)
    print("Accuracy:", model_accuracy)
    print("Percentage:", round(model_accuracy * 100, 2), "%")
    # --------------------------------
# Save the best model
# --------------------------------

best_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train the Random Forest
best_model.fit(X_train, y_train)

# Save the trained model
import joblib

joblib.dump(best_model, "heart_disease_model.pkl")

print("\nBest model saved successfully!")
print("File: heart_disease_model.pkl")