def main():
    time = input("What time is it? ").strip()

    converted_time = convert(time)

    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")


def convert(time):

    if " " in time:
        time, convention = time.split(" ")
        if 'p' in convention:
            hours, minutes = time.split(":")
            if hours == "12":
                converted_time = (float(hours)) + (float(minutes) / 60)
            else:
                converted_time = (float(hours) + 12) + (float(minutes) / 60)
            return (converted_time)

    hours, minutes = time.split(":")
    converted_time = float(hours) + (float(minutes) / 60)

    return (converted_time)


if __name__ == "__main__":
    main()
