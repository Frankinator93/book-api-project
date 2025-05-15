import requests

# Replace with your actual GitHub Pages URL
url = "https://github.com/Frankinator93/book-api-project/tree/main"

def fetch_and_display_books(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()

        print("📚 Fetched Book Data:\n")
        for book in data:
            print(f"Title: {book.get('name', 'N/A')}")
            print(f"Description: {book.get('description', 'N/A')}")
            print("Specifications:")
            specs = book.get('specifications', {})
            for key, value in specs.items():
                print(f"  {key.capitalize()}: {value}")
            tags = book.get('tags', [])
            print(f"Tags: {', '.join(tags)}")
            print("-" * 40)

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Connection error. Please check your internet or URL.")
    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    except ValueError:
        print("Error parsing JSON. Please check the file format.")

# Call the function
fetch_and_display_books(url)
