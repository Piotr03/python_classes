import os

def files_count(my_folder = r'C:\python_hw_folder'):
    # It will store the number of files and the total size occupied respectively
    number_of_files, overall_size = 0, 0
    for file_name in os.listdir(my_folder):
        current_file = os.path.join(my_folder, file_name)
        # Here, if currentFile is a file, add 1 to number_of_files and add the file size to overall_size
        if os.path.isfile(current_file):
            number_of_files = number_of_files + 1
            overall_size = overall_size + os.path.getsize(current_file)
        #else recursively call the same function on the subfolder
        else:
            [temp1, temp2] = files_count(current_file)
            number_of_files = number_of_files + temp1
            overall_size = overall_size + temp2
    return [number_of_files, overall_size]

def result(my_folder = r'C:\python_hw_folder'):
    [number_of_files, overall_size] = files_count()
    print(f"Number of files counted: {number_of_files}\nOverall occupied size: {overall_size} Bytes\n")

result()