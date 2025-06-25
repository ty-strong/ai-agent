import os

def get_files_info(working_directory, directory=None):
    # Determine the target path to list files from
    if directory and directory != ".":
        path_to_list = os.path.join(working_directory, directory)
    else:
        path_to_list = working_directory

    # Security check: ensure the resolved path is within the working directory
    real_working_dir = os.path.realpath(working_directory)
    real_path_to_list = os.path.realpath(path_to_list)

    if not real_path_to_list.startswith(real_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(real_path_to_list):
        return f'Error: "{directory if directory else working_directory}" is not a directory'

    try:
        files_info = []
        for content in os.listdir(real_path_to_list):
            content_path = os.path.join(real_path_to_list, content)
            try:
                is_dir = os.path.isdir(content_path)
                if is_dir or os.path.isfile(content_path):
                    file_size = os.path.getsize(content_path)
                    files_info.append(f"{content}: file_size={file_size}, is_dir={is_dir}")
            except OSError:
                # Skip files we can't access, like broken symlinks
                continue
        return "\n".join(files_info)
    except Exception as e:
        return f"Error: {e}"