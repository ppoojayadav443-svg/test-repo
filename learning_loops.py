# A list of fake AI accuracy scores starting low and getting better
accuracy_scores = [0.45, 0.60, 0.78, 0.89, 0.95]

print("Starting AI Model Training...")

# A loop to print the progress of our training
epoch_number = 1
for score in accuracy_scores:
    print(f"Epoch {epoch_number}: Model accuracy is {score * 100}%")
    epoch_number = epoch_number + 1

print("Training Complete! Ready for GitHub.")