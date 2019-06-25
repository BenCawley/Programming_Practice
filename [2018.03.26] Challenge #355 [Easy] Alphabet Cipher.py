def setup(mask = 'abcdefghijklmnopqrstuvwxyz'):
    y_axis = {} #Collumns
    mask_dict = {} #Mask dictionary for later use in encryption
    position = 0
    for c in mask:
        if c.upper() == mask[0].upper(): #Sets the initial row and collumn
            y_axis[c.upper()] = mask
            last_entry = mask
        else: #Takes the last row / collumn, removes the first entry / letter then adds it to the end and iterates through every possible combination in the mask
            y_axis[c.upper()] = last_entry[1:len(mask)] + last_entry[0]
            last_entry = last_entry[1:len(mask)] + last_entry[0]
        mask_dict[c] = position
        position += 1
    return y_axis, mask_dict

def encrypt(sentence, keyword):
    collumn = setup()[0]
    mask_dict = setup()[1]
    encryption = ''
    sentence, keyword = sentence.lower(), keyword.lower()
    crypt_collumn, crypt_dict = '', {}
    
    if len(sentence) < len(keyword): #Makes the sentence and keyword the same length
        keyword = keyword[:len(sentence)]
    elif len(sentence) % len(keyword) != 0:
        remainder = len(sentence) % len(keyword)
        whole = int(len(sentence) / len(keyword))
        keyword = (keyword * whole) + keyword[:remainder]
    
    for p, k in enumerate(keyword): #Iterates through the collumns to find the one associated with the keyword letter
        for key in collumn.keys():
            if k.upper() == key:
                position = 0
                crypt_collumn = collumn[k.upper()] #Defines the collumn to use for encryption
                for c in crypt_collumn: #Converts the selected collum into a dictionary its, with keys starting at 0
                    crypt_dict[position] = c
                    position += 1
                for n, s in enumerate(sentence): #Iterates through the mask letter (the row) to find the one associated with the sentence letter
                    if n == p: #Checks to see if the sentence and keyword are on the same letter
                        for key in mask_dict.keys():
                            if s == key:
                                encryption += crypt_dict[mask_dict[key]] #Selects the letter in the collumn that corresponds to the selected row
    return (encryption)

print (encrypt('thepackagehasbeendelivered', 'snitch'))
                        
