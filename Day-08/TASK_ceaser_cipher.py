from ceaser_cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
        
    print(f"\nHere's the {direction}d result : {end_text}")


print(logo)
should_continue = True

while should_continue:
    direction = input("\nType 'encode' to encrypt and 'decode' to decrypt : ")
    text = input("Type your message : ").lower()
    # if the shift is greater than the length of alphabet list then we will simply modulo it so we get reminder of it to use for shifting
    shift = int(input("Type the shift number : ")) % 26
    ceaser(start_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' to go perform one of the operation once again, or press 'no' to exit : ")
    if result == "no":
        should_continue = False
        print("\nGoodby")