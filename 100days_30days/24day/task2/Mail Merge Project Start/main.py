# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
STARTING_LETTER_FILE_PATH = "/Users/jonaszsojka/python_git/Python_projects_git/100days_30days/24day/task2/Mail Merge Project Start/Input/Letters/starting_letter.txt"
INVITED_NAMES_FILE_PATH = "/Users/jonaszsojka/python_git/Python_projects_git/100days_30days/24day/task2/Mail Merge Project Start/Input/Names/invited_names.txt"
template = ""
names = []

with open(STARTING_LETTER_FILE_PATH, mode="r") as file:
    template = file.read()

with open(INVITED_NAMES_FILE_PATH, mode="r") as file:
    names = file.read().split() # albo strip() readlines()

for name in names:
    filename = f"letter_for_{name}.txt"
    text = template.replace("[name]", name)
    with open(filename, mode="w") as file:
        file.write(text)


