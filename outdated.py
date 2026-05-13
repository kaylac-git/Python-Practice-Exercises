def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date = input("Date: ").strip()

            # Format MM/DD/YYYY
            if "/" in date:
                month, day, year = date.split("/")

                month = int(month)
                day = int(day)
                year = int(year)

            # Format Month Day, Year
            else:
                parts = date.split()

                if len(parts) != 3:
                    continue

                month_str = parts[0]
                day = parts[1].replace(",", "")
                year = parts[2]

                if month_str not in months:
                    continue

                month = months.index(month_str) + 1
                day = int(day)
                year = int(year)

            # Validation
            if month < 1 or month > 12:
                continue
            if day < 1 or day > 31:
                continue

            print(f"{year:04}-{month:02}-{day:02}")
            break   # ✅ stop after valid input

        except ValueError:
            continue


main()