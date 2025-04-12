import os

# Specify the path to the directory containing the files.
directory = r"D:\Coding\FlexTalkLessons\Lessons"

# Iterate over every item in the directory.
for filename in os.listdir(directory):
    # Create the full path to the current file.
    old_path = os.path.join(directory, filename)
    
    # Check if the path corresponds to a file and if "Flex Talk" is in the file name.
    if os.path.isfile(old_path) and "Flex Talk" in filename:
        # Replace "Flex Talk" with "FT" in the file name.
        new_filename = filename.replace("Flex Talk", "FT")
        new_path = os.path.join(directory, new_filename)
        
        # Rename the file.
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")


