# Convert hex to base64
# The string:

# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# Should produce:
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
# So go ahead and make that happen. You'll need to use this code for the rest of the exercises.

# Cryptopals Rule
# Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.

import binascii

from common import decrypt_with_single_char
from common import hex2bin

best_score = 0
best_str = ""

lines = open('1.1.txt').read().split("\n")

for line in lines:
	encoded = hex2bin(line)
	decrypted, score = decrypt_with_single_char(encoded)

	if score > best_score:
		best_score = score
		best_str = decrypted

print(best_str)

