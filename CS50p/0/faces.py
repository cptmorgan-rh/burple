def main():
    msg = input()

    print(convert(msg))

def convert(msg):

    converted_msg = msg.replace(":)", "🙂")

    return(converted_msg.replace(":(", "🙁"))

main()