from common import *

assert hamming("this is a test", "wokka wokka!!!") == 37, "hamming_distance incorrect"




lines = open('1.6.txt').read().split("\n")
bin_str = a2b_base64("".join(lines))

min_key_size = 2
max_key_size = 40

best_key_size = get_best_key_size(bin_str, min_key_size, max_key_size)
matrix = split_str_chunks_len(bin_str, best_key_size)

t_matrix = zip(*matrix[:-1])

result_key = ""
for t_row in t_matrix:
    row_str = "".join(t_row)
    result_key += decrypt_with_single_char(row_str)[2]

print result_key

print repxor(bin_str, result_key, True)



# print trow


# def keyWithLowestVal(d):
#      return min(d, key=d.get)


# def findRepeatingXORKeysize(s):

#     norm_edit_distances = {}
#     for KEYSIZE in range(2,40):
#         keysize_message = splitString(s, (KEYSIZE*8))
#         total_blocks = len(keysize_message)
#         distance = 0

#         for i,k in zip(keysize_message[0::2], keysize_message[1::2]):
#             distance +=hamming_distance(i,k)

#         norm_edit_distances[KEYSIZE] = (float(distance)/float(total_blocks)) / float(KEYSIZE)

#     return keyWithLowestVal(norm_edit_distances)

# def findRepeatingXORKey(binary_cipher):

#     # calculate possible keysize
#     KEYSIZE = findRepeatingXORKeysize(binary_cipher)
    

#     # break the ciphertext into blocks of KEYSIZE length.
#     keysize_blocks = splitString(binary_cipher, 8*KEYSIZE)

#     transposed_blocks = []

#     # Now transpose the blocks: make a block that is the first byte of every 
#     # block, and a block that is the second byte of every block, and so on.
#     for i, block in enumerate(keysize_blocks[0:-1]):
#         for j, byte in enumerate(splitString(block, 8)):
#             if i == 0:
#                 transposed_blocks.append(byte)
#             else:
#                 transposed_blocks[j] = transposed_blocks[j] + byte

#     KEY = ''
#     for block in transposed_blocks:

#         #solve each block as if it where a single key XOR
#         KEY += findSingleCharacterKey(block)

#     return KEY


# # Converts a number to a 8-bit binary number
# def intToBinary(n):
#     return '{0:08b}'.format(int(n))

# def intTo6BitBinary(n):
#     return '{0:06b}'.format(int(n))

# def base64ToBinary(s):
#     baseList = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
#     binary_str = ''
#     padding_bits = 0

#     for c in s:
#         if c == '=':
#             padding_bits+= 2
#             continue
#         binary_str += intTo6BitBinary(baseList.index(c))

#     # remove padding
#     if(padding_bits):
#         binary_str = binary_str[:-padding_bits]

#     return binary_str

# # read message from file into list of blocks
# with open ("6.txt", "r") as myfile:
#     blocks = myfile.readlines()

# # strip new lines
# blocks = [x.strip('\n') for x in blocks]

# # concatonate into a single string
# b64_cipher =  "".join(blocks)

# # convert base64 to binary
# binary_cipher = base64ToBinary(b64_cipher)

# # find our repeating KEY
# key = findRepeatingXORKey(binary_cipher)

# # lines = open('6.txt').read().split("\n")
# # for line in lines:
# # 	encoded = binascii.unhexlify(line)




