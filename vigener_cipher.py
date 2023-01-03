from pprint import pprint

# YOUTUBE 1: So first we need a function that generates the key at the length of the inputted message. Example with the key 'like' -> subscribe to my channel: likelikel ik el ikelike
def generate_key(message, key, alphabet='abcdefghijklmnopqrstuvwxyz'):
    generated_key = ''
    while len(generated_key) <= len(message):
        for i in key:
            generated_key += i

    generated_key_same = generated_key[:len(message)]

    # YOUTUBE 2-1: One problem i encountered was encrypting messages with space included. So this for loop stores the index of spaces in a list,
    space_and_sign_indexes = []
    for index,letter in enumerate(message):
        #print(f'Index {index} is the character: {letter}')
        if letter not in alphabet:
            space_and_sign_indexes.append(index)

    # YOUTUBE 2-2: Then i turn the initial message in to a list. I do this to insert spaces easily,
    generated_key_list = [x for x in generated_key_same]

    # YOUTUBE 2-3: And finally in this for loop we are inserting SPACE's in that list,
    for char in space_and_sign_indexes:
        generated_key_list.insert(char, ' ')

    generated_key_final = ''.join(generated_key_list)[:len(message)]
    # YOUTUBE 3: So here we have the key for the inputted message. This key will be used for both encrypting and decrypting.
    return generated_key_final

def encrypt(message_to_encrypt, key='password', alphabet='abcdefghijklmnopqrstuvwxyz'):
    
    #THE PROBLEM IS WITH THE GENERATED KEYS
    #MAKE THE KEY SKIP AND NOT GENERATE FOR THE SPACES IN THE MESSAGE
    message = message_to_encrypt #i am onur and this is ismo

    ###### NEW FUNCTION FOR GENERATING KEYWORDS (this section works fine)

    generated_keys = generate_key(message,key, alphabet)
    print(f'Generate Key function call in encrypt: {generated_keys}')

    ciphered_alphabets = []

    #Creates the ciphered alphabet for each character in the generated keyword
    for letter in generated_keys:
        if letter in alphabet:
            ciphered_alphabets.append(alphabet[alphabet.find(letter):] + alphabet[:alphabet.find(letter)])
        else:
            ciphered_alphabets.append(' ')

    message_list = [x for x in message]
    
    #every character of the message is matched with the corresponding ciphered_alphabets
    message_alphabet_combined_list = []
    for c,v in enumerate(message_list):
        message_alphabet_combined_list.append([v, ciphered_alphabets[c]])

    encrypted_elements = []

    #encrypting part NEW
    for element in message_alphabet_combined_list:
        if element[0] in alphabet:
            encrypted_elements.append(element[1][alphabet.find(element[0])])
        else:
            encrypted_elements.append(element[0])

    final_ciphered_message = ''.join(encrypted_elements)
    return final_ciphered_message

#decrypting part. 
# TAKE THE CRYPTED MESSAGE AND THE CIPHERED ALPHABET 
# AND LOOK FOR THE INDEX OF EACH ELEMENT IN THE CIPHERED MESSAGE
def decrypt(message_to_decrypt, key='password', alphabet='abcdefghijklmnopqrstuvwxyz'):

    generate_cipher_key = generate_key(message_to_decrypt, key, alphabet)
    print(f'generate key function in DECRYPT: {generate_cipher_key}')

    ciphered_m_alphabets = []

    #creates alphabets for ciphered message
    for x in generate_cipher_key:
        ciphered_m_alphabets.append(alphabet[alphabet.find(x):] + alphabet[:alphabet.find(x)])

    ciphered_message_list = [i for i in message_to_decrypt]
    decrypted_message_list = []

    for c,v in enumerate(ciphered_message_list):
        if v in alphabet:
            decrypted_message_list.append(alphabet[ciphered_m_alphabets[c].find(v)])
        else:
            decrypted_message_list.append(v)

    decrypted_message = ''.join(decrypted_message_list)
    
    return decrypted_message

print(encrypt('subscribe to my channel', 'like'))
print(decrypt('dclwnzsfp by qj kreyvop', 'like'))
