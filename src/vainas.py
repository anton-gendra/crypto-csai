#!/usr/bin/env python3

import os
import sys

from time import time
from vigenere_cryptanalysis.vigenere import main as vg_main



ITERATIONS = 32


















def main():
    if len(sys.argv) < 2:
        print("\033[91mArgument not supplied\033[00m")
        exit()

    file_path = sys.argv[1] if "JdP_vigenere_alumnos/" in sys.argv[1] else "JdP_vigenere_alumnos/" + sys.argv[1]
    with open(file_path , 'r') as f:
        encoded_msg = f.read()

    if not encoded_msg:
        print("\033[91mCould not read the message\033[00m")

    start_time = time()

    for _ in range(ITERATIONS):
        vg_main(encoded_msg, 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ') # Aquí en estos hay que meter el diccionario y hash

    print(f"\033[92m-\033[00m {sys.argv[1]} -> {(time() - start_time):.4f} seconds")

if __name__ == '__main__':
    main()