# Machine Learning Model Performance Analysis

# Training and Validation Loss
training_loss = [2.8, 2.5, 2.2, 2.0, 1.8, 1.6, 1.5, 1.3]
validation_loss = [2.4, 2.2, 2.0, 2.1, 2.3, 2.6, 2.9, 3.2]

# Find the epoch where overfitting begins
overfit_epoch = None

for i in range(1, len(training_loss)):
    if training_loss[i] < training_loss[i-1] and validation_loss[i] > validation_loss[i-1]:
        overfit_epoch = i + 1
        break

# Display Results
print("Model Performance Analysis")
print("---------------------------")
print("Overfitting starts at Epoch:", overfit_epoch)

print("\nTechniques to Reduce Overfitting:")
print("1. Early Stopping")
print("2. Dropout Regularization")

print("\nEffect of Overfitting:")
print("The model performs well on training data but poorly on unseen data.")
print("It reduces the model's generalization ability and increases validation error.")
