def caesar_cipher(text, direction, shift = 3):
    result = "" #empty string for the final result
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a') # 65 or 97
            if direction == "encrypt":
                encrypted = chr((ord(char) - base + shift) % 26 + base)
                result += encrypted
            else:
                decrypted = chr((ord(char) - base - shift) % 26 + base) 
                result += decrypted
        else:
            result += char
    return result


#User's input text
text = input("Enter the text you want to encrypt/decrypt: ")

#Encrypting or decrypting text
direction = input("Type 'encrypt' or 'decrypt': ").lower()
while True:
    if direction not in ("encrypt", "decrypt"):
        direction = input("❌ Invalid input. Please type 'encrypt' or 'decrypt': ").lower()
    else:
        print()
        break

#Check if the user wants to change the shift amount
shift = input("Do you want to change the shift amount (default: 3) ? (yes/no): ").lower()
while True:
    if shift not in ("yes", "no"):
        shift = input("❌ Invalid input! Try again: ").lower()
    else:
        break

if shift.lower() == "yes":
    shift = int(input("Enter the shifting distance: "))
    while True:
        if shift < 0 or shift > 26:
            shift = int(input("❌ Invalid input! You might get unexpected results! Try again: "))
        else:
            print()
            break
    #Result
    print(f"✅ Your {direction}ed text is: <{caesar_cipher(text, direction, shift)}>")
else:
    #Result
    print(f"✅ Your {direction}ed text is: <{caesar_cipher(text, direction)}>")
