import sys

def huffman_encoding(data):
    table = dict()
    for char in data:
        table[char] = table.get(char, 0) + 1
    tree = dict()
    temp = '1'
    for i in sorted(table.items(), key = lambda x: x[1]):
        tree[i[0]] = temp
        temp = '0' + temp

    encoded = ''
    for i in data:
        encoded += tree[i]
    return encoded, tree

def huffman_decoding(data,tree):
    huff = dict()
    for char in tree:
        huff[tree[char]] = char
    store = ''
    decoded = ''
    for d in data:
        if d == '1':
            decoded += huff[store + d]
            store = ''
        else:
            store += d
    return decoded

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    '''
    Output:
    The size of the data is: 69

    The content of the data is: The bird is the word

    The size of the encoded data is: 48

    The content of the encoded data is: 100000010000000100000000000101000000001000000000100000000001000000000001000000001001000000000001000100000010000000100000000000100001000001000000000100000000001

    The size of the decoded data is: 69

    The content of the encoded data is: The bird is the word

    '''
# Case: If repetitive strings

    codes = {}

    a_great_sentence = "aaaaaa"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    '''
    The size of the data is: 55

    The content of the data is: aaaaaa

    The size of the encoded data is: 28

    The content of the encoded data is: 111111

    The size of the decoded data is: 55

    The content of the encoded data is: aaaaaa
    '''

    # edge case - If string is empty then shows error
    codes = {}

    a_great_sentence = ""

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
    '''
    The size of the data is: 51

    The content of the data is: 
    invalid literal for int() with base 2: ''
    '''
    # edge case - If string has just one space but still empty
    codes = {}

    a_great_sentence = " "

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
'''
The size of the data is: 50

The content of the data is:  

The size of the encoded data is: 28

The content of the encoded data is: 1

The size of the decoded data is: 50

The content of the encoded data is:  

'''
