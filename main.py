# salvador aleguas

def encode_str(s):
    # taking an 8 digit password
    # take each digit and move it 3 places ahead
    # "12345555" -> "45678888"
    
    encoded_str = ""
    for c in s:
        encoded_str += str((int(c) + 3) % 10)
        
    return encoded_str

def decode(x):
    decoder = ""
    for y in x:
        decoded_password = int(y) - 3
        if decoded_password < 0:
            decoded_password = decoded_password + 10
        decoder = decoder + str(decoded_password)
    return decoder

# make a menu to prompt the user for input
# 1. encode a string
# 2. decode a string
# 3. exit

if __name__ == "__main__":
    stored_password = ""
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")
        
        if choice == "1":
            s = input("Please enter your password to encode: ")
            stored_password = encode_str(s)
            print("Your password has been encoded and stored!")
        elif choice == "2":
            if stored_password:
                print(f"The encoded password is {stored_password}, and the original password is {decode(stored_password)}.")
            else:
                print("No encoded password found.")
        elif choice == "3":
            break
        else:
            print("Invalid choice")