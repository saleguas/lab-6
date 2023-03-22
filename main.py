def encode_str(s):
    # taking an 8 digit password
    # take each digit and move it 3 places ahead
    # "12345555" -> "45678888"
    
    encoded_str = ""
    for c in s:
        encoded_str += str((int(c) + 3) % 10)
        
    return encoded_str

# make a menu to prompt the user for input
# 1. encode a string
# 2. decode a string
# 3. exit

if __name__ == "__main__":
    while True:
        print("1. encode a string")
        print("2. decode a string")
        print("3. exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            s = input("Enter a string to encode: ")
            print("Encoded string: ", encode_str(s))
        elif choice == "2":
            pass
        elif choice == "3":
            break
        else:
            print("Invalid choice")