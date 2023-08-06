import os
import shutil
import argparse

def organize_files(source_folder, destination_folder, file_extension):
    for root, _, files in os.walk(source_folder):
        for file in files:
            extension = os.path.splitext(file)[1][1:].lower()
            if extension == file_extension:
                file_path = os.path.join(root, file)
                shutil.move(file_path, destination_folder)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Automation')
    parser.add_argument('--source_folder', type = str, help='Source folder')
    parser.add_argument('--destination_folder', type = str, help='destination folder')
    parser.add_argument('--extension', type = str, help='destination folder')
    args = parser.parse_args()
    
    organize_files(args.source_folder,args.destination_folder,args.extension)
    
    if not os.path.exists(args.source_folder):
        print("Source folder does not exist.")
    elif not os.path.exists(args.destination_folder):
        print("Destination folder does not exist.")
    else:
        organize_files(args.source_folder, args.destination_folder, args.extension)
        print("Files organized successfully.")
