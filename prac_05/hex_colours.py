COLOUR_TO_HEX = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
               "alizarin crimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc",
               "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc",
               "antiquewhite3": "#cdc0b0", "antiquewhite4": "#8b8378", "apricot": "#fbceb1", "aqua": "#00ffff"}


while True:
    colour_input = input("Enter Colour Name: ").lower()
    if (colour_input == ""):
        print("End.")
        break
    try:
        print(f"{colour_input}:{COLOUR_TO_HEX[colour_input]}")
    except:
        print("Invalid Colour.")
