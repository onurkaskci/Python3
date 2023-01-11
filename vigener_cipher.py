from pprint import pprint

# YOUTUBE 1: So first we need a function that generates the password using the key. 
# And the password should have the same length as our message
# Example with the key 'like' -> subscribe to my channel: likelikel ik el ikelike
def generate_key(message, key, alphabet='abcdefghijklmnopqrstuvwxyz'):
    generated_key = ''
    while len(generated_key) <= len(message):
        for i in key:
            generated_key += i

    generated_key_same = generated_key[:len(message)]

    # YOUTUBE 2-1: One problem i encountered was encrypting messages with space and other specail characters included. 
    # So this for loop stores the index of those characters in a list, (make a compared image of password and message with spaces included)
    space_and_sign_indexes = []
    for index,letter in enumerate(message):
        #print(f'Index {index} is the character: {letter}')
        if letter not in alphabet:
            space_and_sign_indexes.append(index)

    # YOUTUBE 2-2: Then i turn the initial message in to a list. I do this to insert special characters easily,
    generated_key_list = [x for x in generated_key_same]

    # YOUTUBE 2-3: And finally in this for loop we are inserting Special characters in that list,
    for char in space_and_sign_indexes:
        generated_key_list.insert(char, ' ')

    generated_key_final = ''.join(generated_key_list)[:len(message)]
    # YOUTUBE 3: So here we have the key for the inputted message. This key will be used for both encrypting and decrypting. (make an image for comparing the inputted text and the output key)
    return generated_key_final

# YOUTUBE 3.2: Lets try this function with an input.

# YOUTUBE 4: Next lets create function for encrypting.
def encrypt(message_to_encrypt, key='password', alphabet='abcdefghijklmnopqrstuvwxyz'):
    
    # YOUTUBE 5: Here we call the generate_key function to create the password for the input. 
    # In this case the input is the message that the user wants to encrypt.
    generated_keys = generate_key(message_to_encrypt,key, alphabet)
    #print(f'Generate Key function call in encrypt: {generated_keys}')

    ciphered_alphabets = []

    # YOUTUBE 6-1: And in this for loop we create the Ciphered alphabets for every individual letter in the 'generated_key'. (Make an image animation for this part as well) --Creates the ciphered alphabet for each character in the generated keyword--
    for letter in generated_keys:
        if letter in alphabet:
            ciphered_alphabets.append(alphabet[alphabet.find(letter):] + alphabet[:alphabet.find(letter)])
        else:
            ciphered_alphabets.append(' ')


    message_list = [x for x in message_to_encrypt]
    
    # YOUTUBE 6-2: And here, every character of the message is matched with the corresponding ciphered_alphabets
    message_alphabet_combined_list = []
    for c,v in enumerate(message_list):
        message_alphabet_combined_list.append([v, ciphered_alphabets[c]])

    encrypted_elements = []

    #encrypting part NEW
    # YOUTUBE 7: Finally we match the letters in the input with the corresponding letters in the 'Ciphered Alphabet' for encrypting. 
    # But if the current element is not a letter, we keep the original. 
    # So things like space, comma or question mark will remain as it is.
    for element in message_alphabet_combined_list:
        if element[0] in alphabet:
            encrypted_elements.append(element[1][alphabet.find(element[0])])
        else:
            encrypted_elements.append(element[0])

    # YOUTUBE 8: Until this point our letters are stored in a list.
    final_ciphered_message = ''.join(encrypted_elements)
    return final_ciphered_message

#decrypting part. 
# TAKE THE CRYPTED MESSAGE AND THE CIPHERED ALPHABET 
# AND LOOK FOR THE INDEX OF EACH ELEMENT IN THE CIPHERED MESSAGE
# YOUTUBE 7: And for decrypting we will use the indexes of the letters in the encrypted message. 
# Lets create a function that will take arguments for the message to decrypt, key and an alphabet. The last two will have default values.
def decrypt(message_to_decrypt, key='password', alphabet='abcdefghijklmnopqrstuvwxyz'):

    # YOUTUBE 8: As usual we are creating the password using the key
    generate_cipher_key = generate_key(message_to_decrypt, key, alphabet)
    print(f'generate key function in DECRYPT: {generate_cipher_key}')

    ciphered_m_alphabets = []

    #creates alphabets for ciphered message
    # YOUTUBE 9: Next we will create the ciphered alphabets for each letter in the encrypted message using a for loop
    for x in generate_cipher_key:
        ciphered_m_alphabets.append(alphabet[alphabet.find(x):] + alphabet[:alphabet.find(x)])

    ciphered_message_list = [i for i in message_to_decrypt]
    decrypted_message_list = []

    # YOUTUBE 10: And this for decrypting the message, we are searching the original English Alphabet with the index of the letter for decrypting
    for c,v in enumerate(ciphered_message_list):
        if v in alphabet:
            decrypted_message_list.append(alphabet[ciphered_m_alphabets[c].find(v)])
        else:
            decrypted_message_list.append(v)

    decrypted_message = ''.join(decrypted_message_list)
    # YOUTUBE 11: Finally we return the value
    return decrypted_message

# CODING SECTION ENDS HERE. SWITCH TO THE OUTRO 
# YOUTUBE 12: Lets see what that message from the super duper cinematic intro meant.
print(encrypt('subscribe to my channel', 'like'))
print(decrypt('dclwnzsfp by qj kreyvop', 'like'))

# YOUTUBE 13: (Me typing the encrypted message then reading this and after I realize what it is a blue screen error pops up and video ends)
#print(encrypt('this message will destroy itself in five seconds', 'like'))
print(decrypt('epsw xmcwloo attv hpadvzg sxdmvj tv pmgm cinwxhd', 'like'))
# fjjjhdyy skjdıefj
# mnvcncmmdmmmdfjjfıuıejmcjkejfjekmcırekfkoeköd