import re  # For more flexible word extraction

# Read the story from file
with open("story.txt", "r") as f:
    story = f.read()

# Extract placeholders using regular expressions
words = set(re.findall(r"<[^<>]+>", story))  # Finds all text between < and >

# Prompt the user for inputs
answers = {}
for word in words:
    clean_word = word.strip("<>")  # Remove < and > for a cleaner prompt
    answer = input(f"Enter a word for {clean_word}: ")
    answers[word] = answer.strip()

# Replace placeholders with user inputs
for word, answer in answers.items():
    story = story.replace(word, answer)

# Display the final story
print("\nHere is your completed story:\n")
print(story)

# Optional: Save the completed story to a new file
with open("completed_story.txt", "w") as f:
    f.write(story)
    print("\nYour story has been saved to 'completed_story.txt'.")
