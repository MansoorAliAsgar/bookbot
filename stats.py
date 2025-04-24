import string


def get_num_words(file_contents):
    """
    Counts the number of words in the given text.

    Parameters:
        file_contents (str): The full text of the book or document.

    Returns:
        int: Total number of words.
    """
    words = file_contents.split()
    return len(words)


def get_char_count(file_contents):
    """
    Counts the frequency of each alphabet and punctuation character (case-insensitive).

    Parameters:
        file_contents (str): The full text of the book or document.

    Returns:
        dict: A dictionary with characters as keys and their frequencies as values.
    """
    result = {}
    file_contents_lower = file_contents.lower()

    # Define the characters to count: lowercase letters and punctuation
    valid_chars = string.ascii_lowercase + string.punctuation

    # Initialize the result dictionary with all valid characters set to 0
    for char in valid_chars:
        result[char] = 0

    # Count occurrences of valid characters
    for char in file_contents_lower:
        if char in result:
            result[char] += 1

    return result


def get_sorted_list_of_dicts(input_dict):
    """
    Converts a character frequency dictionary into a sorted list of dictionaries.

    Parameters:
        input_dict (dict): A dictionary with character frequencies.

    Returns:
        list: A list of dictionaries sorted by frequency in descending order.
    """
    # Convert the input dictionary into a list of dictionaries
    char_list = [{"char": char, "num": count} for char, count in input_dict.items()]

    # Sort the list based on frequency (descending)
    char_list.sort(key=lambda item: item["num"], reverse=True)

    return char_list
