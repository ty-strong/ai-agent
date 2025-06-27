import os
import subprocess
import sys

def run_python_file(working_directory, file_path, args=None):
    abs_path_to_file = os.path.abspath(os.path.join(working_directory, file_path))
    abs_working_dir = os.path.abspath(working_directory)

    # Security check: Ensure the target path is inside the working directory.
    if not abs_path_to_file.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_path_to_file):
        return f'Error: File "{file_path}" not found.'
    
    if not os.path.isfile(abs_path_to_file):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        commands = [sys.executable, abs_path_to_file]
        if args:
            commands.extend(args)

        result = subprocess.run(
            commands,
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=30,
        )

        output_parts = []
        if result.stdout:
            output_parts.append(f'STDOUT:\n{result.stdout.strip()}')
        if result.stderr:
            output_parts.append(f'STDERR:\n{result.stderr.strip()}')
        if not output_parts:
            output_parts.append('No output was produced.')
        output_parts.append(f'Process finished with exit code {result.returncode}.')
        return "\n".join(output_parts)
    except subprocess.TimeoutExpired:
        return f'Error: Execution of "{file_path}" timed out after 30 seconds.'
    except Exception as e:
        return f'Error: An unexpected error occurred while executing the python file: {e}'