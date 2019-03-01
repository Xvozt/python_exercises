"""RGB values are usually given in the 0–255 range;
if they are in the 0–1 range,
the values are multiplied by 255 before conversion.
This number divided by sixteen (integer division;
ignoring any remainder) gives us the first hexadecimal digit (between 0 and F,
where the letters A to F represent the numbers 10 to 15.
See hexadecimal for more details).
The remainder gives us the second hexadecimal digit.
For instance the RGB value 201 divides into 12 groups of 16,
thus the first digit is C.
A remainder of nine gives us the hexadecimal number C9.
This process is repeated for each of the three color values.
Conversion between number bases is a common feature of calculators,
including both hand-held models and the software calculators
bundled with most modern operating systems.
Web-based tools specifically for converting color values are also available.
"""

MAP_LIST = ['A', 'B', 'C', 'D', 'E', 'F']


def hexcolor(r, g, b) -> int:
    color_code = ''.join(['#', hexadecimal(r), hexadecimal(g), hexadecimal(b)])
    print(color_code)


def hexadecimal(channel) -> int:
    if 0 <= channel <= 1:
        channel = channel*255
    first, second = divmod(channel, 16)
    a = str(first) if first < 10 else MAP_LIST[first % 10]
    b = str(second) if second < 10 else MAP_LIST[second % 10]
    return a + b


hexcolor(255, 99, 71)
hexcolor(184, 134, 11)
hexcolor(189, 183, 107)
hexcolor(0, 0, 205)
