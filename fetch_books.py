import requests

# Replace with your actual GitHub Pages URL
url = "https://<username>.github.io/book-api-project/custom_data.json"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    print("Fetched Book Data:\n")
    for book in data:
        print(f"Title: {book['name']}")
        print(f"Description: {book['description']}")
        print("Specifications:")
        for key, value in book['specifications'].items():
            print(f"  {key.capitalize()}: {value}")
        print(f"Tags: {', '.join(book['tags'])}")
        print("-" * 40)

except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
