# Confusion Matrix Values
TP = 138  # Diseased identified as Diseased
FN = 12   # Diseased identified as Healthy
TN = 135  # Healthy identified as Healthy
FP = 15   # Healthy identified as Diseased

# Calculate Metrics
accuracy = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP)
sensitivity = TP / (TP + FN)   # Recall
specificity = TN / (TN + FP)
f1_score = (2 * precision * sensitivity) / (precision + sensitivity)

# Display Results
print("Accuracy    :", round(accuracy * 100, 2), "%")
print("Precision   :", round(precision * 100, 2), "%")
print("Sensitivity :", round(sensitivity * 100, 2), "%")
print("Specificity :", round(specificity * 100, 2), "%")
print("F1-Score    :", round(f1_score * 100, 2), "%")
