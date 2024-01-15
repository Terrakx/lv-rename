import os

def list_filenames_with_new_names(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            # Extract the year and month from the filename using the correct indices
            year = filename[36:40]  # Indices for the year
            month = filename[40:42]  # Indices for the month

            new_name = f"Lohnverrechnung {month}-{year}.pdf"

            print(f"Original: '{filename}' -> New: '{new_name}'")

# Example usage
folder_path = 'F:\\Lohnzettel\\rename'  # Replace with your folder path
list_filenames_with_new_names(folder_path)
