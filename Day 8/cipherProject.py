alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caeser(orignal_text,shift_amount,encode_decode):
    output_text=""
    for letter in orignal_text:
        if letter not in alphabet:
            output_text+=letter
        else:
            if encode_decode=='encode':
                shifted_position=alphabet.index(letter)+shift_amount
            elif encode_decode=='decode':
                shifted_position=alphabet.index(letter)-shift_amount

            shifted_position=shifted_position%len(alphabet)
            output_text+=alphabet[shifted_position]
        
    print(f"Here is the {encode_decode}d result: {output_text}")


should_continue=True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))

    caeser(orignal_text=text,shift_amount=shift,encode_decode=direction)
    restart=input("Type 'yes' if you want to go again. Otherwise, type 'no'/n.").lower()
    if restart=='no':
        should_continue=False
        print("Goodbye")