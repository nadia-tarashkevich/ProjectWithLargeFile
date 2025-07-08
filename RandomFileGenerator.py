import random
import string
import os

def generate_random_filename(extension=".txt"):
    """Generates a random filename."""
    name = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return f"{name}{extension}"

def create_files_with_text(num_files, text):
    """Creates files with the specified text."""
    for _ in range(num_files):
        filename = generate_random_filename()
        with open(filename, 'w') as file:
            file.write(text)
        print(f"File created: {filename}")

if __name__ == "__main__":
    num_files_to_create = 20
    file_content = "example text"

    print(f"Creating {num_files_to_create} files containing the text: '{file_content}'")
    create_files_with_text(num_files_to_create, file_content)
    print("File creation complete.")