import binascii
import sys

if len(sys.argv) != 1:
    print('You have to drag the file onto the player first...')
with open(sys.argv[1],'rb') as f:
    print('Bytecode opened. Now Playing...')
    print('I said in the Wiki there was no official player. Though someone is working on one. See https://www.youtube.com/watch?v=dQw4w9WgXcQ ;)')
