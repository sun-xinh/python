import chardet
import sys

def detect_file_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

if len(sys.argv) != 2:
    print("Please provide the file path as an argument.")
    sys.exit()

file_path = sys.argv[1]
detected_encoding = detect_file_encoding(file_path)

print('Detected encoding:', detected_encoding)

