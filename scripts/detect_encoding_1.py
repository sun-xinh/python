import sys
import chardet
import string

def detect_file_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def clean_file(file_path, encoding):
    with open(file_path, 'r', encoding=encoding) as f:
        text = f.read()
    printable = set(string.printable)
    cleaned_text = ''.join(filter(lambda x: x in printable, text))
    return cleaned_text

if len(sys.argv) != 2:
    print("Please provide the file path as an argument.")
    sys.exit()

file_path = sys.argv[1]
detected_encoding = detect_file_encoding(file_path)
cleaned_text = clean_file(file_path, detected_encoding)

print('Cleaned text:', cleaned_text)

