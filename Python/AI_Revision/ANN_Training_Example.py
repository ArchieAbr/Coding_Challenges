# Free online compiler: https://www.programiz.com/python-programming/online-compiler/
#  Input Layer   Output Layer
#    (x)-----------(y)


# Initialize weights and biases
w = 0.5
b = 0.1

# Define observation
x = 1
observed_y = 0.5

# Forward pass
y = w * x + b

print("Initial w:", w)
print("Initial b:", b)
print("Predicted y:", y)
print("True y:", observed_y)
# Calculate loss
loss = (y - observed_y)**2

# Backward pass
dloss_dy = 2 * (y - observed_y)
dy_dw = x
dy_db = 1
# Chain rule
dw = dloss_dy * dy_dw
db = dloss_dy * dy_db

# Update weights and biases
learning_rate = 0.1
w = w - learning_rate * dw
b = b - learning_rate * db

# Use updated weights and biases for next forward pass
y = w * x + b

# Print updated values
print('**********After training for 1 step ***********')
print("Updated w:", w)
print("Updated b:", b)
print("Predicted y:", y)



# Calculate loss
loss = (y - observed_y)**2

# Backward pass
dloss_dy = 2 * (y - observed_y)
dy_dw = x
dy_db = 1
# Chain rule
dw = dloss_dy * dy_dw
db = dloss_dy * dy_db

# Update weights and biases
learning_rate = 0.1
w = w - learning_rate * dw
b = b - learning_rate * db

# Use updated weights and biases for next forward pass
y = w * x + b

# Print updated values
print('**********After training for 2 steps ***********')
print("Updated w:", w)
print("Updated b:", b)
print("Predicted y:", y)



# Calculate loss
loss = (y - observed_y)**2

# Backward pass
dloss_dy = 2 * (y - observed_y)
dy_dw = x
dy_db = 1
# Chain rule
dw = dloss_dy * dy_dw
db = dloss_dy * dy_db

# Update weights and biases
learning_rate = 0.1
w = w - learning_rate * dw
b = b - learning_rate * db

# Use updated weights and biases for next forward pass
y = w * x + b

# Print updated values
print('**********After training for 3 steps ***********')
print("Updated w:", w)
print("Updated b:", b)
print("Predicted y:", y)
