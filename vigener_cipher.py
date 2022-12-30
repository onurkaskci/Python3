import pprint

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'password'

def encrypt():
    
    #THE PROBLEM IS WITH THE GENERATED KEYS
    #MAKE THE KEY SKIP AND NOT GENERATE FOR THE SPACES IN THE MESSAGE
    message = 'hello\' world!' #i am onur and this is ismo
    generate_key = ''

    ###### NEW FUNCTION FOR GENERATING KEYWORDS (this section works fine)
    def generate_key(message, key):
        generated_key = ''
        while len(generated_key) <= len(message):
            for i in key:
                generated_key += i

        generated_key_same = generated_key[:len(message)]

        # Loop through the message to check for empty spaces 
        # if there is one shift the Generated Key Same

        space_and_sign_indexes = []
        for index,letter in enumerate(message):
            #print(f'Index {index} is the character: {letter}')
            if letter not in alphabet:
                space_and_sign_indexes.append(index)

        generated_key_list = [x for x in generated_key_same]

        #inserting SPACE's in the generated_key_same
        for char in space_and_sign_indexes:
            generated_key_list.insert(char, ' ')

        generated_key_final = ''.join(generated_key_list)[:len(message)]

        return generated_key_final

    generated_keys = generate_key(message,key)

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
def decrypt():
    ciphered_message = 'xm gfqf! rqs tzao wj lhmg!'

    def generate_key(message, key):
        generated_key = ''
        while len(generated_key) <= len(message):
            for i in key:
                generated_key += i

        generated_key_same = generated_key[:len(message)]

        # Loop through the message to check for empty spaces 
        # if there is one shift the Generated Key Same

        space_and_sign_indexes = []
        for index,letter in enumerate(message):
            if letter not in alphabet:
                space_and_sign_indexes.append(index)

        generated_key_list = [x for x in generated_key_same]

        #inserting SPACE's in the generated_key_same
        for char in space_and_sign_indexes:
            generated_key_list.insert(char, ' ')

        generated_key_final = ''.join(generated_key_list)[:len(message)]

        return generated_key_final
    
    generate_cipher_key = generate_key(ciphered_message, key)

    ciphered_m_alphabets = []

    #creates alphabets for ciphered message
    for x in generate_cipher_key:
        ciphered_m_alphabets.append(alphabet[alphabet.find(x):] + alphabet[:alphabet.find(x)])

    ciphered_message_list = [i for i in ciphered_message]
    decrypted_message_list = []

    for c,v in enumerate(ciphered_message_list):
        if v in alphabet:
            decrypted_message_list.append(alphabet[ciphered_m_alphabets[c].find(v)])
        else:
            decrypted_message_list.append(v)
        #print('\n')

    decrypted_message = ''.join(decrypted_message_list)
    
    return decrypted_message


print(encrypt())
print('\n')
print('#######')
print('\n')
print(decrypt())

#for count,value in enumerate():

# FINAL VARIABLES ARE: 
# generate_key for the last key generated,
# message_list for the message string turned into a list
# ciphered_alphabets for the individual alphabets for ciphering
# alphabet for the DEFAULT alphabet!