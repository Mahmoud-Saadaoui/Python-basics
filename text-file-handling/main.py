# "x" creates a new file. It throws an error if the file already exists.
# "w" creates a new file or overwrites the existing one.
file_two = open('file_two.txt', 'w')


# Writing text into the file
file_two.write("Hello World!\n")
file_two.write("Hello Python!\n")


# Always close the file when not using "with"
file_two.close()


# --- File Handling Process in Python ---
# 1. Open the file
# 2. Read or write
# 3. Close the file


# Create or overwrite a file (previous content is removed)
with open('file_two.txt', 'w') as f:
    f.write('This is a new file')


# Append to a file (previous content is preserved)
with open('file_two.txt', 'a') as f:
    f.write('This is a new file')


# The "with" statement automatically closes the file
# This prevents keeping files open unintentionally,
# which can waste system resources or lock the file.