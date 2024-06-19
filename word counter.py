def word_count(filename):
    try:
        with open("sushma.txt", "r" )as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return -1  # Return -1 to indicate an error

def main():
    print("Welcome to the Word Counter program!")
    filename = input("Enter the filename to count words from: ")

    # Call word_count function to get the number of words
    count = word_count(filename)

    if count != -1:
        print(f"Number of words in the file '{filename}': {count}")

if __name__ == "__main__":
    main()
