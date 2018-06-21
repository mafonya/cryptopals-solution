# Single-byte XOR cipher
# The hex encoded string:

# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# ... has been XOR'd against a single character. Find the key, decrypt the message.

# You can do this by hand. But don't: write code to do it for you.

# How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

# Achievement Unlocked
# You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.


import binascii

from common import decrypt_with_single_char
from common import hex2bin

best_score = 0
best_str = ""

lines = open('1.4.txt').read().split("\n")

for line in lines:
	encoded = hex2bin(line)
	decrypted, score, _ = decrypt_with_single_char(encoded)

	if score > best_score:
		best_score = score
		best_str = decrypted

print(best_str)

