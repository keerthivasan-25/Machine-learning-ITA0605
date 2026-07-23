# Bayes' Theorem - Probability that the selected box was Box C

# Prior probabilities
P_A = 1/4
P_B = 1/2
P_C = 1/4

# Probability of drawing a blue ball from each box
P_Blue_A = 4/12
P_Blue_B = 7/15
P_Blue_C = 2/15

# Total probability of drawing a blue ball
P_Blue = (P_Blue_A * P_A) + (P_Blue_B * P_B) + (P_Blue_C * P_C)

# Bayes' Theorem
P_C_given_Blue = (P_Blue_C * P_C) / P_Blue

# Display result
print("Probability that the selected box was Box C =", P_C_given_Blue)
print("Answer in fraction = 2/21")
