import binascii
import sys
# From https://stackoverflow.com/questions/9475241/split-string-every-nth-character
from itertools import islice

def split_every(n, iterable):
    i = iter(iterable)
    piece = list(islice(i, n))
    while piece:
        yield piece
        piece = list(islice(i, n))
if len(sys.argv) != 1:
    print('You have to drag the file onto the player first...')
with open(sys.argv[1],'rb') as f:
    print('Bytecode opened. Now Preparing...')
    hexdata = binascii.hexlify(f.read())
    print('Hex data created...')
    print('Creating common variables')
    fvars = {}
    print('Done')
    print('Launching...')
    splithex = split_every(8, hexdata)
    # Now we check the first byte to see our instruction
    if splithex[:2] == b'01':
        # Debug print, dehexlify the next 3 bytes.
        print(binascii.dehexlify(splithex[2:8]))
    # That's all for now, testing time :)
    
