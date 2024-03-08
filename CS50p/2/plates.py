def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(input_text):
    punc = [" ", ".", "!", "?", ",", ":", ";"]

    # Check that the length is between 2 and 6
    if 2 <= len(input_text) <= 6:
        # Check that the first two char are letters
        if input_text[0].isalpha() and input_text[1].isalpha():
            # Check that the first number isn't a 0
            i = 0
            while i < len(input_text):
                if input_text[i].isalpha():
                    if input_text[i] == '0':
                        return False
                    else:
                        break
                i += 1

            # Check if a digit comes before a letter
            x = 0
            while x < (len(input_text) - 1):
                if input_text[x].isdigit() and input_text[x+1].isalpha():
                    return False
                x += 1

            # Check that there are no char in the punc list
            for c in input_text:
                if c in punc:
                    return False
                    break
            return True
        else:
            return False


main()
