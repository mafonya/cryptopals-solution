from common import *

best_score = 0
best_str = ""

lines = open('1.1.txt').read().split("\n")

for line in lines:
	decrypted, score = decrypt_with_single_char(line)

	if score > best_score:
		best_score = score
		best_str = decrypted

print(best_str)

