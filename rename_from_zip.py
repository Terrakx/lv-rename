import os

def rename_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            # Extract the year and month from the filename using the correct indices
            year = filename[36:40]  # Indices for the year
            month = filename[40:42]  # Indices for the month

            new_name = f"Lohnverrechnung {month}-{year}.pdf"

            # Construct full file paths
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_name)

            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed '{filename}' to '{new_name}'")

# Example usage
folder_path = 'F:\\Lohnzettel\\rename'  # Replace with folder path
rename_files(folder_path)
