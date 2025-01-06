languages = ['English', 'German', 'Spanish']

for item in languages:
    with open(f"{item}.txt","w") as file:
        file.write(item)

with open("German.txt", "r") as file:
    content = file.read()
    with open("story_copy.txt", "w") as copy:
        copy.write(content)