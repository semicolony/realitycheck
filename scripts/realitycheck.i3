#!/usr/bin/python3

import os
import argparse
from sys import exit, argv

### warn/error func
def _warning(input):
    print(f"WARN: {input}")

def _error(input,err):
    print(f"ERROR: {input}")
    if err:
        print(f"Exception: {err}")
    exit(1)

### parse the arguments
def parse_arguments():
    global METHOD
    global TARGETS
    global OPTIONS
    global SHOW
    parser = argparse.ArgumentParser(description = "Usage for " + _self)
    parser.add_argument(
            "-m",
            help="set method, either server or check",
            choices=['server','check']
    )
    parser.add_argument(
            "-t",
            nargs="+",
            help="set targets, either single host or group",
            metavar=''
    )
    args = parser.parse_args()
    METHOD = args.m
    TARGETS = args.t

### build the listener
def build_serverside(port):
    print(f"build the server, listening on input port")
### start the listener
# OR
### build the target dictionary
### send requests
### store request replies

### thread control

def main():
    parse_arguments()

###
if __name__ == '__main__':
    main()
