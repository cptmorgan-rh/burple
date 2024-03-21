months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()
        if "/" in date:
            month, day, year = date.split("/")

        elif "," in date:
            month, day, year = date.split(" ")
            if month in months:
                month = months.index(month) + 1

        if (int(day.strip(',')) < 32) and (int(month) < 13):
            print(f"{year}-{int(month):02}-{int(day.strip(',')):02}")
            break

    except (ValueError, NameError):
        continue
