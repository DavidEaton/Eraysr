import os
import time


def pretend_overwrite_file(file_path, passes=3):
    """Simulate overwriting the file by printing file metadata instead of modifying it."""
    file_size = os.path.getsize(file_path)
    modified_time = time.ctime(os.path.getmtime(file_path))

    print(f"Starting overwrite simulation for: {file_path}")
    print(f"File size: {file_size} bytes")
    print(f"Last modified: {modified_time}")

    for pass_num in range(1, passes + 1):
        print(f"Pass {pass_num}/{passes}: Simulating overwrite...")
    print(f"Pretend deletion complete for: {file_path}")
    print("=" * 50)


def pretend_secure_delete_directory(directory_path, passes=3):
    """Simulate securely deleting all files in a directory without making actual changes."""
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            pretend_overwrite_file(file_path, passes)
    print("Simulation complete. No files were modified.")


# Set your directory path here for testing
directory_path = "C:\\Users\\HoobaLou\\Pictures"
pretend_secure_delete_directory(directory_path, passes=3)
