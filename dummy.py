import os
import logging as log

log.basicConfig(level=log.INFO) # Set the threshold to INFO

def double(input1: int) -> int:
    return input1 + input1

if __name__ == "__main__":
    #print(double(56))
    log.info(f"Double for 56: {double(56)}")
    #current_folder = os.listdir()
    #result = double(13)
    #log.info(f"Current folder: {current_folder}")