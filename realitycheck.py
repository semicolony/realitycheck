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

# Hardcoded dictionary of IPs with matching labels
address_dict={
'159.65.63.221':['dig','web','ubuntu'],
'157.230.30.0':['dig','web','stream']
}

target='ubuntu'

# Sends the http request, processes the status code
def ring(door):
    r = requests.get('http://' + door + ':666')
    print('Send request to ' + door)
    print(r.status_code)
    if r.status_code >= 400:
        print('%s is not reachable' % door)
    else:
        print('%s is reachable' % door)

# Main
if __name__ == '__main__':
    if not target:
        print('no target given')
    if target == 'all':
        for door,label in address_dict.items():
            ring(door)
    else:
        for door,label in address_dict.items():
            if target in label:
                ring(door)
