def main():
    groceryitems = {}

    while True:
        try:
            item = input().lower()

            if item in groceryitems:
                groceryitems[item] += 1
            else:
                groceryitems[item] = 1

        except EOFError:
            break

    for item in sorted(groceryitems):
        print(groceryitems[item], item.upper())


main()