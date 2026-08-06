# Confusion Matrix Values
TP = 119  # Front identified as Front
FN = 6    # Front identified as Back
TN = 120  # Back identified as Back
FP = 5    # Back identified as Front

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
