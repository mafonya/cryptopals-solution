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