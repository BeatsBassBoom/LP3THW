# Imports the sys library for use later.
import sys
# takes the filename, encoding scheme (utf-8) and aggressiveness of how to handle errors from the command line.
script, encoding, error = sys.argv

# creates the main function taking 3 parameters supplied when the script is called.
def main(language_file, encoding, errors):
    # creates a variable that is assigned the lines within the file supplied in the language_file
    line = language_file.readline()

    # Checks if there is still a line of content in the file.
    if line:
        # calls the print_line function passing in the lines variable with the content of the file along with the encoding type and error aggresiveness
        print_line(line, encoding, errors)
        # returns the current language file by calling main again creating a loop with the new language lines after each is read and will cycle through until all lines are read.
        return main(language_file, encoding, errors)

# creates the print_line fucntion responsible for printed the converted strings with three parameters passed in.
def print_line(line, encoding, errors):
    # assigns the line from the language_file passed in stripping off the new lines.
    next_lang = line.strip()
    # converts to string to raw bytes stores in the variable
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # converts to bytes the raw bytes variable.
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    # prints the raw bytes and transformed strings so the difference can be seen.
    print(raw_bytes, "<===>", cooked_string)

# assigns the language file and encoding scheme for use in the main function.
languages = open("languages.txt", encoding="utf-8")

# first call to get things started to the main function.
main(languages, encoding, error)