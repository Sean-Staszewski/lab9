def encoder(string):
    encoded = ""
    for digit in string:
        digit = int(digit)
        digit += 3
        if digit >= 10:
            digit -= 10

        encoded = encoded + str(digit)
    return encoded
