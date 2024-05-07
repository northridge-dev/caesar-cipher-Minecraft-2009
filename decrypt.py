#!/usr/bin/env python
from values import letter_values
from time import sleep
import os


def decrypt(message, shifter = None):
    """
    Decrypts a Caesar cipher encrypted message.
    :param ciphertext: The message to be encrypted
    :param shift: The number of positions to shift each letter
    """
    decoded_message = ""
    if shifter != None:
        if not shifter.isnumeric():
            return "Input a proper shift you nitwit"
        shifter = int(shifter)
        for l in message:
            n = (letter_values[l]-shifter)
            if n <1:
                n += 26
            for k in letter_values.keys():
                if n == letter_values[k]:
                    decoded_message += k
        return decoded_message

    elif shifter == None:
        nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
        decodings = []
        for shift in nums:
            de_mess = ""
            for l in message:
                n = (letter_values[l]-shift)
                if n <1:
                    n += 26
                for k in letter_values.keys():
                    if n == letter_values[k]:
                        de_mess += k
            decodings.append(de_mess)
        return decodings
            
            

    # return ciphertext


if __name__ == "__main__":
    ciphertext = input("Message to decrypt: ")
    sleep(0.5)
    shift = input("Shift: ")
    print(decrypt(ciphertext, shift))
