#!/usr/bin/python3

# Either loop over all IPs or loop only over a certain set
# defined by the label argument passed from commandline.
#
# The loop runs a http request and the exit code is used to
# decide if the host is reachable or not.
#
# The list if IPs is hardcoded in dict style with each matching
# label as a value to the IP.

import sys
import requests
import http.server
import socketserver
import os

# Hardcoded dictionary of IPs with matching labels
address_dict={
'159.65.63.221':['dig','web','ubuntu'],
'157.230.30.0':['dig','web','stream'],
'162.55.182.118':['htz','web','test']
}

### preflight checks
if len(sys.argv) > 2:
    print(f"too many arguments given")
    sys.exit(2)

### sys.args handling
def set_method():
    global method
    if len(sys.argv[1:]) == 0:
        method = 'all'
        return
    for arg in sys.argv[1:]:
        if arg == 'server':
            method = 'server'
        else:
            method = str(arg)

### Server part
# DOES NOT WORK YET
def start_server():
#    server_dir = '/root/realitycheck/'
    port = 666
    handler = http.server.SimpleHTTPRequestHandler
    os.chdir(server_dir)
    try:
        with socketserver.TCPServer(("", port), handler) as httpd:
            httpd.serve_forever()
    except:
        sys.exit(2)

### Client part
def ring(door):
    try:
        r = requests.get('http://' + door + ':666')
        if r.status_code != 200:
            print(f"unexpected status code returned: {r.status_code}") #debug
        else:
            print(f"{door} is reachbale") #debug
            print(f"index.html: {r.text.rstrip()}") #debug
    except:
            print(f"server {door} not reachable") #debug

# Main
if __name__ == '__main__':
    set_method()
    if method == 'server':
        print(f"starting the http listener on port 666") #debug
        start_server
    elif method == 'all':
        print(f"looping over all targets") #debug
        for door,label in address_dict.items():
            print(f"Send request to {door}:") #debug
            ring(door)
    else:
        for values in address_dict.values():
            if method in values:
                is_in = True
            else:
                is_in = False
        if is_in:
            print(f"looping over subset {method}") #debug
            for door,label in address_dict.items():
                if method in label:
                    ring(door)
        else:
            print(f"{method} is not a valid method")
            sys.exit(2)
