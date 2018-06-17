# 1.1 
# Convert hex to base64
# The string:

# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# Should produce:
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
# So go ahead and make that happen. You'll need to use this code for the rest of the exercises.

# Cryptopals Rule
# Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.

import binascii

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

	encoded = binascii.unhexlify(s)
	# print (encoded)
	for xor_key in range(256):
	    decoded = ''.join(chr(ord(b) ^ xor_key) for b in encoded)
	    score = calc_score(decoded)

	    if score > best_score:
	    	best_score = score
	    	best_str = decoded

	return best_str, best_score