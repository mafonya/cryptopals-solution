# --------------------------------------------
# Common

from binascii import hexlify, unhexlify, b2a_base64, a2b_base64

def hex2bin(s):
	return unhexlify(s)

def bin2hex(s):
	return hexlify(s)

# --------------------------------------------
# 1.1 

def hex2b64(s):
	return b2a_base64(unhexlify(s))

def b642hex(s):
	return hexlify(a2b_base64(s))



# --------------------------------------------
# 1.2

def fixed_xor(s1, s2):
	assert(len(s1) == len(s2)), "Lengths are different in strings to XOR"
	
	return "".join([chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2)])

# --------------------------------------------
# 1.3

def find_single_char_xor_key(s1):
	pass

# --------------------------------------------
# 1.4

scores = {
	"e":12.702,
	"t":9.056,
	"a":8.167,
	"o":7.507,
	"i":6.966,
	"n":6.749,
	"s":6.327,
	"h":6.094,
	"r":5.987,
	"d":4.253,
	"l":4.025,
	"c":2.782,
	"u":2.758,
	"m":2.406,
	"w":2.360,
	"f":2.228,
	"g":2.015,
	"y":1.974,
	"p":1.929,
	"b":1.492,
	"v":0.978,
	"k":0.772,
	"j":0.153,
	"x":0.150,
	"q":0.095,
	"z":0.074,
	" ": 10
}

def calc_score(str):
	score = 0
	for c in str:
		score += scores.get(c, 0)

	return score

def decrypt_with_single_char(s):
	best_score = 0
	best_str = ""
	best_chr = ""

	# print (encoded)
	for xor_key in range(256):
	    decoded = ''.join(chr(ord(b) ^ xor_key) for b in s)
	    score = calc_score(decoded)

	    if score > best_score:
	    	best_score = score
	    	best_str = decoded
	    	best_chr = xor_key

	return best_str, best_score, chr(best_chr)


# --------------------------------------------
# 1.5

def repxor(str, key, binary_input=False):
	chipher = ""

	for i,c in enumerate(str):
		k = key[i % len(key)]		
		chipher += chr(ord(k) ^ ord(c))

	if binary_input:
		return chipher
	else:
		return hexlify(chipher)


# --------------------------------------------
# 1.6

def hamming(s1, s2):
	if len(s1) != len(s2):
		return -1;

	diff = 0
	diff_arr = [ord(a) ^ ord(b) for a,b in zip(s1,s2)]

	for x in diff_arr:
		diff += bin(x).count("1")

	return diff


def split_str_chunks_len(s, l=2):
    """ Split a string into chunks of length l """
    return [s[i:i+l] for i in range(0, len(s), l)]

def get_best_key_size(bin_str, min_key_size, max_key_size):
    d = {}
    
    for size in range(min_key_size, max_key_size):
        hamming_distance = 0
        chunks = split_str_chunks_len(bin_str, size)
        # print chunks

        keysize_ham = 0
        for a,b in zip(chunks[0::2], chunks[1::2]):
            x = hamming(a,b)
            keysize_ham += x

        d[size] = float(keysize_ham) / ( float(size) * float(len(chunks)) )
        
    return min(d, key=d.get)
