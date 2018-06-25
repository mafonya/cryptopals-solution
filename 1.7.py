from Crypto.Cipher import AES
from common import *

key = 'YELLOW SUBMARINE'

# cipher = AES.new(key, AES.MODE_ECB)

# msg =cipher.encrypt('TechTutorialsX!!TechTutorialsX!!')
# print (type(msg))
# print(msg.encode("hex"))

# decipher = AES.new(key, AES.MODE_ECB)
# print(decipher.decrypt(msg))


bin_str = a2b_base64(open('1.7.txt', "r").read())
decipher = AES.new(key, AES.MODE_ECB)

print(decipher.decrypt(bin_str))