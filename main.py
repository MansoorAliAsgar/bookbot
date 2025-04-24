import sys
from stats import get_num_words, get_char_count, get_sorted_list_of_dicts


def main():
    # Check if a path to the book was provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the path to the book from the command-line argument
    book_path = sys.argv[1]

    # Read the contents of the book file
    file_contents = read_book_text(book_path)

    # Get total word count from the book content
    num_words = get_num_words(file_contents)

    # Get character frequency dictionary from the book content
    char_count = get_char_count(file_contents)

    # Generate the analysis report header
    report_lines = [
        "============ BOOKBOT ============",
        f"Analyzing book found at {book_path}...",
        "----------- Word Count ----------",
        f"Found {num_words} total words",
        "--------- Character Count -------",
    ]

    # Sort the character frequency dictionary into a list of dicts and append to the report
    sorted_chars = get_sorted_list_of_dicts(char_count)
    for item in sorted_chars:
        report_lines.append(f"{item['char']}: {item['num']}")

    # Join the report lines and print the final report
    print("\n".join(report_lines))


def read_book_text(book_path):
    """Read and return the contents of the book file at the given path."""
    try:
        with open(book_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {book_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Run the main function and exit with its return code
    sys.exit(main())
