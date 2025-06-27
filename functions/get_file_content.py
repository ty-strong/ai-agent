import os

def get_file_content(working_directory, file_path):
    abs_path_to_file = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_dir = os.path.abspath(working_directory)

    # Security check: Ensure the target path is inside the working directory.
    if not abs_path_to_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_path_to_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        MAX_CHARS = 10000
        # Open with UTF-8 encoding and ignore errors for robustness against binary files.
        with open(abs_path_to_file, "r", encoding="utf-8", errors="ignore") as f:
            # Read one extra character to detect if the file is larger than the limit.
            content = f.read(MAX_CHARS + 1)
        
        # If the file is larger than the limit, truncate it and add a notice.
        if len(content) > MAX_CHARS:
            return content[:MAX_CHARS] + f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        else:
            return content
    except Exception as e:
        return f'Error: {e}'