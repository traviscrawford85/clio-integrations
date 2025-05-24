import sys


def search_ref_in_file(file_path):
    with open(file_path) as f:
        lines = f.readlines()

    for line in lines:
        if '$ref' in line:
            print(line.strip())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python search_ref.py schema_keys.txt")
    else:
        search_ref_in_file(sys.argv[1])
