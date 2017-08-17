ct = 'Cvht_Cvooz{D35bS_3OD0E3_4S3_O0U_T3DvS3_BU_4MM}'
mes = ''
rot = 0
while 'Bugs_Bunny' not in mes:
    mes = ''
    for ch in ct:
        c = ord(ch)
        if ord('a') <= c <= ord('z'):
            mes += chr((c - ord('a') + rot) %26 + ord('a'))
        elif ord('A') <= c <= ord('Z'):
            mes += chr((c - ord('A') + rot) %26 + ord('A'))
        else:
            mes += ch
    rot += 1
print '[*] Decrypted text: ' + mes
print '[*] Rot : ' + str(rot-1) 
