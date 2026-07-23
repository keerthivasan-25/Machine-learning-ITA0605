# Medical Image Classification Performance Metrics

# Given values
TP = 210
TN = 190
FP = 30

# Total samples
total_samples = 1800 * 2      # 3600
test_samples = total_samples * 0.20   # 720

# Calculate False Negatives
FN = int(test_samples - (TP + TN + FP))

# Performance Metrics
accuracy = (TP + TN) / test_samples
precision = TP / (TP + FP)
recall = TP / (TP + FN)
specificity = TN / (TN + FP)

# Display Results
print("False Negatives (FN):", FN)
print("Accuracy:", round(accuracy * 100, 2), "%")
print("Precision:", round(precision * 100, 2), "%")
print("Sensitivity (Recall):", round(recall * 100, 2), "%")
print("Specificity:", round(specificity * 100, 2), "%")
