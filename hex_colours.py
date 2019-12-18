HEX_COLOUR_CODES = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "AQUAMARINE1": "#7fffd4",
                    "AQUAMARINE2": "#76eec6", "AZURE1": "#f0ffff", "AZURE2": "#e0eeee",
                    "BEIGE": "#f5f5dc", "BISQUE1": "#ffe4c4", "BLUE1": "#0000ff", "BURLYWOOD": "#deb887"}

colours = input("Enter a colour:").upper()
while colours != "":
   if colours in HEX_COLOUR_CODES:
       print(colours, "is", HEX_COLOUR_CODES[colours])
   else:
       print("The code for colours is none")
   colours = input("Enter a colour:").upper()