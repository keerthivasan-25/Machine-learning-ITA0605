# Machine Learning Model Performance Analysis using Accuracy

# Training and Validation Accuracy
training_accuracy = [60, 65, 70, 75, 80, 85, 88, 92]
validation_accuracy = [58, 63, 68, 72, 73, 72, 70, 68]

# Find the epoch where overfitting starts
overfit_epoch = None

for i in range(1, len(training_accuracy)):
    if training_accuracy[i] > training_accuracy[i-1] and validation_accuracy[i] < validation_accuracy[i-1]:
        overfit_epoch = i + 1
        break

# Display Results
print("Machine Learning Model Performance")
print("----------------------------------")
print("Overfitting starts at Epoch:", overfit_epoch)

print("\nReason for decrease in Validation Accuracy:")
print("The model memorizes the training data instead of learning general patterns.")
print("Hence, training accuracy increases while validation accuracy decreases.")

print("\nMethods to Improve Validation Performance:")
print("1. Early Stopping")
print("2. Dropout Regularization")
