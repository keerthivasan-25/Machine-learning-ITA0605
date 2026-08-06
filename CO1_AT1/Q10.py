# Confusion Matrix Values
TP = 230  # Defective identified as Defective
FN = 20   # Defective identified as Non-Defective
TN = 225  # Non-Defective identified as Non-Defective
FP = 25   # Non-Defective identified as Defective

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
