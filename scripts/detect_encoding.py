# Import necessary libraries
import sys
import chardet
import string
import re  # Regular expression library

# Function to detect file encoding
def detect_file_encoding(file_path):
    with open(file_path, 'rb') as f:  # Open the file in binary mode
        result = chardet.detect(f.read())  # Detect the encoding of the file
    return result['encoding']  # Return the detected encoding

# Function to clean the file
def clean_file(file_path, encoding):
    with open(file_path, 'r', encoding=encoding) as f:  # Open the file with the detected encoding
        text = f.read()  # Read the file
    printable = set(string.printable)  # Set of printable characters
    cleaned_text = ''.join(filter(lambda x: x in printable, text))  # Filter out non-printable characters
    # Split the cleaned text on the phrase "new words? and expressions", case-insensitively. The "?"
    # in "words?" means the "s" is optional, so this matches both "word" and "words".
    cleaned_text = re.split('new words? and expressions', cleaned_text, flags=re.IGNORECASE)[0]
    return cleaned_text  # Return the cleaned and split text

# This line checks if the script is being run directly (not imported from another script)
if __name__ == '__main__':
    # Check if the file path was provided as an argument
    if len(sys.argv) != 2:
        print("Please provide the file path as an argument.")
        sys.exit()  # Exit if no file path was provided

    # Extract the file path from the command line arguments
    file_path = sys.argv[1]
    # Detect the encoding of the file
    detected_encoding = detect_file_encoding(file_path)
    # Clean the file
    cleaned_text = clean_file(file_path, detected_encoding)

    # Print the cleaned text
    print('Cleaned text:', cleaned_text)

