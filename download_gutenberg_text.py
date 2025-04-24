import requests
import os

# Mapping of filenames to their corresponding Project Gutenberg URLs
GUTENBERG_BOOKS_URL_MAPPING = {
    "frankenstein.txt": "https://www.gutenberg.org/cache/epub/41445/pg41445.txt",
    "mobydick.txt": "https://www.gutenberg.org/cache/epub/2701/pg2701.txt",
    "prideandprejudice.txt": "https://www.gutenberg.org/cache/epub/1342/pg1342.txt",
}


def download_and_save_text(url, folder="books", filename="file.txt"):
    """
    Downloads a text file from the specified URL and saves it to a local folder.

    Parameters:
        url (str): The URL of the text file to download.
        folder (str): The folder where the file should be saved. Default is "books".
        filename (str): The name to save the file as. Default is "file.txt".
    """
    # Create the folder if it does not exist
    os.makedirs(folder, exist_ok=True)

    # Define the full path to save the file
    filepath = os.path.join(folder, filename)

    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Write the content to a local file in binary mode
        with open(filepath, "wb") as file:
            file.write(response.content)

        print(f"Downloaded and saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {filename}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while processing {filename}: {e}")


def main():
    """
    Downloads all books listed in the GUTENBERG_BOOKS_URL_MAPPING dictionary.
    """
    for filename, url in GUTENBERG_BOOKS_URL_MAPPING.items():
        download_and_save_text(url, filename=filename)


if __name__ == "__main__":
    main()
