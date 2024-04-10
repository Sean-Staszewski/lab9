from encoder import encoder

from encoder import decoder

def main():
    while True:
        print("""
        
 Menu
-------------
1. Encode
2. Decode
3. Quit""")
        option = input("Please enter an option: ")

        if option == "1":
            password = encoder(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        elif option == "2":
            print(f"The encoded password is {password}, and theoriginal password is {decoder(password)}.")
        elif option == "3":
            break
        else:
            print("Invalid Selection")
if __name__ == 'main':
    main()