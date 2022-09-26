#Caesar Cypher

from operator import truediv


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

run = True

while run:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    def encrypt(text, shift):
        text1 = []
        for n in range(0, len(text)):
            text1.append(text[n])
        for n in range(0, len(text1)):
            for j in range(0, len(alphabet)):
                if(text1[n] == alphabet[j]):
                    text1[n] = alphabet[j+shift]
                    break
        print(f"The encoded text is {''.join(text1)}")


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

    def decrypt(text, shift):
        text1 = []
        for n in range(0, len(text)):
            text1.append(text[n])
        for n in range(0, len(text1)):
            for j in range(0, len(alphabet)):
                if(text1[n] == alphabet[j]):
                    text1[n] = alphabet[j-shift]
                    break
        print(f"The decoded text is {''.join(text1)}")

    #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

    if(direction == "encode"):
        encrypt(text, shift)
    elif(direction == "decode"):
        decrypt(text, shift)
    else:
        print("Type encode to encrypt, and decode to encrypt.")

    go_again_question = input("Would you like to go again? Enter Y for yes and N for no. ").lower()
    if (go_again_question == "y"):
        run = True
    else:
        run = False
