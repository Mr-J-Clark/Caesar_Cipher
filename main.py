# Create a list of lowercase letters 
letters = 'abcdefghijklmnopqrstuvwxyz'

# Get user input for the message and shift number
message = input("Enter your message: ")
shift = int(input("Enter the shift number: "))

encrypted_message = ''

for char in message:
    # Check if the character is a letter
    if char.lower() in letters:
        # Find the index of the character in the  letters list
        original_index = letters.index(char.lower())
        # Calculate the new index with the shift, wrapping around using modulo 26
        new_index = (original_index + shift) % 26
        # Get the new shifted character
        shifted_char = letters[new_index]
        # Preserve the original case
        if char.isupper():
            shifted_char = shifted_char.upper()
        encrypted_message += shifted_char
    else:
        # If it's not a letter, keep it as it is
        encrypted_message += char

print("Your encrypted message is:", encrypted_message)


