import os

def list_filenames_with_indices(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            # Displaying the filename and indices for inspection
            print(f"Filename: {filename}")
            for i, char in enumerate(filename):
                print(f"Index {i}: {char}")

# Example usage
folder_path = 'F:\\Lohnzettel\\rename'  # Replace with your folder path
list_filenames_with_indices(folder_path)
