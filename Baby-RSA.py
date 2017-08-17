import gmpy2
from Crypto.Util.number import long_to_bytes

file = open('enc.txt','r')
ct = file.read().split('\n')
file.close()

M = ''
N = 20473673450356553867543177537
E = 17
P = 2165121523231
Q =  9456131321351327

phi = (P - 1) * (Q - 1)
D = int(gmpy2.invert(E, phi))
for C in ct:
    try:
        M += long_to_bytes(pow(int(C), D, N))
    except:
        continue
print '[*] Decrypted text: ' + M

