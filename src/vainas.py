#!/usr/bin/env python3

import sys

from queue import Queue
from time import time
from vigenere_cryptanalysis.vigenere import main as vg_main

from threading import Thread, Event



ITERATIONS =  256

DEBUG = False

DICTIONARIES = [
    'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ',
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
]









def execute_algorithm(encoded_msg, dictionary, message_hash, start_time, event_queue: Queue):
    for _ in range(ITERATIONS):
        key = vg_main(encoded_msg, dictionary, message_hash, event_queue)
        if key == "Kill signal":
            exit()
        
        if key:
            print(''.join(key))
            print(f"\033[92m-\033[00m {sys.argv[1]} -> {(time() - start_time):.4f} seconds")
            if not DEBUG:
                event_queue.put("Finished")
                exit()


def main():
    if len(sys.argv) < 3:
        print("\033[91mNot enough arguments supplied\033[00m")
        exit()

    message_hash = sys.argv[2]
    file_path = sys.argv[1] if "JdP_vigenere_alumnos/" in sys.argv[1] else "JdP_vigenere_alumnos/" + sys.argv[1]
    with open(file_path , 'r') as f:
        encoded_msg = f.read()

    if not encoded_msg:
        print("\033[91mCould not read the message\033[00m")

    start_time = time()

    threads = []
    queue = Queue()
    for dictonary in DICTIONARIES:
        threads.append(Thread(target=execute_algorithm, kwargs={
            'encoded_msg': encoded_msg, 
            'dictionary': dictonary,
            'message_hash': message_hash,
            'start_time': start_time,
            'event_queue': queue
        }) ) 

    for t in threads:
        t.start()


if __name__ == '__main__':
    main()