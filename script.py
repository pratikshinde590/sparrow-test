import os

# Define the path to your file
file_path = "path/to/your/file"

# Read the content of the file
with open(file_path, "r") as file:
    file_content = file.read()

# Set the content as an environment variable
os.environ["FILE_CONTENT"] = file_content

# Print the content to verify
print("File content:", file_content)
