import inflect

def main():
    p = inflect.engine()
    names = []

    while True:
        name = input("Name: ")
        print(f"DEBUG: '{name}'")
        if name.strip() == "":
            break
        names.append(name)

    print("Adieu, adieu, to " + p.join(names))


if __name__ == "__main__":
    main()