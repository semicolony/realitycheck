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
ip_dict={
"143.198.186.125":["dig","web","centos"],
"157.230.30.0":["dig","gateway"]
}

# Sends the http request, returns the statuc code
def ring(door):
    r = requests.get("http://" + door)
    return(r.status_code)

# Main
if __name__ == "__main__":
    for ip,types in ip_dict.items():
        print("Send request to " + ip)
        if ring(ip) != 200:
            print("%s is not reachable" % ip)
        else:
            print("%s is reachable" % ip)
