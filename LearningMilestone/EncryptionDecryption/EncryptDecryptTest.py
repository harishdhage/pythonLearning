
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



def encrypt(original_msg, shift_amount):
    encrypt_str = ""
    for letter in original_msg:
        shift_pos = alphabets.index(letter) + shift_amount
        shift_pos %= len(alphabets)
        encrypt_str += alphabets[shift_pos]
    print(f"Encrypted message : {encrypt_str}")

def decrypt(encoded_msg, shift_amount):
    decrypt_str = ""
    for letter in encrypt_msg:
        shift_pos = alphabets.index(letter) - shift_amount
        shift_pos %= len(alphabets)
        decrypt_str += alphabets[shift_pos]
    print(f"Decrypted message : {decrypt_str}")

def encode_decode(original_msg, shift_code, encode_or_decode):
    output_str = ""
    if encode_or_decode == "d":
        shift_code = -shift_code
    for letter in original_msg:
        if letter not in alphabets:
            output_str += letter
        else:
            shift_pos = alphabets.index(letter) + shift_code
            shift_pos %= len(alphabets)
            output_str += alphabets[shift_pos]
    print(f"{encode_or_decode} message : {output_str}")

#encrypt(original_msg=message, shift_amount=shift_code)
#decrypt(encoded_msg=encrypt_str, shift_amount=shift_code)

repeat = True
while repeat==True:
    direction = input("Type 'e' - for encrypt and 'd' - for decrypt : ").lower()
    message = input("Enter the message to encrypt : ").upper()
    shift_code = int(input("Enter the shift code to encrypt the message : "))
    encode_decode(original_msg=message, shift_code=shift_code, encode_or_decode=direction)

    restart = input("Enter 'Yes' if you want to restart, else type 'No' : ").lower()
    if restart == 'no':
        repeat == False
        print("Good Bye!!! ")