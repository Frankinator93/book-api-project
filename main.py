import json

with open('custom_data.json', 'r') as file:
    data = json.load(file)

for book in data:
    print(f"Name: {book['name']}")
    print(f"Description: {book['description']}")
    print("Tags:", ", ".join(book["tags"]))
    print("-" * 30)
