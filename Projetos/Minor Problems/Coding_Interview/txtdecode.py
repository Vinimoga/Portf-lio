'''
though that same idea of a staircase in python, you should get only the
numbers on the rightmost edge of the staircase and decode the message
named "file.txt", where the number represents exactly the word you
should read.

'''
def decode(message_file):
    # Read the contents of the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Create a dictionary to store the words and their corresponding numbers
    words_dict = {}

    # Process each line in the file
    for line in lines:
        # Split the line into number and word
        num, word = line.split()

        # Add the word to the dictionary with its corresponding number
        words_dict[int(num)] = word

    # Create a list to store the selected words based on the pyramid structure
    selected_words = []

    # Loop through the pyramid structure to get the selected words
    current_num = 1
    step = 1

    while current_num <= len(lines):
        step += 1
        selected_words.append(words_dict[current_num])
        current_num += step

    # Join the selected words into a string and return
    decoded_message = ' '.join(selected_words)
    return decoded_message


# Example usage:
message_file = "Projetos\Minor Problems\Coding_Interview\Code.txt"

decoded_message = decode(message_file)
print(decoded_message)
