from pyfiglet import Figlet
import random
import sys

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        font = random.choice(fonts)

    elif len(sys.argv) == 3:
        if sys.argv[1] in ["-f", "--font"]:
            font = sys.argv[2]
            if font not in fonts:
                sys.exit("Invalid font")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    
    text = input("Input: ")
    figlet.setFont(font=font)
    print("Output:")
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()