import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(mode,start_text,shift_amount):
    end_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            if mode == "encode":
                new_position = (position + shift_amount) % 26
            elif mode == "decode":
                new_position = (position - shift_amount) % 26
            new_letter = alphabet[new_position]
            end_text += new_letter
        else:
            end_text += char
    print(f"The {mode}d text is {end_text}.")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(mode=direction, start_text=text, shift_amount=shift)

    run_again = input("Run again? (Y/N) ")
    if run_again == "Y":
        continue
    else:
        break