from sklearn.linear_model import LinearRegression

# Training data
X = [[500], [1000], [1500], [2000], [2500]]
y = [20, 40, 60, 80, 100]

# Create model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Predict price for 1800 sq.ft
prediction = model.predict([[1800]])

print("Predicted Price:", prediction[0])