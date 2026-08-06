# Training and Validation Loss Analysis

training_loss = [3.0, 2.6, 2.3, 2.1, 1.9, 1.7, 1.6, 1.4]
validation_loss = [2.7, 2.3, 2.1, 2.0, 2.2, 2.5, 2.8, 3.1]

# i) Find the epoch with minimum validation loss
best_epoch = validation_loss.index(min(validation_loss)) + 1

print("i) Optimal Generalization")
print("Best Epoch:", best_epoch)
print("Minimum Validation Loss:", min(validation_loss))

# ii) Detect overfitting
print("\nii) Overfitting Analysis")
for i in range(1, len(training_loss)):
    if (training_loss[i] < training_loss[i-1] and
            validation_loss[i] > validation_loss[i-1]):
        print("Overfitting starts from Epoch", i + 1)
        break

# iii) Regularization Techniques
print("\niii) Recommended Regularization Techniques")
print("1. Dropout")
print("   - Randomly disables neurons during training.")
print("   - Reduces overfitting and improves generalization.")

print("\n2. L2 Regularization (Weight Decay)")
print("   - Penalizes large weight values.")
print("   - Prevents overfitting and improves model performance on unseen data.")
