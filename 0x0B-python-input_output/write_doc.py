#!/usr/bin/python3
import sys

def copy_file_lines(source_file, destination_file, line_number):
    """
    Copies lines from a source file to a destination file up to a specified line number.

    Args:
        source_file (str): The path to the source file.
        destination_file (str): The path to the destination file.
        line_number (int): The line number up to which lines will be copied.

    Returns:
        None
    """
    with open(source_file, 'r', encoding='utf-8') as src_file, open(destination_file, 'w', encoding='utf-8') as dest_file:
        for index, line in enumerate(src_file, start=1):
            dest_file.write(line)
            if index == line_number:
                break

if __name__ == "__main__":
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py source_file destination_file line_number")
        sys.exit(1)
    
    # Extract command-line arguments
    source_file = sys.argv[1]
    destination_file = sys.argv[2]
    line_number = int(sys.argv[3])
    
    # Call the function
    copy_file_lines(source_file, destination_file, line_number)
    print(f"Lines up to line {line_number} copied from {source_file} to {destination_file}.")

