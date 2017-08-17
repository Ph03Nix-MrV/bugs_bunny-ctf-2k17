import base64
f=open('enc.txt','r')
ct = f.read()
f.close()
while 'Bugs_Bunny' not in ct:
    ct = base64.b64decode(ct)
print '[*] Decrypted text: ' + ct

