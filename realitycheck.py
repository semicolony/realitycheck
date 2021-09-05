#!/usr/bin/python3

import requests

ip_dict={
"143.198.186.125":["DIG","WEB","COS"],
"157.230.30.0":["DIG","GTW"]
}

def ring(door):
    r = requests.get("http://" + door)
    return(r.status_code)

for ip,types in ip_dict.items():
    if any(type == "DIG" for type in types):
        print("Send request to " + ip)
        if ring(ip) != 200:
            print("%s is not reachable" % ip)
