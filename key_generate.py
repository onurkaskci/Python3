message = 'ben!im adim onur! on\'un adi ismail'
key = 'password'
alphabet = 'abcdefghijklmnopqrstuvwxyz'


def generate_key(message, key):
    generated_key = ''
    while len(generated_key) <= len(message):
        for i in key:
            generated_key += i

    generated_key_same = generated_key[:len(message)]

    # Loop through the message to check for empty spaces 
    # if there is one shift the Generated Key Same

    space_indexes = []
    for index,letter in enumerate(message):
        #print(f'Index {index} is the character: {letter}')
        if letter not in alphabet:
            space_indexes.append(index)

    generated_key_list = [x for x in generated_key_same]

    #inserting SPACE's in the generated_key_same
    for space in space_indexes:
        generated_key_list.insert(space, ' ')

    generated_key_final = ''.join(generated_key_list)[:len(message)]
   #print(f'Generated Key List with Spaces shifted: {generated_key_list}')
    print(f'Message: {message}. Length: {len(message)}')
    print('\n')
    print(f'Generated Key List with Spaces shifted: {generated_key_final}. Length: {len(generated_key_final)}')

    return generated_key_final

generate_key(message,key)