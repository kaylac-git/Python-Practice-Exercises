def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # must have min 2 carcters and max 6 carcaters
    if len(plate) < 2 or len(plate) > 6:
        return False
    # must start with 2 letters
    if not plate[0].isalpha() or not plate[1].isalpha():
        return False
    
    number_started = False
    
    for char in plate:
        if char.isdigit():
            if not number_started:
                number_started = True
                # first number cannot be 0
                if char == "0":
                    return False
            
        else:
            # numbers must be at the end
            if number_started:
                return False
    
        # no space or exclamation marks
        if not char.isalnum:
            return False
        
    return True
    

main()