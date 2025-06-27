import os

def get_files_info(working_directory, directory="."):
    # Resolve the absolute path for the target directory to list.
    path_to_list = os.path.abspath(os.path.join(working_directory, directory))
    abs_working_dir = os.path.abspath(working_directory)

    # Security check: Ensure the target path is inside the working directory.
    if not path_to_list.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(path_to_list):
        return f'Error: "{directory}" is not a directory'

    try:
        files_info = []
        for item_name in os.listdir(path_to_list):
            item_path = os.path.join(path_to_list, item_name)
            try:
                is_dir = os.path.isdir(item_path)
                # We only list regular files and directories, skipping others (e.g., symlinks, pipes).
                if is_dir or os.path.isfile(item_path):
                    file_size = os.path.getsize(item_path)
                    files_info.append(f'{item_name}: file_size={file_size}, is_dir={is_dir}')
            except OSError:
                # Skip items we can't access, such as broken symlinks or due to permissions.
                continue
        return "\n".join(files_info)
    except Exception as e:
        return f'Error: {e}'