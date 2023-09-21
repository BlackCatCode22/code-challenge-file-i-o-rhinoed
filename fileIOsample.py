# Code Challenge - Strings and Lists
# fileIOsample.py 9/20/23
#
# Python file name: _______________
#
# Date: _______________
#
# Programmer's name: ___________

# ********************************************************************************************
# Part 1: File I/O
#
# Demonstrate file i/o by reading and writing a text file.
#
# Instructions: Using the open() function, open a text file named ArrivingAnimals that exists on your local machine.
#   Process each line of text from arrivingAnimals.txt by breaking the line into substrings on the commas. Each line
#   in arrivingAnimals represents an individual animal. Output the substrings
#     Create comments for all code operations.
#
# Part 2: User-defined Functions
#
# Create a function that returns a string and has one String parameter. The string returned will be the animal species.
#
# Instructions: Create a function named get_species that inputs a string like this: "12 year old male hyena" or
#       this: "2 year old male tiger" and returns (outputs) a string that is the species(hyena or lion). Call the
#       function when you are processing your input file and output the species before outputing the group of
#       substrings that represent an individual animal.


# Define the input and output file paths
input_file_path = "C:\\2023fall\\python\\dataFiles\\arrivingAnimals.txt"
# Use r (raw) before the path string to tell Python to not use the backslash as an escape character
output_file_path = r"C:\2023fall\python\dataFiles\outputFile.txt"

# Using try-except blocks with text files in Python.....
#       is not always necessary, but it's good programming practice. Various reasons to use try-except blocks include:
#
# 1. **File Existence**: When you open a file for reading or writing, the file may not exist at the specified path.
#       Use a try-except block with "FileNotFoundError" handling to catch the error and handle this situation.
# 2. **File Access Permissions**: In some cases, your program may not have the necessary permissions to read or
#       write to a file. Use a try-except block to handle "PermissionError" or related exceptions gracefully.
# 3. **File I/O Errors**: While reading or writing to a file, various errors can occur, such as disk full, file is
#       locked by another process, or file is corrupted. Using try-except blocks with a broader exception handling
#       strategy can help you capture and handle these errors.
# 4. **Input Validation**: When processing files, it's often a good practice to validate the content of the file to
#       ensure it meets your expectations. If the file doesn't adhere to the expected format, you can raise custom
#       exceptions and handle them within the try-except block.
# 5. **Resource Cleanup**: Using try-except-finally blocks allows you to ensure that file resources are properly closed,
#       even if an exception is raised during file operations. This prevents memory leaks!
#
# In summary: While it's not always necessary to use try-except blocks when dealing with files, it's a defensive
#       programming practice that helps improve the robustness and reliability of your code, especially when dealing
#       with potentially unpredictable external resources like files.

def get_species(my_str):
    # Split my_str using the character space
    words = my_str.split()
    # TODO: find the data type of words. What can you do with words?
    return words[4]

# Open the input file for reading
try:
    with open(input_file_path, 'r') as input_file:
        # Read lines from the input file
        lines = input_file.readlines()
        # 'lines' now contains a list of all lines in the input file
        # TODO: Output the type of 'lines'
        # TODO: Fill in the blank: The readlines() method returns a _____ containing all the text lines of input_file.
        # TODO: Output the 2nd and 4th list elements
        #   print("The second list element is: " + _______________ )
        #   print("The fourth list element is: " + _______________ )
        print(f"The second list element is: { lines[1]}")
        print("\n\n")
        print(lines)
        print("\n\n")

        # Open the output file for writing
        with open(output_file_path, "w") as output_file:
            for line in lines:
                # Split each line on the comma
                substrings = line.strip().split(',')

                # TODO: Spend an hour exploring 'substring'
                #   Examine it, ask yourself "what is this" each time you perform a method on it
                #   Spend some time thinking about the many operation you can use on 'substrings' and how this
                #   can help you present your processed data in various ways.
                # TODO: Output the data type of 'substrings'
                # print(f"\n The data type of substrings is ...")

                # TODO: Output "substrings" and think about what you see
                #
                # TODO: Output the first and second elements of substrings
                #
                # TODO: Call get_species and output the species. What will you use for input?

                # hint: print(f"the species is: {....}")
                # TODO: Use a "for each" loop to output the substrings on different lines.
                #
                #
                # TODO: Code up this line to do the same thing. Observe and think about it. This is Python shorthand!
                #   print("\n".join(substrings))
                #
                # TODO: Use "***************" in place of "\n" and examine your output. Read your code from right to
                #   left and think about what is happenening. Communicate with someone on our Discord server and ask
                #   a question about this.
                #
                #
                #
                #
                #
                # Write each substring to the output file separated by newlines
                output_file.write("\n".join(substrings))
                #
                # Add two empty lines between groups of substrings
                output_file.write("\n\n")

    print("\n\nData processed and written to 'outputFile.txt'!")


# TODO: Look at these errors and think how you could modify your input file to cause an error
# TODO: Modify your input file to throw an error!
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
