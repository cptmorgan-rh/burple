def main():
    time = input("What time is it? ")

    converted_time = convert(time)

    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")


def convert(time):

    if time.endswith("a.m."):
        am_time = time.removesuffix(" a.m.")
        hours, minutes = am_time.split(":")
        converted_time = float(hours) + (float(minutes) / 60)
        return (converted_time)
    elif time.endswith("p.m."):
        pm_time = time.removesuffix(" p.m.")
        hours, minutes = pm_time.split(":")
        if hours != "12":
            converted_time = (float(hours) + 12) + (float(minutes) / 60)
        elif hours == "12":
            converted_time = (float(hours)) + (float(minutes) / 60)
        return (converted_time)
    else:
        hours, minutes = time.split(":")
        converted_time = float(hours) + (float(minutes) / 60)
        return (converted_time)


if __name__ == "__main__":
    main()
