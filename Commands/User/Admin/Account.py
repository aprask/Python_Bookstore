'''

def encrypt(text, shift):
    for letters in range(len(user_text)):
        x = ord(user_text[letters])
        blank_list.append(x + user_shift)
    for letters in range(len(blank_list)):
        y = chr(blank_list[letters])
        print(y, end="")


def decrypt(text, shift):
    for letters in range(len(user_text)):
        x = ord(user_text[letters])
        blank_list.append(x - user_shift)
    for letters in range(len(blank_list)):
        y = chr(blank_list[letters])
        print(y, end="")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
blank_list = []


while True:
    user_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if user_direction == "decode":
        user_text = input("Type your message:\n").lower()
        user_shift = int(input("Type the shift number:\n"))
        decrypt(user_text, user_shift)
        break
    elif user_direction == "encode":
        user_text = input("Type your message:\n").lower()
        user_shift = int(input("Type the shift number:\n"))
        encrypt(user_text, user_shift)
        break
    else:
        print("Sorry that is not an option")
        continue

'''