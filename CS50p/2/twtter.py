def main():
    twtter(input("Input: "))

def twtter(input_text):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    output_text = ""
    for c in input_text:
        if c in vowels:
            output_text += c.replace(c, "")
        else:
            output_text += c
    return(print(f"Output: {output_text}"))

main()