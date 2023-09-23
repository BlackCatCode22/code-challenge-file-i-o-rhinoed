# Code Challenge - File I/O
#
# Python file name: fileIO_code_challenge.py
#
# Date: September, 21 2023
#
# Programmer's name: Mark Edmunds

# ********************************************************************************************
import os

# Define the input and output file paths
# Use os.getcwd() to get the current working directory
# checking the operating system name to determine the correct path separator
input_file_path = os.getcwd() + "/arrivingAnimals.txt" if os.name == "posix" else os.getcwd() + r"\\arrivingAnimals.txt"
# Use r (raw) before the path string to tell Python to not use the backslash as an escape character
output_file_path = os.getcwd() + "/outputFile.txt" if os.name == "posix" else os.getcwd() + r"\\outputFile.txt"
print(f"input_file_path: {input_file_path}")
print(f"output_file_path: {output_file_path}")


def get_species(my_str):
    # check if my_str is a string if not raise TypeError
    if type(my_str) != str:
        raise TypeError("my_str must be a string")

    # Split my_str using the character space
    words = my_str.split()
    print(type(words))
    # words is a list you iterate over it, access elements by index, etc.
    # try to ger the 5th element on exception return None
    try:
        return words[4]
    except IndexError:
        print(f"IndexError: {my_str} is not long enough")
        return None


# Open the input file for reading
try:
    with open(input_file_path, 'r') as input_file:
        # Read lines from the input file
        lines = input_file.readlines()
        # 'lines' now contains a list of all lines in the input file
        # type of 'lines'
        print(type(lines))
        print(" Fill in the blank: The readlines() method returns a list containing all the text lines of input_file.")
        # 2nd element and 4th element of lines
        print(f"The second list element is: {lines[1]}")
        print(f"The fourth list element is: {lines[3]}")
        print("\n\n")
        print(lines)
        print("\n\n")

        # Open the output file for writing
        with open(output_file_path, "w") as output_file:
            for line in lines:
                # Split each line on the comma
                substrings = line.strip().split(',')
                # type of substrings
                print(f"\n The data type of substrings is ...{type(substrings)}")
                print(substrings)
                # first and second element of substrings
                print(f"The first substring is: {substrings[0]}")
                print(f"The second substring is: {substrings[1]}")
                # call get_species() and print the species using the first element of substrings
                print(f"The species is: {get_species(substrings[0])}")
                # output each substring on a separate line
                for string in substrings:
                    print(string)
                # using join() to join substrings with a newline character
                print("\n".join(substrings))
                #
                # using join() to join substrings with an asteriks character
                print("*************** ".join(substrings))

                # Write each substring to the output file separated by newlines
                output_file.write("\n".join(substrings))
                #
                # Add two empty lines between groups of substrings
                output_file.write("\n\n")

    print("\n\nData processed and written to 'outputFile.txt'!")

except TypeError:
    print("TypeError: my_str must be a string")

    # modify the input file path to cause a FileNotFoundError
    print(os.getcwd() + "/arrivingAnimal.txt")
except FileNotFoundError:
    # This is probably the most common file i/o error.
    print(f"Error: The file '{input_file_path}' was not found.")
except IOError as e:
    # Handle file I/O errors
    if "No space left on device" in str(e):
        # Disk full error
        print("Exception caught! Disk full. Cannot write to the file.")
    elif "Permission denied" in str(e):
        # File locked error
        print("Error: File is locked. Cannot write to the file.")
    else:
        # Other I/O errors (file is corrupted - this happens sometimes on thumb drives )
        print(f"An error occurred: {str(e)}")

except PermissionError:
    # Handle the PermissionError exception here
    print("Error: Permission denied. You don't have the necessary permissions to modify this file.")

except Exception as e:
    # Handle other exceptions you did not imagine.
    print(f"An error occurred: {str(e)}")

finally:
    # Code in this block will execute regardless of whether an exception occurred or not.
    print(f"\n\n End of try/catch block! Good job!")
