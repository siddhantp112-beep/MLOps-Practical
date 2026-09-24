from sklearn.neighbors import KNeighborsClassifier

# Training data
X = [[150, 50], [160, 55], [170, 65], [180, 75], [190, 85]]
y = ["Short", "Short", "Medium", "Tall", "Tall"]

# Create model
model = KNeighborsClassifier(n_neighbors=3)

# Train the model
model.fit(X, y)

# Predict for a new person
prediction = model.predict([[175, 70]])

print("Predicted Class:", prediction[0])