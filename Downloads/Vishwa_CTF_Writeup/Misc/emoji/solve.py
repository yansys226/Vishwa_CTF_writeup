
import itertools

"""
Cry:    o (1)
Blush:  h (0)
Angry:  a
Sleep:  z
Smile:  w
Tissue: t
Snow:   x
Think:  b

oha hah ozz ohz hao ohw ohw hat ooa otx oha ozz ozb hao ozw

I suspect it's an octal encoding
"""

decoded = {
    'o': '1',
    'h': '0',
    ' ': ' '
}

cipher = "oha hah ozz ohz hao ohw ohw hat ooa otx oha ozz ozb hao ozw"

decode = lambda x: decoded[x] if x in decoded.keys() else x

print(''.join(map(decode, cipher)))

leftover = "azwtxb"
perms = list(itertools.permutations([2, 3, 4, 5, 6, 7]))

for p in perms:
    decoder = decoded
    for i, l in enumerate(leftover):
        decoder[l] = str(p[i])
    
    decode = lambda x: decoder[x]
    d = ''.join(map(decode, cipher))
    final = ''.join(map(chr, map(lambda x: int(x, 8), d.split(' '))))
    print(final, decoder)

"""
F0RB1DD3N_FRU1T {'o': '1', 'h': '0', ' ': ' ', 'a': '6', 'z': '2', 'w': '4', 't': '3', 'x': '7', 'b': '5'}

VishwaCTF{F0RB1DD3N_FRU1T}
"""
